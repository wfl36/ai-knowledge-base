# Interpreting Latent CoT Reasoning as Dynamical Systems

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 推理, 潜在推理, 可解释性, 动力系统, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09698v1 Announce Type: new Abstract: Recent latent reasoning methods, such as CODI and COCONUT, face a fundamental interpretability problem: they maintain multiple superimposed candidate traces in the hidden space at each step, unlike explicit- CoT, which follows a single transparent reasoning trace. Existing mechanistic methods show compression, shortcuts, and superposition without explaining how reasoning evolves across latent steps. To address this gap, we model latent token sequences as trajectories in representation space and apply dynamical systems analysis to characterize the evolution of reasoning. Using quantitative measures, such as step-to-step change, direction consistency, and Lyapunov sensitivity, alongside qualitative projections, such as UMAP and DMD/PHATE, we show that latent CoT exhibits structured, non-random dynamics with two distinct stability classes. CODI behaves as a stable attractor, while COCONUT behaves as an unstable expanding system, and SIM-CoT supervision tightens both behaviors without changing the underlying dynamics. This framework advances the interpretability of latent CoT reasoning dynamics and provides actionable insights for improving latent reasoning performance. Code1 and Project page2 available online.

## 综合总结
本文针对潜在推理方法（如CODI和COCONUT）存在的可解释性难题，创新性地引入动力系统理论，将潜在token序列建模为表示空间中的轨迹。通过定量与定性分析，揭示了潜在CoT非随机的结构化动力学特征，并发现CODI表现为稳定吸引子，而COCONUT表现为不稳定扩张系统。该研究不仅深化了对潜在推理演化机制的理论理解，还为优化模型动力学行为和提升推理性能提供了可操作的指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在潜在推理的可解释性方面展现了极高的研究深度与新颖性。创新性地将动力系统理论引入潜在CoT（Chain-of-Thought）分析，将隐空间中的token序列建模为轨迹，突破了现有机制性解释仅停留在压缩和叠加的局限。通过引入Lyapunov敏感性、方向一致性等定量指标与UMAP/DMD等定性投影，严谨地揭示了CODI（稳定吸引子）与COCONUT（不稳定扩张系统）两种截然不同的动力学本质，论证严密且具有深刻的理论洞见。

### 实用性 (评分: 7.5/10)
对AI研究者和工程师具有较高参考价值。虽然动力系统分析偏理论，但论文明确指出了不同潜在推理架构的动力学行为差异，并提供了改进潜在推理性能的'可操作见解'（actionable insights），例如SIM-CoT监督能在不改变底层动力学的情况下收紧行为。结合其开源的代码与项目页面，从业者可以复现分析流程，用于评估和指导自家潜在推理模型的架构选择与训练策略优化。

### 社区活跃度 (评分: 8.5/10)
潜在推理是当前大模型推理能力提升的前沿热点，而其可解释性黑盒问题是社区亟待解决的痛点，本文时效性极强。arXiv作为权威预印本平台，保证了成果的及时传播；针对CODI和COCONUT这两种社区高度关注的代表性方法进行剖析，切中要害。该框架为后续潜在推理研究提供了新的分析范式，预计将在大模型推理与机制可解释性细分领域产生显著影响力。

## 项目链接
https://arxiv.org/abs/2607.09698
