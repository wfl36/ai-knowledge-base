# Scalable and Culturally Specific Stereotype Dataset Construction via Human-LLM Collaboration

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 偏见评估, 跨文化, 数据集构建, 人机协作, 论文  
**更新日期：** 2026-07-11  
**来源：** rss  

## 项目描述
arXiv:2607.07895v1 Announce Type: new Abstract: Research on stereotypes in large language models (LLMs) has largely focused on English-speaking contexts, due to the lack of datasets in other languages and the high cost of manual annotation in underrepresented cultures. To address this gap, we introduce a cost-efficient human-LLM collaborative annotation framework and apply it to construct EspanStereo, a Spanish-language stereotype dataset spanning multiple Spanish-speaking countries across Europe and Latin America. EspanStereo captures both well-documented stereotypes from prior literature and culturally specific biases absent from English-centric resources. Using LLMs to generate candidate stereotypes and in-culture annotators to validate them, we demonstrate the framework's effectiveness in identifying nuanced, region-specific biases. Our evaluation of Spanish-supporting LLMs using EspanStereo reveals significant variation in stereotypical behavior across countries, highlighting the need for more culturally grounded assessments. Beyond Spanish, our framework is adaptable to other languages and regions, offering a scalable path toward multilingual stereotype benchmarks. This work broadens the scope of stereotype analysis in LLMs and lays the groundwork for comprehensive cross-cultural bias evaluation.

## 综合总结
本文提出了一种低成本的人机协作标注框架，通过LLM生成与文化内人类验证相结合的方式，构建了涵盖多国西语的EspanStereo刻板印象数据集。评估表明，支持西语的LLM在不同国家的刻板印象表现存在显著差异。该框架可扩展至其他语言，为多语言和跨文化的大模型偏见评估提供了可规模化落地的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出了一种LLM生成候选与文化内人类验证相结合的人机协作标注框架，方法设计合理且具有针对性。研究不仅填补了非英语语境下刻板印象数据集的空白，还深入揭示了不同西语国家间LLM刻板印象行为的细微差异，展现了较好的研究深度与文化洞察力。

### 实用性 (评分: 8.5/10)
该框架具有高度的可扩展性和可复用性，能够以较低成本迁移至其他低资源语言和特定文化区域，为AI安全与对齐团队进行跨文化偏见评估、红队测试及多语言模型微调提供了极具实操价值的方法论和数据构建工具。

### 社区活跃度 (评分: 8.0/10)
多语言与跨文化AI安全是当前大模型全球化落地中的核心痛点与热点话题，具有极高的时效性。论文发布于arXiv，作者学术背景可靠，且构建的EspanStereo数据集直接回应了社区对非英语评测基准的迫切需求，具备较好的行业影响力。

## 项目链接
https://arxiv.org/abs/2607.07895
