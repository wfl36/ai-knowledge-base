# Infinity-Parser2 Technical Report

**评分：** 9.2  
**状态：** 正常  
**标签：** 多模态, 文档解析, 强化学习, OCR, 数据合成, 技术报告  
**更新日期：** 2026-07-10  
**来源：** rss  

## 项目描述
arXiv:2607.07836v1 Announce Type: new Abstract: We present Infinity-Parser2, a large multimodal model that couples a controllable data-synthesis pipeline with multi-task reinforcement learning for end-to-end document parsing, addressing the persistent scarcity of faithfully annotated parsing corpora. Our contributions are threefold. First, we build a scalable synthesis engine, pairing a controllable rendering framework with an iterative refinement loop, and use it to construct and open-source Infinity-Doc2-5M: a 5-million-sample bilingual (Chinese/English) corpus spanning diverse document types, annotated with element bounding boxes, canonical content forms (Markdown, HTML, LaTeX, SMILES, structured charts), and full-page reading order. Second, we introduce a verifiable, multi-task reward system that enables Joint Reinforcement Learning across eight co-trained objectives (document parsing, layout analysis, table parsing, math formula parsing, chart parsing, chemical formula parsing, document VQA, and general multimodal understanding), unifying perception, structure, and reasoning in a single optimization signal. Third, we release two variants under a shared architecture: Infinity-Parser2-Flash, optimized for low-latency inference with a $3.68\times$ throughput gain over Infinity-Parser-7B, and Infinity-Parser2-Pro, engineered for precision-critical settings. Infinity-Parser2-Pro reaches state-of-the-art 87.6% on olmOCR-Bench and 74.3% on ParseBench, surpassing DeepSeek-OCR-2, PaddleOCR-VL-1.5, and MinerU2.5, with strong generalization to charts, chemical formulas, and document VQA.

## 综合总结
Infinity-Parser2通过结合可控数据合成管道与多任务联合强化学习，解决了文档解析领域的高质量数据稀缺与多任务协同优化难题。该研究开源了500万规模的双语数据集Infinity-Doc2-5M，并推出Flash与Pro两种模型变体，在olmOCR-Bench和ParseBench等基准上刷新SOTA，超越DeepSeek-OCR-2等强基线，为工业级端到端文档解析提供了极具落地价值的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了一种结合可控数据合成管道与多任务强化学习的大型多模态模型Infinity-Parser2，有效解决文档解析中高质量标注语料稀缺的痛点。技术创新点显著：1）构建了可扩展的合成引擎并开源5M双语数据集，支持多种内容格式与版面标注；2）设计了可验证的多任务奖励系统，在8个目标上进行联合强化学习，统一了感知、结构与推理的优化信号；3）模型在olmOCR-Bench和ParseBench上达到SOTA，论证严谨，技术深度极高。

### 实用性 (评分: 9.5/10)
对从业者具有极高的落地参考价值。开源了包含500万样本的双语数据集Infinity-Doc2-5M，直接填补了领域数据空白；提供Flash（低延迟，吞吐量提升3.68倍）和Pro（高精度）两种变体，完美适配工业界对速度和精度的不同需求；在表格、数学公式、图表、化学式及文档VQA等复杂任务上表现优异，全面超越DeepSeek-OCR-2等主流方案，可直接指导并应用于RAG和知识提取等业务场景。

### 社区活跃度 (评分: 9.0/10)
文档解析与多模态理解是当前AI社区的核心热点，对大模型落地应用至关重要。该技术报告在arXiv发布，开源了高质量数据集与模型，且在权威基准测试上取得SOTA，超越了DeepSeek-OCR-2、PaddleOCR等知名模型，具有极高的时效性、来源可信度与社区影响力，必将引发广泛关注。

## 项目链接
https://arxiv.org/abs/2607.07836
