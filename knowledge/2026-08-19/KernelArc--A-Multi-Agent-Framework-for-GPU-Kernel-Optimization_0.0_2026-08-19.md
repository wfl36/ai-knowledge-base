# KernelArc: A Multi-Agent Framework for GPU Kernel Optimization

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-19  
**来源：** rss  

## 项目描述
arXiv:2608.17071v1 Announce Type: new Abstract: We present KernelArc, a multi-agent framework for autonomous GPU kernel optimization across heterogeneous workloads. Strategy-specialized agents run in parallel and coordinate through conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-triggered drafting. We evaluate \kernelarc{} on NVIDIA H100 and B200 GPUs using category-representative SOL-ExecBench workloads. The resulting implementations span custom BF16 GEMM, static cuBLASLt Expert-API configuration tables, fused mixture-of-experts backward, shape-gated decoder-layer fusion, native NVFP4 grouped-query attention, and paged prefill attention. At the public SOL-ExecBench leaderboard snapshot recorded on July~30, 2026, these submissions ranked first on representative L1, L2, Quantization, and FlashInfer tasks. The trajectories support the paper's central motivation: shared multi-agent search can broaden exploration and reach stronger incumbents within a fixed candidate budget, while the value of individual coordination features depends on the kernel and optimization stage.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.17071
