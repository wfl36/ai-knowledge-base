# LLM Parameters for Math Across Languages: Shared or Separate?

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 推理, 多语言, 可解释性, 论文  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18453v1 Announce Type: new Abstract: Large language models (LLMs) exhibit substantial cross-lingual variation in mathematical reasoning performance, but it remains unclear whether these differences reflect language-specific parameters or a shared mechanism that manifests differently by language. We present a cross-lingual mechanistic analysis of mathematical reasoning in LLMs, enabling us to localize and compare model parameters that support mathematical reasoning across languages. We find that the extracted math-associated parameters exhibit partial cross-lingual overlap, with the strongest overlap concentrated in intermediate model layers. We further observe that English consistently produces the largest set of math-relevant parameters, whereas lower-resource languages reveal smaller sets of relevant parameters. These results suggest that math-related behavior in multilingual LLMs is neither fully language-invariant nor fully language-specific, but instead exhibits partial cross-lingual parameter overlap with systematic language-dependent differences.

## 综合总结
本文通过跨语言机制分析，探讨了LLM在数学推理中是否共享参数。研究发现，数学相关参数在不同语言间存在部分重叠，且重叠集中在模型中间层；英语拥有最大的数学参数集，而低资源语言参数集较小。这表明多语言LLM的数学行为既非完全语言无关，也非完全语言特定，而是部分重叠并伴随系统性差异。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
深入LLM内部机制，通过跨语言参数定位与比较，揭示了数学推理在多语言模型中的部分重叠现象（尤其是中间层），以及高/低资源语言的参数集差异，论证严谨，对理解多语言模型内部表征与知识共享机制具有重要洞见。

### 实用性 (评分: 6.5/10)
研究结论对多语言大模型的训练和微调具有指导意义，例如提示低资源语言可能需要针对性的参数增强或跨语言迁移策略（如PEFT），但作为机制可解释性研究，其距离直接的工程落地应用仍有一定转化距离。

### 社区活跃度 (评分: 8.0/10)
跨语言推理与模型可解释性均为当前AI社区的核心热点，该研究结合两者填补了多语言数学推理机制分析的空白，来源为arXiv学术论文，作者群专业，具有较高的学术权威性和话题时效性。

## 项目链接
https://arxiv.org/abs/2606.18453
