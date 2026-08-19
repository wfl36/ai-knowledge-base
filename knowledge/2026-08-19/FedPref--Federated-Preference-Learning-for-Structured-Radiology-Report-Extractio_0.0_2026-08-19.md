# FedPref: Federated Preference Learning for Structured Radiology Report Extraction

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-19  
**来源：** rss  

## 项目描述
arXiv:2608.16971v1 Announce Type: new Abstract: Radiology reports describe findings and locations in free text, but downstream search and analysis require these relations in a fixed schema. Learning this extraction requires labels that are unevenly distributed across institutions: smaller hospitals have less local evidence, and pooling data may be infeasible. We introduce FedPref: frozen public language models propose alternative JSON extractions, local annotations rank them, and sites collaboratively train compact Qwen3-8B adapters while sharing only model updates. A heterogeneous teacher pool provides cross-model contrast when repeated single-model samples collapse. On development data from six simulated hospitals with unequal data volume and disease prevalence, FedPref improves client-mean F1 by 2.49 points and worst-site F1 by 9.10 points compared with training each site in isolation, with the largest gains at the sites holding the least data. Central training on the pooled preference-pair union is 2.66 points higher on client-mean F1. On a locked, 400-report manually validated gold test set, FedPref reaches 68.68 F1 and pooled training 71.67, preserving that same ordering. FedPref thus lets institutions with unequal, unpooled data benefit from collaboration without ever sharing reports or annotations.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.16971
