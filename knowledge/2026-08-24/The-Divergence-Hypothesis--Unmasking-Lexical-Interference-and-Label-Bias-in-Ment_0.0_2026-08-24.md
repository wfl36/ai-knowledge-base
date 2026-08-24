# The Divergence Hypothesis: Unmasking Lexical Interference and Label Bias in Mental Health NLP

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-24  
**来源：** rss  

## 项目描述
arXiv:2608.20353v1 Announce Type: new Abstract: Computational mental health (CMH) classifiers often degrade under distribution shift because human annotators and distant-supervision pipelines reward different linguistic signals. We introduce TSS (Triple-Stream Stress probe), a multi-channel diagnostic framework that decomposes text into (A) lexical character n-grams, (B) a small, mostly content-free morpho-syntactic channel, and (C) a 154-feature psycholinguistic style channel. Across four English datasets (N=12,906), TSS reveals a lexical interference effect: adding lexical features to the style channel reduces Macro-F1 on human-labeled data (mean drop 0.072, p<10^-4) but not on auto-labeled data. We propose Degree of Divergence (DoD), a difference-in-differences statistic adapted from econometrics for label-source auditing, with instance-level bootstrap inference; the headline estimate is DoD(BC-A) = 0.0374, 95% CI [0.0097, 0.0651], p=0.0032. A platform-stratified Twitter-only DoD (which removes the Reddit vs. Twitter contrast) reproduces the pattern with bootstrap inference: DoD-Tw(BC-A) = +0.096 (p<0.001) and DoD-Tw(AC-A) = -0.089 (p<0.001). Interventional masking (pos_only) retains ~95-99% of Channel C's performance after destroying content words on human datasets, indicating that the style channel does not rely primarily on lexical surface form. TSS is positioned as a diagnostic audit framework, not a clinical screening tool: it flags label-source-specific shortcut learning before generalization claims are made.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.20353
