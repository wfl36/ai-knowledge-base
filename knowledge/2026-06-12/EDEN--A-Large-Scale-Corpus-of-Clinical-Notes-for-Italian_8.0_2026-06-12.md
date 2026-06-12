# EDEN: A Large-Scale Corpus of Clinical Notes for Italian

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 数据集, 信息抽取, 意大利语NLP, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12569v1 Announce Type: new Abstract: We present EDEN (Emergency Department Electronic Notes), a new and unique large-scale corpus of clinical notes produced in Emergency Departments of Italian hospitals. The corpus, in its current version, is composed of approximately 4 million clinical notes fully anonymized, covering diverse phases of patient care during the stay in the emergency department. In addition, a subset of about six thousand notes has been manually annotated by clinical experts through a structured Case Report Form (CRF) containing 132 items relevant for two patient situations in emergency departments, dyspnea and loss of consciousness. Items may assume numerical values (e.g., for blood saturation), categorical (e.g., for level of consciousness ), binary (e.g., for presence of traumas), and mixed value types. The annotation process involved multiple clinicians and underwent iterative revision to resolve ambiguities in item formulation, resulting in a richly structured (although high imbalanced) resource. The dataset aims to fill a relevant gap of data able to support both the development and the use of Large Language Models in concrete medical applications. We describe the data collection protocol, the on-site anonymisation pipeline, corpus statistics, and the annotation scheme. Finally, we propose CRF-filling as a novel structured information extraction benchmark, and provide zero-shot baseline resulting from Gemma-27B and MedGemma-27B. To the best of our knowledge, the EDEN dataset is the largest freely available corpus of clinical notes existing for the Italian language.

## 综合总结
本文发布了EDEN，目前最大的免费意大利语急诊科临床笔记语料库，包含约400万份匿名化笔记。其中6000份笔记由临床专家通过132项结构化病例报告表（CRF）进行了精细标注（涵盖数值、类别、二元等类型）。研究提出了CRF填充作为新的结构化信息提取基准，并提供了Gemma-27B和MedGemma-27B的零样本基线结果。该数据集有效填补了意大利语医疗大模型训练与评估的数据空白，对推动非英语医疗AI落地具有重要价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该研究在数据工程和基准设计上展现了较好的深度。构建了包含约400万条匿名化临床笔记的大规模语料库，并创新性地设计了包含132个多类型（数值、类别、二元、混合）项目的结构化病例报告表（CRF）标注方案。提出将CRF填充作为结构化信息提取的新基准，并提供了Gemma-27B和MedGemma-27B的零样本基线，论证严谨，但核心贡献偏重数据资源而非算法突破。

### 实用性 (评分: 8.5/10)
对医疗NLP从业者具有极高的落地参考价值。400万规模的真实急诊科笔记可直接用于意大利语医疗大模型的预训练或微调；6000条多类型专家标注数据为信息抽取任务提供了高质量的评估标准。CRF填充基准非常贴近临床实际需求（从自由文本提取结构化电子病历），能有效指导医疗AI系统的开发与评估。

### 社区活跃度 (评分: 8.0/10)
医疗大模型应用是当前AI社区的热点，而非英语（尤其是意大利语）医疗数据的稀缺是公认的痛点，该数据集的发布具有极强的时效性和填补空白的意义。数据开源且来源于真实医院急诊科，经过严格的匿名化和多轮专家标注修订，权威性与可信度高。作为目前最大的免费意大利语临床笔记语料库，预计在医疗NLP社区将产生较好的影响力。

## 项目链接
https://arxiv.org/abs/2606.12569
