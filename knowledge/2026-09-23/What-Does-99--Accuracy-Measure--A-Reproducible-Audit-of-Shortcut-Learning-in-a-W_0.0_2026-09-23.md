# What Does 99% Accuracy Measure? A Reproducible Audit of Shortcut Learning in a Widely Used Fake News Corpus

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.25006v1 Announce Type: new Abstract: Text classifiers trained on the ISOT/Kaggle "Fake and Real News" corpus routinely report accuracy and F1 above 0.98, a level of performance that sits uneasily beside the difficulty of assessing veracity. Using a transparent TF-IDF and linear-classifier pipeline as a measurement instrument, we audit the corpus along three leakage channels and two distribution-shift protocols, releasing all code and derived numbers. First, the benchmark is partly degenerate: a classifier given only the subject metadata field, with the article text discarded, attains F1 = 1.000, since the two classes have disjoint subjects. Second, removing all three leakage channels, metadata, a newswire source tag present in 99.2% of real articles, and 6,251 duplicate documents contaminating 19.4% of a naive test split, lowers F1 by only 1.21 points (0.9935 to 0.9814); the residual signal is diffuse editorial style rather than a few giveaway tokens, since deleting the 1,000 highest-weight unigrams still leaves F1 = 0.926. Third, this style signal does not transfer: under a topic-disjoint protocol, average precision falls from 0.9995 to 0.9475 and deployed F1 from 0.9905 to 0.8067, with a prior-matched analysis confirming a genuine 5.2-point loss of discrimination, while temporal transfer is nearly lossless. A fine-tuned DistilBERT is stronger in-distribution (F1 = 0.9993) but degrades far more under topic shift, losing 12.9 average-precision points against the linear model's 5.2. Transferred to the independent LIAR benchmark, all three models fall to near-chance ranking (ROC-AUC 0.54-0.57), none beating a majority-class baseline. We conclude that within-corpus scores here quantify source and topic separability rather than veracity, that added capacity exploits the shortcut rather than avoiding it, and we recommend metadata-only, small-sample, and topic-disjoint baselines as inexpensive diagnostics for future work.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.25006
