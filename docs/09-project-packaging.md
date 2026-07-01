# 面试项目包装建议

| 项目 | 推荐技术栈 | 必须实现的亮点 | 面试表达 |
| --- | --- | --- | --- |
| 企业知识库 Agent | LlamaIndex + LangGraph + 向量库 + LangSmith | hybrid retrieval、rerank、citation、ACL 权限、离线评测 | 解决企业私有知识问答中的召回、幻觉和权限问题 |
| 客服工单 Agent | LangChain/LangGraph + 工单 API + RAG | 意图识别、工具调用、HITL、失败降级、审计日志 | 把 Agent 做成可控业务流程，而不是聊天机器人 |
| 运营周报 Agent | LangGraph + SQL 工具 + 报告模板 | 只读 SQL、异常检测、草稿审核、定时运行、成本统计 | 体现大厂数据产品和自动化场景理解 |
| 论文/竞品调研多 Agent | AutoGen/MAF 思想 + LlamaIndex | 检索、阅读、批判、写作、引用校验多角色 | 体现多 Agent 分工、冲突解决和事实校验能力 |
