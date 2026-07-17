# LBA: Textual Hard-Label Adversarial Attack under Low Query Budgets

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 对抗攻击, 文本安全, 低查询预算, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14101v1 Announce Type: new Abstract: Generating high-quality adversarial texts with low query budgets remains a challenging problem in the hard-label scenario. Most existing approaches rely on greedy algorithms, where one position in the text is selected for substitution, followed by the substitutions of other positions. This local search approach may fail to discover high-quality adversarial examples and often leads to excessive query costs. Ideally, an optimal adversarial sample would consider all possible position combinations in the text, but exhaustive search is computationally impractical. To address this challenge, we propose a sampling-based method called LBA, which constructs an approximate distribution of high-quality adversarial examples by integrating both prior and posterior knowledge, and utilizes this distribution for sampling. As sampling progresses, posterior knowledge updates the approximate distribution, which in turn guides more effective sampling. Extensive experiments on six language models, ranging from small-scale to large-scale architectures across four datasets, demonstrate that LBA significantly outperforms state-of-the-art baselines on all evaluation metrics. Additionally, LLM-based assessment indicates that LBA generates more semantically preserved and comprehensible adversarial texts.

## 综合总结
本文提出了一种名为LBA的基于采样的文本硬标签对抗攻击方法，旨在解决低查询预算下现有贪心算法局部搜索导致的查询成本高和次优解问题。LBA通过动态整合先验与后验知识构建高质量对抗样本的近似分布，并利用后验反馈不断优化采样策略。在4个数据集和6个不同规模语言模型上的实验表明，LBA在各项指标上显著超越现有SOTA方法，且LLM评估显示其生成的对抗文本具有更好的语义保留性和可读性，对模型安全评估具有重要实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对现有硬标签文本对抗攻击中贪心算法的局部搜索局限，LBA创新性地引入基于概率分布的采样机制，通过动态整合先验与后验知识构建近似分布，有效逼近全局最优解，避免了穷举搜索的计算不可行性，理论严谨且方法新颖。

### 实用性 (评分: 8.0/10)
该方法直击现实场景中API查询受限且仅能获取硬标签的痛点，显著降低了攻击的查询成本，生成的对抗样本语义保真度高，对大模型安全评估、鲁棒性测试及红队对抗具有极高的实践指导价值。

### 社区活跃度 (评分: 8.5/10)
论文发布时间新，时效性强；作者团队包含知名安全与NLP领域学者，权威性高；实验覆盖从小模型到LLM的6种架构及4个数据集，验证充分，且引入LLM评估指标符合当前社区关注焦点，具有较高的学术影响力。

## 项目链接
https://arxiv.org/abs/2607.14101
