# 四、AutoGen / Microsoft Agent Framework / 多智能体面试题

## Q21：AutoGen 的核心思想是什么？

**候选人回答：** AutoGen 强调通过多个可对话 Agent 协作完成任务。不同 Agent 可以有不同角色、工具和系统提示，通过消息传递、组聊或编排机制共同解决复杂问题。

**追问：** AutoGen 当前生态状态？答：旧 AutoGen 仍有学习价值，但官方 GitHub 已标注维护模式，新项目建议关注 Microsoft Agent Framework。

## Q22：AutoGen 的 Studio、AgentChat、Core、Extensions 分别是什么？

**候选人回答：** Studio 是无代码原型界面；AgentChat 是构建单 Agent/多 Agent 对话应用的高层 API；Core 是事件驱动的多 Agent 编程框架；Extensions 提供外部服务集成，如模型客户端、MCP、Docker code executor、分布式 runtime。

**追问：** 入门先学哪个？答：概念入门看 Studio/AgentChat；做严肃多 Agent 系统要理解 Core 和运行时。

## Q23：Microsoft Agent Framework 和 AutoGen 的关系是什么？

**候选人回答：** Microsoft Agent Framework 可以理解为吸收 AutoGen 和 Semantic Kernel 经验后的新一代微软 Agent SDK。它更强调生产级 API、typed graph workflow、多语言支持、企业互操作和长期维护。

**追问：** 面试时如何表述才专业？答：我了解 AutoGen 的多 Agent 协作思想，同时知道新项目应关注 Microsoft Agent Framework，旧 AutoGen 更多用于理解历史设计和维护存量项目。

## Q24：多 Agent 一定比单 Agent 好吗？

**候选人回答：** 不一定。多 Agent 会带来通信成本、角色漂移、循环讨论、错误互相强化和调试困难。只有当任务天然可分工、需要多视角审核、工具权限不同或流程很复杂时，多 Agent 才有价值。

**追问：** 举例？答：论文调研可拆成检索 Agent、阅读 Agent、批判 Agent、写作 Agent；客服系统可拆成意图识别、知识检索、工单执行、质检审核。

## Q25：多 Agent 协作有哪些常见拓扑？

**候选人回答：** 常见拓扑包括 supervisor-worker、planner-executor、debate、committee、pipeline、blackboard、group chat。生产系统更常用 supervisor-worker 或 pipeline，因为控制边界清晰、可观测、可降级。

**追问：** GroupChat 有什么问题？答：自由度高但容易跑偏，必须设置发言规则、终止条件、角色约束和审计。

## Q26：多 Agent 冲突如何解决？

**候选人回答：** 可以设置仲裁 Agent、规则优先级、投票机制、置信度评分、外部验证工具或人工裁决。关键是不要让模型“吵完自动算对”，最终输出必须经过可验证标准。

**追问：** 哪些任务适合 debate？答：开放式方案评审、代码审查、论文批判；不适合强确定性事务操作。
