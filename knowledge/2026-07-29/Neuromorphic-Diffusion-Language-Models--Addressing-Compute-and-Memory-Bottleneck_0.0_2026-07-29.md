# Neuromorphic Diffusion Language Models: Addressing Compute and Memory Bottlenecks via Sparsity and Block Denoising

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-29  
**来源：** rss  

## 项目描述
arXiv:2607.24841v1 Announce Type: new Abstract: Autoregressive (AR) large language models (LLMs) are inherently inefficient at inference time because each generated token requires accessing the full set of model parameters, leading to low operational intensity and high energy consumption. Masked diffusion language models (MDLMs) partially address this limitation for memory-bound settings by allowing multiple tokens to be generated per parameter access. In order to further enhance inference efficiency on modern platforms with extensive in-chip memory, this work proposes neuromorphic MDLMs (N-MDLMs), which integrate block diffusion with spike-based neuromorphic computation to jointly improve throughput and energy efficiency. While block diffusion increases token throughput by producing multiple tokens per parameter access, spike-induced sparsity reduces effective parameter traffic and computations by skipping inactive channels. To analyze the synergistic effect of sparsity and diffusion, we develop a token-level roofline-inspired model that captures the combined impact of block-parallel generation and spike sparsity on decoding efficiency. Experimental results on translation tasks show that, thanks to spike-induced sparsity, N-MDLMs achieve substantial improvements in energy efficiency and throughput even in compute-bound platforms for which MDLMs would fail to improve over AR-LLMs.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.24841
