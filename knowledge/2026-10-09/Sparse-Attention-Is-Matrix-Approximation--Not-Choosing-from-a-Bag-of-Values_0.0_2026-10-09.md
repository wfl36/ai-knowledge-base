# Sparse Attention Is Matrix Approximation, Not Choosing from a Bag of Values

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10871v1 Announce Type: new Abstract: Large Language Models (LLMs) achieve strong performance across many domains, but their efficiency is limited by the quadratic cost of attention with respect to prompt length. Sparse attention reduces this cost by retaining only a small fraction of query-key interactions to approximate the full attention matrix. However, existing methods are trapped in a mathematically wrong view: they simply keep large scalar entries or high-mass regions of the attention matrix. This treats the attention matrix as a bag of values, ignoring that it is used as a structured matrix whose entries jointly determine the attention output through multiplication with value vectors. We argue that this is the core conceptual issue: sparse attention should be formulated as matrix approximation, not as blindly choosing the largest values from a bag of entries. Based on this view, we propose Matrix Approximation Sparse Attention (MASA). MASA replaces raw attention-mass ranking with a closed-form score that measures how much each sparse unit reduces matrix-product approximation error. As a theory-grounded plug-in correction, MASA can be added to existing sparse attention frameworks without changing their sparse kernels or budgets. Extensive experiments across multiple sparse attention methods, benchmarks, and LLM backbones show consistent accuracy gains, supporting both MASA and the matrix-approximation view of sparse attention.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10871
