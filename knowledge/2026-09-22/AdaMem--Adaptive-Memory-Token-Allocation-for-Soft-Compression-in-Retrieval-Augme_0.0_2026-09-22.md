# AdaMem: Adaptive Memory Token Allocation for Soft Compression in Retrieval-Augmented Generation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.22100v1 Announce Type: new Abstract: Retrieval-augmented generation (RAG) improves language models with retrieved evidence, but processing many long passages is costly and can introduce distracting information. Soft compression addresses this challenge by encoding passages as compact sequences of continuous memory embeddings before generation. However, existing methods typically assign each retained passage an identical number of memory embeddings, irrespective of its query-specific relevance. To address this, we propose AdaMem, a relevance-guided soft-compression framework that maps learned passage-relevance estimates to a query-dependent allocation of a fixed memory-token budget. A shared query-conditioned compressor produces both continuous passage memories and relevance scores in a single pass; a deterministic allocation rule assigns more memory tokens to higher-scoring passages and can omit low-scoring ones. Across six open-domain QA benchmarks, AdaMem consistently outperforms OSCAR (the closely matched soft-compression baseline that uses uniform allocation) as well as other soft-compression methods at matched memory budgets. Under standard 16$\times$ compression, AdaMem improves sub-string match by up to 3.2 points (5.5%) over uniform allocation baseline, with an average relative gain of 3.4%; under aggressive 64$\times$ compression the average relative gain grows to 14.6%, with a maximum of 9.8 points (19.7%) on PopQA. AdaMem matches the answer quality of the uncompressed at up to 4$\times$ lower inference latency than full context baseline. AdaMem retains an efficiency profile comparable to the uniform-compression baseline, while achieving up to $4\times$ lower inference latency than full-context inference. Thus, relevance-guided memory allocation is particularly effective when retrieval pools are large and the available memory budget is tight.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.22100
