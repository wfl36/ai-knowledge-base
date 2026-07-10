# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 5.2  
**状态：** 待复核  
**标签：** DevOps, CI/CD, 工具, 发布, 开源  
**更新日期：** 2026-07-10  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者开发并开源了 gh-slimify，一个 GitHub CLI 扩展工具，用于自动化将 GitHub Actions 工作流从 ubuntu-latest 安全迁移到更便宜的 ubuntu-slim runner。该工具能扫描仓库、检测兼容性、标记不兼容模式并一键更新安全的工作流。此外，README 中还附带了一个 AI Agent 提示词，可用于复现相同的迁移分析逻辑。该工具对 DevOps 从业者具有较高实用价值，但社区讨论度一般。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 4.0/10)
工具核心逻辑基于 YAML 解析与规则匹配，判断 CI 工作流的兼容性，技术实现相对常规；AI 相关部分仅为 README 中提供的一个 LLM 提示词，用于复现迁移分析逻辑，整体技术深度与含金量一般。

### 实用性 (评分: 7.5/10)
对 DevOps 工程师和 CI/CD 维护者具有较高参考与使用价值，能显著降低迁移成本与试错风险；附带的 AI Agent 提示词也为 AI 从业者探索自动化代码/配置重构提供了实践思路，但应用场景相对局限。

### 社区活跃度 (评分: 4.0/10)
获得了 69 个点赞，作为 Show HN 项目获得了一定初始关注，但仅有 3 条评论，表明社区讨论深度不足，未引发广泛热议或深入的技术反馈。

## 项目链接
https://github.com/fchimpan/gh-slimify
