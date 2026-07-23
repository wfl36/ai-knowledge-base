# Lightweight Person-Place Relation Extraction from Historical Newspapers with Dependency Graphs and Proximity Features

**评分：** 7.8  
**状态：** 正常  
**标签：** 关系抽取, 轻量级模型, 数字人文, 数据泄露, 论文, 竞赛报告  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19718v1 Announce Type: new Abstract: The HIPE-2026 shared task introduces person-place relation extraction from multilingual historical newspapers as a new evaluation track, classifying the at and isAt relations between pre-annotated person and location mentions in English, French, and German. Motivated by the cost of processing historical archives at scale, our team (DS@GT HIPE, team 2 in the official results) investigates how far a lightweight, interpretable system can go without any pretrained language model at the relation classification stage. Our approach builds a document-level graph from dependency parses, extracts proximity-based and part-of-speech features for each entity pair, and classifies them with small scikit-learn ensembles or compact Graph Attention Networks, keeping every submitted run under 847K parameters. On the official evaluation (Test A, the newspaper test set), our best run reached a macro recall of 0.5142, ranking 3rd on the Efficiency profile while placing mid-table on Accuracy among the 17 participating teams. Two findings stand out. First, minimum character distance alone captures most of the classification signal; adding further engineered features yields inconsistent gains and sometimes degrades performance, echoing prior evidence that argument distance dominates relation extraction. Second, document-grouped cross-validation is essential on this corpus: pair-level splits inflate scores by 25-37 percentage points because entity mentions recur across documents, a data-leakage effect that grouped cross-validation removes.

## 综合总结
本文针对HIPE-2026共享任务中历史报纸的人物-地点关系抽取，提出了一种不依赖预训练语言模型的轻量级系统（基于依存图和邻近度特征，参数量<847K）。该系统在官方评测中取得了效率第三、准确率中游的成绩。研究两大核心发现：1）最小字符距离包含了绝大部分分类信号，复杂特征工程反而可能损害性能；2）传统交叉验证存在严重的数据泄露，导致分数虚高25-37个百分点，必须采用文档级分组交叉验证。该研究为资源受限场景下的关系抽取提供了高效范式，并对NLP评测标准提出了重要警示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文在历史报纸人物-地点关系抽取任务中，探索了不依赖预训练语言模型的轻量级方案。技术深度体现在严谨的实验设计与分析上：不仅证明了最小字符距离这一简单特征包含了大部分分类信号，复杂特征工程反而可能带来负面影响；更深刻揭示了传统数据划分导致的严重数据泄露问题（虚高25-37个百分点），强调了文档级分组交叉验证的必要性，实证分析极具洞察力。

### 实用性 (评分: 8.5/10)
对从业者具有极高的实践指导价值。首先，证明了在资源受限或处理大规模历史档案场景下，轻量级系统（<847K参数）同样能取得有竞争力的效果；其次，揭示了简单距离特征的统治力，帮助开发者避免无效的复杂特征工程；最后，关于数据泄露的发现为关系抽取任务的评估提供了关键的避坑指南，可直接指导数据集划分实践。

### 社区活跃度 (评分: 7.5/10)
论文基于HIPE-2026这一最新共享任务，时效性极强。作为官方评测中效率排名第三、准确率居中的团队，其结果具有较高可信度。虽然属于垂直领域（数字人文/NLP）的竞赛报告，但对NLP评测方法论（数据划分与泄露）的纠偏具有广泛的社区警示意义。

## 项目链接
https://arxiv.org/abs/2607.19718
