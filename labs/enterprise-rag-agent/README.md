# 企业知识库 RAG Agent

## 一、项目目标

构建一个面向企业内部文档的 RAG Agent，支持：

- 文档导入；
- 语义/关键词混合检索；
- rerank；
- 带引用回答；
- 权限过滤；
- 低置信度拒答；
- 离线评测。

## 二、推荐架构

```text
用户问题
→ 意图识别
→ 权限校验
→ query rewrite
→ hybrid retrieval
→ rerank
→ context packing
→ answer with citation
→ faithfulness check
→ 返回答案或拒答
```

## 三、源码关联

| 项目模块 | 对应源码/框架理解 |
| --- | --- |
| 文档解析 | LlamaIndex Document / Node / Reader |
| 切块 | NodeParser / SentenceSplitter 思想 |
| 检索 | Retriever / VectorStore / BM25 |
| 重排 | NodePostprocessor / reranking module |
| 回答生成 | Query Engine / Response Synthesizer |
| Agent 化 | QueryEngineTool / FunctionTool 思想 |
| 编排 | LangGraph StateGraph 思想 |

## 四、评测指标

- Retrieval Recall@K；
- Answer Faithfulness；
- Citation Accuracy；
- Permission Violation Rate；
- Latency；
- Token Cost；
- Refusal Accuracy。

## 五、面试亮点

这个项目不是普通知识库问答，而是关注企业落地难点：权限、引用、幻觉、低置信度拒答、评测和可观测性。
