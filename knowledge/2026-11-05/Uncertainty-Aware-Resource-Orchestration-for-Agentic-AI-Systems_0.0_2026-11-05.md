# Uncertainty-Aware Resource Orchestration for Agentic AI Systems

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05392v1 Announce Type: new Abstract: Agentic artificial intelligence (AI) systems powered by large language models (LLMs) execute as autonomous multi-step pipelines that dynamically invoke tools, integrate observations into memory, and iterate until a task is resolved or a resource budget is exhausted. Unlike classical workflows with fixed graphs, the aggregate compute, bandwidth, and end-to-end latency demands of such pipelines are unknown at dispatch time: they emerge at runtime from intermediate observations and stochastic token sampling, yielding heavy-tailed, multi-modal random variables. This unpredictability forces infrastructure orchestrators into a dilemma: under-provisioning risks mid-execution throttling and deadline violations, while over-provisioning wastes scarce edge or cloud capacity. Existing schedulers require a fully known pipeline graph, while edge resource-management methods rely on parametric or stationary demand models, and neither fits the unknown, non-stationary profiles of agentic pipelines. We formalize this setting as the uncertainty-aware agentic orchestration problem, where the goal is to reserve, at dispatch time, compute and bandwidth allocations that cover actual pipeline demands, and to verify that the pipeline can meet its deadline, each with a prescribed probability. We then propose Conformal Reservation for Orchestration (CRO), an online algorithm that translates a sliding window of past execution traces into dispatch-time resource allocations with finite-sample, distribution-free coverage guarantees via conformal prediction. Simulations over heterogeneous task mixes with multi-modal and heavy-tailed profiles show that CRO is the only evaluated method that simultaneously satisfies target probabilistic coverage across all risk levels while, among coverage-feasible methods, attaining the lowest over-reservation, roughly halving the resource waste of the Chebyshev-bound baseline.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05392
