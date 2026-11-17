# Tabular Population Priors as Structured Retrieval for EHR Medication Set Prediction

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-17  
**来源：** rss  

## 项目描述
arXiv:2611.17341v1 Announce Type: new Abstract: Medication prediction from electronic health records is a fixed vocabulary structured prediction problem, yet recent clinical RAG systems often treat it like open ended case based reasoning: retrieve similar patient admissions and ask an LLM to infer a medication set. This retrieval object is indirect the model receives retrieved patient records while the target is a discrete set of medication class labels. We propose a more task aligned retrieval object: a tabular population prior ranked medication class candidates from a sparse condition medication co occurrence table estimated from training admissions. Using PACERAG as a fixed downstream pipeline and replacing only its patient retriever, this drop in swap improves F1 from 0.303 to 0.338 (+11.5% relative) and Jaccard from 0.218 to 0.237 on 1,004 heldout MIMIC IV admissions, with no additional LLM calls and no inference time patient index. A non LLM top k baseline reaches F1=0.248, confirming the prior is predictive before LLM integration. Aggregate population statistics can provide a more task aligned, efficient, and auditable retrieval source than patient level nearest neighbors for fixed vocabulary EHR set prediction.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.17341
