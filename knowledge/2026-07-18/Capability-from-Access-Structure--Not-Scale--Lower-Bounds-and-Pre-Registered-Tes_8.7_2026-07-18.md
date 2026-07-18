# Capability from Access Structure, Not Scale: Lower Bounds and Pre-Registered Tests for Hybrid Sequence Models

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 混合架构, 序列模型, 推理, 长上下文, 论文  
**更新日期：** 2026-07-18  
**来源：** rss  

## 项目描述
arXiv:2607.14144v1 Announce Type: new Abstract: The Platonic Representation Hypothesis (PRH) holds that as models scale, representations of heterogeneous networks converge toward a shared model of reality. We propose its sequel and boundary, the Capability Convergence Hypothesis (CCH): under a fixed per-token inference budget, representational convergence does not entail capability convergence. Capability instead converges toward a class, the access-complete hybrid: any architecture holding both a compressive O(1)-state channel and a scalable verbatim-index channel. We anchor it on a witness task, the Newton's-apple problem in an infinite stream, and name three resource walls: a Shannon wall barring any o(Nb)-state architecture, a horizon wall barring any fixed window, and a circuit wall barring fixed-depth attention-only composition (conditional on TC0 != NC1). Under an explicit separability assumption a hybrid crosses all three by paying each wall's price, so capability is strictly super-additive under composition. We separate what we prove from what we conjecture: the access-completeness principle rests on information-theoretic lower bounds and pre-registered experiments, while the field-level convergence trend is an economics-motivated conjecture. We report the first pre-registered small-scale tests under criteria frozen before the data: the predicted scissors gap is measured (exact-retrieval error 0.994 vs. 0.000 once a 64-scalar state gains one global-attention layer), the state-tracking bifurcation lands at the registered boundary, and a conjunction witness shows an irreducibly two-channel solution; one prediction failed with its direction reversed and is reported as such. Representational convergence is given freely by scale; capability convergence must be purchased by access structure.

## 综合总结
本文挑战了“柏拉图表征假设”(PRH)，提出“能力收敛假设”(CCH)，指出在固定推理预算下，表征收敛不等于能力收敛，能力取决于架构的“访问结构”而非单纯规模。作者定义了“访问完备混合”架构（包含压缩O(1)状态通道和可扩展逐字索引通道），并通过“牛顿苹果问题”揭示了限制单一架构的三面墙（Shannon、Horizon、Circuit）。结合信息论下界与严格的预注册实验，论文证明了混合架构在跨越这三面墙时能力具有严格超可加性，为当前大模型混合架构（如SSM+Attention）的必要性提供了坚实的理论基石。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
论文极具理论深度与创新性，挑战了表征收敛即能力收敛的直觉，提出基于访问结构的能力收敛假设(CCH)。研究引入了信息论下界和计算复杂性理论，定义了限制单一架构的Shannon、Horizon和Circuit三面墙，论证了混合架构能力的严格超可加性。论证过程严谨，严格区分了证明与猜想，并采用预注册实验验证，甚至如实报告了反向的预测结果，展现了极高的学术规范与科学精神。

### 实用性 (评分: 7.5/10)
为当前大模型混合架构（如SSM+Attention）的设计提供了坚实的理论支撑，明确指出了纯状态压缩或纯注意力机制的局限性，论证了双通道（O(1)压缩状态+逐字索引）结合的必要性。对底层模型架构选型、长上下文推理与检索任务的设计具有高度指导价值，但理论偏底层，对上层业务应用的直接落地指导相对有限。

### 社区活跃度 (评分: 9.0/10)
话题紧贴当前大模型架构演进的核心前沿（混合序列模型、长上下文处理），极具时效性。研究方法极其规范透明，采用预注册实验并公开失败预测，来源可信度极高。其核心观点直接回应了社区关于Scale law边界与架构收敛的讨论，若被广泛认可，将对下一代大模型的基础架构设计方向产生深远影响。

## 项目链接
https://arxiv.org/abs/2607.14144
