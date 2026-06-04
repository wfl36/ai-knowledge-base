# Cross-Prompt Generalization in Detecting AI-Generated Fake News Using Interpretable Linguistic Features

**评分：** 7.7  
**状态：** 正常  
**标签：** AI检测, 虚假新闻, 大模型, 泛化性, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04199v1 Announce Type: new Abstract: The increasing use of large language models has raised concerns about the spread of AI-generated fake news, particularly under varying prompting strategies. Most existing detection models are trained and evaluated under a single generation setting, leaving their ability to generalize across unseen prompts unclear. In this study, we investigate cross-prompt generalization in fake news detection using three datasets of AI-generated articles produced under distinct prompts, combined with real news articles. We extract interpretable linguistic features capturing lexical diversity, readability, and emotion-based characteristics and evaluate a random forest classifier under a cross-prompt framework, where models trained on one prompt are tested on another. Across all six train-test combinations, performance remains consistently high, with AUC values ranging from 0.988 to 1.000. Analysis of feature distributions shows that AI-generated text exhibits increased lexical diversity, reduced readability, and substantially lower emotional intensity compared to the overall dataset, with variations across prompts. Despite these distributional shifts, the classifier maintains strong performance, indicating that these features capture stable properties of AI-generated text that generalize across prompting strategies. These findings suggest that feature-based approaches can provide robust detection of AI-generated fake news under prompt variability.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
研究聚焦于AI生成虚假新闻检测中的跨提示泛化问题。采用可解释的语言特征（词汇多样性、可读性、情感）结合随机森林分类器，发现AI文本具有词汇多样性高、可读性低和情感强度低的特点。尽管不同提示下特征分布存在偏移，但模型在六种跨提示组合中仍保持0.988-1.000的极高AUC，证明了这些特征的跨提示稳定性。方法相对传统，但实验设计严谨，结论明确。

### 实用性 (评分: 8.5/10)
对从业者具有较高参考价值。基于可解释特征和随机森林的方案轻量且易于部署，相比大型神经网络检测器成本更低且可解释性更强。跨提示泛化能力的验证解决了实际应用中提示策略多变的痛点，为构建鲁棒、低延迟的AI生成内容检测系统提供了切实可行的工程实践方向。

### 社区活跃度 (评分: 7.5/10)
选题紧扣当前大模型滥用和虚假信息传播的社会热点，具有极高的时效性和现实意义。作为arXiv预印本，其学术规范可信度良好。虽然极端的AUC数值可能引发对数据集难度和边界条件的讨论，但其对跨提示泛化性的关注填补了现有检测模型评估的空白，有望引起AI安全和内容风控领域的广泛关注。

## 项目链接
https://arxiv.org/abs/2606.04199
