# Thought-Aware KV Cache Compaction for Reasoning via Adaptive Attention Matching

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-14  
**来源：** rss  

## 项目描述
arXiv:2608.12331v1 Announce Type: new Abstract: Reasoning language models generate lengthy chain-of-thought (CoT) sequences whose key-value (KV) cache grows linearly and becomes a memory bottleneck during decoding. Existing compaction methods treat reasoning trajectories as flat token sequences and apply uniform compression, ignoring the hierarchical structure of CoT reasoning where different steps vary drastically in importance. We propose \textbf{Thought-Aware Attention Matching (TAM)}, which exploits this structure through three mechanisms: (i)~thought segmentation that decomposes the trajectory into reasoning blocks, (ii)~adaptive budget allocation that assigns compression budget based on each segment's importance and size, and (iii)~pivotal token protection that preserves high-attention reasoning anchors. We prove that the allocation rule is optimal under a convex error model and that cumulative error under sequential compaction remains bounded. Experiments on AIME 2024 and MATH-500 with Qwen3-4B show that TAM improves accuracy over uniform compaction at the same memory footprint, with periodic compaction bounding peak memory to 3.1--3.2\,GB (a 65\% reduction) while maintaining competitive accuracy.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.12331
