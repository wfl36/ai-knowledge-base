# Prompt Breadth and Rollout Refresh Interact in On-Policy Distillation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.25048v1 Announce Type: new Abstract: How many prompts does on-policy distillation (OPD) need, and how does the answer depend on the student policies that generate its training responses? We study these two controls jointly: prompt breadth and rollout refresh. A 3x3 mathematical-reasoning experiment fixes 14,080 trajectories and 110 optimizer updates while varying the prompt bank and the number of response-generating policy snapshots. With ten snapshots, eight prompts reach 24.09% average accuracy, close to 24.51% for 14,080 distinct prompts. With responses frozen at the initial policy, however, increasing breadth lowers accuracy from 21.16% to 19.05%; under per-update refresh, it raises accuracy from 23.61% to 25.57%. The resulting interaction is 4.07 percentage points, with a 95% question-paired interval of [2.00, 6.28]. Matched comparisons under two teachers reveal a second reversal: the periodic models have higher short-budget accuracy and answer completion, but frozen-response models overtake in average accuracy at a 32K output limit, using 1.7-1.8x as many response tokens. These results show that prompt efficiency in OPD can depend on both refresh and inference budget.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.25048
