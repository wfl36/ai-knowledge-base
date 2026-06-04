# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.7  
**状态：** 正常  
**标签：** DevOps, CI/CD, GitHub-Actions, 开源工具, 发布  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者开源了 GitHub CLI 扩展 gh-slimify，用于自动分析并安全地将 GitHub Actions 工作流迁移至更便宜的 ubuntu-slim runner，以降低 CI 成本。该工具能检测不兼容模式并一键修复安全项，同时附带可复现该逻辑的 AI Agent prompt，为自动化重构提供了思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
工具基于 GitHub CLI 扩展开发，通过静态扫描分析 YAML 工作流文件，识别 Docker、services、缺失包等不兼容模式，技术实现偏向 DevOps 自动化与规则匹配；同时附带 LLM Agent prompt，展示了传统自动化工具与 AI 结合的思路，但整体技术深度属于常规工程实践。

### 实用性 (评分: 8.0/10)
对重度使用 GitHub Actions 的团队极具实用价值，能安全、自动化地完成向 ubuntu-slim 的迁移以降低 CI 成本，解决了手动排查的繁琐痛点；提供的 AI prompt 也为从业者构建自动化代码重构 Agent 提供了参考范例。

### 社区活跃度 (评分: 5.5/10)
获得 69 个点赞，表明社区认可该工具解决痛点的实用价值，但仅 3 条评论说明未引发深入的技术讨论或争议，互动热度偏低。

## 项目链接
https://github.com/fchimpan/gh-slimify
