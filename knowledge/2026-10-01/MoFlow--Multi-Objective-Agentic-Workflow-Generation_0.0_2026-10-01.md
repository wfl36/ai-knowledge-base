# MoFlow: Multi-Objective Agentic Workflow Generation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-01  
**来源：** rss  

## 项目描述
arXiv:2609.38294v1 Announce Type: new Abstract: We study the generation of agentic workflows that jointly optimize multiple objectives, such as accuracy, cost, latency, robustness, and consistency. Existing methods for workflow generation typically optimize accuracy alone or a weighted sum of objectives, so each trained generator commits to one fixed trade-off and must be retrained from scratch when preferences change. To alleviate this, we propose MoFlow, which generates workflows optimized across varied preferences. Specifically, MoFlow formulates workflow generation as a multi-objective Markov decision process and solves it by leveraging Convex-Hull Monte Carlo Tree Search with optimistic set-valued backups, where every node stores a set of reachable trade-offs rather than one weighted score. A single search thus approximately covers the Pareto front, from which MoFlow can return a workflow for any preference by lookup without retraining. We evaluate MoFlow against six strong baselines on six benchmarks spanning mathematics, code, and question answering. Since the baselines are single-scalar optimizers by design, an apples-to-apples comparison is difficult. We instead adopt an evaluation setup that favors the baselines, in that they are rerun for each testing preference, which MoFlow never sees. Even under this stringent setup, MoFlow achieves the highest average hypervolume.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.38294
