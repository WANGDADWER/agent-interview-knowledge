# 二、LangChain / LangGraph 高频面试题

## Q8：你如何概括 LangChain 的核心价值？

**候选人回答：** LangChain 的价值不是“把 Prompt 串起来”，而是为 LLM/Agent 应用提供模型、工具、消息、Agent loop 与第三方集成等抽象，并配合 LangSmith 做 tracing、evaluation 和部署监控。回答时要把它放在 Agent engineering 生命周期里讲。

**追问：** 为什么现在还要学 LangGraph？答：LangChain 适合快速构建常见 Agent；LangGraph 适合复杂、长时、有状态、需要可恢复和人工介入的 Agent 编排。

## Q9：LangGraph 的核心抽象是什么？

**候选人回答：** 核心是 StateGraph：状态 State、节点 Node、边 Edge、条件边 Conditional Edge、入口/出口、编译后的可执行图。节点通常执行模型调用、工具调用、检索或业务逻辑；边决定下一步流转；状态承载消息、变量、工具结果和控制标记。

**追问：** LangGraph 和普通 Chain 的差异？答：Chain 更像线性/组合式调用；Graph 更适合循环、分支、多 Agent、持久化和人类在环。

## Q10：LangGraph 为什么适合生产级 Agent？

**候选人回答：** 因为它把 Agent 执行显式建模为图和状态，便于持久化、checkpoint、恢复、流式输出、人类在环和调试。对于长任务，失败后可以从中间状态恢复，而不是从头重新跑。

**追问：** Checkpoint 存什么？答：消息、任务状态、中间变量、工具结果、当前节点位置、必要的运行元数据。

## Q11：Human-in-the-loop 在 Agent 系统中怎么做？

**候选人回答：** 常见做法是在敏感节点前暂停，把当前状态、模型建议、工具参数展示给人，由人批准、修改或拒绝。适用场景包括发邮件、删库、下单、转账、发布内容、修改生产配置等。

**追问：** HITL 会不会影响效率？答：只对高风险动作启用；低风险动作自动执行，敏感动作审批。

## Q12：LangSmith/Tracing 面试怎么讲？

**候选人回答：** Tracing 的作用是记录一次 Agent 运行中的模型输入输出、工具调用、延迟、token、错误和状态变化。它帮助定位“是检索错、Prompt 错、模型错、工具错还是编排错”。生产系统没有 tracing 很难排查幻觉和偶发错误。

**追问：** 线上发现用户反馈答案错，你怎么定位？答：先查 trace，分解为输入理解、检索召回、rerank、上下文构造、模型生成、工具调用、后处理各环节。

## Q13：LangChain/LangGraph 的一个典型项目怎么设计？

**候选人回答：** 可以设计“企业知识库 + 工单处理 Agent”：LangChain 接模型和工具，LlamaIndex 或自建检索负责知识库，LangGraph 编排“意图识别→检索→答案生成→置信度判断→必要时创建工单→人工审批→回复用户”。

**追问：** 项目亮点怎么说？答：不是跑通 demo，而是实现评测集、trace、错误恢复、权限控制、成本统计和降级策略。
