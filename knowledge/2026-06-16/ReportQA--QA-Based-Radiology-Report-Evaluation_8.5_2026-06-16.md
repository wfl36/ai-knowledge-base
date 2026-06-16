# ReportQA: QA-Based Radiology Report Evaluation

**评分：** 8.5  
**状态：** 正常  
**标签：** 医疗AI, 大模型评估, 视觉语言模型, 放射学报告, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15037v1 Announce Type: new Abstract: Radiology report evaluation is essential for advancing automated report generation. Natural language generation metrics have limited clinical relevance. Clinical efficacy (CE) metrics evaluate important medical findings, but focus mainly on presence and cover only a limited set of entities. Due to heavy reliance on manual annotations, it is difficult for CE metrics to extend clinical entities or attributes. In clinical practice, radiology reports serve as a medium for information transfer. Clinicians use them to perform downstream diagnostic tasks without directly inspecting images. Based on this insight, we propose ReportQA, a clinical-related and flexible radiology report evaluation framework, supporting detailed quantitative analysis of radiology report generation systems. We first collect datasets covering multiple imaging modalities and anatomical regions. We then construct knowledge trees of clinical entities and attributes with radiologist guidance, and use large language models (LLMs) to extract structured information from raw reports. Next, we generate QA pairs from predefined templates and apply quality control through self-filtering and report-based filtering. During evaluation, the report is treated as context, and an LLM acts as a judge model to answer the QA pairs. Based on the resulting QA accuracy, we introduce QAScore metric. Compared with existing metrics, QAScore shows better alignment with radiologist judgments. Experiments on multiple state-of-the-art vision-language models reveal that current report-based inference paradigms struggle to learn fine-grained clinical representations and exhibit strong negative prior biases. In contrast, question-driven inference provides a more effective alternative. For reproducibility and extensibility, we release the knowledge trees, structured reports, and QA pairs, along with the pipeline code for QA construction and evaluation.

## 综合总结
本文提出ReportQA，一种基于QA的放射学报告评估框架。针对现有评估指标临床相关性差及依赖人工的痛点，该框架模拟临床医生基于报告进行下游诊断的流程，利用LLM提取结构化信息并生成QA对，通过LLM裁判模型计算QAScore。实验表明QAScore与医生判断高度一致，并揭示了当前VLM在细粒度临床表征上的缺陷及负先验偏差，指出问题驱动推理是更优范式。项目全面开源，为医疗AI评估提供了高实用性的新基准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了新颖的基于QA的放射学报告评估框架ReportQA，突破了传统NLG指标临床相关性弱和CE指标严重依赖人工标注、实体覆盖有限的瓶颈。通过构建临床实体与属性的知识树，结合LLM提取结构化信息并自动化生成QA对，采用LLM-as-a-judge范式进行评估，提出了QAScore指标。研究不仅论证了该指标与放射科医生判断的更高一致性，还深刻揭示了当前VLM在医学报告生成中难以学习细粒度临床表征且存在强负先验偏差的问题，提出了问题驱动推理的替代范式，技术深度与洞察力俱佳。

### 实用性 (评分: 9.0/10)
该研究对医疗AI从业者具有极高的落地指导价值。ReportQA直接解决了自动放射学报告生成领域长期存在的评估痛点，提供了与临床实际需求对齐的量化指标QAScore。项目开源了涵盖多模态和多解剖区域的知识树、结构化报告、QA数据集及完整的构建与评估Pipeline代码，极大降低了临床实体扩展和评估系统搭建的门槛，可直接作为医疗视觉语言模型评估的新基准，指导模型优化与迭代。

### 社区活跃度 (评分: 8.0/10)
医疗大模型评估是当前AI for Science与医疗社区的前沿热点，LLM-as-a-judge也是备受关注的范式。作者团队具备深厚的学术与工业背景（如Dejing Dou, Ji Wu等），保证了研究的权威性与可信度。项目全面开源数据和代码，将有效推动医学影像分析社区的评估标准化进程，具备较高的社区影响力和时效性。

## 项目链接
https://arxiv.org/abs/2606.15037
