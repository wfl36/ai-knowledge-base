# Alignment Forecasting: Predicting Misalignment From Training Data

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35805v1 Announce Type: new Abstract: Training a language model on data with a narrow flaw can sometimes make the model broadly misaligned. Inspecting the data at face value often does not settle whether it will emerge, and today it is caught only after training, by auditing the resulting model. To complement post-hoc audits, we introduce Alignment Forecasting: the task of predicting alignment failures before training. Given a target model, a fine-tuning dataset, and a failure mode such as deception or sycophancy, a forecaster outputs the probability that fine-tuning would meaningfully increase that failure mode. To measure progress on alignment forecasting, we introduce ALIGNMENTFORECASTBENCH, a benchmark of over 5,000 forecasting questions spanning 17 target models, 32 datasets, and 16 failure modes. Frontier models prompted directly perform poorly on ALIGNMENTFORECASTBENCH. We therefore propose a forecasting scaffold in which an LLM reads the dataset and rates how strongly and broadly it pushes the model toward misbehavior, and a simple learned model combines that rating with the failure mode's base rate and the target model's prior tendency. This forecasts well above chance, and beats a model fine-tuned on the task and a simple forecaster allowed to see how weaker models behaved after fine-tuning on the same data. Its signals also flag problematic training examples that a frontier-model classifier misses. Filtering those examples out from real post-training data such as UltraChat results in more aligned models on our multiple-choice evaluation in most cases, though the benefit in open-ended conversations is unclear. More progress is needed before forecasts can reliably guide training data curation in practice, but our results suggest that forecasting many alignment failures before training can be tractable in the SFT setting.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35805
