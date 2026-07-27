# Evaluation design conditions the expert-vs-auto MeSH gap: a controlled comparison of bag-of-words and BiomedBERT on the Cohen benchmark

**评分：** 7.5  
**状态：** 正常  
**标签：** 评估方法论, 医学信息学, 文献筛选, NLP, 实证研究  
**更新日期：** 2026-07-27  
**来源：** rss  

## 项目描述
arXiv:2607.21685v1 Announce Type: new Abstract: A systematic review begins with someone reading thousands of abstracts to identify the few that are relevant, and classifiers are used to prioritise that reading. Their inputs are often augmented with Medical Subject Headings (MeSH), assigned either by expert indexers weeks or months after publication or by automatic tools at once. To our knowledge the two have not been compared directly as classifier features, and no previous work has asked whether that comparison's outcome depends on how the classifier is evaluated. Using the Cohen et al. (2006) drug-class benchmark on three topics, we characterise a bag-of-words logistic regression classifier (seven reruns) and BiomedBERT (five seeds), then examine how the Statins result changes under alternative designs. Under the canonical 5-fold full-corpus design, the bag-of-words expert-vs-auto gap on Statins is +0.096 WSS@95%. Matching the corpus size to the smaller topics (n = 803) reduces it to +0.033 (95% bootstrap CI includes zero), and 10-fold cross-validation at full size to +0.021 (CI narrowly excludes zero). Under canonical evaluation BiomedBERT gives +0.020, within sampling noise of the bag-of-words 10-fold result. A power analysis indicates a Statins-sized effect would not have been detectable at the Opioids or ADHD variance, so those nulls are design-limited rather than informative. A representation asymmetry remains: 15.1% of Statins inputs exceed BiomedBERT's 512-token limit when expert MeSH terms are appended, so truncation may contribute to the smaller transformer gap, although this cannot be separated from training volume here. In screening pipelines using transformers or 10-fold bag-of-words, the gap on the topics tested is about 0.02 WSS@95%, with CIs spanning zero on at least one bound. More broadly, benchmark conclusions about feature sources can change substantially under reasonable changes to the evaluation design.

## 综合总结
本文研究了在系统评价文献筛选任务中，评估设计如何影响专家标注与自动生成的MeSH特征对分类器性能贡献的比较结果。基于Cohen基准测试，作者发现传统的5折全语料评估夸大了专家MeSH的优势（词袋模型下差距为+0.096 WSS@95%），而在调整语料大小或采用10折交叉验证后，该差距大幅缩小（约+0.02至+0.033）。BiomedBERT的实验也显示了类似的微小差距。此外，统计功效分析表明部分主题的零结果受限于评估设计而非信息不足，且专家MeSH的引入导致15.1%的输入超过Transformer的512 token限制，可能引入截断偏差。研究强调，基准测试中关于特征源优劣的结论高度依赖于评估设计的选择。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文论证严谨，揭示了评估设计（如交叉验证折数、语料库大小）对特征源（专家vs自动MeSH）比较结果的显著影响。通过对照实验和统计功效分析，指出传统5折评估夸大了专家特征的优势，并探讨了Transformer 512-token截断对长文本特征引入的表示不对称性，技术深度与方法论反思俱佳。

### 实用性 (评分: 7.5/10)
对从事医学文献筛选、系统评价自动化及NLP评估的从业者具有直接的指导意义。提醒工程师在构建筛选管道时，不应盲目迷信专家特征或大模型的原生优势，而需重点关注评估设计的稳健性（如采用10折交叉验证）以及长文本截断带来的潜在信息损失。

### 社区活跃度 (评分: 7.0/10)
话题涉及大模型评估方法论反思，具有较强时效性；来源为arXiv预印本，未经同行评审，但引用了经典的Cohen benchmark，具备一定学术可信度；研究在医学信息学及系统评价细分领域有较好影响力，但在更广泛的AI社区影响力相对有限。

## 项目链接
https://arxiv.org/abs/2607.21685
