# 资料来源与审核结论

## 审核结论

- 优先使用官方文档、官方 GitHub、微软官方博客与 MCP 官方规范。
- 旧教程中只讲 AutoGen GroupChat 的内容已经不够，面试时必须补充 Microsoft Agent Framework 的生态变化。
- LangChain 不能只按“Chain 调 API”学习，而应结合 LangGraph 与 LangSmith 讲工程化闭环。
- LlamaIndex 不应只学 5 行 RAG demo，而要重点理解数据管道、索引、召回、rerank、评测和 Agent 工具化。

## 参考资料

- **[R1]** LangChain Docs 首页：Agent engineering 平台，覆盖构建、测试、部署、监控与治理。  
  https://docs.langchain.com/
- **[R2]** LangGraph 官方概览：低层编排框架与运行时，面向长时运行、有状态 Agent；强调持久化、流式、人类在环、内存、LangSmith 调试。  
  https://docs.langchain.com/oss/python/langgraph/overview
- **[R3]** LlamaIndex 官方文档：Context augmentation、RAG、Agents、Workflows、数据连接器、索引、Query/Chat Engines。  
  https://developers.llamaindex.ai/python/framework/
- **[R4]** LlamaIndex Agents 文档：Workflows 是事件驱动编排基础，支持自定义 Agentic workflows。  
  https://developers.llamaindex.ai/python/framework/use_cases/agents/
- **[R5]** AutoGen 官方文档：Studio、AgentChat、Core、Extensions 的分层定位。  
  https://microsoft.github.io/autogen/stable/index.html
- **[R6]** AutoGen GitHub：AutoGen 已进入维护模式；新项目建议使用 Microsoft Agent Framework。  
  https://github.com/microsoft/autogen
- **[R7]** Microsoft Agent Framework 1.0 官方公告：Python/.NET 生产就绪、稳定 API、长期支持、多模型提供商、A2A 与 MCP 互操作。  
  https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/
- **[R8]** AutoGen 到 Microsoft Agent Framework 迁移指南：AutoGen 与 MAF 的相同点和编排差异。  
  https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/
- **[R9]** Model Context Protocol Tools 规范：MCP server 暴露可被模型调用的工具；建议敏感操作保留 human-in-the-loop。  
  https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- **[R10]** CrewAI 官方文档：面向协作 Agent、Crews 与 Flows，包含 guardrails、memory、knowledge、observability。  
  https://docs.crewai.com/
