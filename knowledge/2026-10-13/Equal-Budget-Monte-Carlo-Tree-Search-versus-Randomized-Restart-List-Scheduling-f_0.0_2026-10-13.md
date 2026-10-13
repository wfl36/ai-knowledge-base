# Equal-Budget Monte Carlo Tree Search versus Randomized-Restart List Scheduling for DAG Workflows: A Controlled Equal-Budget Computational Study

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-13  
**来源：** rss  

## 项目描述
arXiv:2610.12542v1 Announce Type: new Abstract: Monte Carlo Tree Search (MCTS) is often proposed for scheduling directed-acyclic-graph (DAG) workflows, yet most studies never run the comparison that could refute it - giving a much simpler method the same search effort. We run that comparison under a controlled protocol. All arms receive an identical budget - the same number of candidate schedules built and evaluated: an MCTS scheduling method, preregistered as the main arm; a randomized-restart list scheduler with no search tree as the control; and a textbook-UCT MCTS arm as a registered follow-up on the same domain. The analysis plan was locked before data collection; an independent checker confirmed all 768 confirmation-stage schedules valid with correct finish times. At the main budget of 2048 evaluated schedules, MCTS is 2.88% worse than the restarts (95% CI [-3.62%,-2.15%]; the 72 of 96 held-out instances with positive baseline-relative headroom). The deficit is not budget starvation: on the separate exploration pool restarts self-improve by 1.85% where MCTS gains 0.24%, and 700 of 720 of MCTS's first results are merely the warm start it was handed. The studied selection rule locks deterministically onto the first-expanded child, keeping its trials correlated while restarts draw gains from the tails; the causal link to makespan remains an inference. A structural map locates where the tree stops paying: restarts win on sparse irregular workflows, no difference is detectable on regular layered ones, and dense ones leave no room to improve. Swapping the rule for textbook UCT removes most of the deficit (-0.26%, 95% CI [-0.71%,+0.23%]) without reversing its sign. Results are confined to a controlled synthetic domain (N in {8,16,32} tasks, 2-8 processors, budgets up to 2048); we make no claim about larger budgets.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.12542
