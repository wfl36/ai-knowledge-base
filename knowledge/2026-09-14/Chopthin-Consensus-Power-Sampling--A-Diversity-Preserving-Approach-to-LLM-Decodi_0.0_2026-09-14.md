# Chopthin-Consensus Power Sampling: A Diversity-Preserving Approach to LLM Decoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-14  
**来源：** rss  

## 项目描述
arXiv:2609.12243v1 Announce Type: new Abstract: Inference-time power sampling via Sequential Monte Carlo (SMC) can substantially improve large language model (LLM) reasoning without requiring post-training. However, many existing SMC approaches rely on equal-weight resampling, which can aggressively prune low-weight trajectories, discarding potentially correct reasoning paths and degrading the genealogical diversity of the search space. To address this, we introduce Chopthin-Consensus Power Sampling (CCPS). Our method applies the Chopthin resampler to LLM decoding: rather than equalizing weights and forcing unnecessary particle duplication, it enforces an upper bound on the ratio between the largest and smallest weights and carries the unequal weights forward. This targeted intervention preserves a richer set of distinct reasoning paths, keeps the weighted SMC approximation unchanged in conditional expectation, and guarantees a lower bound on the post-resampling effective sample size (ESS). To fully exploit this enriched population, we employ a semantic-majority selection mechanism that merges token-identical final trajectories, clusters semantically equivalent answers, and returns the answer supported by the largest number of distinct trajectories. Evaluating across three open-weight models and five reasoning benchmarks, we show that Chopthin increases oracle coverage in 13 of 15 settings. Combined with semantic-majority selection, CCPS matches or exceeds the final-answer accuracy of the Power-SMC baseline in 14 of 15 settings, delivering absolute gains of up to 10.6 percentage points. These findings demonstrate that diversity-preserving resampling and diversity-aware selection are complementary mechanisms for training-free LLM reasoning. Code is available at github.com/MinooAhmadii/chopthin-consensus-power-sampling.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.12243
