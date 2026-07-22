# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.7  
**状态：** 正常  
**标签：** GitHub Actions, DevOps, 开发者工具, AI Agent, 发布  
**更新日期：** 2026-07-22  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
开发者发布了 GitHub CLI 扩展工具 gh-slimify，能够自动分析并安全地将 GitHub Actions 工作流迁移至成本更低的 ubuntu-slim runner。该工具可识别不兼容模式并一键修复安全项，同时附带了一个可复现相同迁移逻辑的 AI Agent prompt，为降低 CI 成本及探索自动化重构提供了实用方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目通过静态分析 GitHub Actions 的 YAML 工作流文件，检测 Docker、services 及缺失包等不兼容模式，实现了向 ubuntu-slim 迁移的自动化。同时，项目将此分析逻辑抽象为 LLM Agent prompt，探索了 AI 辅助代码重构与静态分析结合的技术路径，具备一定的工程技巧与 AI 应用实践价值。

### 实用性 (评分: 8.0/10)
对 DevOps 工程师和开发者具有很高的实用价值，能够直接帮助团队降低 CI/CD 运行成本，并规避手动排查迁移带来的潜在风险。附带的 AI Agent prompt 也为 AI 从业者提供了将代码分析逻辑转化为 LLM 自动化工作流的参考范例。

### 社区活跃度 (评分: 5.5/10)
获得 69 个点赞但仅有 3 条评论，表明该项目在特定受众群体中引起了关注并解决了实际痛点，但尚未引发广泛或深度的技术讨论，社区互动热度一般。

## 项目链接
https://github.com/fchimpan/gh-slimify
