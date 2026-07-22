# PathReportEval: A Systematic Benchmark for Pathology Report Generation

**评分：** 8.7  
**状态：** 正常  
**标签：** 多模态, 医疗AI, 病理报告, 评估基准, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18448v1 Announce Type: new Abstract: Pathology report generation from whole-slide images (WSIs) is a rapidly growing multimodal learning problem, yet progress is difficult to measure because existing studies use heterogeneous datasets, model settings, visual encoders, and evaluation protocols. Moreover, commonly used natural language generation metrics, including BLEU, ROUGE, and METEOR, primarily reward lexical similarity and often fail to detect clinically consequential errors such as omitted diagnoses, hallucinated findings, or discordant tumor attributes. We present a standardized benchmark and evaluation framework for pathology report generation. The benchmark evaluates four representative methods across three datasets (TCGA, HistAI, and REG 2025) using three pathology foundation encoders (CONCHv1.5, UNI2-h, and H-Optimus-1). Our framework standardizes preprocessing, feature extraction, training, decoding, and evaluation, enabling fair comparison across models while providing a modular platform for integrating new methods, datasets, and encoders. A central contribution is the Clinical Report Quality Score (CRQS), a clinically grounded metric for evaluating factual correctness. CRQS maps reference and generated reports into structured clinical attributes and measures four complementary dimensions: clinical fact coverage, key information recall, hallucination rate, and clinical discordance, producing both an overall score and interpretable sub-scores. Experiments demonstrate that conventional language-generation metrics are weakly aligned with clinical correctness and frequently overestimate report quality. In contrast, CRQS reveals clinically meaningful differences between models and encoders that lexical metrics fail to capture. Together, the benchmark, public plug-and-play framework, and CRQS establish a reproducible foundation for rigorous evaluation of pathology report generation.

## 综合总结
本文针对病理报告生成评估标准不一及传统NLG指标无法检测临床关键错误的问题，提出了PathReportEval基准及临床报告质量分数（CRQS）。CRQS通过将报告映射为结构化临床属性，从事实覆盖、关键信息召回、幻觉率和临床不一致性四个维度评估事实正确性。实验表明传统指标与临床正确性弱相关且易高估质量，而CRQS能有效揭示模型间的临床显著差异，为该领域提供了标准化、可复现的严格评估基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
深刻揭示了传统自然语言生成指标（如BLEU、ROUGE）在医疗场景下的局限性，创新性地提出了临床报告质量分数（CRQS）。CRQS将文本映射为结构化临床属性，从事实覆盖、关键信息召回、幻觉率及临床不一致性四个维度构建了基于临床事实的评估体系，论证严谨，实验充分证明了新指标比传统词汇指标更能反映临床真实性。

### 实用性 (评分: 9.0/10)
提供了即插即用的标准化评估框架，统一了从预处理、特征提取到训练解码的完整流程，对医疗AI从业者评估和开发病理报告生成模型具有极高的实践指导意义；CRQS指标直接切中临床应用痛点（如漏诊、幻觉），可操作性强，适用范围明确。

### 社区活跃度 (评分: 8.5/10)
病理多模态大模型是当前医疗AI的前沿热点，本文由该领域学者提出，填补了病理报告生成领域缺乏统一且贴合临床需求的评估基准的空白。研究来源权威，针对行业痛点，具有较高的话题时效性和行业影响力。

## 项目链接
https://arxiv.org/abs/2607.18448
