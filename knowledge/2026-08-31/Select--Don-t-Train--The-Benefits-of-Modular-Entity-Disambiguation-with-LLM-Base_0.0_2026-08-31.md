# Select, Don't Train: The Benefits of Modular Entity Disambiguation with LLM-Based Selection

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-31  
**来源：** rss  

## 项目描述
arXiv:2608.27470v1 Announce Type: new Abstract: Entity Disambiguation (ED) is a key task for constructing and using knowledge graphs. State-of-the-art neural approaches commonly model ED as a single task, although it consists of two distinct subproblems: retrieving candidate entities and selecting the correct one given context. Dual-encoder models optimize for both within a shared embedding space, forcing representations to balance high-recall retrieval with fine-grained selection, and they require trained retrievers, which are costly to maintain as knowledge graphs change. While recent work has begun to combine retrievers with LLM-based selectors, the interplay between the two stages has not been studied systematically. In this paper, we present a systematic comparison of retrieval strategies for candidate generation under a shared LLM-based selection stage, combining sparse retrieval (BM25), Web KB search, and a state-of-the-art trained dense retriever with several open- and closed-source LLMs. We show that, once selection is delegated to a capable LLM, training the retriever provides only modest additional value: a fully training-free BM25 retriever paired with an LLM selector reaches a new state of the art on the ZELDA benchmark, raising inKB micro-F1 from 82.3 to 86.3 (+4); pairing the same LLM with a trained dense retriever reaches 88.5. Decoupling retrieval from selection also exposes a limitation of current ED systems: when the correct entity is missing from retrieved candidates, they are forced to predict an incorrect entity. In contrast, our framework allows for abstention when retrieval failure is detected. In an evaluation setting that rewards correct abstentions, the training-free BM25 + LLM pipeline reaches 90.7 F1.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.27470
