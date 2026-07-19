# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.7  
**状态：** 正常  
**标签：** DevOps, CI/CD, GitHub Actions, Developer Tools, Show HN, 开源工具  
**更新日期：** 2026-07-19  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者开源了一款 GitHub CLI 扩展 gh-slimify，用于自动分析并安全地将 GitHub Actions 工作流迁移至更便宜的 ubuntu-slim runner，同时附带了一个可复现该逻辑的 AI Agent Prompt。该工具对 DevOps 降本增效极具实用价值，但社区讨论热度一般。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目涉及 GitHub Actions 工作流的静态分析与自动化重构，通过解析 YAML 并检测依赖、Docker 和服务使用情况来判断迁移兼容性，具备一定的工程解析深度；AI 部分仅作为附加提供 Prompt 来复现逻辑，核心并非 AI 底层技术突破。

### 实用性 (评分: 8.0/10)
对使用 GitHub Actions 的开发者和 DevOps 工程师极具实用价值，能自动化繁琐的迁移检查，帮助团队安全地降低 CI/CD 成本；附带的 AI Agent Prompt 也为将代码审查与重构逻辑集成到 LLM 工作流中提供了直接参考。

### 社区活跃度 (评分: 5.5/10)
获得 69 个点赞，但仅有 3 条评论，表明社区认可其解决痛点的实用性，但未引发广泛或深入的探讨，互动热度偏低。

## 项目链接
https://github.com/fchimpan/gh-slimify
