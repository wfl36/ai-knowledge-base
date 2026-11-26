# Directly Maximizing On-policy Expected Accepted Length for Speculative Decoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-26  
**来源：** rss  

## 项目描述
arXiv:2611.31256v1 Announce Type: new Abstract: Speculative decoding accelerates large language model inference by using a lightweight draft model to propose tokens for verification by a target model. Draft training commonly optimizes token-level distribution alignment, but this does not directly optimize the length of the accepted prefix: once a draft token is rejected, all subsequent draft tokens are discarded. We propose FreDraft, an on-policy training method that directly maximizes the expected accepted length of drafts sampled from the current draft model. This objective accounts for first-rejection truncation and induces prefix-aware credit assignment, weighting each token by its contribution to the acceptance of the current and subsequent tokens. To optimize the objective efficiently, we analytically marginalize token-level acceptance rate, using the target model's vocabulary distribution to reduce gradient variance. We further redistribute part of this distribution-level gradient into an explicit penalty for sampled tokens whose probabilities are overestimated by the draft model, while preserving the expected gradient. Experiments across multiple benchmarks and target models show that FreDraft improves accepted length and decoding speedup over strong baselines, achieving faster on-policy training convergence.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.31256
