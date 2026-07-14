# Faithful by Design: Evaluating and Improving LLM-Generated Clinical Trial Summaries for Multi-Stakeholder Audiences

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 幻觉, RAG, 知识图谱, 评估基准, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09932v1 Announce Type: new Abstract: Large language models are increasingly used to summarize clinical trial results for healthcare providers, patients, and payers, but their tendency to hallucinate poses significant risks in this high-stakes context. This study introduces a benchmark evaluation framework for measuring the faithfulness of LLM-generated clinical trial summaries across three stakeholder audiences. The framework consists of 200 stratified trials drawn from the Aggregate Analysis of ClinicalTrials.gov database, evaluated using audience-specific prompt templates and a six-dimension faithfulness annotation schema. Baseline measurements were established for GPT-4o, Claude Sonnet 4.6, and Gemini 2.5 Flash across 1,800 generated summaries scored using a cross-encoder natural language inference (NLI) model. Unsupported Claims was identified as the dominant failure mode across all three models, with a mean annotation score of 1.55 out of three. A knowledge-graph-augmented retrieval system was developed and evaluated against the baseline, producing statistically significant improvements in NLI-based faithfulness scores (entailment +0.0125, faithfulness +0.0130, p < 0.0001). Improvement pathways were model-dependent, with GPT-4o improving primarily through contradiction reduction while Claude Sonnet 4.6 and Gemini 2.5 Flash improved through increased entailment.

## 综合总结
本文针对LLM生成临床试验总结时的幻觉风险，构建了面向多利益相关者的忠实度评估基准，并开发了知识图谱增强检索（KG-RAG）系统。实验表明，KG-RAG能显著提升生成内容的忠实度，且不同模型的改进机制存在差异。该研究为高合规医疗场景下的LLM应用提供了严谨的评估框架与有效的幻觉缓解方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了一种针对多利益相关者临床试验总结的忠实度评估框架，包含六维度标注模式和基于交叉编码器NLI的自动评分机制。创新性地结合知识图谱增强检索（KG-RAG）系统缓解幻觉，并深入剖析了不同主流LLM（GPT-4o, Claude, Gemini）在提升忠实度时的差异化路径（GPT-4o侧重减少矛盾，Claude/Gemini侧重增加蕴含），实验设计严谨，具有较好的方法学深度。

### 实用性 (评分: 9.0/10)
对医疗AI落地具有极高的参考价值。针对高合规医疗场景的幻觉痛点，提供了从评估基准（200个分层试验/特定受众提示词）到缓解方案（KG-RAG）的完整闭环，可直接指导医疗文本生成系统的提示词工程、RAG架构搭建及安全性评估，适用范围覆盖所有高事实性要求的垂直领域。

### 社区活跃度 (评分: 8.0/10)
聚焦LLM幻觉与医疗安全这一高热度核心议题，基于最新主流模型进行实验，时效性强。作为arXiv新发论文，为医疗AI的可信生成提供了重要的基准和方法，尽管KG-RAG的绝对提升幅度有限，但在高风险场景下具有显著的行业警示与应用潜力。

## 项目链接
https://arxiv.org/abs/2607.09932
