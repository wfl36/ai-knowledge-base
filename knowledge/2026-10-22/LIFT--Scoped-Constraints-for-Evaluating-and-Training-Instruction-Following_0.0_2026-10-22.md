# LIFT: Scoped Constraints for Evaluating and Training Instruction Following

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-22  
**来源：** rss  

## 项目描述
arXiv:2610.28819v1 Announce Type: new Abstract: Common instruction following (IF) benchmarks, such as IFEval, evaluate the ability of language models (LMs) to follow simple constraints that can easily be verified programmatically. These same constraints, in turn, are used as reward signals for reinforcement learning. This design may lead to reward hacking of constraints, pushing models away from the main task. Recent attempts to address this resulted in benchmarks with richer constraints, but required expert labor, remained closed-access, and cannot be easily extended. We present Lift-Bench, an IF benchmark that asks a model to draft a document given a topic and a structured outline. Constraints are scoped to certain document sections, providing finer control over constraint density. Lift-Bench includes both verifiable and judged constraints, as well as a training counterpart, Lift-Train. Importantly, Lift-Bench provides both main task and instruction-following constraints, mitigating shallow reward hacking. On experiments with multiple models, we find that frontier models struggle with the harder subsets of our benchmark and analyze model performance along multiple axes. We also find that training on Lift-Train is much less susceptible to reward hacking than training on the common IFTrain. Lift-Bench and Lift-Train are publicly available, as well as the data generating pipeline.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.28819
