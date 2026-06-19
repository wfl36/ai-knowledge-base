# Ensembles of Large Language Models for Identifying EQ-5D Studies in PubMed Based on Their Abstracts

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 集成学习, 医学信息抽取, 文献筛选, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19345v1 Announce Type: new Abstract: The rapid increase in scientific publications leads to the fact that manual study screening in systematic literature reviews (SLRs) is increasingly resource consuming, inefficient, and inconsistent. Classifying studies that clearly report health-related quality-of-life results, such as EQ-5D data, requires a high level of clinical interpretation and poses challenges for human reviewers. This study investigates the use of Google's Gemini and Gemma large language models (LLMs) in automating EQ-5D detection in the PubMed biomedical database based only on published abstracts. A multi-phase framework is proposed that integrates few-shot prompting, weight ensembling aggregation, and a soft stacking meta-classifier. Nine LLMs are evaluated on a dataset of PubMed studies manually labeled by two experts regarding EQ-5D reporting. The weighted ensemble of gemini-2.5-pro, gemma-3-12b, and gemma-3-27b obtained a 0.74 weighted F1-score and 0.74 accuracy, exceeding individually attained results. The ensembling of top-performing models improved the balance between precision and recall compared to individual models, while the soft stacking approach provided greater reliability and interpretability. Feature analysis shows that the probability results from the models are important in guiding the final predictions. The findings suggest that an ensemble-based LLM setup is a reliable and scalable approach for automating screening in biomedical research.

## 综合总结
本文提出了一种基于大语言模型（LLM）集成的多阶段框架，用于自动化识别PubMed摘要中的EQ-5D（健康相关生活质量）研究。该框架结合了少样本提示、权重集成聚合和软堆叠元分类器。通过对9个LLM的评估，发现gemini-2.5-pro、gemma-3-12b和gemma-3-27b的加权集成模型取得了0.74的加权F1分数和准确率，优于单一模型，并在精确率与召回率之间取得了更好的平衡。研究表明，基于集成的LLM方法是生物医学文献自动化筛选的可靠且可扩展的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
论文提出了一种结合少样本提示、权重集成聚合和软堆叠元分类器的多阶段LLM集成框架。虽然集成学习和堆叠方法在传统机器学习中较为常见，应用于LLM输出概率层面的融合具有一定工程创新性，但整体技术路径并非底层算法的突破。论证过程严谨，通过特征分析解释了模型概率对最终预测的指导作用，0.74的加权F1分数在医学文本分类任务中表现良好但未达惊艳水平。

### 实用性 (评分: 8.5/10)
针对系统性文献综述（SLR）中人工筛选耗时低效的痛点，该研究提供了高度可落地的解决方案。自动化识别EQ-5D数据报告可直接应用于生物医学文献筛选流程，大幅降低专家审阅成本。其提出的集成框架基于开源与闭源API模型组合，具备良好的可扩展性，对医疗AI、文献挖掘和NLP从业者具有极高的实践指导价值。

### 社区活跃度 (评分: 7.5/10)
利用LLM自动化文献筛选是当前医疗AI与NLP交叉领域的热点，时效性强。研究基于专家人工标注的PubMed数据集进行验证，来源与结论可信度较高。使用了较新的模型系列（如gemini-2.5-pro和gemma-3系列），贴合前沿，但作为arXiv预印本，其学术影响力的沉淀仍需同行评审和社区引用的进一步检验。

## 项目链接
https://arxiv.org/abs/2606.19345
