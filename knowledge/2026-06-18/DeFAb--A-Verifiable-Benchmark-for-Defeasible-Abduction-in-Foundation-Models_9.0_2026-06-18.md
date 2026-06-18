# DeFAb: A Verifiable Benchmark for Defeasible Abduction in Foundation Models

**评分：** 9.0  
**状态：** 正常  
**标签：** 大模型, 推理, 逻辑推理, 评估基准, 强化学习, 论文, 数据集  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18557v1 Announce Type: new Abstract: A rule-based logic solver resolves every instance in our benchmark in under 50 microseconds with 100% accuracy; the best frontier language model reaches 65% at best and drops to 23.5% under rendering-robust evaluation (worst case over four surface renderings). We introduce DeFAb (Defeasible Abduction Benchmark), a dataset and generation pipeline that converts four decades of publicly funded knowledge bases into formally grounded instances for defeasible abduction: constructing hypotheses that explain anomalies by overriding defaults while preserving unrelated expectations. Because every hypothesis must pass polynomial-time checks for valid derivation, conservativity, and minimality, DeFAb makes logical rigor the instrument for measuring creativity and theoretical reasoning, scoring the disciplined construction of theory revisions rather than fluent but theory-destroying prose. The pipeline pairs taxonomic hierarchies (OpenCyc, YAGO, Wikidata) with behavioral property graphs (ConceptNet, UMLS) to produce 372,648+ instances across 33.75M materialized rules from 18 sources, in three levels with polynomial-time verifiable gold standards. Four frontier models do not reliably internalize defeasible reasoning: rendering-robust Level 2 accuracy is 7.8-23.5%; chain-of-thought variance (~36 pp) exceeds any inter-model gap; and a matched contamination control isolates a +19.4 pp Level 3 gap. We further release DeFAb-Hard (a 235-instance Level 3 difficulty variant; best model 53.3% vs 100% symbolic) and CONJURE (a kernel-verified transformative-creativity variant of 560 Lean 4/Mathlib instances whose gold answers are definitions the proof kernel did not previously contain, judge-free verifier; a pilot finds zero novel concepts). The same verifier doubles as an exact reward for preference optimization (DPO, RLVR/GRPO). Released under MIT at https://huggingface.co/datasets/PatrickAllenCooper/DeFAb.

## 综合总结
本文提出了DeFAb，一个针对基础模型可废止溯因推理的可验证基准。该研究将40年的公共知识库转化为37万+形式化实例，通过多项式时间验证器严格评估模型在保留无关期望的同时覆盖默认值解释异常的能力。实验表明，前沿大模型在此任务上表现极差（渲染鲁棒评估下最高仅23.5%），且CoT方差极大。此外，作者还发布了DeFAb-Hard和基于Lean 4的CONJURE变体，并指出其验证器可直接作为DPO/RLVR等偏好优化的精确奖励信号，为提升大模型逻辑推理能力提供了新路径。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
论文在可废止溯因推理领域展现了极高的新颖性与技术深度。通过将40年的公共知识库转化为形式化验证的实例，并引入多项式时间验证机制（有效推导、保守性、最小性），严谨地定义了逻辑推理与创造力的评估标准。对前沿模型CoT方差大、易受表面渲染影响及数据污染的剖析深刻，且创新性地提出了基于Lean 4的CONJURE变体以测试变革性创造力，论证极其严密。

### 实用性 (评分: 8.5/10)
对AI从业者具有极高的实践指导价值。不仅提供了一个严苛的评估基准，其内置的多项式时间验证器更可直接转化为偏好优化（DPO, RLVR/GRPO）的精确奖励信号，为解决大模型强化学习中的奖励作弊和逻辑幻觉提供了可落地的工程方案。数据生成管道也可扩展至其他知识库。

### 社区活跃度 (评分: 9.0/10)
话题极具时效性，直击当前大模型推理能力评估的痛点与热点。基于权威知识库（OpenCyc, Wikidata等）构建，数据与代码均以MIT协议开源，可信度极高。其揭示的前沿模型在可废止推理上的低准确率（7.8-23.5%）及CoT的不稳定性，对AI社区关于LLM真实推理能力的认知将产生重要冲击与广泛影响。

## 项目链接
https://arxiv.org/abs/2606.18557
