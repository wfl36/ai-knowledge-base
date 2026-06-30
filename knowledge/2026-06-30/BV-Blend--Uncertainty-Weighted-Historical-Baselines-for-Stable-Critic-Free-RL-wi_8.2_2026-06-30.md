# BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 强化学习, RLVR, GRPO, 对齐, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28707v1 Announce Type: new Abstract: Critic-free reinforcement learning with verifiable rewards (RLVR), exemplified by Group Relative Policy Optimization (GRPO), avoids training a value function (critic) and reduces memory and compute overhead relative to critic-based PPO pipelines for aligning large language models. However, GRPO-style advantage estimation depends on prompt-local (within-prompt-group) reward statistics and can be unstable. In particular, when all rollouts in a prompt group receive identical rewards, the within-group reward variance becomes zero, and group normalization yields zero advantages for that group, impeding learning in cold-start regimes with binary verifiers. We introduce BV-Blend, a critic-free framework that stabilizes advantage estimation by combining prompt-local on-policy statistics with semantic-cluster-conditioned historical moments. BV-Blend maintains EMA-tracked reward moments for each cluster, derives a confidence weight from a standard error of the mean (SEM) proxy, and uses this weight to blend historical and prompt-local baseline and variance statistics into a standardized advantage for PPO-style clipped updates. Experiments on verifiable reasoning benchmarks show that BV-Blend improves training stability and performance, and remains robust in regimes where group-normalized methods may stall.

## 综合总结
本文提出BV-Blend框架，解决GRPO等无Critic RLVR方法在二元奖励下因组内方差为零导致学习停滞的问题。通过不确定性加权融合局部在线统计量与语义聚类历史矩，BV-Blend稳定了优势估计，提升了训练鲁棒性，且易于在现有大模型对齐流程中落地。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对GRPO等无Critic强化学习（RLVR）在二元奖励冷启动场景下因组内方差为零导致优势估计失效、学习停滞的痛点，提出了BV-Blend框架。该框架创新性地引入基于语义聚类的历史矩（EMA追踪），与局部在线统计量进行不确定性加权混合，利用标准误差（SEM）代理作为置信度权重来融合基线与方差，有效稳定了优势估计，方法设计严谨且具有针对性。

### 实用性 (评分: 8.0/10)
BV-Blend保持了无Critic架构的低资源消耗优势，同时解决了GRPO在实际训练中容易停滞的问题。其优势计算模块的改进可无缝集成到现有的PPO/GRPO训练管线中，对大模型对齐和推理能力训练的工程实践具有很高的参考价值，落地可行性较强。

### 社区活跃度 (评分: 8.0/10)
研究聚焦于当前大模型强化学习对齐（特别是RLVR和GRPO）的前沿热点，时效性极强。针对DeepSeek R1等模型带火的GRPO算法的已知痛点提出改进，契合社区对稳定、高效RL训练方案的迫切需求，具备较高的潜在影响力和关注度。

## 项目链接
https://arxiv.org/abs/2606.28707
