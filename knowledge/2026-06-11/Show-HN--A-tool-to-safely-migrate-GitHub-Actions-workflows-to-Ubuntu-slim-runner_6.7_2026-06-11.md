# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.7  
**状态：** 正常  
**标签：** DevOps, CI/CD, GitHub-Actions, LLM-Agent, Show-HN, 开源工具  
**更新日期：** 2026-06-11  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
一个开源的 GitHub CLI 扩展（gh-slimify），用于自动分析并安全地将 GitHub Actions 工作流迁移到更廉价的 ubuntu-slim runner。该工具通过静态分析检测不兼容模式，并额外提供了实现相同功能的 AI 智能体提示，对 DevOps 从业者降低 CI 成本具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
该工具涉及对 GitHub Actions YAML 工作流的静态分析与语义解析，以检测操作系统级别的依赖项（如 Docker、系统服务、缺失包等）。此外，项目附带了一个 AI 智能体提示，展示了如何将 LLM 应用于自动化代码/工作流重构，结合了传统解析与 LLM 智能体能力。

### 实用性 (评分: 8.0/10)
对 DevOps 和 CI/CD 从业者具有很高的实用价值，自动执行了繁琐且易错的兼容性检查任务，帮助团队安全地迁移到更廉价的 ubuntu-slim runner 以降低成本。附带的 AI 智能体提示也为 AI 工程师探索自动化重构提供了参考。

### 社区活跃度 (评分: 5.5/10)
获得了 69 个 points 和 3 条评论，表明社区对该痛点有中等程度的认可，但讨论深度有限。作为实用型小工具，它解决了一个具体问题，但缺乏引发广泛热议的争议性或颠覆性。

## 项目链接
https://github.com/fchimpan/gh-slimify
