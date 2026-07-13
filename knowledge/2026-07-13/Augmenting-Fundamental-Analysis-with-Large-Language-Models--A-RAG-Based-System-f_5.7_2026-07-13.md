# Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs

**评分：** 5.7  
**状态：** 待复核  
**标签：** 大模型, RAG, 金融分析, 基本面分析, 论文, 工程实践  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.09121v1 Announce Type: new Abstract: In this study, we examine the opportunities brought by Large Language Models (LLMs) to various aspects of fundamental analysis of companies based on their reports as well as data and documents describing macroeconomic situation like GDP and inflation changes as well as documents filled to the U.S. Securities and Exchange Commission (SEC) which can be found in EDGAR. We were preprocessing those data and than sending via API to gpt-4o model in a Retrieval-Augmented Generation (RAG) like regime. We prepared as well a document describing an exemplar investor knowledge based on Kitchin cycles. We were scanning data important for analysis of 9 companies for 4 weeks. Using LLM we were producing automatic briefs about them. They were sent to nine participants who are individual investors to evaluate usefulness of such approach to data analysis.

## 综合总结
本文探讨了利用大语言模型（GPT-4o）结合RAG架构增强公司基本面分析的潜力。系统整合了SEC EDGAR文件、宏观经济数据以及基于Kitchin周期的投资者知识库，为9家公司生成了为期4周的自动投资简报，并由9名个人投资者进行了有用性评估。研究展示了LLM在金融数据处理和简报生成方面的可行性，但评估样本较小，技术方案相对常规，缺乏深度的定量验证。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
采用常规的RAG架构结合GPT-4o处理SEC文件和宏观数据，引入Kitchin周期作为领域知识，方法上缺乏算法或架构层面的创新；评估仅基于9名个人投资者的主观反馈，样本量小且缺乏严格的定量回测或与专业分析师的对比，研究深度有限。

### 实用性 (评分: 6.5/10)
RAG+LLM生成投资简报的流程对金融从业者具有直接的落地参考价值，数据处理和知识库构建（Kitchin周期）流程可复制性强，但实际投资指导效果因评估规模限制尚未得到充分验证。

### 社区活跃度 (评分: 5.5/10)
LLM在金融领域的应用是当前热点，具备一定时效性；arXiv预印本提供了一定可信度，但作者知名度一般，且小规模用户调研的结论说服力较弱，整体影响力和权威性有限。

## 项目链接
https://arxiv.org/abs/2607.09121
