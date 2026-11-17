# Small Open-Weight Language Models for Crowd Decision-Making: Capabilities and Limits of Output-Level Fusion and Linguistic Aggregation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-17  
**来源：** rss  

## 项目描述
arXiv:2611.17589v1 Announce Type: new Abstract: Small open-weight language models can run crowd decision-making (CDM) on an institution's own infrastructure, which keeps the checkpoint, the inference settings and the opinions under its control. Their judgements vary across repeated queries; whether repeating and aggregating them, often through the 2-tuple linguistic representation, settles the decision rather than the labels is untested. Five open-weight models of 8-36B total parameters on one consumer GPU and a hosted reference classify 474 TripAdvisor reviews of four London restaurants ten times each; three open-weight models repeat the protocol on 600 reviews of twelve Madrid restaurants. Continuous evaluations preserve resolution: snapping each review leaves 5 distinct values against 21-65, and snapping at every level at most two collective values. Sensitivity to the participants persists once run-to-run variability is reduced: in London, redrawing the reviewers keeps the winner on 47-81% of replicas against 86-100% for redrawing the runs. With simultaneous intervals over every pair of alternatives under crowd resampling, no system on either corpus names a single winner: in London every system keeps all four restaurants as candidates, and in Madrid the candidate sets hold five to eight of the twelve. Extra runs and output-level fusion stabilize the winner but do not remove that sensitivity, and the fusion does not beat its best member. The three larger open-weight models name the hosted reference's London winner and at least match its per-review correlation with the reviewers' stars, so small open-weight models can support local CDM, reported as candidate sets with margins rather than forced rankings.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.17589
