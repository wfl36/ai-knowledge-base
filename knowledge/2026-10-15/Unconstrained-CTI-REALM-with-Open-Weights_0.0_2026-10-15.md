# Unconstrained CTI-REALM with Open-Weights

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-15  
**来源：** rss  

## 项目描述
arXiv:2610.14180v1 Announce Type: new Abstract: Organisations that want language-model agents for security work face a choice between open-weight models, which they can run and audit themselves, and far more expensive closed frontier models. We study that choice on CTI-REALM (arXiv:2603.13517), a benchmark in which an agent turns a threat-intelligence report into a working detection by querying a live telemetry store. We evaluate twenty-six models, nineteen open-weight and seven closed, under a common harness, scorer and panel of LLM judges. Our main finding is that an open-weight model can match the strongest closed models at less than a tenth of their cost, provided it is given enough turns. The benchmark's published limit on agent messages is a confound: a task that exhausts the limit scores zero on every checkpoint, including those it had already passed, so results at that limit partly measure which models finish in time. At the published limit the leading open-weight and closed models cannot be distinguished. With the limit relaxed, the models it was truncating recover, and the highest rewards belong to open-weight models. Among the leading models, price is a poor guide to capability: models with similar rewards differ in cost by more than an order of magnitude. Because the benchmark's checkpoint scores largely record what an agent did or mentioned, we also introduce stage-level metrics that score what the agent submits, by executing its detection queries in the telemetry store and judging its outputs against the answer key. Rather than combining them into one more overall reward, we show that different models lead different stages, which suggests routing each stage of the workflow to the model that performs it best rather than choosing a single model by its overall score. We also report how many tokens each model generates, and find that the share of output spent on thinking does not track the reward.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.14180
