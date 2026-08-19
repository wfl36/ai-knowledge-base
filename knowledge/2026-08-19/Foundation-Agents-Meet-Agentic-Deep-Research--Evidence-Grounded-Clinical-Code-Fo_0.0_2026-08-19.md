# Foundation Agents Meet Agentic Deep Research: Evidence-Grounded Clinical Code Forecasting

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-19  
**来源：** rss  

## 项目描述
arXiv:2608.17075v1 Announce Type: new Abstract: Next-encounter ICD forecasting predicts which standardized diagnosis codes will be documented at a future visit from the longitudinal record available beforehand. The task is prospective and multi-label: the target note does not yet exist, and several codes may be correct. Structured EHR foundation models capture recurrence and temporal progression, whereas language foundation models generate flexible diagnostic hypotheses. We introduce ICD-Deepresearch, a DeepResearch workflow that composes these predictive foundation models with medical search and ICD dictionaries. Because no source reveals the future code set, research evaluates candidate transitions by linking patient evidence, external clinical relations, and exact code semantics under a fixed top-K budget. Candidate Generation uses SparseEHR to produce an EHR Prior that initializes two bounded Research Expansion rounds; an independent GPT-5 Direct Forecast supplies complementary candidates. Final Selection validates, deduplicates, and jointly ranks both paths, after which a separate module writes rationales without changing predictions. Finally ICD-Deepresearch achieves patient-averaged precision/recall of 24.60/35.09% on MIMIC-III and 25.14/48.32% on MIMIC-IV. Physicians rate 51% and 68% of its retrieved documents useful, compared with 22% and 39% for standalone GPT-5 web search and 32% and 41% for Medical Deep Research. ICD-Deepresearch therefore improves over the registered local comparators while retrieving evidence with higher physician-rated usefulness than the standalone research systems

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.17075
