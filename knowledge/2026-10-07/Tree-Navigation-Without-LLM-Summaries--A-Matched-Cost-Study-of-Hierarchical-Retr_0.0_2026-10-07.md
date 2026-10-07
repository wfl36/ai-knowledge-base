# Tree Navigation Without LLM Summaries: A Matched-Cost Study of Hierarchical Retrieval for Long-Document QA

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-07  
**来源：** rss  

## 项目描述
arXiv:2610.06902v1 Announce Type: new Abstract: Retrieval-augmented generation grounds language models in external context, but for long documents flat top-$k$ retrieval can cluster on a single region and miss complementary evidence. RAPTOR-style summary trees address this by recursively clustering chunks and using a language model to summarize each cluster at indexing time, then ranking summary nodes alongside raw chunks at query time. We show the main benefit of summary trees in long-document QA can come from navigation rather than the generated summary content. We introduce NavTree, a leaves-only retriever that builds a deterministic balanced segment tree over chunks (zero language-model calls at indexing) and uses the tree purely as a navigation scaffold: a hybrid lexical-and-dense frontier walk, anchored on top retrieved leaves, descends from the root and emits only leaf chunks to the reader. On a matched-cost evaluation against flat retrievers and an extractive re-implementation of RAPTOR, NavTree is the strongest matched-cost hierarchical retriever in our evaluated grid and ties the strongest flat baseline. On long-document multi-hop QA, it is the only hierarchical method that significantly beats BM25 on a class-vs-class basis, corroborated by a reader-free retrieval-recall check. A matched-reader replication of the published abstractive RAPTOR variant, given strong cluster summaries, still loses to NavTree at every multi-chunk budget, at zero indexing cost. The ranking carries across stronger and open-weight readers, a stronger encoder, and a full factorial that isolates leaves-only emission as the structural lever.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.06902
