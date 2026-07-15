# Belief-reality separation lives in routing over a shared value slot in language models

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 机制可解释性, 心智理论, 推理, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11945v1 Announce Type: new Abstract: Capable language models hold what a character believes apart from what is true: told "Anna believes the cup is blue; in reality it is red," they answer blue about Anna and red about the world. Where in the computation does that separation live? We show it rests on two separable mechanisms at two positions. A generic value slot binds the attributed value. A router at the query position selects which frame, the character's belief or reality, a query reads out. Two routes fill the slot: an asserted belief, whose value the text supplies, binds in directly; a derived belief, whose value must be inferred from what the character could see, arrives by a visibility-gated lookback. A subspace trained on either route steers the other, and only the derived route depends on described visibility. The slot itself carries no belief-reality tag: intervening on it moves a reality readout as strongly as a belief one. The separation lives instead in a dissociated pair of routing subspaces, which flip a query between frames without injecting the donor's value. These results hold across three architectures, on stimuli de-confounded against theory-of-mind-benchmark shortcuts; the behavior itself emerges between 3B and 7B across five model families. This paper develops the single belief-reality axis in depth; a companion paper shows the same slot-and-router format is shared across the other non-actual contexts a sentence can open (counterfactual, fictional, temporal).

## 综合总结
本文深入研究了语言模型如何区分“角色信念”与“现实真相”的内部计算机制。研究发现，这种分离依赖于两个可分离的机制：一个通用的“值槽”用于绑定属性值，以及一个位于查询位置的“路由器”用于选择读取框架（信念或现实）。分离并非源于值槽的标签，而是存在于分离的路由子空间中。该机制在3B至7B参数模型中涌现，并在多种架构和去混淆测试中均得到验证，为理解LLM的心智理论及非实际语境处理提供了重要的机制性解释。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文在机制可解释性领域展现了极高的研究深度，创新性地提出了“槽-路由”模型来解释LLM中信念与现实的分离机制。研究不仅区分了断言信念与推导信念的不同绑定路径，还严谨地证明了分离机制存在于路由子空间而非值槽本身，并通过跨架构验证和去混淆实验排除了传统心智理论基准的捷径问题，论证极其严密且新颖。

### 实用性 (评分: 6.5/10)
该研究对理解LLM的幻觉、角色扮演和心智理论能力具有底层启发意义，为未来通过干预路由子空间来纠正模型错误信念或改善对齐提供了理论依据。然而，作为机制解释性基础研究，其结论离直接指导工业界模型训练或应用落地的工程实践尚有距离，主要提供底层认知与架构参考。

### 社区活跃度 (评分: 8.5/10)
主题紧扣当前大模型可解释性与心智理论的研究热点，具有高度的时效性。arXiv预印本发布，研究去除了传统ToM基准的捷径问题，大幅提升了结论的可信度。发现3B-7B参数规模是此能力涌现的临界点，且跨模型家族和语境通用，对学术界理解大模型认知机制具有较强的影响力和参考价值。

## 项目链接
https://arxiv.org/abs/2607.11945
