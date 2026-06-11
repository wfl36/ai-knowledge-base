# Compatibility-Aware Dynamic Fine-Tuning for Large Language Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 微调, SFT, 优化, 对齐  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11206v1 Announce Type: new Abstract: Supervised Fine-Tuning (SFT) is the predominant paradigm for aligning large language models (LLMs), yet it suffers from optimization instability and limited generalization. Recent work attributes this issue to pathological gradient scaling and proposes Dynamic Fine-Tuning (DFT) to correct it at the token level. However, DFT assumes all demonstrations are equally suitable learning targets, an assumption violated by the strong heterogeneity of large-scale instruction data, where demonstration-policy mismatch induces high-variance updates at the sample level. We introduce Compatibility-Aware Dynamic Fine-Tuning (CADFT), a principled extension of DFT that controls sample-level optimization variance. CADFT derives a dynamic, policy-dependent compatibility signal from model likelihoods to modulate supervised updates, suppressing high-variance gradients from incompatible demonstrations. We further propose a delayed, low-frequency compatibility-guided rewriting strategy to transform persistently incompatible demonstrations into learnable targets. We show that CADFT can be interpreted as a variance-controlled estimator that generalizes token-level stabilization in DFT to the sample level. Extensive experiments demonstrate improved stability, generalization, and cold-start reinforcement learning initialization, while remaining fully supervised and independent of explicit reward modeling.

## 综合总结
本文提出兼容性感知的动态微调方法（CADFT），解决了现有动态微调（DFT）在大规模异构指令数据下因样本不匹配导致的高方差更新问题。CADFT通过模型似然推导动态兼容性信号来抑制不兼容样本的梯度，并引入延迟低频重写策略转化不兼容样本。理论上，CADFT将DFT的token级稳定泛化至样本级，作为一种方差控制估计器。实验表明，该方法在提升稳定性、泛化能力及RL冷启动初始化方面效果显著，且无需显式奖励模型。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文精准识别了SFT中DFT方法在处理异构指令数据时的样本级方差问题，从理论上将token级稳定化扩展至样本级，提出方差控制估计器视角。兼容性信号的推导与延迟重写策略设计严谨，理论深度与创新性较高。

### 实用性 (评分: 8.0/10)
CADFT无需显式奖励模型即可提升SFT的稳定性与泛化能力，对大模型训练从业者具有直接指导意义。兼容性引导重写策略也可用于数据清洗与构造，但动态似然计算与重写可能带来额外计算开销，需工程优化后落地。

### 社区活跃度 (评分: 8.5/10)
SFT与LLM对齐是当前大模型领域的核心痛点，话题时效性极强。作为arXiv最新论文，其扎实的理论推导和切中要害的问题定义，有望在学术和工业界引发关注与后续研究。

## 项目链接
https://arxiv.org/abs/2606.11206
