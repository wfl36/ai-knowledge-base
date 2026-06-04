# A Systematic Analysis of Linguistic Features in AI-Generated Text Detection Across Domains and Models

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, AI检测, 文本分析, 可解释性, 论文, 实证研究  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04177v1 Announce Type: new Abstract: Interpretable linguistic features offer a promising approach for explaining why a given text appears machine-generated, particularly for non-expert users. However, existing findings on which features reliably indicate LLM-generated text remain fragmented across feature sets, models, and text domains. To address this gap, we conduct a large-scale empirical study assessing the robustness of linguistic signals for characterizing AI-generated text. Our analysis covers 284 interpretable linguistic features across outputs from 27 LLMs and ten text domains under cross-model and cross-domain generalization settings. We show that classifiers based solely on linguistic features can reliably distinguish AI-generated from human-written text. However, many previously proposed indicators prove strongly context-dependent, with the exception of measures of lexical richness, which remain robust signals across model families and text domains. These results demonstrate which linguistic signals generalize across contexts and provide a foundation for more reliable, interpretable analyses of AI-generated language.

## 综合总结
本文针对AI生成文本检测中语言特征发现零散的问题，进行大规模实证研究，覆盖284个特征、27个LLM和10个文本领域。研究发现仅基于语言特征的分类器即可有效区分AI与人类文本，且“词汇丰富度”是唯一在跨模型和跨领域均保持鲁棒性的指标，其他多数指标则高度依赖上下文。该研究为构建可靠、可解释的AI文本检测系统提供了重要实证基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
覆盖284个特征、27个LLM和10个领域的大规模实证研究，论证严谨；澄清了先前零散甚至矛盾的发现，明确指出“词汇丰富度”是唯一跨模型和跨领域鲁棒的语言信号，而其他指标多具上下文依赖性，研究深度与系统性俱佳。

### 实用性 (评分: 8.0/10)
对AI文本检测工具的开发者具有高参考价值，直接指导特征工程（优先采用词汇丰富度指标，谨慎使用上下文依赖特征）；可解释性特征对非专家用户友好，适用于内容审核、学术诚信等广泛场景。

### 社区活跃度 (评分: 8.0/10)
AI生成文本检测是AIGC时代的持续热点；研究源自arXiv，方法扎实，结论对社区内现有分歧的统一具有重要价值，为后续可解释性检测研究确立了基准。

## 项目链接
https://arxiv.org/abs/2606.04177
