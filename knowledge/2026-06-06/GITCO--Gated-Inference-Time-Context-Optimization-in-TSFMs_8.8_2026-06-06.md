# GITCO: Gated Inference-Time Context Optimization in TSFMs

**评分：** 8.8  
**状态：** 正常  
**标签：** 时间序列, 基础模型, 推理优化, 论文  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05332v1 Announce Type: new Abstract: Patch-based Time Series Foundation Models (TSFMs) suffer from context poisoning: structurally anomalous patches capture disproportionate attention and silently degrade zero-shot forecast quality. We propose improving TSFM accuracy at inference time by optimizing the input context rather than modifying model weights. We present GITCO (Gated Inference-Time Context Optimization), a lightweight three-component framework: Gate, Router, and Critic that selectively identifies and suppresses harmful patches without any parameter updates. Evaluated on TimesFM 2.5 across 53 GIFT-Eval datasets under K-fold cross-validation, GITCO achieves an average +1.95% MASE reduction on TimesFM 2.5 while capturing 89.9% of the improvement upper bound. We introduce context sensitivity profiles as a new characterizable property of TSFMs: the mapping from time series meta-features to expected accuracy improvement under inference-time context intervention, shaped jointly by model architecture and the statistical structure of the data.

## 综合总结
本文针对基于补丁的时间序列基础模型（TSFMs）中异常补丁捕获过多注意力从而降低零样本预测质量的'上下文污染'问题，提出了GITCO（Gated Inference-Time Context Optimization）框架。该框架通过Gate、Router和Critic三个轻量级组件，在无需参数更新的推理阶段选择性地识别并抑制有害补丁。在TimesFM 2.5上的实验表明，GITCO实现了MASE平均降低1.95%，并捕获了89.9%的改进上限。此外，论文还首次引入了'上下文敏感性特征'作为TSFMs的新属性，为模型与数据交互提供了新解释。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
论文首次揭示并定义了时间序列基础模型（TSFMs）中的'上下文污染'问题，创新性地提出在推理阶段优化输入上下文而非修改模型权重的解决思路。GITCO框架设计精巧，通过Gate、Router和Critic三个组件实现有害补丁的精准抑制，逻辑严密。实验在53个数据集上进行K-fold交叉验证，并对比了改进上限（捕获89.9%），论证极其严谨。此外，引入的'上下文敏感性特征'概念为理解模型架构与数据统计结构的交互提供了新颖的理论视角。

### 实用性 (评分: 9.2/10)
GITCO框架具有极高的工程落地价值。其'无需参数更新'和'推理时生效'的特性意味着从业者可以即插即用地提升现有TSFM的预测精度，无需承担高昂的微调成本。对于金融、运维、气象等存在异常干扰的时间序列预测场景，该方法提供了一种低成本、高回报的精度优化实践指导，适用范围广泛。

### 社区活跃度 (评分: 8.5/10)
时间序列基础模型（TSFM）是当前AI for Science与落地的热点方向，本文结合最新的TimesFM 2.5与GIFT-Eval基准进行评估，时效性极强。arXiv首发来源可靠，提出的'上下文污染'概念直击TSFM痛点，'上下文敏感性特征'有望成为该领域评估与优化模型的新焦点，具备引发社区广泛讨论与后续研究的潜力。

## 项目链接
https://arxiv.org/abs/2606.05332
