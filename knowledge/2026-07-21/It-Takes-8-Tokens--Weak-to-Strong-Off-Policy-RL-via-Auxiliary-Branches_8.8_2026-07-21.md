# It Takes 8 Tokens: Weak-to-Strong Off-Policy RL via Auxiliary Branches

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 强化学习, 推理, 弱到强学习, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16205v1 Announce Type: new Abstract: Reinforcement learning with verifiable rewards has emerged as a standard approach for enhancing reasoning in large language models, which typically optimizes the policy by contrasting multiple self generated rollouts. However, we identify a critical support limited bottleneck in this paradigm: on challenging reasoning tasks, the target model's samples often exhibit semantic redundancy, converging into the same erroneous "reasoning basins" that offer negligible reward contrast for policy updates. In this paper, we propose to overcome this limitation through a weak to strong learning paradigm, where a policy's exploration is informed by a weaker but computationally efficient auxiliary model. We introduce W2SPO, an off policy RL method that injects short auxiliary segments often as brief as 8 tokens into intermediate target model trajectories and the target model then completes the reasoning path from these diverted states. Policy updates are restricted to these short inserted segments based on final verifiable rewards. Empirically, W2SPO achieves superior performance among evaluated 4B scale models on mathematical reasoning benchmarks, outperforming evaluated post trained baselines. Compared with vanilla GRPO under the same sampling budget, W2SPO improves Pass@1 from 62.3% to 64.2% while achieving a 3.55 times training speedup. These results suggest that weak auxiliary branches can induce stronger target reasoning policies by expanding local exploration support.

## 综合总结
本文针对LLM强化学习中因'推理盆地'导致的探索受限问题，提出了一种弱到强的离线强化学习方法W2SPO。该方法通过在目标模型推理轨迹中注入弱模型生成的极短辅助片段（短至8 tokens），有效打破局部最优并扩大探索空间。实验表明，在4B模型上，W2SPO相比GRPO不仅提升了Pass@1指标，还实现了3.55倍的训练加速，为大模型推理强化学习提供了一种高效且易落地的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
深刻揭示了LLM在on-policy RL中面临的'推理盆地'导致支持受限的瓶颈问题，创新性地提出弱到强学习范式W2SPO。通过引入弱模型生成的极短辅助分支（仅8 tokens）来扰动目标模型的推理轨迹，有效扩大了局部探索支持，理论分析与算法设计巧妙且严谨。

### 实用性 (评分: 9.0/10)
对LLM强化学习从业者具有极高的实践指导价值。W2SPO方法实现简单，对现有GRPO框架改动小，在同等采样预算下不仅将Pass@1提升了1.9%，还实现了3.55倍的训练加速，极具工业落地前景，可直接应用于数学、代码等推理任务的RL微调流程中。

### 社区活跃度 (评分: 8.5/10)
紧扣当前大模型强化学习与推理能力提升的热点，将'弱到强'概念与RL探索机制结合，视角新颖。虽然目前仅在4B规模模型上验证，但其显著的效率与效果提升使其具备成为RL训练新范式的潜力，话题时效性与关注度极高。

## 项目链接
https://arxiv.org/abs/2607.16205
