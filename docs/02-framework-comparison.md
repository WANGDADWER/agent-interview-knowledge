# 主流框架对比：面试版

| 框架/生态 | 定位 | 面试重点 | 适合场景 | 注意点 |
| --- | --- | --- | --- | --- |
| LangChain | Agent 与 LLM 应用开发框架，提供模型、工具、Agent loop、集成能力 | 不是只会 chain；要会说明 Agent 工程生命周期：构建、测试、部署、监控、治理 | 快速搭建工具调用、RAG、业务 Agent 原型 | 现在面试要一起讲 LangGraph/LangSmith |
| LangGraph | 低层 Agent 编排运行时，强调有状态、长任务、可靠执行 | StateGraph、节点、边、状态、checkpoint、HITL、持久化 | 复杂多步任务、可恢复流程、多 Agent 编排 | 不是高层 Prompt 框架，更像可控运行时 |
| LlamaIndex | 以“让 LLM 使用你的数据”为核心的 context augmentation/RAG/Agent 框架 | 数据摄取、解析、索引、检索、rerank、Query Engine、Agent 工具化 | 知识库问答、文档理解、结构化抽取、数据 Agent | 不要只会 5 行入门代码，要能讲索引与召回优化 |
| AutoGen | 微软早期多 Agent 框架，分为 Studio、AgentChat、Core、Extensions | AgentChat/Core/Extensions；GroupChat；异步消息；多 Agent 协作 | 理解多 Agent 设计思想和旧项目维护 | 官方 GitHub 标注维护模式，新项目转向 MAF |
| Microsoft Agent Framework | AutoGen/Semantic Kernel 思想演进后的生产级微软 Agent SDK | Workflow、typed graph、A2A、MCP、生产支持、多模型提供商 | 微软/Azure 技术栈、大企业 Agent 工程 | 面试时可作为 AutoGen 最新生态补充 |
| CrewAI | 以角色化 Agent、Crew 和 Flow 为核心的多 Agent 编排框架 | role/goal/backstory、tasks、processes、guardrails、memory、observability | 任务分工清晰的协作型自动化 | 适合作补充，不必作为主线框架 |
| MCP | 标准化工具/资源接入协议，不是 Agent 框架本身 | tools/list、tools/call、schema、human approval、安全边界 | 让 Agent 统一接入数据库、API、文件系统、业务工具 | 工具越强，权限与审计越重要 |
