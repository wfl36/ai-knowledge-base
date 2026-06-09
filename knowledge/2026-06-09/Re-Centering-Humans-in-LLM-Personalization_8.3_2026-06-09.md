# Re-Centering Humans in LLM Personalization

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 个性化, 评估, 对齐, 论文, 实证研究  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06614v1 Announce Type: new Abstract: Despite growing interest, most evaluations of large language models' (LLMs') personalization abilities have relied on synthetic data. It remains unclear how well current personalization systems work for real users. In this paper, we study the gap in LLM personalization performance when using synthetic versus human data. We collect human conversations (550 conversations) and judgments across three stages of personalization: extracting user attributes from conversations (5,949 judgments), pairing relevant attributes with new prompts (11,919), and incorporating relevant attributes into a personalized response (1,101). Incorporating human data reveals system limitations at each stage. Models struggle to extract attributes from human conversations, disagree with human judgments on relevant attributes, and generate personalized responses that humans judge no better than generic responses (though that LLM judges widely rate as better). We introduce two lightweight training-based interventions that shift automated personalization evaluation closer to human data in our first two stages. However, in our third stage we find that learned reward models achieve only modest correlation with human ratings, suggesting that human-aligned personalization quality judgments are difficult to model directly. Our collected data provides a foundation for studying how models should extract, select, and incorporate user information in ways that humans find useful.

## 综合总结
本文研究了LLM个性化评估中合成数据与真实人类数据的差距，通过收集大量人类对话和评判，发现模型在提取用户属性、判断属性相关性及生成个性化回复时存在显著局限，且LLM评判与人类评判严重不符。虽然提出的轻量级干预改善了前两阶段，但奖励模型在生成阶段仍难以对齐人类偏好，为个性化系统的评估与优化提供了重要启示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究深入剖析了LLM个性化在合成数据与真实人类数据间的性能差距，通过大规模人类实验揭示了模型在提取、匹配和生成三个阶段的局限性。特别是发现LLM评判与人类评判在个性化回复质量上存在严重背离，且现有奖励模型难以有效建模人类偏好，论证严谨且具有深刻洞见。

### 实用性 (评分: 8.0/10)
提出了两种轻量级训练干预措施，有效提升了前两阶段自动评估与人类评判的对齐度，对工业界改进个性化系统的评估和训练具有直接参考价值；同时其发布的人类对话与评判数据集为后续研发提供了重要基准。

### 社区活跃度 (评分: 8.5/10)
话题直击当前LLM个性化应用中过度依赖合成数据和模型自评的痛点，来源权威，发现对现有个性化评估范式构成挑战，在学术界和工业界均具有高度的时效性和影响力。

## 项目链接
https://arxiv.org/abs/2606.06614
