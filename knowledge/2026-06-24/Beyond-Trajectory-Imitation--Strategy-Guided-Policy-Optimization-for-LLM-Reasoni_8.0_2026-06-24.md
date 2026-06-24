# Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, 策略蒸馏, 强化学习, 论文  
**更新日期：** 2026-06-24  
**来源：** rss  

## 项目描述
arXiv:2606.24064v1 Announce Type: new Abstract: Distilling reasoning capabilities from strong to weak language models typically involves imitating specific solution trajectories, effectively transferring what to answer rather than how to reason. This trajectory-level imitation encourages memorization of instance-specific steps rather than acquisition of transferable problem-solving skills, limiting generalization to novel problems. We propose Strategy-Guided Policy Optimization (SGPO), which replaces instance-level trajectory imitation with reusable strategy distillation. SGPO extracts structured strategy descriptions from strong-model responses and, for each problem, constructs both autonomous and strategy-guided trajectories to enable direct comparison of the model's behavior with and without strategic guidance. The framework then addresses two key questions. For how to distill, a token-level forward-KL objective selectively transfers the distributional shift induced by strategy conditioning into the unguided policy, with proximal constraints ensuring stability. For when to distill, adaptive instance-level weighting strengthens guidance when autonomous exploration falls short and reduces it as the model's own competence grows. Experiments on four mathematical benchmarks across two model families show that SGPO consistently outperforms SFT, on-policy RL, and hybrid-policy baselines, improving the average score by 2.2 points over the strongest baseline on Qwen2.5-7B-Instruct. Analysis reveals that the forward-KL objective provides an inherently selective distillation signal that outperforms direct trajectory imitation, and that strategy distillation exhibits complementary scaling with base model capability.

## 综合总结
本文提出SGPO（Strategy-Guided Policy Optimization），旨在解决传统轨迹模仿导致的泛化性差的问题。SGPO通过从强模型中提取可复用的结构化策略，替代实例级别的轨迹模仿，并利用前向KL目标进行选择性策略转移，结合自适应实例加权动态调整蒸馏时机。实验表明，该方法在多个数学推理基准上显著优于SFT和RL基线，有效提升了弱模型的推理泛化能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了从'轨迹模仿'到'策略蒸馏'的范式转变，直击SFT泛化性差的痛点。在方法设计上，创新性地引入前向KL目标实现选择性策略转移，并结合近端约束保证训练稳定性；同时提出自适应实例加权机制动态调整蒸馏时机，理论论证严谨，技术深度与创新性较高。

### 实用性 (评分: 7.5/10)
SGPO框架为LLM推理能力蒸馏提供了可操作的实践指南，特别是'策略提取+双轨轨迹对比+自适应加权'的流程可直接应用于现有大模型的后训练阶段。但由于需要构建自主与策略引导的双轨轨迹并计算前向KL，工程实现复杂度相对较高，对算力和数据构建有一定要求。

### 社区活跃度 (评分: 8.0/10)
LLM推理能力提升是当前AI领域的核心热点，本文针对SFT泛化性差的问题提出了有效解决方案，极具时效性。实验在多个主流数学基准和开源模型上验证了其优越性，结果显著（平均提升2.2分），来源可信度高，对后续的模型对齐与蒸馏研究有重要启发意义。

## 项目链接
https://arxiv.org/abs/2606.24064
