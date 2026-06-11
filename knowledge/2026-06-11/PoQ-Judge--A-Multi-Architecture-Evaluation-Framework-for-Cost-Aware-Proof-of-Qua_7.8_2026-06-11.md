# PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, 去中心化推理, 评估框架, 质量证明, 成本优化, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11196v1 Announce Type: new Abstract: Decentralized LLM inference networks need lightweight, reference-free quality evaluation for Proof of Quality (PoQ). We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references. We study three architectures across the quality-cost tradeoff: a TextCNN judge, a MiniLM cross-encoder, and a DeBERTa judge. Using two-stage training on UltraFeedback plus GPT-labeled in-domain data, the best model reaches 0.747 Pearson correlation with the ground-truth proxy on a held-out test set, outperforming reference-based evaluators from prior work. As a reference-free component in composite scoring, it achieves 0.645 Pearson correlation, matching the best single reference-based evaluator while removing the need for reference answers. We also show that online calibration identifies semantic quality as the dominant dimension and that cascade evaluation reduces cost by 72.7 percent with only modest quality loss. Results are much stronger on QA than summarization, pointing to proxy quality as the main remaining limitation.

## 综合总结
本文提出PoQ-Judge，一个面向去中心化LLM推理网络的无参考质量评估框架。通过训练TextCNN、MiniLM和DeBERTa三种架构的评判模型，并结合两阶段训练，该框架在无参考条件下实现了与有参考评估器相当甚至更优的性能（Pearson相关系数0.747）。此外，研究提出的级联评估机制能在仅带来轻微质量损失的情况下将成本降低72.7%，为去中心化AI基础设施的节点质量证明提供了低成本、高效率的实用解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.8/10)
提出了PoQ-Judge框架，针对去中心化LLM推理网络的无参考质量评估需求，创新性地设计了多架构（TextCNN, MiniLM, DeBERTa）对比与级联评估机制。两阶段训练策略严谨，在成本与质量的权衡分析上具有深度，且无参考评估性能超越了传统有参考方法，但受限于代理质量，在摘要任务上表现较弱，整体研究扎实但未脱离现有模型范式。

### 实用性 (评分: 8.5/10)
对去中心化AI网络从业者具有极高的落地指导价值。其提供的无参考评估方案和级联降本策略（降低72.7%成本）可直接应用于节点质量证明系统的构建，解决了去中心化场景下缺乏标准答案的痛点，工程适用性极强。

### 社区活跃度 (评分: 7.2/10)
去中心化LLM推理是当前及未来的热点方向，该论文紧扣“质量证明”这一核心痛点，时效性强。作为arXiv预印本，其方法论详实，但在广泛社区中的权威性和影响力仍需时间检验，主要影响圈层集中在去中心化AI基础设施领域。

## 项目链接
https://arxiv.org/abs/2606.11196
