# Large Language Models are Approximate Survival Estimators

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-02  
**来源：** rss  

## 项目描述
arXiv:2609.38181v1 Announce Type: new Abstract: Survival analysis estimates time-to-event outcomes from patient covariates and is widely used for medical risk assessment. Patients seeking prognostic information after a diagnosis may turn to large language models (LLMs), now readily accessible through consumer applications. However, whether LLMs can provide accurate survival predictions has not been rigorously evaluated. We introduce Survprompt, a framework that converts structured patient covariates into free-text clinical vignettes and prompts pre-trained LLMs to predict survival zero-shot. We benchmark Survprompt against conventional survival models, including random survival forests (RSF), across two multi-institutional pan-cancer cohorts: the publicly available MSK-CHORD cohort and a newly curated cohort from the Providence St. Joseph Health Network constructed using an LLM-based medical abstraction framework. We report censored mean absolute error (cMAE) and concordance index (c-index) and conduct feature ablations to identify variables influencing LLM predictions. Frontier LLMs achieved surprisingly competitive cMAE for individual survival times. For example, GPT-5.6-Sol achieved cMAE within 10% of state-of-the-art RSF models specifically trained for survival prediction for several cancer types and lower cMAE than RSF for prostate cancer in MSK-CHORD. Feature ablations revealed that LLMs prioritized clinical variables similarly to specialized survival models. However, LLMs showed inconsistent accuracy across cancer types and institutions and poorly discriminated between high- and low-risk patients (lower c-index). Zero-shot LLMs can generate surprisingly accurate prognostic estimates without specialized training, but their variable performance across cancer types and institutions remains an important limitation for clinical use.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.38181
