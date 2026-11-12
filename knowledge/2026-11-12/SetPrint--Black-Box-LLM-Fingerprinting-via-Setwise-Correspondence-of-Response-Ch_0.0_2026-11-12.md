# SetPrint: Black-Box LLM Fingerprinting via Setwise Correspondence of Response Changes

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-12  
**来源：** rss  

## 项目描述
arXiv:2611.12950v1 Announce Type: new Abstract: Black-box LLM fingerprinting aims to determine whether a target model was derived from a source model when only the output responses to input queries are observable. One way to reveal this relationship is to perturb each query and observe the resulting responses of both models, yielding two corresponding sets of response variations. These sets provide two complementary sources of information: the relations among response changes within each set, and the correspondence of response changes between the two sets. Existing approaches, however, have not fully exploited both. We introduce \textbf{SetPrint}, a training-free method that jointly captures both within-set relations and between-set correspondence. SetPrint expresses each response change relative to the mean change of its own set, and then compares changes from the two models that were induced by the same perturbation. On LeaFBench, SetPrint consistently outperforms existing training-free black-box fingerprinting methods. Further analyses attribute these gains to both within-set relations and between-set correspondence.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.12950
