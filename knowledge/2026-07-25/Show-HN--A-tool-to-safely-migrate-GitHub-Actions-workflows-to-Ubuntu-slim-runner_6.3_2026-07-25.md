# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.3  
**状态：** 正常  
**标签：** DevOps, GitHub Actions, AI Agent, 开源项目, 工具  
**更新日期：** 2026-07-25  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
开发者发布了一款 GitHub CLI 扩展 gh-slimify，用于自动化将 GitHub Actions 工作流安全迁移至更便宜的 ubuntu-slim runner。该工具能扫描并标记不兼容模式，一键安全更新，同时提供了可复现此分析逻辑的 AI Agent prompt，方便集成至 LLM 自动化重构流程中。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
工具核心基于 YAML 解析与依赖静态分析，检测 GitHub Actions 工作流中的 Docker、Services 及缺失包等不兼容模式，技术深度偏向工程实践与 CI/CD 配置解析；附带 LLM Agent prompt 实现逻辑复现，体现了 AI 辅助代码重构的应用探索。

### 实用性 (评分: 7.5/10)
对使用 GitHub Actions 的开发者及 DevOps 工程师有直接的经济与效率价值，能安全降低 CI 运行成本；其附带的 AI Agent prompt 设计，对构建自动化代码重构与 DevOps 工具链的 AI 从业者具有实际参考意义。

### 社区活跃度 (评分: 5.0/10)
获得 69 个点赞但仅 3 条评论，属于中等偏小的 Show HN 项目，受众面相对局限于 CI/CD 成本优化群体，社区讨论的深度与广度较为有限。

## 项目链接
https://github.com/fchimpan/gh-slimify
