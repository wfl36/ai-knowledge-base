# Rater State Bias in RLHF Preference Data: An Audit Framework

**评分：** 8.5  
**状态：** 正常  
**标签：** RLHF, 偏好数据, 数据偏差, 奖励模型, 对齐, 论文, 审计框架  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16195v1 Announce Type: new Abstract: We identify a structured confound in Reinforcement Learning from Human Feedback (RLHF). Pairwise preference labels are intended to reflect the compared outputs, but they may also reflect the rater's state during annotation. Under sustained stressful or distressing conditions, raters' preferences may shift over time. As a result, preference data can encode rater state alongside judgments about response quality. These shifts differ from ordinary disagreement or random label noise. They are state dependent, can be shared across annotators working under similar conditions, and can propagate through reward modeling and policy optimization. We therefore propose rater state shift as a plausible and testable source of structured bias in RLHF preference data. This paper develops a hypothesis and an audit framework for studying this source of bias. We define rater state shift, rater state confound, and correlated rater state bias. We also define survival level emotional authenticity as a measurable response pattern using lexical, pragmatic, discourse, and safety related features. We analyze how correlated rater state bias can survive aggregation and enter learned reward signals. We derive five falsifiable predictions and effect size thresholds for an initial audit. Finally, we present an audit protocol and pilot study plan that can be applied to publicly available instruction tuned models. We do not infer the training history of any specific deployed model. Our goal is to isolate a plausible and testable source of structured bias in RLHF preference data.

## 综合总结
本文揭示了RLHF偏好数据中存在的一种结构性混淆因素——标注者状态偏移，指出持续的负面情绪或压力会导致标注偏好发生系统性变化，且这种偏差能在聚合和奖励建模中存活。作者创新性地提出了相关概念、可测量的特征（生存级情感真实性）以及五个可证伪预测，并提供了一套可落地的审计框架与试点计划，为提升RLHF数据质量和对齐安全性提供了重要理论支撑与实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深入剖析了RLHF中除随机噪声外的一种结构性混淆因素——标注者状态偏移。创新性地提出了“标注者状态混淆”和“相关性标注者状态偏差”概念，并定义了“生存级情感真实性”以量化该偏差。通过推导五个可证伪的预测和效应量阈值，展现了严谨的论证逻辑与理论深度。

### 实用性 (评分: 8.0/10)
论文提出的审计框架和试点研究计划可直接应用于公开的指令微调模型和偏好数据集的质量评估。对于从事RLHF数据标注和奖励模型训练的从业者而言，该框架提供了识别和过滤系统性心理状态偏差的实操方法，具有极高的数据治理参考价值。

### 社区活跃度 (评分: 8.5/10)
RLHF数据质量与大模型对齐是当前AI社区的核心议题。该研究从标注者心理与工作环境角度切入，切中了数据标注行业痛点，话题时效性强且极具启发性。若审计结果被验证，将对现有的偏好数据收集规范产生深远影响。

## 项目链接
https://arxiv.org/abs/2607.16195
