# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.2  
**状态：** 正常  
**标签：** DevOps, CI/CD, GitHub Actions, 开源工具, 发布, LLM Agent  
**更新日期：** 2026-06-08  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者发布了一款开源 GitHub CLI 扩展 gh-slimify，用于自动化且安全地将 GitHub Actions 工作流迁移至更便宜的 ubuntu-slim runner。该工具能扫描并检测不兼容模式，一键修复安全项。此外，项目还附带了一个 LLM Agent prompt 以复现该分析逻辑。该工具对 DevOps 工程师极具实用价值，但在 HN 上讨论深度有限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
工具通过静态分析解析 GitHub Actions YAML 工作流，检测 Docker、服务、缺失包等不兼容模式，实现安全迁移。技术实现涉及 GitHub CLI 扩展开发与工作流配置解析，并创新性地将迁移逻辑转化为 LLM Agent prompt，展示了将具体工程规则映射给 AI 执行的技术探索，具有一定技术深度但非底层突破。

### 实用性 (评分: 8.0/10)
对 DevOps 和 CI/CD 维护者具有极高的实用价值，能自动化繁琐的迁移检查，降低运行成本并避免构建失败；对 AI 从业者而言，其附带的 Agent prompt 提供了“如何将确定性工程逻辑转化为 LLM 可执行指令”的良好参考案例，具备实际借鉴意义。

### 社区活跃度 (评分: 4.5/10)
获得 69 个点赞，表明社区认可其解决的痛点与实用价值，但仅有 3 条评论，说明讨论未深入展开，缺乏对边缘情况或底层逻辑的深度探讨，社区互动热度偏低。

## 项目链接
https://github.com/fchimpan/gh-slimify
