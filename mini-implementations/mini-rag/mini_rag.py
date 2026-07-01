"""
mini-rag: 学习用最小 RAG 流程。

说明：
- 这是教学用简化实现，不是 LlamaIndex 官方源码。
- 不使用真实 embedding 和向量数据库，只用关键词重叠模拟检索。
"""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Document:
    doc_id: str
    text: str
    source: str


@dataclass
class Chunk:
    chunk_id: str
    text: str
    source: str


class MiniRAG:
    def __init__(self, chunk_size: int = 80):
        self.chunk_size = chunk_size
        self.chunks: List[Chunk] = []

    def ingest(self, documents: List[Document]) -> None:
        for doc in documents:
            for i, start in enumerate(range(0, len(doc.text), self.chunk_size)):
                text = doc.text[start : start + self.chunk_size]
                self.chunks.append(
                    Chunk(
                        chunk_id=f"{doc.doc_id}-{i}",
                        text=text,
                        source=doc.source,
                    )
                )

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        return [token.strip().lower() for token in text.replace("，", " ").replace("。", " ").split() if token.strip()]

    def retrieve(self, query: str, top_k: int = 2) -> List[Tuple[Chunk, int]]:
        query_terms = set(self._tokenize(query))
        scored: List[Tuple[Chunk, int]] = []

        for chunk in self.chunks:
            chunk_terms = set(self._tokenize(chunk.text))
            score = len(query_terms & chunk_terms)
            if score > 0:
                scored.append((chunk, score))

        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:top_k]

    def answer(self, query: str) -> str:
        evidence = self.retrieve(query)
        if not evidence:
            return "没有找到足够证据，建议补充资料或扩大检索范围。"

        lines = [f"问题：{query}", "", "证据："]
        for chunk, score in evidence:
            lines.append(f"- [{chunk.source} | score={score}] {chunk.text}")

        lines.extend(
            [
                "",
                "回答：根据上述证据，可以给出一个初步回答。生产系统中这里应调用 LLM，并要求答案必须被证据支持。",
            ]
        )
        return "\n".join(lines)


if __name__ == "__main__":
    docs = [
        Document(
            doc_id="agent",
            source="agent-notes.md",
            text="Agent loop 包括观察、决策、工具调用、状态更新和终止判断。生产系统需要权限、审计和错误恢复。",
        ),
        Document(
            doc_id="rag",
            source="rag-notes.md",
            text="RAG 包括数据解析、切块、索引、检索、重排、上下文构造和答案生成。",
        ),
    ]

    rag = MiniRAG(chunk_size=60)
    rag.ingest(docs)
    print(rag.answer("Agent loop 工具调用 状态"))
