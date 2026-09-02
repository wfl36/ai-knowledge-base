# Medical Causal Hypothesis Verification with Large Language Models

**评分：** 6.0  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 因果推理, 评估基准, RAG, 论文  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00063v1 Announce Type: new Abstract: The growing use of large language models (LLMs) for search and information retrieval underscores the need to evaluate their reliability in high-stakes domains such as healthcare. Although LLMs can effectively answer questions about diseases, symptoms, and treatments, their ability to accurately assess causal relationships and ground their conclusions in verified scientific evidence remains unclear. Here, we present a preliminary, small-scale study that investigates the accuracy of LLMs in evaluating causal medical claims and supporting them with peer-reviewed research. We propose an evaluation framework for causal hypothesis verification that can be used to systematically track the performance of existing and future LLMs. We assess the performance of eight LLMs on 17 medical causal hypotheses to evaluate whether they can reliably verify these hypotheses using scientific evidence from the literature. We systematically annotate the scientific evidence they provide according to six criteria (a total of 1,067 annotation points) and assess them with nine evaluation metrics. Our analysis shows that while LLMs exhibit strong recall, they often perform poorly at providing valid scientific articles and evidence for support and at rejecting unsupported hypotheses. These findings highlight a critical limitation of current LLMs, as they cannot yet be trusted fully to verify causal relationships from the biomedical literature. This work underscores the need for rigorous evaluation before using LLMs for search and retrieval in healthcare settings.

## 综合总结
本文是一项针对LLM在医疗因果假设验证任务上的小规模评估研究，构建了包含6项标注标准、9项评估指标的系统化评估框架，并在8个主流LLM上测试了17个医疗因果假设。研究发现LLM虽能高召回地识别相关问题，但在提供有效科学文献证据和拒绝无依据假设方面表现不佳，揭示了当前LLM尚不能可靠用于生物医学文献因果关系验证的局限性。研究为医疗领域LLM部署提供了有价值的警示，但样本规模和深度有限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文提出了一个针对医疗因果假设验证的评估框架，覆盖8个LLM在17个因果假设上的表现，使用6个标注标准和9个评估指标共1067个标注点。方法论较为系统，但属于小规模初步研究（17个假设样本量有限），且框架设计相对直接，缺乏对更深层因果推理机制的探讨。技术贡献在于评估范式而非新方法或新模型。

### 实用性 (评分: 6.0/10)
对医疗AI从业者和LLM评估研究者具有一定参考价值，揭示了LLM在因果关系验证中'高召回但证据质量差'的具体问题模式，对构建医疗领域RAG/检索增强系统有警示意义。但样本规模过小、具体假设集未充分说明，对实际部署决策的指导有限。

### 社区活跃度 (评分: 5.5/10)
主题贴合LLM在医疗高风险领域应用的可信度讨论，是当前热点话题。但arXiv预印本（2609.00063v1，发布时间标注为2026年9月）未经同行评审，来源权威性一般；小规模研究的结论普适性存疑，影响力较为有限。

## 项目链接
https://arxiv.org/abs/2609.00063
