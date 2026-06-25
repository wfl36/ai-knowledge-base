# Error-Aware TF-IDF Retrieval-Augmented Generation for ASR Error Correction

**评分：** 8.5  
**状态：** 正常  
**标签：** ASR, RAG, 错误纠正, 低资源语言, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.24915v1 Announce Type: new Abstract: End-to-end automatic speech recognition systems frequently hallucinate rare entities and domain-specific terms, especially in low-resource languages. While retrieval-augmented generation frameworks can mitigate these errors using large language models, current architectures face significant challenges. They either rely on standard sparse retrieval that ignores phonetic misrecognitions or utilize heavyweight cross-modal embeddings that introduce high latency. This letter proposes a highly efficient, purely lexical error-aware framework designed to explicitly resolve phonetic and loop hallucinations. Our approach integrates a symmetric text normalization module with a novel error-aware term frequency-inverse document frequency algorithm. By constructing a sparse diagonal penalty matrix based on historical errors, the retriever mathematically prioritizes corrective documents containing specific high-risk misrecognitions. Evaluated on the Persian subset of the FLEURS dataset, our method increased the error-aware hit rate from 53.7% to 90.9%. In end-to-end evaluations, the integrated framework reduced the final word error rate from 23.06% to 18.83%, achieving significant accuracy gains with near-zero inference latency.

## 综合总结
本文提出了一种高效的纯词汇错误感知RAG框架，用于纠正端到端ASR系统中的罕见实体和领域术语幻觉。该框架结合对称文本归一化模块和错误感知TF-IDF算法，通过构建基于历史错误的稀疏对角惩罚矩阵，使检索器优先匹配纠正文档。在FLEURS波斯语子集上的实验表明，该方法将错误感知命中率提升至90.9%，词错率降至18.83%，且几乎不增加推理延迟，为低资源语言ASR纠错提供了一种轻量高效的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了一种新颖的错误感知TF-IDF算法，通过构建稀疏对角惩罚矩阵将历史ASR错误显式融入检索过程，有效解决了传统稀疏检索忽略语音误识别的问题。该方法在数学上严谨，且相比重量级的跨模态嵌入方案更为轻量，展现了较好的研究深度与算法创新性。

### 实用性 (评分: 9.0/10)
对工业界极具参考价值，同时解决了ASR幻觉和跨模态检索高延迟两大痛点。基于TF-IDF的改进工程实现成本低，且实现了近零推理延迟，非常适合对实时性要求高的生产环境部署，可直接应用于语音识别后处理、智能客服及低资源语言ASR纠错场景。

### 社区活跃度 (评分: 8.5/10)
ASR与RAG结合是当前大模型落地的重要方向，该研究针对低资源语言幻觉和检索延迟这两个热点问题提出了有效方案。arXiv论文来源，实验数据详实且指标提升显著（命中率提升至90.9%，WER降低逾4个百分点），具有较高的来源可信度和社区潜在关注度。

## 项目链接
https://arxiv.org/abs/2606.24915
