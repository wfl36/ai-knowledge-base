# Cross-Prompt Generalization in Detecting AI-Generated Fake News Using Interpretable Linguistic Features

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, AI安全, 假新闻检测, 文本检测, 论文, 实证研究  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04199v1 Announce Type: new Abstract: The increasing use of large language models has raised concerns about the spread of AI-generated fake news, particularly under varying prompting strategies. Most existing detection models are trained and evaluated under a single generation setting, leaving their ability to generalize across unseen prompts unclear. In this study, we investigate cross-prompt generalization in fake news detection using three datasets of AI-generated articles produced under distinct prompts, combined with real news articles. We extract interpretable linguistic features capturing lexical diversity, readability, and emotion-based characteristics and evaluate a random forest classifier under a cross-prompt framework, where models trained on one prompt are tested on another. Across all six train-test combinations, performance remains consistently high, with AUC values ranging from 0.988 to 1.000. Analysis of feature distributions shows that AI-generated text exhibits increased lexical diversity, reduced readability, and substantially lower emotional intensity compared to the overall dataset, with variations across prompts. Despite these distributional shifts, the classifier maintains strong performance, indicating that these features capture stable properties of AI-generated text that generalize across prompting strategies. These findings suggest that feature-based approaches can provide robust detection of AI-generated fake news under prompt variability.

## 综合总结
本文研究了AI生成假新闻检测模型在跨提示词场景下的泛化能力。通过提取词汇多样性、可读性和情感等可解释语言学特征，并使用随机森林分类器，研究发现尽管不同提示词会导致AI文本特征分布偏移，但模型在6种跨提示词测试组合中均保持极高AUC（0.988-1.000）。这表明基于简单语言学特征的方法能有效捕捉AI文本的稳定属性，为构建轻量、可解释且抗提示词变化的假新闻检测系统提供了有力支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
研究聚焦AI生成假新闻检测中的跨提示词泛化难题，采用可解释语言学特征（词汇多样性、可读性、情感）与随机森林分类器。方法虽非深度学习前沿，但论证严谨，通过6组交叉实验证明简单特征能捕捉AI文本的稳定属性，AUC达0.988-1.000，揭示了AI文本在词汇与情感表达上的固有缺陷，提供了反直觉且有价值的洞见。

### 实用性 (评分: 9.0/10)
极具落地参考价值。基于语言学特征和随机森林的方案计算开销极小、部署门槛低且具备强可解释性，可直接指导内容平台和风控系统构建轻量级、抗提示词变化的AI文本过滤与假新闻拦截机制，适用范围广泛。

### 社区活跃度 (评分: 7.5/10)
话题切中当前大模型滥用与虚假信息治理的社会痛点，时效性极强。arXiv论文来源具备基本学术可信度，但AUC接近1.000的完美结果在面对更复杂大模型或对抗样本时的真实鲁棒性，可能在社区引发进一步讨论与验证。

## 项目链接
https://arxiv.org/abs/2606.04199
