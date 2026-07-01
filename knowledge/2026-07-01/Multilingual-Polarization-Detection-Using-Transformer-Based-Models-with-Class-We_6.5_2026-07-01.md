# Multilingual Polarization Detection Using Transformer-Based Models with Class Weighting and Threshold Tuning

**评分：** 6.5  
**状态：** 正常  
**标签：** NLP, 多语言, 极化检测, 文本分类, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30857v1 Announce Type: new Abstract: This paper describes our submission to SemEval-2026 Task 9 on detecting multilingual, multicultural, and multievent online polarization. We address all three subtasks: binary polarization detection, polarization type classification, and manifestation identification for English and Swahili. Our approach leverages transformer-based models (RoBERTa-base for English, AfroXLMR-base for Swahili) with class-weighted loss functions to address severe label imbalance and per-label threshold tuning to optimize multi-label classification. On the test set, we achieve F1 macro scores of 0.7901 (English) and 0.7910 (Swahili) for Subtask 1, 0.4615 (English) and 0.4808 (Swahili) for Subtask 2 and 0.4791 (English) and 0.5830 (Swahili) for Subtask 3, which give competitive performance on the leaderboard, demonstrating the effectiveness of our methods for handling imbalanced multi-label polarization detection. Our error analysis reveals that models struggle with dehumanization detection and lack of empathy.

## 综合总结
本文介绍了参与SemEval-2026 Task 9的工作，针对多语言在线极化检测任务，采用RoBERTa和AfroXLMR结合类加权损失与阈值调优的方法，有效缓解了标签不平衡问题。模型在英语和斯瓦希里语的三个子任务中取得了有竞争力的表现，但错误分析表明在去人性化检测等方面仍有不足。该方案为多语言内容审核提供了实用的工程参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
采用成熟的Transformer模型（RoBERTa, AfroXLMR）结合类加权损失和阈值调优解决多标签不平衡问题，方法属于常规的工程组合，缺乏底层算法或架构上的创新，但针对低资源语言（斯瓦希里语）的跨语言适配具有一定的研究参考价值。

### 实用性 (评分: 7.5/10)
针对在线极化检测这一实际需求，提供了从二分类到多标签分类的完整解决方案。类加权和阈值调优方法简单有效，易于在实际内容审核系统中复现和部署，对处理低资源语言的极化内容检测具有直接的落地指导意义。

### 社区活跃度 (评分: 7.0/10)
论文提交至NLP领域权威评测SemEval-2026，话题涉及多语言和在线极化，符合当前社会计算和内容安全领域的热点，时效性强且来源可信。但作为竞赛短文，其长期学术影响力相对有限。

## 项目链接
https://arxiv.org/abs/2606.30857
