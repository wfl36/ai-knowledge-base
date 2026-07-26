# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 5.7  
**状态：** 待复核  
**标签：** DevOps, CI/CD, GitHub Actions, 开源, 发布  
**更新日期：** 2026-07-26  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者开源了一款 GitHub CLI 扩展 gh-slimify，用于自动检测并安全地将 GitHub Actions 工作流迁移到更经济的 ubuntu-slim runner，帮助降低 CI 成本。此外，项目还附带了一个 AI agent prompt 以实现类似的分析逻辑。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
项目核心是基于静态分析和模式匹配的 YAML 工作流转换工具，技术实现相对常规。AI 部分仅提供了一个用于复现分析逻辑的 LLM prompt，未涉及深度 AI 技术或模型创新。

### 实用性 (评分: 7.5/10)
对使用 GitHub Actions 的开发者或 DevOps 工程师具有较高实用价值，能自动化评估并安全迁移至更省钱的 ubuntu-slim runner，有效降低 CI/CD 成本。附带的 AI prompt 也为自动化重构提供了可借鉴的实践。

### 社区活跃度 (评分: 4.5/10)
获得 69 个点赞但仅有 3 条评论，表明项目获得了一定关注但未引发深入讨论，社区互动性偏低。

## 项目链接
https://github.com/fchimpan/gh-slimify
