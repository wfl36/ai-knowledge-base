# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.2  
**状态：** 正常  
**标签：** GitHub Actions, DevOps, 开源工具, 发布  
**更新日期：** 2026-07-14  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者发布了 gh-slimify，一个开源的 GitHub CLI 扩展，用于安全地将 GitHub Actions 工作流迁移到更便宜的 ubuntu-slim runner。该工具能自动扫描、检测兼容性并安全更新工作流，同时提供了一个 AI agent prompt 以支持 LLM 自动化重构，对降低 CI/CD 成本有直接帮助。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
该工具基于静态分析和规则匹配解析 GitHub Actions YAML 文件，检测 Docker、services、缺失包等不兼容模式并实现自动化重构，技术实现偏向工程应用，深度适中；附带的 AI Agent prompt 展示了 LLM 在自动化代码/配置重构场景中的应用思路。

### 实用性 (评分: 8.0/10)
对使用 GitHub Actions 的开发者和 DevOps/MLOps 工程师具有较高实用价值，直接解决了向 ubuntu-slim runner 迁移时的安全排查痛点，有助于降低 CI/CD 运行成本并减少人工试错成本。

### 社区活跃度 (评分: 4.5/10)
获得 69 个点赞和仅 3 条评论，社区关注度偏低。虽然工具解决的痛点明确，但受众相对局限，且工具逻辑直白，未引发广泛或深入的社区讨论。

## 项目链接
https://github.com/fchimpan/gh-slimify
