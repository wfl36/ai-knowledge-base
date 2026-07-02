# RareDxR1: Autonomous Medical Reasoning for Rare Disease Diagnosis Beyond Human Annotation

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 推理, 医疗AI, 强化学习, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00147v1 Announce Type: new Abstract: Rare disease differential diagnosis is a critical yet arduous clinical task, requiring physicians to identify precise phenotypes from complex, unstructured patient symptoms and execute intricate reasoning within a vast search space. However, existing AI approaches typically rely on pipeline-based phenotype extraction or retrieval-augmented generation, which suffer from critical information loss due to predefined ontologies, retrieval bottlenecks, and a lack of diagnostic logic. To address these challenges, we introduce RareDxR1, an end-to-end reasoning-centric large language model designed for open-domain rare disease diagnosis directly from unstructured clinical notes. We design a progressive end-to-end training framework by synergizing knowledge internalization with autonomous evolutionary learning, thereby bypassing reliance on structured phenotypes and closed-set decision-making. To overcome the limitations of RAG and phenotype restriction, we enabled the deep internalization of fragmented rare-disease knowledge directly into the model's parameters. Moreover, to bridge the gap between model generation and expert reasoning, we propose Reflection-Enhanced Reasoning Sampling (RERS), a strategy that synthesizes expert-level diagnostic trajectories by learning from failures without human annotation. Additionally, we propose a dual-level curriculum reinforcement learning approach for gradually mastering rare disease diagnosis. Experimental results demonstrate that RareDxR1 achieves state-of-the-art accuracy across different benchmarks, marking a significant breakthrough in open-domain rare disease diagnosis. Our code and dataset will be publicly available.

## 综合总结
本文提出RareDxR1，一种用于罕见病诊断的端到端推理大模型。该模型克服了传统RAG和表型提取导致的信息丢失与检索瓶颈，通过反思增强推理采样（RERS）和双层级课程强化学习，实现了无需人工标注的自主推理进化与罕见病知识内化。实验表明其在多个基准上达到SOTA，为开放域罕见病诊断提供了突破性的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该论文提出RareDxR1模型，创新性地摒弃了传统基于RAG和表型提取的流水线方法，转而采用端到端的推理中心架构。通过反思增强推理采样（RERS）实现无需人工标注的自主进化学习，并结合双层级课程强化学习逐步掌握诊断逻辑，将碎片化罕见病知识深度内化于模型参数中，技术路径新颖且论证严谨，具有极高的研究深度。

### 实用性 (评分: 8.5/10)
针对罕见病诊断这一临床痛点，提供了可直接从非结构化临床笔记进行诊断的端到端解决方案，有效避免了传统流水线的信息损耗和检索瓶颈。其无需人工标注的训练策略大幅降低了数据构建成本，对医疗AI从业者具有极高的工程参考价值，但在实际临床部署前仍需严格的医疗合规与安全验证。

### 社区活跃度 (评分: 8.5/10)
紧扣当前大模型推理（如R1系列）和医疗AI的前沿热点，针对罕见病诊断这一高难度且极具社会价值的领域。作为arXiv首发论文，其方法在开放域罕见病诊断上实现了SOTA，极具话题性和启发性，有望在医疗大模型和推理模型社区引发广泛关注和后续研究。

## 项目链接
https://arxiv.org/abs/2607.00147
