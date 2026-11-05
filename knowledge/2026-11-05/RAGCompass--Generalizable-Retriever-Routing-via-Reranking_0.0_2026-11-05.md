# RAGCompass: Generalizable Retriever Routing via Reranking

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05596v1 Announce Type: new Abstract: Different retrievers exist for retrieval-augmented generation, yet none performs best for all queries. Therefore, the key question is: given a query and retrieved passages from different retrievers, which one is most suited for that query? Existing routers usually make predictions from query-specific features and a fixed pool of retrievers; such routers have no output for an unseen retriever and are incapable by design on a new corpus. To fill these gaps, RAGCompass reads the retrieved passage sets themselves: passages from an unfamiliar retriever or corpus stay directly comparable to other passages, so routing stays well designed where a query-only map would fail. We contrastively fine-tune a reranker against the answer each evidence set produces, which accounts for most of the gain; a small comparison head adds a moderate improvement, and neither component has retriever-specific parameters. RAGCompass improves answer F1 by 28% relative to the best fixed retriever, and outperforms fusion baselines, three query-only routers, and a prompted 8B language model. Generalization experiments show that RAGCompass keeps most of its gain under an unseen corpus, retriever, or reader, while query-only baselines fall to the best fixed retriever or below.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05596
