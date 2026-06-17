# Quantifying Consistency in LLM Logical Reasoning via Structural Uncertainty

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 推理, 一致性, 不确定性, 逻辑推理, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17312v1 Announce Type: new Abstract: Large language models can arrive at the same answer through reasoning paths that are unstable, contradictory, or difficult to rank consistently -- a failure mode especially prevalent in multi-step deductive reasoning. Existing methods assess reliability primarily through output dispersion -- measuring how much sampled answers differ -- but this discards a complementary signal: whether the model can consistently rank competing reasoning candidates. We propose structural uncertainty, a consistency-aware framework derived from the stability of self-preference-induced rankings over sampled reasoning solutions. Given a query, we generate multiple candidate solutions and ask the model to judge pairwise preferences among its own outputs. We aggregate self-preferences into ranking distributions via Bradley-Terry modeling with PageRank, and decompose the signal into two entropy-based components: across-trial ranking instability and within-trial candidate ambiguity. Across five LLMs and eight benchmarks, structural signals provide information complementary to answer dispersion: on logical and mathematical reasoning tasks, the combination improves identification of unreliable instances, while on factual retrieval the structural signal collapses toward uniformity, diagnosing a regime boundary where reasoning-level consistency evaluation is uninformative. The two components relate differently to accuracy: within-trial ambiguity correlates positively with correctness -- consistent with settings where multiple plausible solution paths remain competitive -- while across-trial instability correlates negatively, signaling unreliable reasoning. Structural uncertainty is best understood not as a universal confidence estimator, but as a regime-sensitive evaluator of logical reasoning consistency.

## 综合总结
本文针对LLM在多步演绎推理中路径不一致的问题，提出了‘结构不确定性’评估框架。该框架通过模型对自身生成候选解的成对偏好判断，结合Bradley-Terry与PageRank构建排序分布，并将其分解为‘跨试验不稳定性’与‘试验内歧义性’。实验表明，该结构信号与传统输出分散度互补，在逻辑和数学推理中能有效识别不可靠实例，但在事实检索中失效。研究还揭示了两种组件与准确率截然不同的相关性，为评估LLM逻辑推理一致性提供了细粒度且机制敏感的新视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了‘结构不确定性’这一新颖框架，突破了传统仅依赖输出分散度来评估LLM可靠性的局限。通过引入自偏好诱导排序，结合Bradley-Terry模型与PageRank算法生成排序分布，并将信号分解为‘跨试验排序不稳定性’和‘试验内候选歧义性’两个熵组件，理论拆解极具深度。特别是发现两种组件与准确率呈现正负相反的相关性，以及方法在事实检索任务中退化的边界条件，论证严谨且洞见深刻。

### 实用性 (评分: 7.5/10)
该框架对需要高可靠性逻辑与数学推理的AI应用具有较强参考价值，能够帮助开发者更精准地识别不可靠的推理实例。然而，其依赖多次采样与成对偏好判断的机制会带来较高的计算开销，且论文明确指出该方法在事实检索场景下失效，适用范围存在明显边界，因此工程落地的普适性和成本效益受到一定限制。

### 社区活跃度 (评分: 8.5/10)
LLM的推理一致性与可靠性是当前大模型领域的核心痛点与热门研究方向。该论文来自arXiv，针对多步演绎推理中的不稳定性问题提出了创新解法，契合业界对大模型自我反思与推理机制评估的迫切需求。其关于‘自偏好排序’和‘评估机制边界’的发现对学术界和工程界均有重要启发，具备较高的话题时效性与潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.17312
