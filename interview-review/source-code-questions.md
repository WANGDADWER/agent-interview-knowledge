# 源码追问题：面试准备版

## 一、Agent Loop

### Q1：Agent 为什么不是简单 while 循环？

回答要点：

- while 循环只是控制结构；
- 生产级 Agent 还需要状态管理、工具权限、错误恢复、最大步数、终止条件、trace、人工审批；
- 框架的价值是把这些机制标准化、可观测化、可复用化。

### Q2：模型输出如何变成工具调用？

回答要点：

- 模型通常输出结构化 tool call；
- 工具侧有 schema、名称、参数说明；
- 执行前需要参数校验、权限校验；
- 执行结果作为 observation 或 tool message 回到上下文。

## 二、LangGraph

### Q3：StateGraph 的核心是什么？

回答要点：

- State 是跨节点共享和更新的数据；
- Node 是对 state 的变换；
- Edge 决定执行顺序；
- Conditional Edge 决定动态路由；
- Checkpoint 支持失败恢复和长任务执行。

### Q4：为什么复杂 Agent 适合图编排？

回答要点：

- 显式流程比自由循环更可控；
- 节点可测试；
- 路由可审计；
- 状态可持久化；
- 高风险动作可插入 human-in-the-loop。

## 三、LlamaIndex / RAG

### Q5：RAG 的错误如何定位？

回答要点：

- 如果召回没有相关证据，是 ingestion/chunking/retrieval 问题；
- 如果召回有证据但答案错误，是 generation/faithfulness 问题；
- 如果引用错，是 citation/context packing 问题；
- 如果用户看到无权限信息，是 ACL/filter 问题。

### Q6：Retriever 和 Query Engine 区别是什么？

回答要点：

- Retriever 负责找相关证据；
- Query Engine 负责组织检索、上下文构造、调用模型和返回答案；
- 生产中还要加入 rerank、citation、拒答和评测。

## 四、多智能体

### Q7：多 Agent 为什么可能更差？

回答要点：

- 增加 token 和延迟；
- 角色可能漂移；
- 错误可能互相强化；
- 调试困难；
- 没有清晰任务分工时不如单 Agent 或确定性 workflow。

### Q8：什么时候需要多 Agent？

回答要点：

- 任务天然可分解；
- 需要多视角审核；
- 不同工具权限需要隔离；
- 需要 supervisor-worker 或 pipeline 化协作；
- 输出需要 Critic 校验。

## 五、可信度追问

### Q9：你怎么保证自己学到的信息不是过期的？

回答要点：

- 优先查官方文档、官方 GitHub、Microsoft Learn；
- 记录核验日期；
- 把事实、推论、工程建议分开；
- 对生态状态类问题，例如 AutoGen 是否维护，必须用官方来源确认。

### Q10：如果官方文档和社区教程冲突，你信哪个？

回答要点：

- 默认以官方文档和官方仓库为准；
- 社区教程用于补充实践经验；
- 对 API 名称、版本状态、迁移路线这类事实，不能依赖旧博客。
