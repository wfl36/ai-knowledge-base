# LRMoE: Demand-Side Load Re-Calibration for Efficient MoE Training on Memory-Constrained Nodes

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-31  
**来源：** rss  

## 项目描述
arXiv:2610.37720v1 Announce Type: new Abstract: Sparse Mixture-of-Experts (MoE) models offer scalable capacity for Web applications, but uneven routing creates computation and communication bottlenecks. Existing placement and replication methods redistribute this workload, yet additional expert copies compete with token-related buffers for limited GPU memory. We present LRMoE, a memory-aware MoE training system that jointly recalibrates backward demand and balances the retained workload. During forward execution, it plans retention quotas and expert placement under resource constraints while preserving all routed computations. During backpropagation, a load recalibration metric estimates each token-expert pair's contribution to the expert update and selects pairs within these quotas. A capacity-aware routing algorithm distributes retained pairs among eligible instances of their original experts. Physical compaction then forms smaller communication payloads and variable-size grouped GEMMs, reducing backward traffic, computation, and execution-buffer demand. Experiments on Qwen3-30B-A3B and GLM4.5-106B-A12B show that LRMoE reduces cumulative MoE-layer training time to fixed-loss targets by 21.2-44.8% relative to SYMI.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.37720
