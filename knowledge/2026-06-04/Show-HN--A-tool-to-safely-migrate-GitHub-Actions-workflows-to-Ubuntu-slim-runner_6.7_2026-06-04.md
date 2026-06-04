# Show HN: A tool to safely migrate GitHub Actions workflows to Ubuntu-slim runner

**评分：** 6.7  
**状态：** 正常  
**标签：** DevOps, CI/CD, GitHub Actions, LLM Agent, 开源, Show HN, 工具  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN!<p>I’ve been running GitHub Actions workflows for a while, and when GitHub announced the new ubuntu-slim runners as a cheaper alternative to ubuntu-latest, I wanted to migrate—but figuring out which workflows are safe to switch turned out to be surprisingly tedious.<p>You need to check for Docker usage, services, containers, step failures due to missing packages, and whether jobs rely on tools not available in the slim image.<p>So I built gh-slimify, a GitHub CLI extension that automates all of this. It scans your repository, detects which jobs can be migrated, flags incompatible patterns, identifies missing commands, and can update only the safe workflows with a single command.<p>gh extension install fchimpan&#x2F;gh-slimify
gh slimfy      # Analyze workflows
gh slimfy fix  # Update only jobs that are safe to migrate<p>It’s open source (MIT).
As a bonus: the README also includes an AI agent prompt that reproduces the same workflow-migration analysis—useful if you want to integrate the logic into an LLM agent or experiment with automated refactoring.<p>I’d love feedback—especially on edge cases, false positives&#x2F;negatives, or patterns it should detect better.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
工具核心在于对GitHub Actions YAML工作流的静态分析，识别Docker、服务、缺失包等依赖兼容性问题，并自动修改配置。同时提供了可复现该逻辑的AI Agent Prompt，展示了将确定性规则分析与LLM推理结合的实践，技术实现具有一定工程深度。

### 实用性 (评分: 8.0/10)
对使用GitHub Actions的开发者和DevOps工程师具有极高的实用价值，能自动化完成繁琐的迁移评估和修改工作，直接帮助团队降低CI成本。附带的AI Agent提示词也为从业者探索自动化代码重构提供了参考。

### 社区活跃度 (评分: 5.5/10)
获得了69个点赞，表明社区对该降本增效工具的认可，但仅有3条评论，说明讨论尚未深入展开，可能处于早期尝鲜阶段。

## 项目链接
https://github.com/fchimpan/gh-slimify
