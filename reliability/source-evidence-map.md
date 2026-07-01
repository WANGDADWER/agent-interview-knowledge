# 官方证据映射表

> 最后核验日期：2026-07-01  
> 本表只记录已核验来源。没有进入本表的信息，不应作为确定事实背诵。

## 1. LangChain / LangGraph

| 结论 | 来源 | 核验说明 |
| --- | --- | --- |
| LangChain 提供 `create_agent`，官方称其为 minimal, highly configurable agent harness。 | https://docs.langchain.com/oss/python/langchain/overview | 官方文档 LangChain overview。 |
| LangChain agents built on top of LangGraph，并利用 LangGraph 的 durable execution、human-in-the-loop、persistence 等能力。 | https://docs.langchain.com/oss/python/langchain/overview | 官方文档 Core benefits。 |
| LangGraph 是 low-level orchestration framework and runtime，用于 building, managing, deploying long-running, stateful agents。 | https://docs.langchain.com/oss/python/langgraph/overview | 官方文档 LangGraph overview。 |
| LangGraph 重点能力包括 persistence、human-in-the-loop、memory、LangSmith debugging、production-ready deployment。 | https://docs.langchain.com/oss/python/langgraph/overview | 官方文档 Core benefits。 |

## 2. LlamaIndex

| 结论 | 来源 | 核验说明 |
| --- | --- | --- |
| LlamaIndex 官方定位为 building LLM-powered agents over your data with LLMs and workflows。 | https://developers.llamaindex.ai/python/framework/ | 官方文档 Welcome 页面。 |
| LlamaIndex agents 是使用 tools 执行 research、data extraction 等任务的 LLM-powered knowledge assistants。 | https://developers.llamaindex.ai/python/framework/ | 官方文档 What are agents。 |
| LlamaIndex 支持把 RAG pipeline 作为 Agent 的工具。 | https://developers.llamaindex.ai/python/framework/ | 官方文档 What are agents。 |
| Context augmentation 的核心是把用户私有/特定数据提供给 LLM；工具包括 ingest、parse、index、process 数据，并实现 query workflows。 | https://developers.llamaindex.ai/python/framework/ | 官方文档 What is context augmentation。 |
| LlamaIndex 提供 data connectors、data indexes、query/chat engines、agents、observability/evaluation integrations、workflows。 | https://developers.llamaindex.ai/python/framework/ | 官方文档 LlamaIndex is the framework for Context-Augmented LLM Applications。 |

## 3. AutoGen / Microsoft Agent Framework

| 结论 | 来源 | 核验说明 |
| --- | --- | --- |
| AutoGen 是用于创建 multi-agent AI applications 的框架，可以 autonomous 或 alongside humans。 | https://github.com/microsoft/autogen | 官方 GitHub README。 |
| AutoGen 当前处于 maintenance mode，不再接收新功能或增强，后续由社区维护。 | https://github.com/microsoft/autogen | 官方 GitHub README Caution。 |
| AutoGen 官方建议新用户从 Microsoft Agent Framework 开始，现有用户参考迁移指南。 | https://github.com/microsoft/autogen | 官方 GitHub README。 |
| Microsoft Agent Framework 是 AutoGen 思想的重要演进，由 Microsoft 的 AutoGen 和 Semantic Kernel 核心团队开发。 | https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/ | Microsoft Learn 迁移指南。 |
| Agent Framework 以 typed, graph-based Workflow 为中心，AutoGen 以 event-driven core 和 high-level Team 为主要编排方式。 | https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/ | Microsoft Learn Key Differences。 |

## 4. MCP

| 结论 | 来源 | 核验说明 |
| --- | --- | --- |
| MCP 允许 server 暴露可被 language models 调用的 tools。 | https://modelcontextprotocol.io/specification/2025-06-18/server/tools | MCP 官方规范。 |
| Tool 可以让模型与外部系统交互，例如查询数据库、调用 API 或执行计算。 | https://modelcontextprotocol.io/specification/2025-06-18/server/tools | MCP 官方规范。 |
| MCP 官方规范建议信任、安全相关场景中应保留 human-in-the-loop，并让用户能够拒绝工具调用。 | https://modelcontextprotocol.io/specification/2025-06-18/server/tools | MCP 官方规范 Trust & Safety。 |

## 5. 不确定信息记录

当前不写入为事实的信息：

- 某个开源仓库内部文件路径的长期稳定性；
- 某个框架在所有企业中的真实采用率；
- 某类 Agent 架构在所有业务上的效果提升；
- 第三方博客对框架优劣的结论。

这些内容可以作为学习参考，但不能作为面试中的确定事实。
