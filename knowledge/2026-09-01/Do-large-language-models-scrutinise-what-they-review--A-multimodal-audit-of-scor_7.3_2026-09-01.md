# Do large language models scrutinise what they review? A multimodal audit of scoring calibration, error detection, and author-identity effects

**评分：** 7.3  
**状态：** 正常  
**标签：** LLM评估, 多模态, 同行评审, AI审计, 基准测试, 论文, AI for Science  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28626v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used to generate peer reviews, prompting examination of their capacity for critical evaluation. This study evaluates two multimodal LLMs, Qwen2.5-VL-72B and Pixtral-Large-124B, as reviewers across 165 submissions to the 2026 International Conference on Learning Representations, a venue that postdates both models' training cutoffs. Manuscripts were presented to both models with author identities blinded, replaced with high-prestige affiliations, or replaced with low-prestige affiliations, and in either text-only or text-with-figure format. Additionally, 145 verifiably detectable errors were inserted into 55 manuscripts to assess error identification under natural and verification-oriented prompts. Across all manuscript groups, including rejected submissions, LLM scores ranged from 7.0 to 8.1, whereas human mean scores ranged from 3.4 to 6.8. The models detected 12.1\% of the verified errors under natural prompting, and a one-sentence verification instruction increased detection to 22.2\%; however, 78\% of the errors remained undetected. Providing figures reduced error detection while increasing review scores. No visual error was reliably verified against its corresponding figure, and half of the text-only reviews described figures that were not provided. Author identity did not influence either review scores or error detection. LLM editorial decisions exactly matched those produced by simple score averaging.

## 综合总结
本文对Qwen2.5-VL-72B和Pixtral-Large-124B两款多模态LLM在165篇ICLR 2026投稿上的审稿表现进行了受控审计。研究发现LLM评分集中在7.0-8.1区间，显著高于人类均值（3.4-6.8）；错误检测率仅12.1%（自然提示）至22.2%（验证提示），78%的错误未被识别；提供图文反而降低错误检测率；作者身份声望不影响评分或错误检测；LLM编辑决策等同于简单分数平均。研究对LLM审稿的能力边界提供了系统性实证，警示当前LLM尚不适合独立承担同行评审任务，但作为审计/基准工作缺乏更深的机制分析与方法论创新。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该研究采用受控实验设计，系统性地考察了多模态LLM在同行评审中的评分校准、错误检测能力及作者身份效应。实验涵盖作者身份盲化、高/低声望机构替换、文本/图文两种模态以及自然/验证导向提示等多种条件，并植入了145个可验证错误。方法论严谨，变量控制较好，但本质上属于审计/基准测试类工作，缺乏新算法或理论贡献。LLM评分压缩在7.0-8.1区间、与人类评分显著偏离的发现具有诊断价值，但分析深度中等，对失败模式的机制解释不够深入。

### 实用性 (评分: 7.0/10)
对学术出版界和AI研究者均有较高参考价值。揭示了LLM作为审稿人的具体局限：评分校准差、错误检测率低、视觉信息未被充分利用、作者身份盲化不影响结果等，这些结论为将LLM集成到评审流程的实践者提供了重要警示。对开发自动评审工具的从业者指明了关键改进方向（错误检测、视觉理解）。但研究覆盖的模型仅两款，且为2025年初版本，结论的泛化性需要谨慎对待。

### 社区活跃度 (评分: 7.5/10)
主题高度契合当前AI社区对LLM在科研流程中应用的广泛讨论与担忧，特别是LLM辅助/替代同行评审的伦理与方法论争议。时间性强，正值AI审稿争议高峰期。arXiv作为预印本来源具有一定可信度，但尚未经过同行评审。ICLR 2026投稿数据的使用增加了实证基础。研究结论与社区普遍担忧一致，但其系统量化贡献具有独立价值。作者为独立研究者，机构背书有限。

## 项目链接
https://arxiv.org/abs/2608.28626
