# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.5  
**状态：** 正常  
**标签：** DevOps, GitHub Actions, LLM Agent, 开源, 发布  
**更新日期：** 2026-06-10  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
一款开源的 GitHub CLI 扩展工具，通过静态分析自动检测并安全地将 GitHub Actions 工作流迁移至更省成本的 ubuntu-slim runner，同时附带可复现该逻辑的 LLM Agent prompt。项目直击 CI 成本优化痛点，实用性强，但社区讨论热度一般。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目核心是基于静态分析扫描 GitHub Actions 的 YAML 工作流，检测 Docker、服务容器及缺失包等不兼容模式，判断能否安全迁移至 ubuntu-slim。技术实现属于特定领域的 AST 解析与模式匹配，并创新性地提供了 LLM Agent prompt 来复现该逻辑，展示了传统静态分析与 LLM 结合的自动化重构思路。

### 实用性 (评分: 8.0/10)
对 DevOps 工程师和重度使用 GitHub Actions 的开发者具有很高的实用价值，能直接帮助降低 CI/CD 运行成本，并消除手动排查迁移风险的繁琐工作。附带的 AI Agent prompt 也为 AI 从业者集成类似代码分析逻辑提供了直接参考。

### 社区活跃度 (评分: 5.0/10)
获得 69 个点赞但仅有 3 条评论，表明社区认可其解决痛点的思路，但讨论深度和互动热度较低，可能由于工具定位垂直，受众主要限于关注 CI 成本优化的开发者群体。

## 项目链接
https://github.com/fchimpan/gh-slimify
