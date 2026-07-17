# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 5.8  
**状态：** 待复核  
**标签：** DevOps, CI/CD, GitHub Actions, 开发工具, 发布, 开源  
**更新日期：** 2026-07-17  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
作者发布了开源 GitHub CLI 扩展 gh-slimify，用于自动化且安全地将 GitHub Actions 工作流迁移至更便宜的 ubuntu-slim runner，支持兼容性检测与一键更新，并附带 LLM agent prompt，对 DevOps 从业者具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
工具基于静态分析和规则匹配对 GitHub Actions YAML 工作流进行解析与修改，工程实现有一定复杂度，但未涉及底层算法或模型创新；AI 部分仅停留在 prompt 层面，技术深度相对有限。

### 实用性 (评分: 8.0/10)
对使用 GitHub Actions 的开发者和运维人员极具实用价值，直接解决迁移至低成本 runner 时的繁琐排查痛点，能有效降低 CI 成本，附带的 AI prompt 也为自动化 DevOps 提供了参考。

### 社区活跃度 (评分: 4.5/10)
获得 69 个点赞，表明项目解决的实际痛点引起了一定共鸣，但仅有 3 条评论，说明未引发深入的技术讨论，社区互动热度较低。

## 项目链接
https://github.com/fchimpan/gh-slimify
