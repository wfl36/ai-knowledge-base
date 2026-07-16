# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.2  
**状态：** 正常  
**标签：** CI/CD, GitHub Actions, DevOps, 开源项目, 工具, Show HN  
**更新日期：** 2026-07-16  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
开发者发布了一款名为 gh-slimify 的 GitHub CLI 扩展，用于自动化安全地将 GitHub Actions 工作流迁移至 ubuntu-slim 运行器以节约成本。该工具能扫描不兼容模式并一键安全更新，同时提供了可复现此逻辑的 LLM Agent 提示词。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
项目核心是对 GitHub Actions 的 YAML 工作流进行静态分析，检测 Docker、services 及缺失依赖等不兼容模式，技术实现涉及 YAML 解析与规则匹配；同时创新性地附带了 LLM Agent 提示词以复现分析逻辑，具有一定工程技巧，但整体无底层 AI 技术深度。

### 实用性 (评分: 7.5/10)
对 DevOps 和后端开发者具有较高实用价值，能自动化排查迁移风险并一键安全更新，有效降低 CI 运行成本；附带的 AI Agent 提示词也为 AI 工程师集成自动化重构逻辑提供了直接参考。

### 社区活跃度 (评分: 5.0/10)
获得 69 个点赞但仅 3 条评论，显示社区认可其解决痛点的实用性，但尚未引发深层技术讨论或争议，整体互动热度偏低。

## 项目链接
https://github.com/fchimpan/gh-slimify
