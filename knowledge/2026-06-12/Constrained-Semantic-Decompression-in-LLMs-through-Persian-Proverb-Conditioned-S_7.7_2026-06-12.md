# Constrained Semantic Decompression in LLMs through Persian Proverb-Conditioned Story Generation

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 语义解压, 推理, 文化对齐, NLP, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12599v1 Announce Type: new Abstract: Transforming a dense, abstract proverb into an engaging and morally faithful narrative requires deep cultural understanding and robust semantic grounding. We frame this problem as a \emph{constrained semantic decompression} task and study proverb-conditioned story generation as a testbed for abstraction-to-realization in large language models (LLMs). Focusing on Persian, we introduce the Proverb Aligned Narrative Dataset (PAND), pairing proverbs with human-written stories and explicit meanings. By a hybrid evaluation framework that combines human-calibrated LLM-as-a-Judge with structural metrics, we analyze model behavior across multiple prompting regimes. Our findings reveal a persistent \emph{decompression gap}: current LLMs often achieve strong surface-level fluency while failing to faithfully instantiate the underlying moral and causal structure encoded in proverbs. We further show that explicit reasoning and iterative refinement can partially mitigate these failures, suggesting that many decompression errors arise from difficulties in translating abstract meaning into narrative form rather than a complete lack of relevant knowledge. Our proposed task naturally extends to other forms of compressed cultural knowledge.

## 综合总结
本文提出了“受约束的语义解压”任务，通过波斯谚语条件化故事生成来测试LLM将抽象概念转化为具体叙事的能力。研究构建了PAND数据集，并采用混合评估框架发现当前LLM存在表面流畅但无法忠实还原谚语道德与因果结构的“解压差距”。实验表明，显式推理和迭代细化能部分缓解此问题，说明模型缺陷在于抽象到具象的转化困难而非知识缺失。该研究为评估和提升LLM的文化及深层语义理解提供了新视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了“受约束的语义解压”这一新颖视角，将谚语到故事的生成定义为从抽象到具象的解压过程，概念创新性强。研究构建了PAND数据集，并设计了结合LLM-as-a-Judge与结构化指标的混合评估框架，方法论严谨。核心发现“解压差距”深刻揭示了当前LLM在深层语义对齐上的缺陷，且通过实验证实错误源于抽象到具象的转化困难而非知识缺失，论证具有洞见。

### 实用性 (评分: 7.0/10)
对NLP及多语言AI从业者具有较高的参考价值。研究指出的“解压差距”现象为评估大模型的文化理解与深层语义能力提供了新基准；文中验证的显式推理和迭代细化方法可直接应用于提示词工程，以改善模型处理高度压缩知识（如法律条文、科学定理）的生成质量。不过，其实际应用场景相对垂直，主要聚焦于文化叙事与语义对齐领域。

### 社区活跃度 (评分: 7.5/10)
该论文为arXiv最新发布（2026年6月），探讨大模型在深层语义理解与文化对齐方面的局限性，契合当前AI社区对模型幻觉和深层推理能力的关注热点。虽然聚焦于波斯语及谚语这一相对小众的领域，但其提出的“语义解压”概念具有高度普适性，能够引发关于大模型如何处理压缩文化知识的广泛讨论，具备一定的学术影响力潜力。

## 项目链接
https://arxiv.org/abs/2606.12599
