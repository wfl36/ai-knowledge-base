# When Sample Selection Bias Precipitates Model Collapse

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 合成数据, 模型崩溃, 数据孤岛, 隐私保护, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13732v1 Announce Type: new Abstract: The proliferation of recursive training on synthetic data can alleviate data scarcity but risks model collapse, where repeated training erodes distributional tails and homogenizes outputs. Data selection is widely viewed as a remedy, yet its reliability depends critically on the reference distribution used by the verifier. We show that in low-resource verification regimes, where each verifier observes only a small, fragmented, and biased slice of the target manifold, selection itself becomes biased. This situation naturally arises in low-resource data silos such as healthcare consortia or proprietary financial institutions, where raw data cannot be pooled and local references are inherently incomplete. As a result, selection preferentially retains samples aligned with the local manifold while pruning globally relevant tail modes, turning from a safeguard against collapse into a mechanism that precipitates it. We theoretically prove that such siloed selection accelerates collapse and induces power-law diversity decay. As an initial mitigation, we construct Wasserstein proxy references from multiple silos without sharing raw data. Empirical results confirm that local-reference selection fails on skewed distributions, whereas collaborative proxy references mitigate diversity degradation, suggesting that recursive synthetic-data pipelines require particular caution when real-data coverage is fragmented or scarce.

## 综合总结
本文针对合成数据递归训练引发的模型崩溃问题，揭示了在数据孤岛（如医疗、金融）等低资源验证场景下，数据选择偏差不仅无法防止崩溃，反而会因局部参考分布的局限性而加速崩溃并导致幂律多样性衰减。作者从理论上证明了这一现象，并提出了无需共享原始数据的Wasserstein协作代理参考方法作为缓解措施。实验表明，局部参考选择在偏态分布上失效，而协作代理参考能有效缓解多样性退化，为数据孤岛场景下的合成数据训练提供了重要理论和实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深刻揭示了在数据孤岛和低资源验证机制下，数据选择偏差不仅无法防止模型崩溃，反而会加速崩溃并导致幂律多样性衰减。通过严格的理论证明和实证分析，颠覆了数据选择作为模型崩溃通用解药的传统认知，并创新性地提出基于Wasserstein距离的跨孤岛协作代理参考方法，技术深度与严谨性极高。

### 实用性 (评分: 8.5/10)
对医疗、金融等存在数据孤岛且无法直接共享原始数据的行业具有极高的实践指导价值。提出的Wasserstein代理参考方法为这些低资源场景下的合成数据递归训练提供了可行的隐私保护缓解方案，能够直接指导相关领域的模型训练与数据筛选流程。

### 社区活跃度 (评分: 9.0/10)
模型崩溃与合成数据是当前AI社区最前沿且紧迫的议题。该论文直击大模型递归训练的核心痛点，来源为arXiv学术论文，逻辑严密，结论对当前普遍依赖合成数据的大模型研发具有强烈的警示和启发意义，具有很高的关注度和影响力。

## 项目链接
https://arxiv.org/abs/2606.13732
