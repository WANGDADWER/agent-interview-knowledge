# mini-langgraph：手写最小状态图执行器

## 目标

理解 LangGraph 类框架为什么要使用“状态 + 节点 + 边”：

```text
State
→ Node 执行业务逻辑
→ Edge 决定下一步
→ State 被更新
→ 可 checkpoint / resume
```

## 运行方式

```bash
python mini_langgraph.py
```

## 这个 mini 版本实现了什么？

- 添加节点；
- 添加普通边；
- 添加条件边；
- 执行状态图；
- JSON checkpoint 保存。

## 它没有实现什么？

- 没有真实 LangGraph runtime；
- 没有并发、流式输出、分布式执行；
- 没有真实 interrupt/resume API；
- 没有 LangSmith tracing；
- 没有完整类型系统。

## 面试表达

通过这个 mini 版本可以说明：图式 Agent 的优势在于把不可控的自由循环拆成显式节点和路由逻辑，每一步都围绕状态更新，可以做 checkpoint、恢复、人工介入和可观测调试。
