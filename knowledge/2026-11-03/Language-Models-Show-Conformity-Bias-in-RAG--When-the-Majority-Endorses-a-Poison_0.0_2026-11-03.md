# Language Models Show Conformity Bias in RAG: When the Majority Endorses a Poisoned Claim

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-03  
**来源：** rss  

## 项目描述
arXiv:2610.41012v1 Announce Type: new Abstract: Retrieval-augmented generation (RAG) can expose language models to misleading evidence in retrieved documents. We investigate whether increasing the number of mutually agreeing poisoned documents affects a model's ability to detect misinformation. We evaluate 200 randomly selected questions from SciFact (random seed 38), comparing contexts with one poisoned and six healthy documents against contexts with six mutually agreeing poisoned documents and one healthy document. For Gemma-3-12b, poison-detection rates decrease from 25% (50/200) in the minority condition to 10% (20/200) in the majority condition. Among the 38 questions with different outcomes across conditions, 34 change from detected to undetected, while only four change in the opposite direction (exact McNemar test, p = 6.04e-7). This pattern is consistent with a conformity-like response to a majority of mutually agreeing poisoned documents. Our results provide initial evidence of conformity bias in RAG-based misinformation detection: Gemma-3-12b is substantially less likely to detect poisoned claims when they dominate the retrieved evidence.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.41012
