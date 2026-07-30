# Kernel Forge: An Agent Harness for LLM-based Generation and Optimization of CUDA Kernels

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-30  
**来源：** rss  

## 项目描述
arXiv:2607.24762v1 Announce Type: new Abstract: Machine learning models are increasingly embedded in everyday software, and most of their runtime is spent in a small set of compute kernels such as matrix multiplication, convolution, and normalization. Optimizing these kernels is one of the most direct ways to reduce latency and cost, but it has traditionally required expert engineers to hand-write low-level GPU code. Agentic systems built on large language models (LLMs) can now generate and optimize kernels with far less human effort, yet existing tools are largely evaluated on randomly generated tensors and isolated kernels, emit standalone CUDA code that developers must manually reintegrate, mostly target only LLM PyTorch models, and offer limited support for inspecting and debugging results. We present Kernel Forge, an open-source, end-to-end agentic harness that accepts any unmodified PyTorch model in place. Kernel Forge supports vision, diffusion, and LLM workloads, uses Monte Carlo Tree Search (MCTS) to explore multiple optimization paths rather than a single linear refinement chain, and ships with a graphical user interface for monitoring progress, inspecting candidate kernels, and debugging failures. We evaluate Kernel Forge on four PyTorch models spanning vision, diffusion, and LLM workloads on an NVIDIA DGX Spark with GB10 GPU. With only 50 optimization iterations per kernel, it optimizes 14 kernels to outperform PyTorch eager mode, reaching $1.52\times$ on adaptive\_avgpool2d in ResNet-50, $1.70\times$ on group\_norm in Stable Diffusion 3.5 Medium, $2.83\times$ on softmax in Gemma 4 E2B, and $1.54\times$ on softmax in Qwen 3.5 35B-A3B.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.24762
