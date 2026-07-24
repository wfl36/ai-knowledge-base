# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.7  
**状态：** 正常  
**标签：** DevOps, GitHub Actions, 开源工具, 发布, AI Agent  
**更新日期：** 2026-07-24  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
开发者发布了一款名为 gh-slimify 的 GitHub CLI 扩展工具，用于自动分析并安全地将 GitHub Actions 工作流迁移至更省钱的 ubuntu-slim runner。该工具能检测不兼容模式并一键修复安全项，同时附带了一个可复现相同分析逻辑的 AI Agent prompt，为 CI 降本增效和 Agent 化重构提供了实用方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目是一个 GitHub CLI 扩展，核心技术在于对 GitHub Actions YAML 工作流的静态解析与依赖分析，检测 Docker、Services 及缺失包等不兼容模式。同时探索了将此逻辑转化为 LLM Agent prompt 的可能性，技术实现偏向工程自动化与 AST 解析，AI 含量属于应用层。

### 实用性 (评分: 8.0/10)
对使用 GitHub Actions 的开发者和 DevOps 工程师具有较高实用价值，能够自动化繁琐的 CI 迁移评估过程，帮助团队安全地降本（切换到 ubuntu-slim）。附带的 AI prompt 也为从业者提供了将传统自动化逻辑迁移至 LLM Agent 的实践参考。

### 社区活跃度 (评分: 5.5/10)
项目获得了 69 个点赞，但仅有 3 条评论。这表明社区认可其解决痛点的实用性，但话题本身缺乏引发深度讨论或争议的属性，互动热度一般。

## 项目链接
https://github.com/fchimpan/gh-slimify
