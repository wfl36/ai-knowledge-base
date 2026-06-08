# Accelerated Fourier SAT (AFSAT): Fully Realising a GPU-based Symmetric Pseudo-Boolean SAT Solver

**评分：** 8.0  
**状态：** 正常  
**标签：** SAT求解器, GPU加速, JAX, 伪布尔可满足性, 连续局部搜索, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06641v1 Announce Type: new Abstract: We present Accelerated Fourier SAT (AFSAT), a GPU-accelerated solver for pseudo-Boolean satisfiability based on continuous local search (CLS). AFSAT realises the proof-of-concept approach, FastFourierSAT, into a fully-engineered solver supporting any heterogeneous mixture of symmetric constraint types and lengths within a single problem instance. Using the JAX compiler, AFSAT leverages pure function composition, automatic vectorisation, automatic differentiation, and just-in-time (JIT) compilation to perform massively parallel CLS across batches of candidate assignments. We demonstrate substantially improved numerical stability, runtime performance, and memory efficiency over the proof-of-concept. We achieve this by way of identifying and addressing various limitations that arise from memory latency and floating-point representation, as well as leveraging automatic parallelisation and compact representations. The inherent representational and stability limitations of floating point are partially addressed by a tailored discrete Fourier transform implementation. We achieve near-linear throughput when scaling to multiple accelerators via JAX array sharding.

## 综合总结
本文介绍了AFSAT，一个基于GPU和JAX编译器的伪布尔SAT求解器。它通过连续局部搜索和定制的离散傅里叶变换，成功将概念验证系统转化为支持异构约束的工程化求解器，有效解决了浮点稳定性与内存延迟瓶颈，实现了大规模并行计算和多加速器近线性吞吐量扩展，显著提升了求解性能与工程可用性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了AFSAT，一种基于GPU加速和连续局部搜索(CLS)的伪布尔SAT求解器。技术深度体现在将早期的概念验证系统转化为完全工程化的求解器，利用JAX编译器实现了纯函数组合、自动向量化、自动微分和JIT编译，以执行大规模并行CLS。同时，针对浮点表示的固有局限和内存延迟问题，设计了定制的离散傅里叶变换实现和紧凑表示方法，显著提升了数值稳定性，并在多加速器扩展中实现了近线性吞吐量。

### 实用性 (评分: 8.0/10)
对组合优化、形式化验证和运筹调度等领域的从业者具有极高的参考价值。GPU加速和JAX框架的引入使得处理复杂异构对称约束的大规模并行求解成为可能，克服了传统SAT求解器的算力瓶颈。其多加速器近线性扩展的特性，使其能够直接应用于高性能计算集群，具备极强的工业级落地潜力。

### 社区活跃度 (评分: 7.5/10)
SAT求解是计算机科学的经典核心问题，而利用GPU和现代深度学习编译器（如JAX）对传统离散搜索问题进行连续化并行加速是当前极具时效性和前沿性的研究方向。论文来自arXiv，具备学术可信度，其从PoC到全功能工程化求解器的跨越，对约束求解和异构计算社区均具有积极的影响力。

## 项目链接
https://arxiv.org/abs/2606.06641
