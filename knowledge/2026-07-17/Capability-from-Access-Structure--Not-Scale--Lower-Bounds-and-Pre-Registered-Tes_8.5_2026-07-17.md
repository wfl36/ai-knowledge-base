# Capability from Access Structure, Not Scale: Lower Bounds and Pre-Registered Tests for Hybrid Sequence Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 混合架构, 序列模型, 表征学习, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14144v1 Announce Type: new Abstract: The Platonic Representation Hypothesis (PRH) holds that as models scale, representations of heterogeneous networks converge toward a shared model of reality. We propose its sequel and boundary, the Capability Convergence Hypothesis (CCH): under a fixed per-token inference budget, representational convergence does not entail capability convergence. Capability instead converges toward a class, the access-complete hybrid: any architecture holding both a compressive O(1)-state channel and a scalable verbatim-index channel. We anchor it on a witness task, the Newton's-apple problem in an infinite stream, and name three resource walls: a Shannon wall barring any o(Nb)-state architecture, a horizon wall barring any fixed window, and a circuit wall barring fixed-depth attention-only composition (conditional on TC0 != NC1). Under an explicit separability assumption a hybrid crosses all three by paying each wall's price, so capability is strictly super-additive under composition. We separate what we prove from what we conjecture: the access-completeness principle rests on information-theoretic lower bounds and pre-registered experiments, while the field-level convergence trend is an economics-motivated conjecture. We report the first pre-registered small-scale tests under criteria frozen before the data: the predicted scissors gap is measured (exact-retrieval error 0.994 vs. 0.000 once a 64-scalar state gains one global-attention layer), the state-tracking bifurcation lands at the registered boundary, and a conjunction witness shows an irreducibly two-channel solution; one prediction failed with its direction reversed and is reported as such. Representational convergence is given freely by scale; capability convergence must be purchased by access structure.

## 综合总结
本文挑战了“规模即能力”的常规认知，提出“能力收敛假说（CCH）”，指出在固定推理预算下，表征收敛不等于能力收敛。作者证明能力收敛于“访问完备混合架构”（即同时具备压缩状态通道和逐字索引通道的架构），并提出了Shannon、Horizon和Circuit三个资源墙。通过信息论下界证明和严格的预注册实验，验证了混合架构能力的严格超加性，强调架构的访问结构才是能力提升的关键，为未来混合序列模型的设计提供了坚实的理论基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
提出了极具深度的“能力收敛假说（CCH）”，对柏拉图表征假说进行了重要边界补充。引入“访问完备混合体”概念，并通过信息论下界和计算复杂性（TC0 != NC1）严格证明了Shannon、Horizon和Circuit三个资源墙的存在。理论论证严谨，清晰区分了证明与猜想，并创新性地采用预注册实验验证预测，甚至如实报告了反向的失败预测，展现了极高的学术规范与研究深度。

### 实用性 (评分: 7.0/10)
对混合架构（如线性RNN/SSM+Attention）的设计具有明确的指导意义，指出单纯堆叠规模无法突破特定推理瓶颈，必须引入具备逐字索引能力的通道。然而，研究主要聚焦于理论下界和理想化见证任务（牛顿苹果问题），距离解决具体的工业级NLP任务尚有转化距离，实际工程落地需进一步探索如何权衡跨越资源墙的代价。

### 社区活跃度 (评分: 9.0/10)
话题极具时效性，直击当前大模型架构演进的核心争议（Scale vs. Architecture）。采用预注册实验并如实报告失败预测，极大提升了结论的可信度与学术声誉。对打破“Scaling Law万能”的迷思、推动混合架构研究具有重要影响力和启发价值。

## 项目链接
https://arxiv.org/abs/2607.14144
