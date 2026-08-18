# Auxiliary uncertainty signals for LLM-assisted systematic review screening: a benchmark across eight Cohen drug-class reviews

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-18  
**来源：** rss  

## 项目描述
arXiv:2608.14551v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used for title-abstract screening in systematic reviews, but their decisions lack calibrated uncertainty. We show that an auxiliary BERT+GCN classifier supplies a structured uncertainty signal that improves LLM screening efficiency, and we identify the prompt-delivery strategy that maximises the benefit-to-cost ratio. We evaluate five LLM prompt-delivery conditions on eight drug-class datasets from the Cohen (2006) benchmark using 3 seeds x 5-fold stratified cross-validation (600 fold-level results). A BERT+GCN model trained per fold classifies each test paper as INCLUDE, EXCLUDE, or MAYBE via two spectral tests (algebraic radical and categorical paradox). Conditions vary information content (none / label / full scores), selectivity (all papers vs. MAYBE only), and timing (proactive vs. reactive two-pass). A cross-model pilot against gpt-4.1-mini on three datasets tests cross-generation transfer. Three findings: (i) Full-context delivery yields significant gains in F1 (+0.011, paired Wilcoxon p=0.008) and WSS@95 (+0.050, p=0.039) at a 1.28x token-cost premium, while preserving recall. (ii) MAYBE-only routing is Pareto-optimal: highest mean recall (0.92) and AUC-ROC (0.54) at only 1.05x baseline cost -- one sixth of full-context overhead. (iii) The two-pass design escalates 22.2% +/- 8.8% of records yet never revises its decision (0% flip rate across all datasets and folds), giving decisive evidence that current instruction-tuned LLMs cannot self-triage. The cross-model pilot shows an identical +0.8% recall uplift for both LLM generations. A per-paper ablation across 20,796 observations shows the dual paradox test reduces empirically to a one-line logit-gap criterion. We release the full pipeline; the 600-run experiment replays in under one hour from cached LLM responses.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.14551
