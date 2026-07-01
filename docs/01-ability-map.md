# 大厂 Agent 面试能力地图

| 能力模块 | 面试官真正想看 | 必须会说的关键词 | 建议作品证据 |
| --- | --- | --- | --- |
| Agent 基础 | 能否把“会调用工具的聊天机器人”上升为可控软件系统 | 目标、状态、工具、记忆、规划、反馈、终止条件 | 实现一个带工具调用和错误恢复的任务助手 |
| RAG 与数据增强 | 能否解决企业私有知识问答、幻觉和可追溯问题 | chunking、embedding、vector DB、hybrid retrieval、rerank、citation、eval | 企业知识库问答，包含召回率/答案忠实性评估 |
| 编排与状态管理 | 能否把多步任务做成稳定可恢复流程 | graph/workflow、checkpoint、persistence、streaming、human-in-the-loop | LangGraph 或 LlamaIndex Workflow 项目 |
| 多智能体协作 | 能否解释何时需要多 Agent，何时不需要 | supervisor-worker、group chat、role decomposition、message protocol、conflict resolution | 研究/客服/运营分析多 Agent Demo |
| 工程化落地 | 是否具备大厂生产思维 | trace、eval、observability、rate limit、retry、timeout、cost、security、权限 | 接入 LangSmith/日志系统，设计离线评测集 |
| 安全与合规 | 能否意识到 Agent 会执行动作而不仅是生成文本 | prompt injection、tool permission、sandbox、approval、audit log、PII | 工具白名单、敏感操作确认、执行沙箱 |
