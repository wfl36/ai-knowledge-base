# Belief-reality separation lives in routing over a shared value slot in language models

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 机制可解释性, 心智理论, 认知机制, 内部表征, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.11945v1 Announce Type: new Abstract: Capable language models hold what a character believes apart from what is true: told "Anna believes the cup is blue; in reality it is red," they answer blue about Anna and red about the world. Where in the computation does that separation live? We show it rests on two separable mechanisms at two positions. A generic value slot binds the attributed value. A router at the query position selects which frame, the character's belief or reality, a query reads out. Two routes fill the slot: an asserted belief, whose value the text supplies, binds in directly; a derived belief, whose value must be inferred from what the character could see, arrives by a visibility-gated lookback. A subspace trained on either route steers the other, and only the derived route depends on described visibility. The slot itself carries no belief-reality tag: intervening on it moves a reality readout as strongly as a belief one. The separation lives instead in a dissociated pair of routing subspaces, which flip a query between frames without injecting the donor's value. These results hold across three architectures, on stimuli de-confounded against theory-of-mind-benchmark shortcuts; the behavior itself emerges between 3B and 7B across five model families. This paper develops the single belief-reality axis in depth; a companion paper shows the same slot-and-router format is shared across the other non-actual contexts a sentence can open (counterfactual, fictional, temporal).

## 综合总结
本文深入探讨了语言模型中‘信念与现实分离’的计算机制，发现该分离并非基于独立表征，而是依赖于‘共享值槽’与‘路由子空间’两个可分离机制。值槽负责绑定归因值（本身不携带信念/现实标签），路由器则决定查询读取哪个框架。信念输入槽位存在直接绑定（断言信念）和可见性门控回溯（推导信念）两条路径。干预实验表明，分离存在于路由子空间而非值槽中。该结论在跨架构、跨模型家族（3B-7B参数涌现）的去混淆实验中得到验证，为理解LLM的非现实语境处理机制提供了突破性洞见。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
本文在机制可解释性领域展现了极高的研究深度与新颖性。研究精准定位了语言模型中‘信念与现实分离’的计算机制，打破了两者在模型内部完全独立表征的直觉假设，创新性地提出了‘共享值槽-路由子空间’的双机制框架。论证极其严谨，不仅区分了断言信念与推导信念的不同路由路径，还通过干预实验证实了分离发生在路由子空间而非值槽内，且跨3种架构、5个模型家族（3B-7B参数规模）进行了去混淆验证，逻辑闭环完整。

### 实用性 (评分: 6.5/10)
对AI安全、对齐和模型可控性编辑具有较高参考价值。通过定位并干预路由子空间，研究为纠正模型的错误信念或调整其现实认知框架提供了潜在的工程实践方向（如内部状态干预、表征工程）。然而，机制可解释性研究本身偏重理论与微观机制解析，距离普通开发者的日常应用落地仍有距离，主要受众为对齐工程师和机制研究者。

### 社区活跃度 (评分: 8.8/10)
极具时效性与权威性。大模型的心智理论及内部认知机制是当前AI前沿研究的核心热点，该工作直击痛点。研究方法严谨，去除了传统ToM基准的捷径干扰，结果可靠，且伴随论文扩展了反事实/虚构等非现实语境，体系宏大，在学术社区具有较高影响和讨论潜力。

## 项目链接
https://arxiv.org/abs/2607.11945
