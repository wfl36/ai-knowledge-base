# Recursive Language Models Generalize Out of Domain

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20831v1 Announce Type: new Abstract: We study when limiting what a language model can see improves learning. We compare standard CoT, the more general learner that reads the full trace, with recursive language models, which restricts itself by solving each subtask in an isolated context. In-distribution, this generality comes for free: CoT can efficiently simulate the recursive rule, so the IID generalization guarantee changes only by a constant factor, and recursion does not offer much. But out of domain, CoT can fit training by relying on context outside the current subtask, i.e. a shortcut that breaks once those tokens change; recursive context isolation rules out this failure mode. Even though CoT's class still covers the recursive rule, simplicity bias picks the shortcut over the truth. Thus, to go beyond distributional accuracy and truly reason, covering the right rule is not enough; this contrasts with classical learning theory.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20831
