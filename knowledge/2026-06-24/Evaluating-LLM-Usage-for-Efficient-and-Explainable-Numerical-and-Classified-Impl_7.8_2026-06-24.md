# Evaluating LLM Usage for Efficient and Explainable Numerical and Classified Implicit Sentiment Analysis of Product Desirability

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, 情感分析, 可解释性, 应用研究, 论文  
**更新日期：** 2026-06-24  
**来源：** rss  

## 项目描述
arXiv:2606.23701v1 Announce Type: new Abstract: Qualitative product feedback can reveal nuanced user experiences, but its implicit sentiment is difficult to measure. This paper presents a scalable and interpretable framework that uses large language models (LLMs) to quantify product desirability from such data. Using two Product Desirability Toolkit (PDT) datasets from ZORQ and CARMA comprising 106 respondent term groupings with gold-standard human annotation, zero-shot continuous numerical sentiment scoring and categorical sentiment classification are evaluated without relying on explicit review scores. Across the datasets, LLMs generated numerical sentiment scores directly from qualitative responses and closely matched expert labels, achieving Pearson correlations up to 0.97 and classification accuracy up to 94%. LLMs maintained robustness even when handling data presented in multiple forms and consistently expressed high confidence. In contrast, lexicon-based and transformer baselines did not produce statistically significant results. Among the models tested, GPT-4o-mini achieved performance comparable to larger models at 94% lower cost, supporting scalable deployment. The framework also incorporates model confidence ratings and human-readable rationale explanations (xAI), improving interpretability, transparency, and trust while supporting practical use in product satisfaction assessment. In general, using the PDT tool as a survey method along with a cost efficient LLM for sentiment analysis has the potential to provide for product evaluation with results that are rich in terms of sentiment scores (both numerical and classified sentiment) and in terms of the high-level user impressions of the product that can be used to identify ideas for product development and improvement, as well as marketing ideas for target audiences.

## 综合总结
本文提出了一种基于LLM的零样本隐式情感分析框架，用于评估产品期望度。在PDT数据集上的实验表明，LLM在数值评分（Pearson相关系数高达0.97）和分类准确率（高达94%）上均显著优于传统基线，且GPT-4o-mini以极低成本实现了与大模型相当的性能。该框架结合了置信度评估与可解释性（xAI），为产品满意度评估和需求挖掘提供了一套高效、可扩展且透明的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
论文提出了一种基于LLM的零样本隐式情感分析框架，用于量化产品期望度。技术深度体现在同时进行连续数值评分和分类评估，且不依赖显式评论分数。实验设计严谨，对比了词典和传统Transformer基线，并引入了模型置信度评估与可解释性（xAI）生成。但整体偏向应用验证，缺乏底层算法或模型结构的根本性创新。

### 实用性 (评分: 9.0/10)
对产品经理、UX研究员和市场营销人员具有极高的落地价值。研究证实了GPT-4o-mini等轻量级模型在极低成本（降低94%）下即可达到与大模型媲美的性能，直接解决了企业规模化部署的成本痛点。结合置信度评估和人类可读的解释生成，使得该框架能够安全、透明地应用于实际的产品满意度评估、需求挖掘和营销洞察中。

### 社区活跃度 (评分: 7.5/10)
研究话题紧贴当前大模型在垂直领域（产品反馈分析）的应用热点，发布于arXiv平台，数据集基于标准PDT工具并含金标准人工标注，具有较好的权威性和时效性。虽然在核心AI算法社区可能影响力有限，但在人机交互（HCI）和产品管理交叉领域具有较高的参考价值和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.23701
