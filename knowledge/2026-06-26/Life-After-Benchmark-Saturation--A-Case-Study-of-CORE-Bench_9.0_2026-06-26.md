# Life After Benchmark Saturation: A Case Study of CORE-Bench

**评分：** 9.0  
**状态：** 正常  
**标签：** Agent, 评测/基准测试, 人机协作, AI for Science, 论文, 案例研究  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26158v1 Announce Type: new Abstract: When a benchmark's accuracy saturates, it is often retired and replaced with a more challenging version. We show that this approach privileges accuracy and misses the opportunity to study six other key dimensions of agent performance: construct validity issues such as shortcuts, out-of-distribution generalizability, efficiency, reliability, the relative importance of the model versus the scaffold, and uplift from human-agent collaboration. We use CORE-Bench Hard, a benchmark for computational reproducibility of scientific code, as a case study to demonstrate that measuring agents along these dimensions yields meaningful insights into agent performance even after accuracy saturates. First, we surface threats to construct validity in CORE-Bench Hard that are difficult to anticipate with less capable agents. We introduce an improved benchmark, CORE-Bench v1.1, and an out-of-distribution task suite, CORE-Bench OOD. Second, we find that despite accuracy saturation, CORE-Bench v1.1 remains useful for measuring efficiency, reliability, model performance, and scaffold performance. Finally, we conduct a small-scale randomized experiment to measure uplift from human-agent collaboration on real-world computational reproducibility tasks. We find a statistically significant speedup by about a factor of two -- likely underestimated due to one-fifth of human-only reproductions reaching the time limit before completing -- and describe various other findings. Together, our contributions present a more rigorous alternative to the dominant accuracy-centric evaluation paradigm.

## 综合总结
本文挑战了AI领域长期以来的“准确率中心”评测范式，指出基准测试准确率饱和并非终点，而是研究Agent在构造效度、泛化性、效率、可靠性及人机协作等多维度表现的起点。基于CORE-Bench的案例研究与随机实验表明，多维度评估能揭示被单一准确率掩盖的关键问题，并提出了更具严谨性的评测新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
挑战了基准测试准确率饱和即废弃的传统范式，提出在饱和后应深入挖掘构造效度、OOD泛化性、效率、可靠性、模型与脚手架相对重要性及人机协作提升等六个关键维度。通过CORE-Bench案例与随机对照实验严谨论证，展现了极高的理论深度与研究洞见。

### 实用性 (评分: 8.5/10)
提出的多维度评估框架为Agent评测提供了可操作的新标准，有效释放了已饱和基准的剩余价值。改进的CORE-Bench v1.1及OOD任务集可直接用于实际评测，人机协作的量化方法对AI工程落地与工具设计具有直接的指导意义。

### 社区活跃度 (评分: 9.5/10)
直击当前大模型社区“刷榜泛滥”与“评测失效”的核心痛点，话题时效性极强。作者团队包含知名学者Arvind Narayanan，权威性与可信度极高，该研究有望引发AI社区对评测范式的深刻反思与重构。

## 项目链接
https://arxiv.org/abs/2606.26158
