# SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG

**评分：** 8.2  
**状态：** 正常  
**标签：** RAG, 长文档, 注意力机制, 层次化检索, 论文  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18381v1 Announce Type: new Abstract: Retrieval-augmented generation (RAG) systems must balance retrieval granularity with contextual coherence, a challenge that existing methods address through LLM-guided chunking, single-level context expansion, or hierarchical summarization. These approaches variously depend on costly LLM calls during indexing or retrieval, limit context aggregation to a single granularity level, or introduce information loss through summarization. We present SproutRAG, an attention-guided hierarchical RAG framework that addresses this trade-off by organizing sentence-level chunks into progressively larger but semantically coherent units, using learned inter-sentence attention to construct a binary chunking tree. Unlike prior approaches that rely on external LLMs, fixed context expansion, or lossy summarization, SproutRAG learns which attention heads and layers best capture semantic document structure, enabling multi-granularity retrieval without additional LLM calls or compressed summaries. At retrieval time, SproutRAG uses hierarchical beam search to retrieve candidates at multiple granularities, capturing multi-sentence relevance beyond flat retrieval. The framework is trained end-to-end with a joint objective that improves both embeddings and tree structure. Experiments across four benchmarks spanning scientific, legal, and open-domain settings demonstrate that SproutRAG improves information efficiency (IE) by 6.1% on average over the strongest baseline. Code is available on https://github.com/AmirAbaskohi/SproutRAG.

## 综合总结
SproutRAG提出了一种基于注意力引导的层次化RAG框架，通过学习句子间注意力自动构建二叉分块树，实现无需LLM调用、无信息损失的多粒度检索。结合层次化束搜索与端到端训练，在四个长文档基准上实现了6.1%的信息效率提升，为长文档RAG提供了一种高效且低成本的落地新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出SproutRAG框架，创新性地利用学习到的句子间注意力构建二叉分块树，实现多粒度语义单元的自动组织。该方法避免了传统层次化RAG中昂贵的LLM调用和信息损失的摘要压缩，采用层次化束搜索进行多粒度检索，并通过端到端联合优化目标同时提升嵌入表示和树结构，技术深度和新颖性较高。

### 实用性 (评分: 8.0/10)
针对长文档RAG中的分块与检索痛点，提供了一种无需额外LLM调用成本的多粒度检索方案。框架已开源，可直接应用于法律、科研等长文档场景的RAG系统优化，但端到端的训练方式可能对工程部署的算力有一定要求，整体落地参考价值高。

### 社区活跃度 (评分: 8.0/10)
RAG及长文档处理是当前AI领域的核心热点。该论文来自arXiv且代码开源，来源可信。其提出的低成本、多粒度RAG方案直击行业痛点，有望在RAG工程与学术社区产生较大影响力与讨论度。

## 项目链接
https://arxiv.org/abs/2606.18381
