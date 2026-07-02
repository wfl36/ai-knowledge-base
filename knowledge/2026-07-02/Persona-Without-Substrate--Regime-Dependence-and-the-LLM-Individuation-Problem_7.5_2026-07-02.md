# Persona Without Substrate: Regime-Dependence and the LLM Individuation Problem

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 可解释性, 表示工程, 个体化, 本体论, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00006v1 Announce Type: new Abstract: Beckmann & Butlin's (2026) ontological framework for the LLM individuation problem inherits an unargued cross-regime co-reference assumption from the persona-vectors literature: that the same direction picks out the same content under prompt-conditioning, gradient-descent fine-tuning, and inference-time steering. We present four empirical wedges from persona-topology experiments on Qwen3-4B-Instruct and Mistral-7B-Instruct-v0.2 - non-collinearity of prompt-extracted vectors and fine-tune basins; fictional personas displacing the model along real-anchor directions more strongly than real anchors do; contradictory-valenced mixtures biased toward a training-history-determined attractor; and asymmetric compositional algebra under inference-time arithmetic versus fine-tune-time chimera training - that jointly undermine the assumption. We propose regime-indexed individuation: the identity unit for representational content is a (vehicle, regime) pair, not a vehicle alone. Under this framework, Beckmann & Butlin's three candidate positions describe three different regime-internal objects rather than competing for the same referent; the same diagnosis applies to Mollo & Milli\`ere, Chalmers, and Cerullo.

## 综合总结
本文批判了LLM个体化研究中的“跨体制同指假设”，通过四组实证反例证明提示词、微调与推理引导下的表征向量不可等价。作者提出“体制索引个体化”框架，主张表征同一性单位为（载体，体制）对，澄清了不同操作体制下的本体论混淆，对大模型可解释性与表示工程具有深刻的理论启示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文针对大模型个体化问题，深刻批判了现有本体论框架中未经证实的“跨体制同指假设”。通过四组严谨的实证反例（涉及提示提取、微调盆地与推理引导的非线性/非对称性），推翻了“同一方向即同一内容”的直觉，并创新性地提出“体制索引个体化”框架，将同一性单位定义为（载体，体制）对，理论深度与论证严密性极高。

### 实用性 (评分: 5.0/10)
论文偏向基础理论与哲学探讨，直接指导工程落地的价值相对有限。但其结论对从事表示工程、模型可控性微调及推理时引导的研究者具有重要警示意义，提醒从业者不同操作体制下的表征向量不可直接混用或等价替换，避免在模型控制与编辑时产生预期外的偏差。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，直击当前大模型可解释性与表示工程的前沿争议，且直接对话2026年最新文献。基于主流开源模型（Qwen3, Mistral）的实证支撑增强了其学术可信度，在AI哲学、认知科学与可解释性交叉领域具有较高影响力潜力。

## 项目链接
https://arxiv.org/abs/2607.00006
