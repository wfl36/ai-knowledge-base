# RouteRec: Strict Evaluation of Recommender-Agent Selection and Aggregation

**评分：** 8.0  
**状态：** 正常  
**标签：** 推荐系统, Agent, 大模型, 路由, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09908v1 Announce Type: new Abstract: Recommender systems increasingly face a choice among heterogeneous agents -- collaborative filters, sequential models, content-based retrievers, and LLM-based rerankers -- yet no single agent is uniformly best. We study this choice as task-aware agent ranking under cost constraints using RouteRec, a framework that compares request-level hard selection with item-level learned aggregation over four traditional recommender agents and one LLM reranker agent. On MovieLens-1M, the full quality oracle has substantial headroom (HR@10 = 0.584), confirming that useful cross-agent signal exists. Under a leakage-free 5-fold out-of-fold protocol, however, hard selection remains below BM25 (0.223 vs. 0.254), and selective LLM escalation does not improve it. The same protocol yields a different outcome for learned aggregation: its cheap-only variant matches BM25 in HR and has a higher NDCG point estimate (0.123 vs. 0.114), while gated all-agent aggregation reaches HR@10 = 0.295 with 70.2\% LLM calls. The resulting lesson is not that routing is solved, but that request-level selection of one complete agent list is too coarse for this sparse fixed-candidate setting; item-level aggregation is the more promising action space.

## 综合总结
本文提出RouteRec框架，严格评估了推荐系统中异构智能体的选择与聚合策略。研究发现，在无泄漏评估下，请求级硬选择效果不如传统BM25，而项级学习聚合能在控制LLM调用成本的同时显著提升性能。该结论为混合推荐系统的架构设计提供了重要指导，表明细粒度的项级聚合比粗粒度的智能体路由更具前景。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出RouteRec框架，将异构推荐智能体的选择建模为成本约束下的任务感知排序问题。通过严格的无泄漏评估协议，发现请求级硬选择表现不及传统基线，而项级学习聚合能显著提升效果，揭示了在稀疏固定候选集下粗粒度路由的局限性与细粒度聚合的优势，论证严谨且具有反直觉的洞见。

### 实用性 (评分: 8.5/10)
对工业界构建混合推荐系统（特别是融合LLM与传统模型）具有高参考价值。研究指出盲目进行请求级智能体路由效果不佳，而采用项级聚合策略并配合门控机制，能在控制LLM调用成本（仅70.2%调用率）的同时显著提升推荐性能，直接指导多模型融合的架构设计与成本优化。

### 社区活跃度 (评分: 7.5/10)
话题紧扣当前LLM与传统推荐系统融合、Agent路由的热点，对“万物皆可路由”的风潮提供了理性的实证反思。论文来自arXiv，评估方法严格，结论具有启发性，易引发学术界和工业界对推荐系统Agent化路径的深入讨论。

## 项目链接
https://arxiv.org/abs/2607.09908
