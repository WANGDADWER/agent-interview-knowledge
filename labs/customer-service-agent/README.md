# 有状态客服流程 Agent

## 一、项目目标

构建一个可控的客服 Agent，不追求“自由聊天”，而是把业务流程做成可恢复、可审批、可审计的状态图。

## 二、推荐架构

```text
用户输入
→ 意图识别
→ 普通 FAQ / 订单查询 / 退款申请 / 人工转接
→ 工具调用
→ 风险判断
→ human-in-the-loop
→ 回复用户
→ trace 与审计日志
```

## 三、状态设计

```text
user_input
intent
user_id
permission
retrieved_context
tool_calls
risk_level
need_approval
final_answer
trace
```

## 四、源码关联

| 项目模块 | 对应源码/框架理解 |
| --- | --- |
| 状态对象 | LangGraph State 思想 |
| 意图识别节点 | Node |
| FAQ 回答节点 | Node + RAG Tool |
| 退款审批节点 | Human-in-the-loop / interrupt 思想 |
| 条件路由 | Conditional Edge |
| 失败恢复 | Checkpoint / persistence 思想 |
| 线上排错 | Trace / observability |

## 五、评测指标

- 意图识别准确率；
- 工具调用正确率；
- 高风险动作拦截率；
- 平均步骤数；
- 平均延迟；
- 人工接管率；
- 用户满意度。

## 六、面试亮点

这个项目体现生产思维：不是让模型随便决定退款，而是通过状态图和审批节点控制高风险动作，并保留 trace 和审计日志。
