# SLIM-RL: Risk-Budgeted Random-Masking RL for Diffusion LLMs Without Trajectory Slicing

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 扩散模型, 强化学习, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00208v1 Announce Type: new Abstract: Reinforcement learning for diffusion large language models (dLLMs) has largely moved to trajectory-aware methods. The current state of the art, TraceRL, holds that random masking is mismatched with the model's inference trajectory, and it reconstructs that trajectory during training by slicing each rollout into up to K/s trajectory-aligned training samples, a cost that grows with the block size K. We show that this mismatch can be mitigated without reconstructing the trajectory. Our method, SLIM-RL, bounds the commit risk of each rollout step with a tau-budget decoder, reducing aggregate commit risk in the training data. During optimization, SLIM-RL trains on these risk-controlled rollouts with a trace-free random-masking objective that adapts variance-reduction tools, combining sequence-level importance sampling, deterministic quadrature over masking levels under a mean-preserving, monotonically decreasing per-block mask schedule that we introduce. On SDAR-4B, SLIM-RL matches TraceRL's best MATH500 accuracy on only 0.46x its training samples at block size 16, improving over TraceRL by 6.32% on MATH500 and 11.05% on GSM8K under matched dynamic sampling. At block size 4, the 4B SLIM-RL surpasses the larger LLaDA-8B and Dream-7B dLLMs on math, exceeding LLaDA-8B by 10.76% on MATH500 while staying below the autoregressive Qwen2.5-7B. On code, it improves over TraceRL by 4.20% on MBPP and 3.65% on HumanEval. The tau-budget decoder transfers training-free across LLaDA, Dream, and SDAR. The source code is available at https://github.com/laolaorkkkkk/SLIM-RL .

## 综合总结
SLIM-RL提出了一种针对扩散大语言模型的无轨迹切片强化学习方法。该方法通过tau-budget解码器控制提交风险，并结合方差缩减技术，有效解决了随机掩码与推理轨迹不匹配的问题。实验表明，SLIM-RL在显著降低训练样本需求（0.46x）的同时，在数学和代码基准测试上大幅超越当前SOTA TraceRL，且4B模型性能超越8B模型。其解码器还能免训练迁移至其他dLLM，具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了一种新颖的无轨迹切片强化学习方法SLIM-RL，挑战了现有SOTA TraceRL的轨迹对齐假设。通过引入tau-budget解码器控制每步的提交风险，并结合序列级重要性采样和单调递减掩码调度等方差缩减技术，在不重构轨迹的情况下有效缓解了掩码与推理轨迹的不匹配问题。理论推导与实验论证严谨，技术深度与创新性高。

### 实用性 (评分: 8.5/10)
对dLLM从业者具有极高的实践指导价值。SLIM-RL避免了高成本的轨迹切片，显著提升了训练样本效率（仅需TraceRL的0.46x样本），大幅降低了计算开销。其核心组件tau-budget解码器可免训练迁移至LLaDA、Dream等多种主流dLLM架构，且代码已开源，易于复现和集成到现有训练流程中。

### 社区活跃度 (评分: 8.5/10)
扩散大语言模型的强化学习是当前AI社区的前沿热点。本文针对dLLM训练效率瓶颈提出创新方案，在MATH500、GSM8K等主流基准测试上显著超越现有SOTA，且开源代码，具备较高的可信度和潜在的广泛影响力，有望成为该领域的新基线工作。

## 项目链接
https://arxiv.org/abs/2607.00208
