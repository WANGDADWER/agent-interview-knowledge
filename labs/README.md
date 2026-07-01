# 实战项目总览

> 目标：把源码理解转化为可展示项目，而不是只停留在笔记。

## 当前规划的三个实战项目

| 项目 | 主线能力 | 推荐技术栈 | 面试价值 |
| --- | --- | --- | --- |
| `enterprise-rag-agent` | 企业知识库问答 | LlamaIndex / LangChain / LangGraph / 向量库 | 证明你理解 RAG、检索优化、引用、权限和评测 |
| `customer-service-agent` | 有状态业务流程 | LangGraph / 工具调用 / human-in-the-loop | 证明你理解状态图、审批、失败恢复、审计 |
| `research-multi-agent` | 多智能体调研 | AutoGen 思想 / Microsoft Agent Framework 思想 / RAG | 证明你理解多 Agent 分工、冲突解决和引用校验 |

## 每个实战项目必须包含

```text
README.md
architecture.md
eval.md
security.md
interview-notes.md
```

## 项目完成标准

- 能跑通最小 demo；
- 有系统架构图或文字架构；
- 有至少 20 条评测样例；
- 有失败案例复盘；
- 有权限、安全、成本、延迟考虑；
- 有 2 分钟面试讲稿。
