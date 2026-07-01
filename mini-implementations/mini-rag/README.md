# mini-rag：手写最小 RAG 流程

## 目标

理解 RAG 的最小链路：

```text
Document
→ Chunk
→ Index
→ Retriever
→ Evidence
→ Answer
```

## 运行方式

```bash
python mini_rag.py
```

## 这个 mini 版本实现了什么？

- 文档对象；
- 简单切块；
- 关键词重叠检索；
- top-k 证据返回；
- 带引用的模板化回答。

## 它没有实现什么？

- 没有真实 embedding；
- 没有真实向量数据库；
- 没有 LlamaIndex 官方 QueryEngine；
- 没有 reranker；
- 没有真实 LLM 生成。

## 面试表达

这个 mini 版本说明 RAG 不是“把文档塞给模型”，而是一个数据管道：解析、切块、索引、检索、证据选择和生成。生产中需要进一步加入 embedding、hybrid retrieval、rerank、metadata filter、权限控制、评测和引用校验。
