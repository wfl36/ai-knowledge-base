# RoPoLL: Robust Panel of LLM Judges

**评分：** 9.2  
**状态：** 正常  
**标签：** 大模型评估, LLM-as-Judge, 鲁棒统计, 评审团, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30931v1 Announce Type: new Abstract: The LLM Jury, a Panel of LLM Evaluators (PoLL) reporting consensus scores, has become a practical alternative to single-judge LLM evaluation, yet its statistical behavior remains poorly understood. We formalize the LLM Jury under the Huber contamination model and show that PoLL incurs unbounded bias under any positive contamination, regardless of jury size, whenever a single judge fails in a biased, LLM-typical way (mode collapse, sycophancy, safety refusal). Framing jury consensus as classical robust mean estimation, we propose RoPoLL (Robust Panel of LLM-as-Judge), which preserves the PoLL panel but replaces the aggregation function with a robust mean estimator, instantiated with the geometric median (GM): tuning-free, with the optimal finite-sample breakdown point 1/2. A finite-sample error bound and a matching information-theoretic minimax lower bound agree on the parametric rate sigma*sqrt(d/N) and differ on the breakdown floor by a factor of sqrt(d), a statistical-computational gap that polynomial-time RoPoLL pays relative to the intractable Tukey halfspace median. Across 13 open-weight judges (4B-675B), three reward-model benchmarks, and four corruption regimes at rates up to 50%, RoPoLL dominates PoLL on every biased corruption type: by about 19% on cross-dimensional attacks at matched compute, and by orders of magnitude on heavy-tailed Byzantine adversaries. A 3-judge RoPoLL committee at 38B beats Mistral-Large-3 (675B) by 1.31x on HelpSteer-2 under 30% bimodal-random corruption, an 18x parameter advantage at better accuracy; a Noisy-GT control confirms the premium is paid against biased contamination, not benign imprecision.

## 综合总结
本文针对LLM评审团在面临偏置污染时产生无界偏差的理论缺陷，将其形式化为Huber污染模型下的鲁棒均值估计问题，并提出RoPoLL框架。RoPoLL以无需调参的几何中位数替代传统均值聚合，具备最优的有限样本破坏点，并在理论上给出了误差界与极小极大下界。实验表明，RoPoLL在各类偏置腐败下全面超越PoLL，且能用极小参数量（3x38B）的委员会击败超大模型（675B），为大模型评估提供了一种高效、鲁棒且低成本的范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
本文在理论深度与论证严谨性上表现卓越。作者创新性地将LLM评审团形式化为Huber污染模型下的鲁棒均值估计问题，严格证明了传统PoLL在存在偏置污染时会面临无界偏差的理论缺陷。提出的RoPoLL采用几何中位数进行聚合，具备最优的1/2有限样本破坏点，并给出了有限样本误差界与匹配的极小极大下界，揭示了由于多项式时间计算限制而产生的sqrt(d)统计-计算差距。整体理论框架严密，洞见深刻。

### 实用性 (评分: 9.0/10)
方案的落地价值极高且实施门槛极低。RoPoLL的核心改进仅是替换聚合函数为几何中位数，无需额外调参，在保持PoLL面板灵活性的同时显著提升了鲁棒性。实验证明，在30%污染率下，3个38B模型组成的RoPoLL委员会即可在HelpSteer-2上击败675B的Mistral-Large-3，实现了18倍的参数效率优势。这对于受限于算力与API成本、又需应对LLM评审偏见（如安全拒绝、谄媚）的从业者而言，提供了极具性价比的实践指导。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，LLM-as-a-Judge是当前大模型评估领域的核心痛点，而现有PoLL方法的统计不可靠性是业界亟待解决的盲区。作者在13个不同参数量（4B-675B）的开源模型、三大主流Reward基准及多种极端腐败机制下进行了详尽实验，数据扎实，极具说服力。该工作对评估社区的范式转换具有重要影响力。

## 项目链接
https://arxiv.org/abs/2606.30931
