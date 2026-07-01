# 手写 mini 实现

> 目标：通过自己实现最小机制，理解框架底层思想。  
> 注意：本目录代码是学习用简化版本，不代表 LangChain、LangGraph、LlamaIndex、AutoGen 或 Microsoft Agent Framework 的官方源码实现。

## 为什么要手写 mini 版本？

只会调用框架 API，面试时容易停留在“调包层”。手写 mini 版本可以帮助你理解：

- Agent loop 为什么需要状态、工具、终止条件；
- Graph workflow 如何通过节点和边控制执行；
- RAG 如何从文档、切块、检索到生成；
- 多 Agent 协作为什么需要角色、消息协议和仲裁机制。

## 当前 mini 项目

| 项目 | 目标 | 对应框架思想 |
| --- | --- | --- |
| `mini-agent-loop` | 手写最小 Agent 执行循环 | LangChain Agent harness / tool calling |
| `mini-langgraph` | 手写最小状态图执行器 | LangGraph StateGraph / node / edge / checkpoint |
| `mini-rag` | 手写最小 RAG 流程 | LlamaIndex Document / Retriever / Query Engine |

## 学习方式

每个 mini 项目都要完成三件事：

1. 运行代码，理解输入输出；
2. 对照官方框架，写出“相似点/不同点”；
3. 把它改造成一个小业务场景，例如客服、知识库、周报生成。
