# Speedrunning Relational Foundation Model Pretraining

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-23  
**来源：** rss  

## 项目描述
arXiv:2610.28855v1 Announce Type: new Abstract: Progress on foundation model pretraining is gated by who can afford a trial, and relational pretraining is no exception. Recipes are developed inside individual labs, reported under private protocols, and do not accumulate. Speedrun leaderboards remove that barrier by decentralizing the search rather than the training run. The problem is fixed, the stack is open, entries are ranked by wall-clock time to a quality target, and one GPU is enough to hold the record. We introduce modded-nanoRT, the first such leaderboard for Relational Transformers. Which database to hold out decides whether the benchmark can resolve improvements at all, so we fix it by calibration, ranking six candidates by how sharply a 45-minute learning curve separates improvement from seed noise. We open the leaderboard with typed trilinear attention, a relational operator that conditions attention scores and values on the foreign key traversed, together with Muon and SIGReg. The recipe reaches the target in 305.63 seconds on one NVIDIA H200, 8.11x faster than the reference implementation, and wins 13 of 15 pairs outside the development database. We will release the benchmark, its frozen artifacts, and the record runs. Our code is available at https://github.com/kunumi/nanoRT.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.28855
