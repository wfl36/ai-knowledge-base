# RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20971v1 Announce Type: new Abstract: Long-context large language model inference is increasingly limited by prefill, where dense self-attention processes the entire prompt before generation begins. Sparse block selection can reduce this cost, but a block centroid may hide a highly relevant token among many irrelevant ones. We call this failure mode mean dilution and propose RBS-Attention, a training-free sparse-prefill method with two complementary selection branches. A centroid base branch captures average relevance, while a rescue branch uses the maximum key-block radius and its prompt-, layer-, and head-dependent distribution to identify blocks at risk of underestimation. Independently thresholding the two branches and combining their masks controls the contribution of rescue blocks while preserving regular block-sparse FlashAttention execution. On H100 GPUs, RBS-Attention achieves 20.65$\times$ standalone prefill-attention speedup, 11.92$\times$ vLLM prefill-attention speedup, and 5.97$\times$ end-to-end time-to-first-token speedup at 128K on Qwen3-30B-A3B-Instruct-2507-FP8. On the dense Qwen3-32B model, it obtains 88.65 overall RULER accuracy versus 89.52 for dense attention; LongBench-v2, InfiniteBench, and Video-MME provide additional quality evaluation. Supporting experiments measure actual retention, compare selectors at matched density, and characterize block-size, threshold, and memory behavior. Together, these results support radius-adaptive dual-branch selection as an effective approach to long-context prefill.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20971
