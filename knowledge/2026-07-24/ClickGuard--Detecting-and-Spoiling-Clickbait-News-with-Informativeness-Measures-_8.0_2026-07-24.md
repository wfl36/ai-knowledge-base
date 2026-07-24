# ClickGuard: Detecting and Spoiling Clickbait News with Informativeness Measures and Large Language Models

**评分：** 8.0  
**状态：** 正常  
**标签：** NLP, 大模型, 文本分类, 工程实践, 浏览器扩展  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20463v1 Announce Type: new Abstract: This paper presents an AI-driven browser extension that identifies clickbait to help users avoid misleading Internet articles. Moving beyond traditional detection, the application employs a hybrid machine learning architecture that combines transformer-based embeddings with linguistically motivated features and a custom "baitness" score. After evaluating various natural language processing techniques -- from classic vectorizers to large language model (LLM) embeddings -- an XGBoost-based model was developed that achieves an F1-score of 91% on the open combined dataset. Most importantly, the tool can warn users before and after they access a clickbait article. After opening an article, the user receives a percentage score indicating the likelihood that it is clickbait. The prediction is explained based on the analyzed metrics, including those specifically developed within the proposed system. The browser extension also provides a clickbait spoiler -- a one- to two-sentence summary of the entire article. Demo video:https://www.youtube.com/watch?v=IJ1gkQV82C4}{https://www.youtube.com/watch?v=IJ1gkQV82C4

## 综合总结
本文介绍了ClickGuard，一个基于AI的浏览器扩展，旨在检测和反制标题党新闻。该系统采用混合架构，结合Transformer嵌入、语言学特征与自定义'baitness'评分，通过XGBoost模型实现了91%的F1分数。工具不仅提供点击诱饵概率预警和解释，还能利用大模型生成简短摘要作为'剧透'，帮助用户避免被误导，具有极高的实用落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
采用混合机器学习架构，结合Transformer嵌入、语言学特征与自定义'baitness'评分，并使用XGBoost进行分类，在开放数据集上达到91%的F1分数。方法虽非底层架构创新，但特征工程与模型融合具有一定深度，且引入LLM生成spoiler增强了系统完整性。

### 实用性 (评分: 9.0/10)
以浏览器扩展形式直接落地，面向普通用户解决标题党痛点。提供访问前预警、概率评分、预测解释及核心内容摘要（spoiler），功能闭环完整，实用价值极高，具备广泛的应用前景。

### 社区活跃度 (评分: 8.0/10)
标题党检测是长期的社会热点话题，该工作结合了LLM技术赋予其新的解决思路。发布时间极新（标注为2026年），且提供了Demo视频，来源为arXiv预印本，具备一定的关注度和可信度。

## 项目链接
https://arxiv.org/abs/2607.20463
