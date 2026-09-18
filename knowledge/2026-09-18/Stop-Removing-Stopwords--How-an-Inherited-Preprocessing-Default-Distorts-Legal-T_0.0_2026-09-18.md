# Stop Removing Stopwords: How an Inherited Preprocessing Default Distorts Legal Text-as-Data

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-18  
**来源：** rss  

## 项目描述
arXiv:2609.19153v1 Announce Type: new Abstract: Empirical legal scholarship increasingly treats judicial text as data, and much of it still runs on sparse, interpretable pipelines -- TF-IDF features and linear classifiers -- because the textual feature is often the object of study, not merely a means to a prediction. Yet these pipelines inherit a chain of preprocessing defaults from mid-century information retrieval that were never validated against classification accuracy, the most entrenched being stopword removal. This study introduces an exhaustive single-word ablation that measures a preprocessing step's effect directly against the downstream objective, and applies it to stopword removal as the hardest case to dislodge. Matching Supreme Court Database labels to Caselaw Access Project opinion texts, it examines two binary tasks that bracket F1 headroom, ideological direction (no-removal baseline F1 ~ 0.68) and constitutional versus non-constitutional law type (~ 0.92), across 7,668 and 7,001 opinions. For each task the analysis approximates the best stoplist any expert could build, removing each of roughly 18,500 candidate words and measuring the effect directly. Three findings follow: generic stoplists in common use fall below the no-removal baseline in every test; even optimized stoplists are statistically indistinguishable from removing nothing; and meta-models trained on word-level features cannot predict which removals help, so list curation has nothing to target. The method generalizes to any inherited preprocessing default, and the result is a caution specific to interpretable legal text-as-data: a step that silently reshapes which features a model sees can distort the very doctrinal and ideological signal such research exists to recover. Leaving stopwords in place is a question of measurement validity.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.19153
