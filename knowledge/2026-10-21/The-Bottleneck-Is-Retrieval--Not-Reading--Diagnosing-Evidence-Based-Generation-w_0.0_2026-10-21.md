# The Bottleneck Is Retrieval, Not Reading: Diagnosing Evidence-Based Generation with RAG for Long Context Question Answering

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26951v1 Announce Type: new Abstract: Retrieval-augmented generation (RAG) is the dominant paradigm for grounding large language models in external corpora, but its similarity-driven, chunked pipeline has structural blind spots: it cannot anticipate which passages a question requires and discards document-level context that resolves cross-passage references. We introduce evidence-based generation (EBG), requiring models to return an answer with line-level citations, and a joint Ans+Evid metric that scores correctness and grounding simultaneously. We reformulate two corpora into evidence-grounded multi-document QA benchmarks- MultiHop-RAG and QASPER-MP, a multi-paper adaptation of QASPER with realistic short paper cues, and pair them with a controlled synthetic two-hop haystack and an evidence-augmented NoLiMa spanning 10K-1M characters. Across ten proprietary frontier and three open-weight LLMs, EBG isolates two RAG limitations that long-context models avoid: similarity retrieval surfaces any relevant chunk far more reliably than all required chunks for multi-fact queries, and chunking destroys document meta-information needed to resolve identity-bearing queries. EBG also exposes grounding failures invisible to answer-only evaluation, including incomplete citations in two-needle settings and a widening gap between Ans and Ans+Evid when context contradicts parametric knowledge. Data and code are available at https://github.com/debobanerjee/LC-EBG.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26951
