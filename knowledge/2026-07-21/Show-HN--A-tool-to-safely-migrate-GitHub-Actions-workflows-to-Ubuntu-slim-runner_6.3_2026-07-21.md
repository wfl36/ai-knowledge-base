# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.3  
**状态：** 正常  
**标签：** DevOps, CI/CD, 开源工具, Show HN, LLM Agent  
**更新日期：** 2026-07-21  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 综合总结
该项目是一个 GitHub CLI 扩展，用于自动分析并安全地将 GitHub Actions 工作流迁移至更便宜的 ubuntu-slim runner，帮助开发者降低 CI 成本。项目还附带了一个可复现该分析逻辑的 AI Agent prompt，为 LLM 自动化重构 CI/CD 提供了思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
工具基于 YAML 解析和规则匹配实现静态分析，检测 CI 工作流中的依赖与兼容性问题；同时结合 LLM Agent prompt 探索自动化重构，技术实现偏向工程应用而非底层创新。

### 实用性 (评分: 8.0/10)
对使用 GitHub Actions 的开发者及 DevOps 从业者具有较高实用价值，能自动化繁琐的迁移检查，直接助力降低 CI 运行成本；AI prompt 部分也为 LLM 集成 CI/CD 流程提供了参考。

### 社区活跃度 (评分: 5.0/10)
获得 69 个点赞但仅有 3 条评论，表明项目具有一定实用吸引力，但未引发深度的技术讨论，社区互动性一般。

## 项目链接
https://github.com/fchimpan/gh-slimify
