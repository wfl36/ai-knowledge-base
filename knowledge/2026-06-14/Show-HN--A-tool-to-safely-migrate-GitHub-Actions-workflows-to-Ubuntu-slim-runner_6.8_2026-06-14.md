# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.8  
**状态：** 正常  
**标签：** DevOps, CI/CD, LLM Agent, 开源, 发布  
**更新日期：** 2026-06-14  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者发布了开源 GitHub CLI 扩展 gh-slimify，用于自动分析并安全地将 GitHub Actions 工作流迁移至更省钱的 ubuntu-slim runner，避免因缺失依赖导致的构建失败。项目还附带了一个 AI Agent prompt，可将此迁移逻辑集成到 LLM 中，实现自动化的工作流重构。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
工具通过静态分析 GitHub Actions 工作流文件，检测 Docker、服务、缺失包等不兼容模式，实现安全迁移到 ubuntu-slim。技术实现属于扎实的工程实践，并创新性地提供了可复现该逻辑的 AI Agent Prompt，展示了 LLM 在自动化代码/配置重构中的应用模式。

### 实用性 (评分: 8.5/10)
对使用 GitHub Actions 的开发者与 DevOps 工程师具有极高的实用价值，能自动化繁琐的迁移审查过程，帮助团队安全地降本增效。附带的 AI prompt 也为 AI 从业者将 DevOps 任务集成到 LLM Agent 中提供了直接可用的参考模板。

### 社区活跃度 (评分: 5.5/10)
获得了 69 个点赞，但仅有 3 条评论。表明社区认可该工具解决的痛点和实用价值，但话题本身偏向工程应用，未引发深度的技术讨论或争议，互动热度一般。

## 项目链接
https://github.com/fchimpan/gh-slimify
