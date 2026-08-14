# Learning to Adapt Cross-Domain Preferences via Meta-LoRA for LLM Personalization

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-14  
**来源：** rss  

## 项目描述
arXiv:2608.12389v1 Announce Type: new Abstract: Cross-domain zero- or few-shot personalization aims to generate user-preferred responses in unseen conversational domains from only a handful of target-domain interactions. Existing adaptation methods struggle to calibrate update magnitude under sparse evidence and thus overfit, whereas history-transfer methods often entangle user preferences with source-domain artifacts, yielding unreliable personalization priors and negative transfer. To calibrate adaptation to evidence quality, we propose PAC-Bayes-regularized Meta-LoRA, which uses a meta-learned LoRA initialization as both the adaptation start and prior center, while adjusting update strength according to support-set size and predictive uncertainty. This limits overfitting under sparse or ambiguous evidence while permitting stronger personalization as evidence grows. Controlled adaptation alone does not determine which preferences should transfer across domains or how they should be expressed. We therefore functionally decompose personalization priors into user and domain components, using a human-readable prompt for stable preferences and topology-preserving soft tokens for domain-specific hidden-space conditioning. Experiments across multiple benchmarks and personalization tasks show consistent gains over strong baselines. On HiCUPID, our method reduces cross-domain win-rate degradation by 47.9% relative to the best competing baseline and improves win rate by 110.2% under unseen-user cold start.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.12389
