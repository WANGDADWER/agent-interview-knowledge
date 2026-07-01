# AutoGen / Microsoft Agent Framework 源码精读路线

> 核验依据：AutoGen 官方文档、AutoGen 官方 GitHub、Microsoft Learn 迁移指南。  
> 注意：AutoGen 官方 GitHub 已标注 maintenance mode；新项目建议关注 Microsoft Agent Framework。

## 一、先记住官方定位

- AutoGen 是用于创建 multi-agent AI applications 的框架。
- AutoGen 官方文档包含 Studio、AgentChat、Core、Extensions 等模块。
- AgentChat 用于 conversational single and multi-agent applications，built on Core。
- Core 是 event-driven programming framework，用于 scalable multi-agent AI systems。
- AutoGen 官方 GitHub 明确写入 maintenance mode，不再接收新功能或增强。
- Microsoft Learn 迁移指南说明 Microsoft Agent Framework 是 AutoGen 思想的重要演进，并由 AutoGen 与 Semantic Kernel 核心团队开发。

## 二、AutoGen 源码精读顺序

建议检索核心符号：

```text
AssistantAgent
AgentChat
Core
Team
GroupChat
FunctionTool
McpWorkbench
DockerCommandLineCodeExecutor
```

重点问题：

- 单个 AssistantAgent 如何接收模型客户端、指令和工具？
- AgentChat 如何构建单 Agent/多 Agent 对话？
- Core 的事件驱动模型如何传递消息？
- GroupChat/Team 如何选择下一个发言者或执行者？
- Extensions 如何接入 MCP、Docker code executor 等外部能力？

## 三、Microsoft Agent Framework 精读顺序

建议检索核心符号：

```text
Agent
@tool
Workflow
Executor
Message
Role
Checkpoint
Middleware
```

重点问题：

- Agent Framework 如何定义 Agent？
- `@tool` 如何自动推断 schema？
- Workflow 如何用 typed graph 路由数据？
- AutoGen 的 event-driven core 与 Agent Framework 的 typed workflow 有什么差异？
- human-in-the-loop、checkpoint、observability 如何进入工作流？

## 四、面试表达

### 简洁版

AutoGen 适合理解多 Agent 的早期设计，例如 GroupChat、事件驱动运行时和 AgentChat；但根据官方 GitHub，AutoGen 当前处于维护模式，新项目应关注 Microsoft Agent Framework。Microsoft Agent Framework 继承了 AutoGen 和 Semantic Kernel 的经验，更强调生产级、多语言、typed workflow 和企业支持。

### 源码版

我会把 AutoGen 和 MAF 对照阅读：AutoGen 看 AssistantAgent、Team/GroupChat、event-driven runtime；MAF 看 Agent、tool、typed Workflow 和 executor。这样可以理解多 Agent 编排从自由对话式协作向类型化工作流编排演进的设计取舍。

## 五、待核验内容

- Microsoft Agent Framework 当前版本中的具体源码目录；
- 某些 hosted tools 的可用性与版本限制；
- AutoGen 旧版本 0.2 与当前 stable 文档的 API 差异。
