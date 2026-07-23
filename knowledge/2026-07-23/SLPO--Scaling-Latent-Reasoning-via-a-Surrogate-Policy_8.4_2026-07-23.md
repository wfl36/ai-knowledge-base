# SLPO: Scaling Latent Reasoning via a Surrogate Policy

**评分：** 8.4  
**状态：** 正常  
**标签：** 大模型, 推理, 强化学习, 测试时计算, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19691v1 Announce Type: new Abstract: Reinforcement learning with verifiable rewards has become the predominant recipe for eliciting test-time scaling in explicit Chain-of-Thought reasoners. Yet this scaling path remains computationally costly, since every intermediate step must be decoded as a language token. Latent reasoning instead carries intermediate computation as continuous vectors and already matches or surpasses explicit CoT at far shorter horizons. Despite this promise, latent reasoners remain largely imitation-bound, while explicit CoT has already moved past imitation via outcome-reward RL. Latent trajectories lack a tractable per-step likelihood and an adaptive stopping interface under fixed thinking budgets, so outcome rewards cannot elicit latent test-time scaling. We introduce Surrogate Latent Policy Optimization (SLPO) to bring outcome-reward RL to autoregressive latent reasoners: an empirical surrogate policy density over latent transitions for trajectory-level credit assignment, and a correctness-supervised stopping head that outcome-reward optimization refines into a variable-horizon policy. Across continuous and soft thinking settings, SLPO improves Pass@$k$ under parallel sampling and allocates longer latent computation to harder instances with higher deterministic accuracy.

## 综合总结
本文针对潜在推理模型受限于模仿学习、无法利用结果奖励进行强化学习扩展的问题，提出了SLPO（Surrogate Latent Policy Optimization）方法。该方法通过经验代理策略密度实现轨迹级信用分配，并利用正确性监督停止头实现动态推理深度，成功将基于结果奖励的RL引入自回归潜在推理中。实验表明，SLPO不仅提升了Pass@k指标，还能根据问题难度自适应分配计算资源，是测试时计算扩展和隐式推理领域的重要突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
提出了代理潜在策略优化（SLPO），首次将基于结果奖励的强化学习引入自回归潜在推理中。通过经验代理策略密度解决潜在轨迹无法进行逐步似然计算的难题，并引入正确性监督停止头实现可变长度的自适应推理，技术方案新颖且论证严谨，有效突破了潜在推理仅依赖模仿学习的瓶颈。

### 实用性 (评分: 8.0/10)
对从事大模型推理和测试时计算优化的工程师具有极高的参考价值。SLPO提供了一套可落地的潜在推理强化学习框架，能够指导如何在连续向量空间中进行轨迹级信用分配和动态停止，适用于需要提升推理效率与性能的模型训练场景。

### 社区活跃度 (评分: 8.5/10)
话题极具时效性，直击当前大模型推理领域从显式CoT向隐式/潜在推理演进的核心痛点。隐式推理与测试时计算是当前学术界和工业界的前沿热点，该研究为隐式推理的强化学习扩展提供了关键解法，来源权威且具备较高影响力。

## 项目链接
https://arxiv.org/abs/2607.19691
