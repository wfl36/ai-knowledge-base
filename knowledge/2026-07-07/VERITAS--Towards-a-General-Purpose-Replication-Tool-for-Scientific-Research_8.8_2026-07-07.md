# VERITAS: Towards a General-Purpose Replication Tool for Scientific Research

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, AI4Science, 代码生成, 复现验证, 论文, 工程实践  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02931v1 Announce Type: new Abstract: AI tools are accelerating scientific publication while the systems that review it struggle to keep up, and independent verification of published research has become both harder and more important. As manual replication is slow and expensive, a growing line of work uses coding agents to automate parts of the process. Existing efforts are largely packaged as benchmarks with companion agents that only run inside the benchmark's own pipeline, and no general-purpose replication tool exists. We present VERITAS, a domain-agnostic replication framework built around CLI coding agents. Given a paper, a code repository, or both, VERITAS extracts the paper's claims, runs the methodology while resolving issues as they arise, and judges each claim against the evidence from experiment runs. The pipeline returns an importance-weighted Replication Score, a severity-rated log of every fix applied, and the patched codebase. We evaluate VERITAS on CORE-Bench and ReplicationBench, 65 papers spanning computer science, social science, medicine, and astrophysics. Against two strong Claude Code baselines on the same model and host environment, VERITAS achieves state-of-the-art performance and leads on every metric on both benchmarks.

## 综合总结
本文介绍了VERITAS，首个面向通用科研复现的自动化框架。针对当前科研论文激增但独立验证困难且昂贵的现状，VERITAS利用CLI编码智能体，实现了从论文/代码库中提取声明、自动运行实验、动态修复问题到最终评判验证结果的端到端闭环。该框架输出复现得分、修复日志及修补代码，在跨学科（计算机、社科、医学、天体物理）的65篇论文评估中，全面超越强基线，达到SOTA。VERITAS为缓解科研可复现性危机提供了极具实用价值的自动化解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了VERITAS，一个基于CLI编码智能体的领域无关科研复现框架。该工作填补了现有复现工具仅限于特定基准测试的空白，通过“提取声明-运行方法-动态解决问题-评判验证”的端到端闭环流程，实现了科研复现的自动化。在65篇跨学科论文的测试中，显著优于强基线模型，展现了出色的技术深度与严谨性。

### 实用性 (评分: 9.0/10)
具有极高的落地价值。VERITAS直接解决当前科研界“论文激增但验证困难”的痛点，输出的重要性加权复现得分、严重性修复日志和修补后的代码库，可为审稿人和研究者提供直接、可操作的参考。其领域无关的特性使其适用范围极广，能切实指导科研复现实践。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击AI加速科研发表带来的可复现性危机这一热点。作者团队具备学术权威性，在主流基准CORE-Bench和ReplicationBench上取得SOTA，结果可信度高。该工作对学术评审机制和科研诚信体系具有潜在的深远影响力。

## 项目链接
https://arxiv.org/abs/2607.02931
