# SELD: Detecting Silent Evidence Loss in Context Compression beyond the Answer

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-12  
**来源：** rss  

## 项目描述
arXiv:2611.12903v1 Announce Type: new Abstract: Context compression is now routine for language models with long inputs, but a compressed context is useful only if it keeps the evidence for the answer. Existing checks compare the reader model's answer or its most likely words, and thus miss a frequent failure, silent evidence loss: key evidence is removed while the answer stays the same, leaving the answer unsupported and risky for other models that reuse the context. To address this challenge, we propose SELD (Silent Evidence Loss Detector), which needs no training and no labels. Its principle is that when evidence is lost, a reader model's preferences among the answers it leaves unsaid shift even if its answer does not, so comparing these preferences before and after compression reveals losses that answer checks cannot see. We also build SEL-Pairs, a benchmark of length-matched evidence and control deletions from three question-answering datasets. Quantitative and qualitative experiments with five reader models on it show that SELD consistently outperforms strong and recent baselines across compressors, compression rates and models, identifying the evidence-removing edit in 83% of matched pairs with unchanged answers, against 70% for the strongest baseline. These results show that evidence loss in compressed contexts can be detected even when the answer is unchanged.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.12903
