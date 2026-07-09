# When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 推理, 上下文搜索, 采样复杂度, 强化学习, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06720v1 Announce Type: new Abstract: Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve high success probability. We show that when reflections reliably localize early mistakes, in-context search can yield exponential improvements over the base model, solving problems with exponentially small zero-shot pass rates using only a polynomial number of sequential attempts, whereas when this property fails, conditioning on past attempts offers no asymptotic benefit over parallel sampling. We further show that these gains are robust and learnable: approximate posterior updates suffice, and cross-entropy training on search rollouts recovers the required behavior with polynomial sample complexity. Finally, we show that under a stagewise abstraction of reinforcement learning with verifiable rewards, the optimal policy extension implements the same posterior reweighting rule. We validate key qualitative predictions of the theory on real large reasoning models.

## 综合总结
本文从采样复杂度理论出发，将大模型的上下文搜索（反思推理）建模为近似推断过程。研究严格证明，当自我反思能可靠定位早期错误时，顺序反思相比基础模型可实现指数级性能提升；否则与并行采样无渐近差异。该增益具备鲁棒性和可学习性，且与RLVR最优策略等价，并在真实推理模型上得到验证，为推理阶段的计算扩展提供了关键理论基石。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
将大模型的上下文搜索（反思推理）创新性地建模为推理轨迹上的近似推断，从采样复杂度理论严格证明：当自我反思能可靠定位早期错误时，顺序反思相比基础模型可实现指数级性能提升；若此条件失效，则退化为与并行采样等价。此外，证明了该增益的鲁棒性与可学习性（近似后验更新与交叉熵训练即可），并在阶段抽象下与RLVR的最优策略建立了理论一致性，理论深度与严谨性极高。

### 实用性 (评分: 8.0/10)
为推理阶段的计算扩展策略提供了明确的理论指导：只有当模型具备可靠的早期错误定位能力时，顺序反思才优于简单的并行采样。这一结论直接指导了反思机制的设计、自我纠错模型的训练以及RLVR策略的优化方向，避免在无效的反思回路上浪费算力。

### 社区活跃度 (评分: 9.0/10)
切中当前大模型推理阶段计算扩展的核心热点，特别是o1-like模型的反思与自我修正机制。作者团队包含知名AI学者Amnon Shashua，理论结合真实大型推理模型的实证验证，来源权威且极具启发性，预计将在学术界和工程界引发广泛关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.06720
