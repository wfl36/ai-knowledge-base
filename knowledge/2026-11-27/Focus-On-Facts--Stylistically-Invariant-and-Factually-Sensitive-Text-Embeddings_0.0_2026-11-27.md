# Focus On Facts: Stylistically Invariant and Factually Sensitive Text Embeddings

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-27  
**来源：** rss  

## 项目描述
arXiv:2611.33250v1 Announce Type: new Abstract: Text embedding models can conflate surface-form similarity with factual identity. Given an altered near-copy with one corrupted fact and a differently worded fact-preserving rewrite, the base model prefers the altered near-copy. We test whether hard-negative contrastive supervision can reduce this surface-similarity shortcut. We construct FOF-Bench, an 83,263-triplet benchmark spanning five domains. Each anchor is paired with an LLM-generated, fact-preserving stylistic rewrite and a matched fact-altered near-copy. We fine-tune FOF-80M (Focus On Facts), an 80M-parameter embedding model, with a triplet contrastive objective that ranks the rewrite above the factual alteration. On 8,327 held-out test triplets, the base model chooses the factually altered text in 99.58% of cases (0.42% factual preference rate; mean separation -0.1650). After fine-tuning, mean positive--negative separation is +0.0329, 98.5% of individual margins move in the intended direction, and the preference rate reaches 29.37%. On DiSC, an external style-transfer corpus, mean cross-style similarity increases from 0.7905 to 0.9559. The model also penalizes omission and transfers poorly to directional tasks such as NLI and summarization. We characterize FOF-80M as a soft factual fingerprint for studying factual retention under stylistic variation, not as a general-purpose factuality metric.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.33250
