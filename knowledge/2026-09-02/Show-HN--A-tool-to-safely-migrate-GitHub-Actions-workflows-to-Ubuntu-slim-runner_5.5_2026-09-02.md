# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 5.5  
**状态：** 待复核  
**标签：** GitHub Actions, DevOps, CI/CD, Show HN, 工具, LLM Agent  
**更新日期：** 2026-09-02  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
gh-slimify 是一个针对 GitHub Actions ubuntu-slim runner 迁移的 CLI 工具，能自动检测 workflow 的兼容性并安全迁移。它解决了一个真实但较为小众的痛点，工程实现扎实，并附带 AI agent prompt 探索 LLM 自动化重构的思路。整体属于实用型 DevOps 工具，AI 相关性较弱。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.5/10)
该项目是一个 GitHub CLI 扩展，技术实现涵盖 GitHub Actions workflow 静态分析、Docker/service/container 模式检测、命令可用性检查等技术点，有一定工程深度但并非前沿 AI/ML 技术。亮点是附带了一个 AI agent prompt 用于复现分析逻辑，涉及 LLM agent 自动化重构的探索，但核心仍是 DevOps 工具而非 AI 技术本身。

### 实用性 (评分: 6.0/10)
对 GitHub Actions 重度用户和 DevOps 从业者有实用价值，能省去手动审查 ubuntu-slim 迁移兼容性的繁琐工作。附带 AI agent prompt 的设计思路对探索 LLM 辅助代码迁移的从业者有一定启发，但整体覆盖面较窄，主要服务于使用 GitHub Actions 的团队。

### 社区活跃度 (评分: 5.0/10)
HN Points 69、评论数仅 3 条，表明有一定关注度但讨论深度有限，属于典型的 Show HN 中等热度项目。话题贴近开发者日常痛点（CI 成本优化），但因受众面相对垂直，未引发广泛讨论。

## 项目链接
https://github.com/fchimpan/gh-slimify
