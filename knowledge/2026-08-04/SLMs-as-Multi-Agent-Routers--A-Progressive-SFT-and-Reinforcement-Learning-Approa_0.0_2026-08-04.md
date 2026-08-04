# SLMs as Multi-Agent Routers: A Progressive SFT and Reinforcement Learning Approach

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-04  
**来源：** rss  

## 项目描述
arXiv:2608.00030v1 Announce Type: new Abstract: Specialised retrieval agents typically surface higher quality results than general-purpose search, but selecting the optimal agent for a given query remains an open problem. Current approaches route queries based on inferred topic or intent, however intent-based selection is fundamentally limited: it does not incorporate signal from retrieved content, and cannot detect when a topically aligned agent produces low-relevance results. We address this by training a small language model via supervised fine-tuning followed by reinforcement learning to jointly perform agent selection and structured parameter generation for downstream tool calls, using a hierarchical reward function grounded in retrieval relevance along with query-agent topic alignment. This enables the model to learn task-dependent agent suitability from retrieval performance: which agents reliably yield high-relevance results for which query distributions, and when to redirect queries away from specialised agents despite surface-level topical overlap. On a targeted subset of such agent-query mismatches, the trained model achieves an NDCG@10 of 0.918 compared to 0.539 and 0.490 for two LLM baselines (Amazon Nova Lite and Claude Haiku 4.5) that route on intent alone. Overall, it achieves a mean NDCG@10 of 0.771 (+0.177 over Nova Lite, +0.219 over Haiku) with a mean selection latency of 120.1ms, an 82.4% reduction over Nova Lite.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.00030
