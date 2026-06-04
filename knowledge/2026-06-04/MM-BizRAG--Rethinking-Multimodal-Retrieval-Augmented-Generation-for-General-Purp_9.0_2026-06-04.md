# MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A

**评分：** 9.0  
**状态：** 正常  
**标签：** RAG, 多模态, 文档解析, 知识库, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04231v1 Announce Type: new Abstract: Recent advances in multimodal retrieval-augmented generation (MM-RAG) have shifted toward minimal parsing, relying on page-level images for producing retriever embeddings and for answer generation. While efficient, this trend often neglects explicit handling of the rich, structured information in complex enterprise documents, instead depending on pre-trained embeddings or vision-language models to implicitly capture such structure. In this work, we take a more direct approach: MM-BizRAG proactively extracts and represents document structure via a document structure-aware split that dynamically routes documents through orientation-specific ingestion pipelines, applying explicit layout-aware parsing for vertically structured documents (e.g., reports) and holistic page-level representations for horizontally structured documents (e.g., slide decks). A unified LLM-driven artifact transformation pipeline with placeholder-based positional alignment preserves natural reading order, while inference-time multimodal assembly decouples retrieval representations from generation context, enabling richer, more grounded answers without any finetuning requirement. Through experiments on a large, heterogeneous enterprise dataset and two public benchmarks (SlideVQA and FinRAGBench-V), MM-BizRAG consistently outperforms state-of-the-art vision-centric baselines by up to 32% points, with especially strong gains on report-style layouts. Furthermore, we introduce FastRAGEval, a single-call LLM Judge metric for fine-grained generative recall that halves RAGChecker's cost while achieving stronger human alignment.

## 综合总结
本文提出MM-BizRAG框架，针对企业级复杂文档多模态RAG场景，摒弃了传统的隐式解析，引入文档结构感知的动态路由机制（垂直文档显式解析，水平文档整体表示），并通过占位符对齐与推理时的检索-生成解耦，在不微调模型的情况下显著提升了回答质量。实验证明其较SOTA最高提升32%，同时提出的FastRAGEval指标实现了降本增效，为企业级多模态知识库问答提供了极具实操性的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文针对当前多模态RAG过度依赖隐式特征捕捉而忽视文档显式结构的痛点，提出了结构感知的动态路由机制（区分垂直与水平结构文档），并创新性地在推理阶段解耦检索表示与生成上下文，结合占位符对齐保留自然阅读顺序。方法设计精巧且论证严谨，在多个数据集上最高提升32%，同时提出的FastRAGEval评估指标在降低成本的同时提升了与人类评价的对齐度，展现了扎实的研究深度与工程巧思。

### 实用性 (评分: 9.5/10)
对业界极具参考价值。企业级复杂文档（如财报、PPT）的多模态QA是RAG落地的核心难点，本文提出的动态路由、显式解析与检索生成解耦策略可直接指导工程实践。无需微调即可大幅提升效果的特点，极大降低了工业界部署与迁移的门槛，适用范围覆盖金融、企服等几乎所有涉及复杂文档知识库的场景。

### 社区活跃度 (评分: 9.0/10)
多模态RAG是当前大模型落地的前沿热点，本文直击企业级应用中的真实痛点，时效性极强。作者团队来自企业界，问题导向明确，且在公开基准与大型企业私有数据集上均给出了显著优于SOTA的实验结果，来源可信度高。其提出的评估指标也为社区提供了新的工具，具备较强的影响力潜力。

## 项目链接
https://arxiv.org/abs/2606.04231
