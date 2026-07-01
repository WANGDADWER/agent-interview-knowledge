# 源码精读总路线

> 目标：从“会用框架”升级到“理解框架为什么这样设计”。  
> 注意：这里的源码精读路线基于官方文档中已核验的核心抽象；具体文件路径可能随仓库版本变化，应以当前官方仓库为准。

## 一、源码精读原则

不要从仓库第一行代码开始读。正确方式是：

```text
最小可运行 Demo
→ 入口 API
→ 核心抽象
→ 数据结构
→ 执行循环
→ 错误处理
→ 可观测性
→ 对照手写 mini 版本
```

## 二、重点阅读对象

| 框架 | 精读目标 | 核心问题 |
| --- | --- | --- |
| LangChain | Agent harness、tool calling、middleware、message | `create_agent` 如何把 model、tools、prompt、middleware 组成执行循环？ |
| LangGraph | StateGraph、Node、Edge、Checkpoint、Interrupt | 状态图如何让 Agent 具备可恢复、可暂停、可观测能力？ |
| LlamaIndex | Document、Node、Index、Retriever、Query Engine、Agent | 私有数据如何从原始文档变成可被 LLM 使用的上下文？ |
| AutoGen | AgentChat、Core、Extensions、message runtime | 多 Agent 如何通过消息和运行时协作？ |
| Microsoft Agent Framework | Agent、Tool、Workflow、typed graph | 新一代微软 Agent SDK 如何把多 Agent 编排转向 typed workflow？ |

## 三、每次源码精读输出模板

每读完一个模块，在本仓库新增一份笔记：

```markdown
# 模块名称

## 1. 官方定位

## 2. 最小使用示例

## 3. 入口 API

## 4. 核心数据结构

## 5. 执行流程

## 6. 关键设计取舍

## 7. 我手写的 mini 版本如何对应

## 8. 面试怎么讲

## 9. 不确定/待核验内容
```

## 四、精通标准

你至少要做到：

- 能从一个 Demo 追踪到核心执行流程；
- 能画出框架内部调用链；
- 能解释为什么需要状态、工具、回调、checkpoint、retriever、reranker；
- 能手写一个 mini 版本；
- 能把源码设计转化为面试表达。
