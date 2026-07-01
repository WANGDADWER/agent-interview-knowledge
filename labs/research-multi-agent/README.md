# 多智能体调研系统

## 一、项目目标

构建一个用于论文/竞品/技术调研的多智能体系统，重点不是“多个角色聊天”，而是可控分工、证据引用和质量审核。

## 二、推荐角色

| Agent | 职责 |
| --- | --- |
| Planner Agent | 拆解调研问题，制定检索计划 |
| Retriever Agent | 检索资料，返回来源和摘要 |
| Reader Agent | 阅读资料，抽取关键信息 |
| Critic Agent | 检查事实、逻辑和遗漏 |
| Writer Agent | 生成最终报告 |
| Supervisor Agent | 控制流程、合并结果、决定是否继续 |

## 三、推荐架构

```text
调研问题
→ Planner 拆解
→ Retriever 检索
→ Reader 抽取
→ Critic 审核
→ Writer 生成
→ Supervisor 判断是否补充检索
→ 最终报告 + 引用
```

## 四、源码关联

| 项目模块 | 对应源码/框架理解 |
| --- | --- |
| 多角色协作 | AutoGen AgentChat / GroupChat 思想 |
| 事件驱动消息 | AutoGen Core 思想 |
| 监督者编排 | supervisor-worker pattern |
| Typed workflow | Microsoft Agent Framework Workflow 思想 |
| 引用校验 | RAG evidence / citation |
| 安全边界 | MCP tool approval / human-in-the-loop |

## 五、评测指标

- 来源覆盖率；
- 引用准确率；
- 报告事实一致性；
- 重复检索率；
- 平均 token 成本；
- Critic 发现问题数量；
- 人工修改率。

## 六、面试亮点

这个项目可以说明你理解多 Agent 的边界：多 Agent 不一定更好，只有在任务可分解、需要多视角审核、需要不同工具权限时才值得使用。
