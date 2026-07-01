# 发布到 GitHub 的说明

本仓库已经整理为中文 Markdown 知识库，适合直接提交到 GitHub。

## 推荐仓库设置

- 仓库名：`agent-interview-knowledge`
- 描述：`AI Agent 面试知识库：LangChain、LlamaIndex、AutoGen、LangGraph、MCP`
- 可见性：建议先设为私有仓库，复习成熟后再考虑公开

## 手动发布命令

如果需要在本地手动发布，可以使用：

```bash
git init
git add .
git commit -m "初始化中文智能体面试知识库"
git branch -M main
git remote add origin https://github.com/WANGDADWER/agent-interview-knowledge.git
git push -u origin main
```

## 维护建议

- `docs/` 存放面试知识；
- `projects/` 存放可展示项目；
- 每周补充新的框架实践、面试追问和项目复盘；
- 遇到官方文档更新时，优先更新 `docs/00-sources.md`。
