# Unveiling Public Opinion: A Study of Sentiment Analysis Using LSTM and Traditional Models

**评分：** 2.0  
**状态：** 待复核  
**标签：** NLP, 情感分析, 论文  
**更新日期：** 2026-07-11  
**来源：** rss  

## 项目描述
arXiv:2607.07772v1 Announce Type: new Abstract: In this age of social media, sites like Twitter have become meeting places for people to share their views and feelings on a wide range of issues and current events as they unfold in real time. Sentiment analysis, a critical application of NLP, has become indispensable due to the massive influx of user-generated content, enabling the extraction of meaningful insights from the opinions and emotions expressed in textual data. Sentiment analysis on Twitter employs sophisticated computational techniques to categorize tweets into positive, negative, or neutral sentiments. This method not only examines individual expressions but also analyzes vast databases related to specific subjects or events. By spotting these emotions, machine learning models help improve public opinion interpretation and trend forecasting. This paper examines the effectiveness of various machine learning and deep learning approaches. Designed for this use, the system evaluates logistic regression, random forest, na\"ive bayes, gradient boosting, and LSTM networks, among other algorithms applied in sentiment classification. This work identifies the optimal sentiment analysis model using a Kaggle Twitter dataset that has been preprocessed through tokenization, lemmatization, and stopword elimination. Emphasizing the better performance of the LSTM approach, the model attained a training accuracy of 90.98%, a testing accuracy of 80.00%, and a micro-average ROC- AUC score of 0.92. These results show that the model outperforms conventional machine learning techniques in capturing contextual and sequential textual aspects.

## 综合总结
本文对比了LSTM与传统机器学习模型在Twitter情感分析任务上的表现，结果显示LSTM在测试集上达到80%准确率并优于传统方法。然而，该研究使用的技术路线严重滞后于当前NLP发展，缺乏创新性与实际应用价值，仅适合作为基础教学案例。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 2.5/10)
研究使用LSTM和传统机器学习模型（逻辑回归、随机森林等）在Kaggle Twitter数据集上进行情感分析对比。LSTM取得了80%的测试准确率和0.92的AUC。但技术路线严重过时，缺乏理论创新，且未涉及当前主流的预训练模型或大语言模型，训练与测试准确率差距明显存在过拟合风险，整体研究深度极浅。

### 实用性 (评分: 2.0/10)
对工业界实践几乎没有参考价值。当前情感分析任务已被基于Transformer的模型（如BERT）及大语言模型主导，LSTM和传统ML方法在性能和泛化能力上均无优势，仅可作为初学者的入门教学案例或基线参考。

### 社区活跃度 (评分: 1.5/10)
话题时效性极差，LSTM文本分类属于近十年前的技术热点；来源为普通arXiv预印本，作者影响力弱，该研究在当前AI社区难以引起关注或产生任何影响力。

## 项目链接
https://arxiv.org/abs/2607.07772
