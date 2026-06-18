# Want Better Synthetic Data? Steer It: Activation Steering for Low-Resource Language Generation

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 合成数据, 低资源语言, 激活引导, 论文  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18389v1 Announce Type: new Abstract: Large language models (LLMs) have become an effective tool for synthetic data generation, including for low-resource languages, where generated data can improve downstream task performance. Current best-performing approaches typically rely on few-shot prompting with target-language examples, which increases inference costs and may reduce diversity through lexical anchoring. In this work, we investigate activation steering as an alternative for low-resource synthetic data generation. We study two steering strategies: Language Steering, which targets the linguistic identity of a language, and Quality Steering, which captures well-formedness by contrasting human-written and backtranslated text representations. We evaluate these methods across four open-source LLMs, multiple layers, and 11 typologically diverse languages by generating sentiment and topic classification data and finetuning smaller classifiers. Steering is applied in both zero-shot and few-shot prompting settings and compared against non-steered counterparts. Our results show that steering on early layers consistently improves the diversity of generated data while often yielding stronger downstream model performance, particularly for low-resource languages.

## 综合总结
本文研究了激活引导在低资源语言合成数据生成中的应用，提出语言引导和质量引导两种策略。实验表明，在LLM早期层应用激活引导，相比传统few-shot prompting，不仅能持续提升生成数据的多样性，还能在低资源语言上获得更优的下游任务性能，同时降低了推理成本。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出将激活引导应用于低资源语言合成数据生成，创新性地设计了语言引导（针对语言身份）和质量引导（对比人类与回译文本表征）两种策略，并在4个开源LLM、11种不同语系语言及不同网络层上进行了严谨的实证评估，论证了早期层引导在提升数据多样性和下游性能上的优势，技术深度和新颖性较高。

### 实用性 (评分: 7.5/10)
为低资源语言数据生成提供了一种替代few-shot prompting的新范式，有效降低了推理成本并缓解了词汇锚定导致的多样性下降问题，对NLP从业者构建低资源语料库具有较高参考价值，但需具备一定的模型内部表征干预操作基础。

### 社区活跃度 (评分: 7.0/10)
关注低资源语言和合成数据两大社区热点，针对当前few-shot方法成本高、多样性差的痛点提出解决方案，来源为arXiv预印本，具有较好的时效性和社区关注度潜力。

## 项目链接
https://arxiv.org/abs/2606.18389
