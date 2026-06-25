# Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 知识蒸馏, 策略优化, 强化学习, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.24064v1 Announce Type: new Abstract: Distilling reasoning capabilities from strong to weak language models typically involves imitating specific solution trajectories, effectively transferring what to answer rather than how to reason. This trajectory-level imitation encourages memorization of instance-specific steps rather than acquisition of transferable problem-solving skills, limiting generalization to novel problems. We propose Strategy-Guided Policy Optimization (SGPO), which replaces instance-level trajectory imitation with reusable strategy distillation. SGPO extracts structured strategy descriptions from strong-model responses and, for each problem, constructs both autonomous and strategy-guided trajectories to enable direct comparison of the model's behavior with and without strategic guidance. The framework then addresses two key questions. For how to distill, a token-level forward-KL objective selectively transfers the distributional shift induced by strategy conditioning into the unguided policy, with proximal constraints ensuring stability. For when to distill, adaptive instance-level weighting strengthens guidance when autonomous exploration falls short and reduces it as the model's own competence grows. Experiments on four mathematical benchmarks across two model families show that SGPO consistently outperforms SFT, on-policy RL, and hybrid-policy baselines, improving the average score by 2.2 points over the strongest baseline on Qwen2.5-7B-Instruct. Analysis reveals that the forward-KL objective provides an inherently selective distillation signal that outperforms direct trajectory imitation, and that strategy distillation exhibits complementary scaling with base model capability.

## 综合总结
本文提出SGPO（Strategy-Guided Policy Optimization），旨在解决传统大模型推理能力蒸馏中仅模仿轨迹导致泛化性差的问题。SGPO通过提取强模型的可复用策略描述，构建自主与策略引导轨迹进行对比，并采用token级forward-KL目标函数和自适应实例级权重机制，实现选择性且稳定的策略转移。实验表明，SGPO在多个数学推理基准上显著优于SFT和常规RL方法，揭示了策略蒸馏相比轨迹模仿的优越性及其与基础模型能力的互补缩放效应。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
本文在LLM推理能力蒸馏上提出了重要的范式转换，从传统的实例级轨迹模仿（学答案）转向可复用的策略蒸馏（学思路）。提出的token级forward-KL目标函数和自适应实例级权重机制，不仅解决了'如何蒸馏'和'何时蒸馏'的核心问题，还从理论和实验上证明了其选择性转移机制优于直接轨迹模仿，且策略蒸馏与基础模型能力呈现互补缩放效应，技术深度和论证严谨度均较高。

### 实用性 (评分: 8.2/10)
对大模型训练从业者具有很高的落地参考价值。SGPO提供了一套清晰的算法框架，可直接应用于数学/逻辑推理等复杂任务的模型蒸馏与强化训练中，替代或补充现有的SFT和RLHF流程，有效提升弱模型的泛化推理能力，算法设计中的近端约束和自适应权重也保障了训练的稳定性。

### 社区活跃度 (评分: 8.5/10)
LLM推理与知识蒸馏是当前AI社区的核心热点话题。该论文源自arXiv，作者团队包含学术界与工业界研究者，其提出的'策略蒸馏优于轨迹模仿'的观点对现有训练范式具有启发意义，且在主流开源模型（Qwen2.5等）和标准数学基准上给出了扎实的实验验证，具备较高的时效性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.24064
