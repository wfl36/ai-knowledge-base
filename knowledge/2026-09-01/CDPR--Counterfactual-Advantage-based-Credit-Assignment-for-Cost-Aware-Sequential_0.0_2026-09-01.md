# CDPR: Counterfactual Advantage-based Credit Assignment for Cost-Aware Sequential Medical Diagnosis

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28599v1 Announce Type: new Abstract: Clinical diagnosis is a step-by-step, cost-aware process: a physician orders examinations one at a time, observes the results, and updates the diagnosis before reaching a final conclusion. Most medical language models instead treat diagnosis as a one-pass classification task and ignore the trade-off between a test's value and its cost. We model diagnosis as a cost-aware sequential decision process and train the policy with reinforcement learning. The main difficulty is credit assignment: the only reliable signal comes once at the end of a long trajectory, so it scores a wasteful workup the same as an efficient one. We propose CDPR (Counterfactual Diagnostic Process Reward), which needs no expert labels and no learned critic. CDPR first finds the states where the policy hesitates, using the uncertainty of its action distribution, and then scores the chosen action by its advantage over the alternatives the policy itself would consider, estimated with short rollouts under a utility that balances correctness against test count, cost, and infeasible requests. A rollout cache reuses within-batch trajectories to keep the cost low. We integrate CDPR into GRPO and test it on one in-domain (MIMIC-IV) and two out-of-domain (ClinicalBench and a private hospital dataset) benchmarks. CDPR improves diagnostic accuracy while clearly reducing the number and cost of examinations.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.28599
