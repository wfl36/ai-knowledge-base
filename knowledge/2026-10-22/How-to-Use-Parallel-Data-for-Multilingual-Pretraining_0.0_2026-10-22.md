# How to Use Parallel Data for Multilingual Pretraining

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-22  
**来源：** rss  

## 项目描述
arXiv:2610.28838v1 Announce Type: new Abstract: High-quality human-translated parallel corpora can improve cross-lingual transfer, but are typically too small for large-scale pretraining. Machine-translated web corpora help overcome this limitation, making parallel data available at pretraining scale. Standard multilingual pretraining, however, samples source documents and their translations independently, without explicitly using their parallel structure. We investigate how to use the parallel structure of the data to improve multilingual pretraining by concatenating each document with its translation in the same training sequence. We compare this parallel pretraining (PPT) approach with standard pretraining (SPT), training models from scratch at matched token budgets. Surprisingly, despite the benefits of parallel data reported in prior cross-lingual work, PPT alone does not consistently improve language understanding over SPT. Our further analysis suggests that although PPT builds a strong cross-lingual foundation, as shown by its better use of shared information across languages, the mismatch between parallel training contexts and single-language task inputs limits its gains in general language understanding. This finding motivates a two-stage approach following the pretraining-fine-tuning paradigm: we first use PPT to build a cross-lingual foundation, then continue with SPT to adapt it to standard language modeling. In both high-resource and low-resource settings, the two-stage approach consistently improves general language understanding and cross-lingual task performance over standard pretraining alone at matched training budgets.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.28838
