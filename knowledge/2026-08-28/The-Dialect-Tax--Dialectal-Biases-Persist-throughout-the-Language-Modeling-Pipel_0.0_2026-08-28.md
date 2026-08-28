# The Dialect Tax: Dialectal Biases Persist throughout the Language Modeling Pipeline

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-28  
**来源：** rss  

## 项目描述
arXiv:2608.24952v1 Announce Type: new Abstract: Systematic dialectal performance gaps in language models (LMs) are well documented, but the source of these disparities within the modern language modeling pipeline remains unclear. Our study traces this "dialect tax" across the natural language processing pipeline. Using parallel English dialect corpora that hold meaning fixed while varying surface form, we first confirm that LMs recognize matched Standard American English (SAE) and dialectal texts as semantically equivalent. However, we discover further representational gaps corresponding to downstream performance gaps. Across model families and generations, modern LMs still encode dialectal texts unequally during tokenization, pre-training, post-training, and inference. Strikingly, bypassing traditional subword segmentation via a character-level counterfactual tokenizer removes neither input and output asymmetries nor dialectal accuracy gaps. During pre-training, dialect pairs induce more divergent gradient updates than pairs of entirely unrelated SAE documents, indicating that models find semantically equivalent dialectal content harder to learn from than unrelated SAE documents. During post-training, reward models show contextual, unstable dialect preferences, assigning higher values to isolated AAVE-exclusive tokens than to SAE-exclusive tokens, while full reasoning contexts receive task- and model-dependent dialect penalties. Overall, our findings suggest that the dialect tax is encoded and accumulated not by any one step in isolation, but at every step of the language modeling process.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.24952
