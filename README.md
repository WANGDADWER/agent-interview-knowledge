# 智能体面试知识库

> 面向大厂互联网面试的 AI Agent / RAG / 多智能体框架中文知识库。  
> 主线框架：LangChain、LangGraph、LlamaIndex、AutoGen、Microsoft Agent Framework、MCP。  
> 升级方向：资料核验 + 源码精读 + 手写 mini 实现 + 实战项目 + 面试表达。

## 仓库定位

这个仓库不是简单收藏教程，而是用于系统化准备 AI Agent 岗位面试：

- 快速理解 Agent、RAG、Workflow、多智能体的核心原理；
- 掌握 LangChain、LangGraph、LlamaIndex、AutoGen 等框架的面试表达；
- 能回答大厂常见系统设计题；
- 能把学习内容包装成可展示的工程项目；
- 通过源码精读和手写 mini 版本提升基础功底。

## 推荐阅读顺序

### 第一部分：面试知识

1. [`docs/00-sources.md`](docs/00-sources.md)：资料来源与审核结论
2. [`docs/01-ability-map.md`](docs/01-ability-map.md)：Agent 面试能力地图
3. [`docs/02-framework-comparison.md`](docs/02-framework-comparison.md)：主流框架对比
4. [`docs/03-agent-core.md`](docs/03-agent-core.md)：Agent 基础与核心原理
5. [`docs/04-langchain-langgraph.md`](docs/04-langchain-langgraph.md)：LangChain / LangGraph 高频问答
6. [`docs/05-llamaindex-rag.md`](docs/05-llamaindex-rag.md)：LlamaIndex / RAG 高频问答
7. [`docs/06-autogen-maf-multi-agent.md`](docs/06-autogen-maf-multi-agent.md)：AutoGen / Microsoft Agent Framework / 多智能体
8. [`docs/07-production-system-design.md`](docs/07-production-system-design.md)：生产落地与系统设计
9. [`docs/08-study-plan.md`](docs/08-study-plan.md)：六周快速入门计划
10. [`docs/09-project-packaging.md`](docs/09-project-packaging.md)：面试项目包装建议
11. [`docs/10-interview-script.md`](docs/10-interview-script.md)：两分钟项目介绍模板

### 第二部分：可信度核验

12. [`reliability/verification-policy.md`](reliability/verification-policy.md)：资料可信度与核验规则
13. [`reliability/source-evidence-map.md`](reliability/source-evidence-map.md)：官方证据映射表

### 第三部分：源码精读

14. [`source-reading/README.md`](source-reading/README.md)：源码精读总路线
15. [`source-reading/langchain-langgraph/01-source-reading-roadmap.md`](source-reading/langchain-langgraph/01-source-reading-roadmap.md)：LangChain / LangGraph 源码精读路线
16. [`source-reading/llamaindex/01-source-reading-roadmap.md`](source-reading/llamaindex/01-source-reading-roadmap.md)：LlamaIndex / RAG 源码精读路线
17. [`source-reading/autogen-maf/01-source-reading-roadmap.md`](source-reading/autogen-maf/01-source-reading-roadmap.md)：AutoGen / Microsoft Agent Framework 源码精读路线

### 第四部分：手写 mini 实现

18. [`mini-implementations/README.md`](mini-implementations/README.md)：mini 实现学习目标
19. [`mini-implementations/mini-agent-loop/`](mini-implementations/mini-agent-loop/)：手写最小 Agent Loop
20. [`mini-implementations/mini-langgraph/`](mini-implementations/mini-langgraph/)：手写最小状态图执行器
21. [`mini-implementations/mini-rag/`](mini-implementations/mini-rag/)：手写最小 RAG 流程

### 第五部分：实战项目

22. [`labs/README.md`](labs/README.md)：实战项目总览
23. [`labs/enterprise-rag-agent/`](labs/enterprise-rag-agent/)：企业知识库 RAG Agent
24. [`labs/customer-service-agent/`](labs/customer-service-agent/)：有状态客服流程 Agent
25. [`labs/research-multi-agent/`](labs/research-multi-agent/)：多智能体调研系统
26. [`interview-review/`](interview-review/)：面试复盘与源码追问题

## 核心判断

- **LangChain 要和 LangGraph / LangSmith 一起学**：只会 chain 不够，面试重点是 Agent 构建、测试、部署、监控与治理。
- **LangGraph 是复杂 Agent 编排核心**：重点理解状态、节点、边、checkpoint、interrupt/resume、human-in-the-loop。
- **LlamaIndex 的主线是 RAG / context augmentation**：重点是数据接入、解析、索引、检索、rerank、Query Engine、Agent 工具化。
- **AutoGen 要结合最新生态理解**：AutoGen 仍适合理解多 Agent 设计，但官方已进入维护模式，新项目应关注 Microsoft Agent Framework。
- **MCP 是工具接入协议，不是 Agent 框架**：面试要能说清 tools/list、tools/call、schema、审批和安全边界。

## 面试表达原则

不要只背框架 API。大厂更看重：

- 能否解释系统边界与适用场景；
- 能否设计可控、可恢复、可观测的 Agent 流程；
- 能否处理权限、安全、成本、延迟、评测和线上监控；
- 能否读懂核心源码并手写 mini 版本证明理解；
- 能否把 Demo 包装成真实业务项目。

## 信息真实性原则

仓库中的框架定位、生态变化和 API 名称优先依据官方文档、官方 GitHub 或 Microsoft Learn。未经核验的经验判断必须标注为“学习建议”或“工程建议”，不能写成事实。

## 许可说明

如果作为个人学习仓库，可以暂不添加开源协议；如果后续公开分享，建议添加 MIT License。
