# Dynamic Coalition Formation and Communication Pricing in Skill-Based Agentic AI Systems

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-11  
**来源：** rss  

## 项目描述
arXiv:2608.07532v1 Announce Type: new Abstract: Modern agentic AI systems combine multiple large language model agents with heterogeneous skills, yet most architectures either fix communication in advance or allow full broadcast. Both can be inefficient because token cost, latency, redundancy, and error propagation increase with the number of active agents and communication links. We model agent selection and communication as a cooperative game with task-conditioned net utility $U(C\mid x)=V(C\mid x)-\sum_{i\in C}c_i$, separating coalition-level costs from agent activation costs. We propose a marginal-value activation rule and greedy router, extend the model to optimize communication edges with per-edge costs, and use estimated Shapley values to predict which agents are worth contacting before and during execution. We connect the problem to submodular maximization and prove two limited guarantees: a curvature-refined bound for a monotone, cardinality-constrained special case, and a tight $1/2$-approximation, with a correction for signed objectives, for an unconstrained non-monotone case via double greedy. Neither guarantee applies directly to the main router, which remains a heuristic. We also prove a Shapley-submodularity sandwich bound linking the error of marginal-value routing to a per-agent diminishing-returns quantity. In synthetic experiments, greedy routing achieves $99.5%$ of brute-force-optimal utility while activating $1.96$ of $8$ agents on average, compared with $38.8%$ for full broadcast. Performance is robust to activation cost and redundancy weight but falls to $66%$ under strong violations of submodularity or noisy value estimates. We distinguish the framework from Shapley pricing, hedonic coalition formation, and communication-graph pruning, and propose evaluation on real multi-agent LLM benchmarks.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.07532
