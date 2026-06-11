# INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration

**评分：** 8.8  
**状态：** 正常  
**标签：** 多智能体, 大模型, 推理优化, 资源调度, 基础设施感知, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11440v1 Announce Type: new Abstract: Existing multi-agent LLM orchestration methods, ranging from brute-force ensembles to learned routers, select models and topologies based on task and model features. However, these methods do not consider the runtime state of the serving infrastructure. On shared GPU clusters under concurrent load, this infrastructure blindness causes systematic resource underutilization: preferred models accumulate deep request queues while equally capable alternatives sit idle. In multi-agent pipelines, where each query triggers multiple sequential model calls, these delays then compound across every downstream step. Closing this gap is challenging because the relevant infrastructure signals (queue depths, KV-cache pressure, latencies) are dynamic and noisy, and they must drive three different decisions: planning, per-step routing, and scheduling. We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware. An infra-aware planner conditions topology and role selection on real-time system load and remaining budget, biasing toward simpler graphs under congestion and richer ones at low load. An infra-aware executor then observes per-model queue depths, cache utilization, and response latencies at each agent step to decide which model to call and how deeply to reason; a budget-aware scheduler further reorders each model's queue so that urgent requests are served first. Cast as a hierarchical constrained MDP and solved end-to-end via reinforcement learning, the system learns to balance quality against latency automatically. Across five benchmarks, INFRAMIND delivers up to +7.6 pp accuracy over the prior baseline at low load with up to 7x lower latency, and sustains up to 99.9% SLO compliance under high load where every baseline drops below 50%.

## 综合总结
本文提出INFRAMIND框架，针对多智能体LLM编排中的‘基础设施盲区’问题，首次将实时系统负载（队列深度、KV缓存压力等）引入规划、路由和调度决策。通过构建分层约束MDP并利用强化学习端到端求解，系统在低负载下实现了+7.6 pp准确率提升和7倍延迟降低，在高负载下维持99.9%的SLO合规性，显著优于现有基线，为多智能体系统的高效部署提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文创新性地指出现有多智能体编排的‘基础设施盲区’问题，将动态系统信号（队列深度、KV缓存压力等）纳入决策。通过构建分层约束MDP模型，联合优化规划、路由和调度三个层级，并使用强化学习端到端求解，技术深度与严谨度高，实验数据显著。

### 实用性 (评分: 8.5/10)
对多智能体系统部署与工程实践具有极高的指导价值。提出的Infra-aware Planner和Executor机制可直接应用于共享GPU集群的LLM服务场景，有效解决高并发下的资源闲置与延迟累积问题，大幅提升SLO合规性。

### 社区活跃度 (评分: 9.0/10)
聚焦多智能体编排与LLM系统优化的交叉热点，时效性极强。arXiv首发，实验数据详实，在低/高负载下均取得突破性指标，对Agent基础设施层的发展具有重要参考意义和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.11440
