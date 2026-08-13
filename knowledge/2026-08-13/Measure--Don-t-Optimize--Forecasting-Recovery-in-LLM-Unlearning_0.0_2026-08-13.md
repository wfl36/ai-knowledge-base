# Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-13  
**来源：** rss  

## 项目描述
arXiv:2608.11408v1 Announce Type: new Abstract: Prior white-box studies show that large language models can retain latent traces of target knowledge after unlearning, even when the knowledge is no longer expressed in their outputs. However, existing audits remain limited to one-off diagnostics: it is unclear whether these residual signals can predict future recovery under continued training or serve as reliable optimization targets. Resolving this gap is essential to determine whether internal auditing can move beyond post-hoc evaluation toward proactive risk monitoring and safer unlearning. We propose J-Access, an inference-time audit that uses the Jacobian lens to map intermediate representations into vocabulary space and measures how often target concepts remain accessible along the model's output pathway. We hypothesize that residual accessibility reflects recovery susceptibility: knowledge that remains closer to the output pathway requires less fine-tuning to restore, leading to faster recovery. We audit 398 public unlearned models spanning eight unlearning methods. We find that: (1) most unlearned models retain access above the retain-only gold level; (2) pre-attack accessibility predicts recovery speed and extent at the model level, but cannot identify which specific facts will be recovered; and (3) directly minimizing J-Access does not promote genuine deletion. Instead, the model learns to hide knowledge from the audit, producing lower audit scores but greater post-attack recovery. These findings position J-Access as a model-level diagnostic for assessing residual susceptibility in unlearned models. We argue internal audits should serve as an independent diagnostic dimension in unlearning evaluation, and should not be converted into optimization targets without validation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.11408
