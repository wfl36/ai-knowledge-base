# Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 安全对齐, 偏见评估, 跨文化, 数据集构建, 论文  
**更新日期：** 2026-07-10  
**来源：** rss  

## 项目描述
arXiv:2607.07895v1 Announce Type: new Abstract: Research on stereotypes in large language models (LLMs) has largely focused on English-speaking contexts, due to the lack of datasets in other languages and the high cost of manual annotation in underrepresented cultures. To address this gap, we introduce a cost-efficient human-LLM collaborative annotation framework and apply it to construct EspanStereo, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America. EspanStereo captures both well-documented stereotypes from prior literature and culturally specific biases absent from English-centric resources. Using LLMs to generate candidate stereotypes and in-culture annotators to validate them, we demonstrate the framework's effectiveness in identifying nuanced, region-specific biases. Our evaluation of Spanish-supporting LLMs using EspanStereo reveals significant variation in stereotypical behavior across countries, highlighting the need for more culturally grounded assessments. Beyond Spanish, our framework is adaptable to other languages and regions, offering a scalable path toward multilingual stereotype benchmarks. This work broadens the scope of stereotype analysis in LLMs and lays the groundwork for comprehensive cross-cultural bias evaluation.

## 综合总结
本文提出了一种低成本的人机协作标注框架，利用LLM生成候选并由文化内标注者验证，成功构建了覆盖多国西语文化的EspanStereo刻板印象数据集。研究填补了非英语语境下偏见数据集的空白，揭示了西语LLM在不同国家间刻板印象行为的显著差异，并提供了一条可扩展至其他语言和地区的跨文化偏见评估路径，对多语言大模型的安全对齐与评估具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了一种新颖的人机协作（Human-LLM）标注框架，通过LLM生成候选刻板印象并结合文化内人类标注者验证，有效解决了非英语语境下刻板印象数据集构建成本高、难度大的问题。研究不仅停留在框架设计，还实际构建了EspanStereo数据集，并深入揭示了西语大模型在不同国家间刻板印象行为的显著差异，方法论证严谨，具有较好的研究深度与新颖性。

### 实用性 (评分: 8.5/10)
对大模型安全对齐与评估从业者具有极高的实践指导价值。该框架提供了一条可扩展、低成本的跨文化偏见评估路径，不仅适用于西班牙语，还可直接迁移至其他低资源语言和地区，为构建多语言刻板印象基准和指导多文化场景下的模型评估提供了清晰的工程实践方案。

### 社区活跃度 (评分: 7.5/10)
话题聚焦于大模型安全与多语言偏见评估，属于当前AI对齐领域的热点与痛点。作者在自然语言处理与计算社会科学领域具有一定的学术背景，arXiv预印本发布保证了话题的时效性，但作为尚未经过同行评审的初版论文，权威性仍有待后续验证。

## 项目链接
https://arxiv.org/abs/2607.07895
