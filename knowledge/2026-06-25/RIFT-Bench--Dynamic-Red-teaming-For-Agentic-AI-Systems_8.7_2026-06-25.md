# RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 安全, 红队测试, 评估基准, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.23927v1 Announce Type: new Abstract: Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. Building on a novel hierarchical representation, RIFT-Bench operates in two automated phases: Discovery, which extracts system structure, and Scanning, which deploys adaptive adversarial attacks and produces a comprehensive evaluation report. It evaluates the examined system itself, leveraging a broad set of dynamically adaptable adversarial probes across diverse attack vectors and objectives. We demonstrate the effectiveness of the proposed evaluation pipeline across 45 agentic systems spanning a diverse range of implementations, showing that the approach generalizes effectively to heterogeneous agentic architectures. Beyond systems and attacks, RIFT-Bench also supports direct evaluation of mitigation strategies. These key capabilities make RIFT-Bench a scalable foundation for security evaluation of agentic AI systems.

## 综合总结
本文提出了RIFT-Bench，一个针对异构Agentic AI系统的动态红队评估基准。该框架基于图表示驱动，通过Discovery（结构提取）和Scanning（自适应攻击）两个自动化阶段，实现了跨45种不同Agent架构的统一安全评估，并支持缓解策略验证，填补了Agent系统安全评估的空白，具有极高的工程落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了一种基于图表示驱动的动态红队评估方法RIFT-Bench，创新性地将评估分为Discovery（系统结构提取）和Scanning（自适应对抗攻击）两个自动化阶段，有效解决了异构Agent系统难以统一进行安全比较的技术难题，技术深度与创新性兼备，论证严谨且泛化能力强。

### 实用性 (评分: 9.0/10)
该基准提供了高度自动化的评估流水线，不仅支持跨45种异构系统的多向量攻击评估，还能直接评估防御缓解策略的有效性，对Agent开发者和安全工程师具有极高的实操落地价值，可直接应用于Agent系统上线前的安全审计与红队测试。

### 社区活跃度 (评分: 8.5/10)
针对当前Agent系统自主决策能力增强导致攻击面扩大、且缺乏统一安全评估标准的痛点，该研究具有极强的时效性和行业需求。arXiv发布且经过大规模系统验证，来源可信度高，有望成为Agent安全评估领域的重要参考基准。

## 项目链接
https://arxiv.org/abs/2606.23927
