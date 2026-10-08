# LRCC: Generalizing Low-Rank Compression with Conditional Computation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-08  
**来源：** rss  

## 项目描述
arXiv:2610.08858v1 Announce Type: new Abstract: Low-rank compression reduces the cost of pretrained language models by replacing linear transformations with low-rank factorizations. However, conventional methods use a fixed rank allocation during inference, assigning the same amount of compute regardless of the input token. We introduce Low-Rank Conditional Computation (LRCC), which adds token-dependent computation to pretrained models by training one lightweight router per Transformer block to select among a small set of nested low-rank paths. During training, the low-rank factors remain frozen, and only the routers are optimized. We evaluate LRCC on Llama and Qwen models for language modeling and zero-shot downstream tasks. Within the same average active-parameter budget, LRCC improves the predictive performance over static low-rank compression, including a 7.6 percentage-point gain in average downstream accuracy on Llama-2-7B over static methods. At matched batch-size-1 decoding latency, LRCC improves both perplexity and downstream accuracy on Llama-3.2-1B and remains competitive on Llama-2-7B, without specialized kernels. Finally, we assess the usefulness of assigning a token-wise path by analyzing the routers' path choices.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.08858
