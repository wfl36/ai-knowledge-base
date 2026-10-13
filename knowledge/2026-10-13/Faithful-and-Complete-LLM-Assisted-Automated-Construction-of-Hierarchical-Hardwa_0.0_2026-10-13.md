# Faithful and Complete LLM-Assisted Automated Construction of Hierarchical Hardware Knowledge Graphs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-13  
**来源：** rss  

## 项目描述
arXiv:2610.12762v1 Announce Type: new Abstract: Hardware datasheets contain engineering specifications essential for component selection, system integration, and hardware compatibility verification. However, manual inspection is tedious and error-prone because datasheets are lengthy and heterogeneous, with dense information fragmented across tables, figures, and text. Although large language models (LLMs) can automate this process, na\"ive one-shot processing omits relevant specifications even when the document fits within the model's context window. We present an automated LLM-driven pipeline that transforms hardware datasheets into general-purpose hierarchical hardware knowledge graphs through chunk-based property extraction, hierarchical routing, and iterative refinement. The framework uses LLMs for information extraction and semantic reasoning while preserving source provenance and applying graph updates through validated instructions and deterministic local execution. This staged design reduces per-query context and maintains traceable intermediate representations. The resulting knowledge graphs provide semantically organized, source-grounded hardware properties for downstream retrieval and reasoning. We evaluate the framework on 20 hardware datasheets spanning diverse component types and document lengths. We assess property faithfulness and introduce inter-graph completeness to measure relative semantic coverage without exhaustive ground truth. Our framework achieves 98.8% property faithfulness compared with 76.1% for the one-shot baseline, while fully covering 83.6% of faithful baseline properties; in the reverse direction, the baseline fully covers only 10.5% of ours. These improvements provide more reliable and comprehensive engineering information for downstream hardware design and verification, reducing the risk of overlooked constraints and incorrect decisions.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.12762
