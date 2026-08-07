# Learning Sexism Detection Using Multi-Agent Perspectivist Preference Optimization

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-07  
**来源：** rss  

## 项目描述
arXiv:2608.04056v1 Announce Type: new Abstract: When people label text for sexism, they often disagree, and not because some of them are wrong: they genuinely perceive sexism differently. Most NLP systems discard this disagreement by collapsing it into a majority vote. We propose the Multi-Agent Perspectivist Preference Optimization (MAP-PO) framework to keep these different perspectives. On the EXIST 2024 dataset of labeled English and Spanish tweets, we first cluster annotators by their labeling behavior rather than their demographic attributes. We then fine-tune one Large Language Model agent per cluster to reproduce that cluster's annotation behavior, and coordinate the agents with preference optimization that combines individual and team-level rewards. We evaluate MAP-PO in four settings defined by two languages and two backbone language models, asking whether each agent reproduces the annotations of its own cluster and whether the agents together reproduce the majority label. Two findings hold in all four settings. First, without fine-tuning the agents behave almost identically, so cluster-specific training is necessary. Second, we show that training each agent only on the labels of its own cluster pushes the agents far beyond the clusters they should represent, while adding a shared team-level training signal consistently keeps each agent calibrated to its cluster.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.04056
