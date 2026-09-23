# Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.22478v1 Announce Type: new Abstract: Behavioural evaluations of hosted language models can vary because the evaluated service, the measurement instrument, or both differ across runs. We separate three validation questions: whether a prior finding recurs on fresh data under its historical configuration (replication), whether the endpoint changes when the evaluation-and-inference configuration is rebuilt under the same identifier (measurement sensitivity), and whether the finding persists across subsequently tested identifiers under one common instrument (persistence). We study these questions in Regent Chess, a sequential environment in which a hidden, mutable state is recorded exactly, allowing stated beliefs to be scored against ground truth at action time; positive endpoint values mean worse performance than a matched-uniform comparator. The previously reported Gemini 3.1 Flash-Lite deficit recurs on fresh games under its historical configuration (+0.0530, 95% CI [+0.0329,+0.0714]). In a back-to-back same-day H/R comparison under the same public identifier, the model-minus-uniform endpoint is 0.0429 lower under the rebuilt configuration (95% CI for the H-minus-R contrast [+0.0182,+0.0667]); all six configuration components vary jointly, so no component is isolated. Under rebuilt R, the prospectively frozen, interleaved same-window 4K comparison reverses sign between Gemini 3.1 and Gemini 3.7, identifiers that differ in release and product tier; additional descriptive and exploratory cells show the same directional pattern. Any additional serving-period contribution remains unresolved (-0.0166, [-0.0483,+0.0157]). Replication, measurement sensitivity, and persistence can therefore yield different conclusions within one evaluation, motivating explicit indexing of hosted-model behavioural claims by tested identifier, serving period, measurement instrument, and inference configuration.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.22478
