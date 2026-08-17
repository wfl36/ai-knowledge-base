# Stable Miscalibration in Large Language Models: A Practical View of High-Confidence Errors

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** rss  

## 项目描述
arXiv:2608.13591v1 Announce Type: new Abstract: High-confidence errors in large language models are often treated as evidence of fragile internal inference. We study a different possibility: stable miscalibration, where a confident wrong answer remains locally stable under small perturbations. We combine two diagnostics: a label-aware output-level audit score that ranks domains by confidence variation and overconfident mistakes under a forced-answer baseline, and an internal sensitivity probe that measures hidden-state movement. On a multi-domain binary factual audit set, this audit score tracks where abstention-aware self-critique reduces decision loss, although direct labeled baselines rank the same gain more strongly. Internally, self-critical prompting consistently reduces hidden-state sensitivity across layers in three open-weight models. This supports prompt-induced local stabilization rather than a purely output-level abstention pattern, but it does not imply calibration: audit-defined overconfident errors are not clearly more locally sensitive than confidently correct answers, so some high-confidence errors may be stable and miscalibrated rather than simply fragile.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.13591
