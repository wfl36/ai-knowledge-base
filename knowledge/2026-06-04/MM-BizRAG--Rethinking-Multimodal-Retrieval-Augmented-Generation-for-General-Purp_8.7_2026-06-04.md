# MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A

**评分：** 8.7  
**状态：** 正常  
**标签：** 多模态, RAG, 大模型, 企业应用, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04231v1 Announce Type: new Abstract: Recent advances in multimodal retrieval-augmented generation (MM-RAG) have shifted toward minimal parsing, relying on page-level images for producing retriever embeddings and for answer generation. While efficient, this trend often neglects explicit handling of the rich, structured information in complex enterprise documents, instead depending on pre-trained embeddings or vision-language models to implicitly capture such structure. In this work, we take a more direct approach: MM-BizRAG proactively extracts and represents document structure via a document structure-aware split that dynamically routes documents through orientation-specific ingestion pipelines, applying explicit layout-aware parsing for vertically structured documents (e.g., reports) and holistic page-level representations for horizontally structured documents (e.g., slide decks). A unified LLM-driven artifact transformation pipeline with placeholder-based positional alignment preserves natural reading order, while inference-time multimodal assembly decouples retrieval representations from generation context, enabling richer, more grounded answers without any finetuning requirement. Through experiments on a large, heterogeneous enterprise dataset and two public benchmarks (SlideVQA and FinRAGBench-V), MM-BizRAG consistently outperforms state-of-the-art vision-centric baselines by up to 32% points, with especially strong gains on report-style layouts. Furthermore, we introduce FastRAGEval, a single-call LLM Judge metric for fine-grained generative recall that halves RAGChecker's cost while achieving stronger human alignment.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对当前多模态RAG过度依赖页面级图像而忽视文档显式结构的问题，提出了文档结构感知的动态路由机制（垂直布局采用显式解析，水平布局采用整体表示），并通过占位符对齐和推理时多模态组装解耦了检索与生成表示。技术方案新颖、系统设计精巧，且在多个基准上较SOTA最高提升32%，论证严谨。

### 实用性 (评分: 9.0/10)
对企业级复杂文档（如报告、幻灯片）的问答场景具有极高的落地价值。方案无需微调即可部署，动态路由和解析策略可直接指导企业RAG系统的工程架构设计，有效解决了传统RAG在处理复杂排版文档时的信息丢失和错位痛点。同时提出的FastRAGEval指标也大幅降低了RAG评估成本，实用性极强。

### 社区活跃度 (评分: 8.5/10)
紧扣当前多模态RAG在企业复杂文档处理中的痛点，时效性极强。在公开基准（SlideVQA, FinRAGBench-V）和异构企业数据集上取得了显著性能提升，且提出的低成本评估方法直击当前RAG评估成本高昂的痛点，来源权威，预期将在RAG工程与评估社区产生较大影响力。

## 项目链接
https://arxiv.org/abs/2606.04231
