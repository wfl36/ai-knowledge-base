# Equity with Efficiency: An Empirical Study of Tokenizers for Multilingual Large Language Models

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 多语言, 分词器, 公平性, 东南亚语言, 论文, 实证研究  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15044v1 Announce Type: new Abstract: Multilingual large language models (LLMs) depend on subword tokenization to bridge discrete text and continuous neural representation. State-of-the-art multilingual LLMs often use Byte-level Byte-Pair Encoding (BPE) tokenizers that structurally favor high-resource languages and Latin scripts. For speakers of underrepresented languages, particularly those across Southeast Asia, this bias inflates inference costs and widens cross-lingual capability gaps. We present the first systematic comparison of equitable tokenizers on a unified benchmark spanning 11 Southeast Asian languages. Beyond tokenizer-level analysis of compression efficiency and cross-lingual equity, we assess downstream task performance through controlled 1.5B-parameter language model training using the same training data. Our results show that Parity-aware BPE lies on the Pareto frontier of the efficiency-equity trade-off, achieving strong compression parity at competitive cost. Morphology-Driven Byte Encoding delivers the best semantic reasoning performance through morphologically richer representations, albeit at a higher computational expense. Byte Latent Transformer underperforms on downstream tasks, possibly because its architectural assumptions misalign with the constraints of limited low-resource training data. Together, our findings demonstrate that cross-lingual fairness and tokenization efficiency are not fundamentally at odds, and offer practical guidance for designing equitable multilingual models.

## 综合总结
本文针对多语言大模型分词器偏向高资源语言的问题，首次在11种东南亚语言上系统比较了多种公平分词器。通过1.5B参数模型的受控训练发现，Parity-aware BPE在效率与公平的权衡中处于帕累托前沿，Morphology-Driven Byte Encoding在语义推理上表现最佳但成本较高，而Byte Latent Transformer在低资源数据下表现不佳。研究证明跨语言公平与分词效率并非根本对立，为构建公平的多语言模型提供了重要实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文首次在涵盖11种东南亚语言的统一基准上系统比较了公平分词器，实验设计严谨，不仅分析了压缩效率与跨语言公平性，还通过控制变量的1.5B参数模型训练评估了下游任务。对Parity-aware BPE、Morphology-Driven Byte Encoding及Byte Latent Transformer的帕累托前沿分析与局限性探讨（如BLT在低资源数据下的不匹配）展现了较深的研究深度与洞见。

### 实用性 (评分: 8.5/10)
对多语言大模型开发者（尤其是面向低资源语言和东南亚市场的团队）具有极高的实践指导价值。明确指出了不同分词策略在效率、公平性和语义推理上的权衡，如Parity-aware BPE在效率与公平间的最优平衡，可直接指导分词器的选型与优化设计。

### 社区活跃度 (评分: 8.0/10)
多语言LLM的公平性与分词效率是当前AI社区关注的重要议题，该研究由资深NLP学者主导，来源权威可信。结论对打破“公平必然牺牲效率”的固有认知有积极意义，在多语言和低资源语言研究社区具有较高的时效性和影响力。

## 项目链接
https://arxiv.org/abs/2606.15044
