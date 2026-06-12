# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.5  
**状态：** 正常  
**标签：** DevOps, CI/CD, GitHub Actions, 开源工具, Show HN  
**更新日期：** 2026-06-12  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者开源了一款名为 gh-slimify 的 GitHub CLI 扩展，用于自动分析并安全地将 GitHub Actions 工作流迁移至更省钱的 ubuntu-slim 运行器。该工具能检测不兼容模式与缺失依赖，仅更新安全的工作流，并附带了一个可复现该分析逻辑的 AI agent prompt，对使用 GitHub Actions 的开发者具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
项目核心在于对 GitHub Actions YAML 工作流的静态分析与依赖检测，技术实现涉及配置解析与兼容性判断，具备一定的工程复杂度，但非底层技术突破；附带的 AI agent prompt 属于应用层面的提示词工程。

### 实用性 (评分: 8.0/10)
对使用 GitHub Actions 的开发者及 DevOps 工程师具有很高的实用价值，能直接降低 CI/CD 成本并减少繁琐的手动排查工作；AI agent prompt 也为自动化代码重构与 LLM 集成提供了参考思路。

### 社区活跃度 (评分: 5.5/10)
获得 69 个点赞但仅有 3 条评论，表明社区对该工具解决痛点的思路有一定认可，但讨论深度和互动热度相对较低，可能处于初步体验阶段。

## 项目链接
https://github.com/fchimpan/gh-slimify
