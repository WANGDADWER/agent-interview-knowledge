# LangChain / LangGraph 源码精读路线

> 核验依据：LangChain 官方文档、LangGraph 官方文档。  
> 注意：本文不写死具体源码文件路径；请在当前官方仓库中搜索核心符号。

## 一、先记住官方定位

- LangChain 官方文档中，`create_agent` 被描述为 minimal, highly configurable agent harness。
- LangChain agents built on top of LangGraph。
- LangGraph 官方定位是 low-level orchestration framework and runtime，用于 long-running、stateful agents。
- LangGraph 重点能力包括 durable execution、streaming、human-in-the-loop、persistence、memory、LangSmith debugging。

## 二、源码精读顺序

### 1. LangChain：从 `create_agent` 读起

建议检索核心符号：

```text
create_agent
model
tools
system_prompt
middleware
messages
structured output
```

重点问题：

- `create_agent` 如何接收 model、tools、system_prompt？
- tool 的 schema 如何生成？
- 模型输出如何被解析为工具调用？
- 工具调用结果如何回到消息列表？
- middleware 在调用链中如何插入？

### 2. LangGraph：从 `StateGraph` 读起

建议检索核心符号：

```text
StateGraph
START
END
add_node
add_edge
add_conditional_edges
compile
invoke
checkpoint
interrupt
resume
```

重点问题：

- State 是如何定义和传递的？
- Node 是普通函数还是特殊对象？
- Edge 如何决定下一个节点？
- 条件边如何实现动态路由？
- `compile()` 之后发生了什么？
- checkpoint 如何保存中间状态？
- interrupt/resume 如何支持 human-in-the-loop？

## 三、面试表达

### 简洁版

LangChain 更像高层 Agent harness，帮助我把模型、工具、prompt 和 middleware 组合起来；LangGraph 更像底层有状态编排运行时，用显式图结构管理节点、边、状态、持久化和人工介入，因此更适合复杂、长时、可恢复的 Agent。

### 源码版

我会从 `create_agent` 和 `StateGraph` 两个入口读源码：前者看 Agent loop 如何把模型输出转成工具调用，后者看状态图如何驱动节点执行、条件路由和 checkpoint。这样可以把框架能力拆成“模型调用、工具调用、状态更新、路由决策、恢复执行、可观测性”几个基本模块。

## 四、手写 mini 版本对应关系

| 官方概念 | mini 实现中对应模块 |
| --- | --- |
| `StateGraph` | `mini-implementations/mini-langgraph/mini_langgraph.py` 中的 `StateGraph` |
| node | 普通 Python 函数 |
| edge | 邻接表或条件路由函数 |
| state | `dict[str, Any]` |
| invoke | 按节点顺序执行并更新 state |
| checkpoint | 把 state 保存为 JSON |

## 五、待核验内容

- 当前版本源码中的具体文件路径；
- LangGraph 内部运行时类名是否发生变化；
- LangChain agent middleware 的最新实现细节。
