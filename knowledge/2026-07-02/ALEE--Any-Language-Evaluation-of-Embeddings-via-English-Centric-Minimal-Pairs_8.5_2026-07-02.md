# ALEE: Any-Language Evaluation of Embeddings via English-Centric Minimal Pairs

**评分：** 8.5  
**状态：** 正常  
**标签：** 嵌入评估, 多语言, 跨语言, 语义表示, 论文, 评测基准  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00171v1 Announce Type: new Abstract: Text embeddings are standard for semantic similarity tasks, yet their evaluation remains an open challenge. Current benchmarks are static, cover only a limited set of languages, are often domain-specific, susceptible to overfitting, and poorly representative of low-resource languages. To address these limitations, we introduce ALEE, a framework that extends Sentence Smith (Li et al., 2025) to the cross-lingual and paragraph level. ALEE uses Abstract Meaning Representations (AMR) to generate English minimal pairs with controlled, fine-grained semantic shifts, which are paired with translations in target languages. This approach enables targeted diagnostics for models in any language with English parallel data. We conduct a large-scale empirical study across a diverse set of embedding models and 275+ languages spanning three parallel datasets. On ALEE, performance varies substantially across languages, text lengths, and linguistic phenomena, exposing persistent gaps in cross-lingual semantic representation that track language prevalence in training resources and subword tokenization. We release ALEE at https://github.com/Andrian0s/any-lang-embed-eval

## 综合总结
本文提出ALEE框架，利用抽象语义表示（AMR）生成带有精细语义变化的英语最小对并配对目标语言翻译，从而实现对任意语言的文本嵌入进行跨语言和段落级别的细粒度评估。大规模实验覆盖275+种语言，揭示了现有嵌入模型在跨语言语义表征上的显著差距，特别是低资源语言和子词分词方面的缺陷。该框架已开源，为多语言嵌入模型的诊断和优化提供了有力工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出基于抽象语义表示（AMR）生成英语最小对并映射至目标语言的评估方法，实现了跨语言和段落级别的细粒度语义诊断。覆盖275+种语言的大规模实证研究设计严谨，有效揭示了现有嵌入模型在低资源语言和不同分词策略下的表征缺陷，方法新颖且论证扎实。

### 实用性 (评分: 8.0/10)
ALEE框架已开源，可直接作为多语言嵌入模型的细粒度诊断工具使用。对模型开发者优化跨语言表征、改进分词策略具有直接的指导价值，但在常规业务落地中更多作为评测组件而非生产组件，适用范围聚焦于模型评估环节。

### 社区活跃度 (评分: 9.0/10)
多语言及低资源语言嵌入评估是当前AI社区的核心痛点，ALEE的出现极具时效性。作者团队包含NLP领域知名学者Rico Sennrich，学术背景权威，且代码开源易于复现，有望对多语言嵌入模型的评测标准产生重要影响。

## 项目链接
https://arxiv.org/abs/2607.00171
