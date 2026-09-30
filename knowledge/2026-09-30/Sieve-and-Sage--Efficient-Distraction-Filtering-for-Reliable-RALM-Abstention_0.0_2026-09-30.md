# Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35794v1 Announce Type: new Abstract: Just as Socrates recognized the limits of his own knowledge, Retrieval-Augmented Language Models (RALMs) should learn to abstain when the retrieved evidence cannot support a reliable response. Existing approaches largely rely on monolithic LLMs to handle heterogeneous retrieval failures in a single step, resulting in limited abstention performance and high computational costs. We instead decompose retrieval failures into two distinct states: (i) the unanswerable state, where the required evidence is absent, and (ii) the distracted state, where relevant evidence is mixed with conflicting, negated, or adversarial information. Based on this decomposition, we introduce a lightweight module (Sieve) that screens retrieved document sets for distracting evidence before invoking a costly LLM (Sage) for grounded generation and abstention. Evaluated across both general and high-stakes expert domains, our Sieve and Sage framework preemptively detects distracting noise, improving system accuracy by up to 69.4 percentage points and Macro-F1 by 55.2 percentage points compared to one-stage baselines. Furthermore, it achieves up to a 1.99x speedup, establishing a highly efficient and reliable abstention pipeline for RALM with abstention.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35794
