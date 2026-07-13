# Automatic Thematic Indexing of Large Literary Corpora: A Machine Learning Approach to Voltaire's Complete Works

**评分：** 7.0  
**状态：** 正常  
**标签：** 大模型, 文本分类, 多标签分类, 数字人文, 论文  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.09316v1 Announce Type: new Abstract: Thematic indexing -- the practice of assigning structured conceptual labels to sections of text -- is essential to scholarly access in large-scale literary and historical editions, yet it remains a largely manual, labour-intensive process. This paper explores the application of machine learning to automatic thematic indexing, using two substantial sub-corpora of the Complete Works of Voltaire as a test case: the Essai sur les m\oe urs et l'esprit des nations and the Questions sur l'Encyclop\'edie. The task is framed as a multi-label classification problem, in which a model must assign the set of index entries that a professional indexer would apply to a given page of text. We compare a range of approaches -- from encoder-based models with classification heads to generative large language models (LLMs) fine-tuned via Low-Rank Adaptation (LoRA) -- spanning model sizes from approximately 3 to 120 billion parameters. Our best-performing model, from the Mistral family in a 4-bit quantised configuration, achieves F1 scores of up to 0.67; we argue that these figures represent lower bounds, given the inherent subjectivity of professional indexing and the frequency with which model predictions prove semantically valid despite diverging from the print index. We further evaluate cross-corpus generalisation and conduct a detailed qualitative analysis of model behaviour on literary and rhetorical features of the source texts that prove particularly resistant to automated treatment. Our findings have implications for the broader challenge of providing structured thematic access to large-scale literary and historical corpora.

## 综合总结
本文探讨了利用机器学习对大规模文学语料库进行自动主题索引的方法，以伏尔泰全集为测试用例，将索引任务转化为多标签分类问题。研究对比了从编码器模型到基于LoRA微调的生成式大模型（3B-120B参数）等多种方案，发现4-bit量化的Mistral模型表现最佳（F1达0.67）。研究还评估了跨语料库泛化能力，并对模型在文学修辞特征上的局限性进行了定性分析，为大规模文史语料库的结构化主题访问提供了有价值的基线和实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
研究将文学主题索引转化为多标签分类问题，系统对比了从传统编码器模型到基于LoRA微调的生成式大模型（3B至120B参数）的多种技术路线。技术实现扎实，包含4-bit量化优化，且不仅提供F1等定量指标，还深入分析了模型在处理文学修辞特征时的局限性及人工索引的主观性对评估的影响，论证严谨，具有一定的技术深度。

### 实用性 (评分: 7.0/10)
对数字人文、历史文献数字化及出版领域的从业者具有较高参考价值。研究明确了4-bit量化Mistral模型在此类任务中的有效性，并探讨了跨语料库泛化能力，为大规模文史语料库的自动化索引提供了可直接借鉴的工程实践方案和基线数据，能有效辅助甚至部分替代繁重的人工索引工作。

### 社区活跃度 (评分: 6.5/10)
话题切合当前大模型在垂直专业领域落地的热点，来源为arXiv学术论文，具备较高的学术可信度。虽然该成果在广泛的AI核心社区中影响力相对有限，但在数字人文和文献检索细分领域具有较高的关注度和应用价值。

## 项目链接
https://arxiv.org/abs/2607.09316
