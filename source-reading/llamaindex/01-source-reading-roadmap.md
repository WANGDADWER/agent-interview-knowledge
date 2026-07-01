# LlamaIndex / RAG 源码精读路线

> 核验依据：LlamaIndex 官方文档。  
> 注意：本文不写死具体源码文件路径；请在当前官方仓库中搜索核心符号。

## 一、先记住官方定位

- LlamaIndex 官方定位是 building LLM-powered agents over your data with LLMs and workflows。
- LlamaIndex 的 context augmentation 目标是把私有/特定数据提供给 LLM。
- 官方文档列出的核心能力包括 data connectors、data indexes、query engines、chat engines、agents、observability/evaluation、workflows。
- 高级用户可以自定义 data connectors、indices、retrievers、query engines、reranking modules。

## 二、源码精读顺序

### 1. 数据进入：Document / Node / Reader

建议检索核心符号：

```text
Document
Node
TextNode
SimpleDirectoryReader
NodeParser
SentenceSplitter
metadata
```

重点问题：

- 原始文件如何变成 Document？
- Document 如何切成 Node？
- metadata 如何保存页码、标题、来源、权限？
- chunk size 和 overlap 在哪里控制？

### 2. 索引构建：Index / VectorStoreIndex

建议检索核心符号：

```text
VectorStoreIndex
StorageContext
VectorStore
Embedding
insert
persist
```

重点问题：

- Node 如何转 embedding？
- embedding 如何写入 vector store？
- index 和 vector store 的边界是什么？
- 如何持久化与重新加载？

### 3. 查询链路：Retriever / Query Engine / Response Synthesizer

建议检索核心符号：

```text
Retriever
NodeWithScore
QueryEngine
ResponseSynthesizer
NodePostprocessor
rerank
```

重点问题：

- Query 如何变成检索请求？
- Retriever 返回什么结构？
- top-k 与 score 如何影响结果？
- reranker 或 node postprocessor 在哪里插入？
- ResponseSynthesizer 如何把多个片段合成答案？

### 4. Agent 工具化

建议检索核心符号：

```text
QueryEngineTool
FunctionTool
AgentWorkflow
Tool
```

重点问题：

- RAG pipeline 如何变成 Agent 工具？
- Agent 如何选择调用知识库工具还是普通函数工具？
- 多工具冲突时如何处理？

## 三、面试表达

### 简洁版

LlamaIndex 的核心不是“向量数据库封装”，而是一套 context augmentation 框架：它负责把私有数据从原始文件变成 Document/Node，再通过索引、检索、重排和 query engine 提供给 LLM，最后还能作为 Agent 工具参与多步任务。

### 源码版

我会沿着数据流读源码：Reader 把文件变成 Document，NodeParser 切分成 Node，Index 把 Node 写入向量存储，Retriever 召回 NodeWithScore，QueryEngine 调用 ResponseSynthesizer 生成答案。这样可以把 RAG 的错误拆成数据解析、切块、召回、重排、生成几个环节定位。

## 四、手写 mini 版本对应关系

| 官方概念 | mini 实现中对应模块 |
| --- | --- |
| Document | `Document` 数据类 |
| Node | 简化为文本 chunk |
| Retriever | 关键词/余弦相似度召回函数 |
| Query Engine | `answer(query)` 函数 |
| Response Synthesizer | 简化为拼接证据并生成模板答案 |

## 五、待核验内容

- 当前版本源码中的具体模块路径；
- 不同 retriever/reranker 的最新类名；
- AgentWorkflow 与旧 Agent API 的版本差异。
