# Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms

**评分：** 7.7  
**状态：** 正常  
**标签：** 多模态, 文档理解, 低资源语言, 基准评测, 论文, 数据集  
**更新日期：** 2026-07-27  
**来源：** rss  

## 项目描述
arXiv:2607.21780v1 Announce Type: new Abstract: Document packets, multiple documents concatenated into a single file, are common in government and administrative workflows, yet splitting them into their constituent documents is difficult, especially for low-resource languages. We introduce Khondo (Bangla for split/segment), the first benchmark for document packet splitting on Bangladeshi government forms. Unlike prior English and OCR-text-based datasets, Khondo is bilingual (Bangla--English) and vision-native; where models operate directly on page images. It spans five concatenation schemes, from sequential to fully shuffled, across 14 administrative domains, with ground-truth boundaries, domain types, and page order. Zero-shot evaluation of MLLMs shows they cluster pages into their source documents fairly well but struggle in restoring the original page order once shuffled. To isolate what drives this difficulty, we run two controlled analyses, varying the prompt instruction and then the packet language. Both primarily affect ordering rather than clustering: (a) explicit page-order instructions are necessary but insufficient, and (b) English packets are ordered more reliably than Bangla, making page arrangement the dominant challenge and language a secondary but consistent factor. Khondo establishes page-order reconstruction as a key open problem in vision-based, low-resource document understanding, and provides a controlled benchmark for measuring progress toward solving it. Our dataset and code is available at https://huggingface.co/datasets/Mausul/khondo

## 综合总结
本文介绍了Khondo，首个针对孟加拉语政府表格的视觉原生、双语（孟加拉语-英语）文档包拆分基准。该基准涵盖5种拼接方案和14个行政领域。通过对MLLM的零样本评估发现，模型在页面聚类上表现良好，但在恢复乱序页面时面临巨大挑战。控制变量分析进一步表明，页面排序是主要难点，而语言是次要但一致的影响因素。该研究为基于视觉的低资源文档理解确立了页面顺序重建这一关键开放性问题。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了首个针对孟加拉语政府表格的视觉原生文档包拆分基准，摒弃了传统的OCR文本依赖。通过设计5种拼接方案和14个行政领域的实验，严谨地揭示了多模态大语言模型（MLLM）在页面聚类与页面顺序恢复上的能力差异，并通过控制变量分析明确了页面排序是主要挑战，语言是次要因素，研究设计严谨且具有深度。

### 实用性 (评分: 7.5/10)
针对政府和行政工作流中常见的多文档拼接痛点，提供了极具实际参考价值的基准和评估方法。对于从事低资源语言文档处理、RAG前置流程构建及多模态信息提取的从业者，该数据集和发现可直接指导工程实践，帮助优化文档拆分与排序策略。

### 社区活跃度 (评分: 7.5/10)
研究高度契合当前多模态大模型和低资源语言理解的热点。基于arXiv发布并开源了Hugging Face数据集，具有较好的时效性和可复现性。虽然受众相对垂直，但在低资源语言视觉文档理解社区具有较高影响力和权威性。

## 项目链接
https://arxiv.org/abs/2607.21780
