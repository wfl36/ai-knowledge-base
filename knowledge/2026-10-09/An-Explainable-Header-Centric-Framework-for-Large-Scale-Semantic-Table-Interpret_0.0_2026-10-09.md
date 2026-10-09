# An Explainable Header-Centric Framework for Large-Scale Semantic Table Interpretation and Data Quality Assessment

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10541v1 Announce Type: new Abstract: Knowledge Graph (KG) quality depends not only on downstream graph validation, but also on the quality of tabular metadata used before integration. In metadata-only Semantic Table Interpretation (STI), where cell values are unavailable, noisy, or unsuitable, column headers become a critical source of semantic evidence for traceable KG preparation. We present an explainable, header-centric framework for metadata-only Column Type Annotation (CTA) and Data Quality Assessment (DQA). The framework maps headers to 39 interpretable FinalFormat types using curated lexical resources and preserves token-level traceability through SourceKeywords. Each assigned type activates validation rules based on a taxonomy of Data Quality Issues (DQIs), producing detections such as missing data, duplicates, domain violations, wrong data type, and temporal mismatch. These detections are aggregated into HeadersIQ, a lightweight, unweighted data source-level quality metric. The framework was evaluated across heterogeneous benchmarks, including UCI, Prague, Kaggle, VizNet/Sato, SOTAB, T2Dv2, and the SemTab 2024 Metadata-to-KG track, comprising around 120,000 header columns. The results show broad practical coverage across noisy real-world metadata, while a parallel KG-mapping pathway supports alignment to DBpedia and Schema.org. On the SemTab 2024 Metadata-to-KG track, the official GT-strict evaluation was modest. However, a blinded diagnostic audit indicates that many mismatches reflect benchmark granularity, aliasing, and ontology-selection effects rather than wholly implausible header-centric predictions. We report this audit as diagnostic evidence on disagreement patterns, not as revised benchmark performance. Overall, the paper presents a reusable workflow for metadata-driven semantic annotation, data source-level quality monitoring, and KG-oriented benchmark diagnosis.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10541
