# Improving LLMs via Validator-to-Generator Alignment

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 对齐, 自我纠错, 一致性, 训练目标, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02668v1 Announce Type: new Abstract: Large language models are inconsistent: varying prompts or including unrelated information can lead to unexpected changes in model outputs. The generator-validator (G-V) gap is one manifestation of this phenomenon, where LLMs generate responses that they then deem as invalid if re-queried to validate them. In this work, we introduce a new formulation of G-V consistency that involves a principled correction for utterance frequency. Specifically, generators often assign low likelihood to valid strings simply because those strings are a priori unlikely, which makes naive notions of G-V consistency unworkable. We show that under a natural model of rational agents answering questions with multiple answers, consistency of the validator with a frequency-corrected generator score emerges naturally. Our method, \emph{\FCPAname} (\FCPA), is a training objective implementing frequency-corrected G-V consistency for real-world LLMs. Our experimental results show that training with \FCPA{} substantially improves both G-V consistency and generator performance over prior methods, with gains of up to $+27$pp in Pearson correlation on IFEval and HumanEval, while preserving validator quality across all evaluated tasks.

## 综合总结
本文针对大模型生成与验证不一致（G-V gap）的问题，揭示了先验频率偏差是导致朴素一致性失效的根本原因。作者基于理性智能体模型提出了一种频率校正的G-V一致性公式，并据此设计了FCPA训练目标。实验表明，该方法在IFEval和HumanEval等基准上显著提升了生成器与验证器的一致性及生成性能（Pearson相关性提升高达27pp），且不损失验证能力，为大模型自我纠错与对齐提供了坚实的理论与实践基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文深入剖析了大模型中生成器与验证器不一致（G-V gap）的现象，创新性地指出朴素一致性失效的根源在于先验语料频率偏差。通过引入基于理性智能体模型的频率校正机制，提出了FCPA训练目标，理论推导严谨，实验验证充分（IFEval和HumanEval上Pearson相关性提升达27pp），展现了极高的研究深度与理论洞见。

### 实用性 (评分: 8.0/10)
该研究提出的FCPA训练目标可直接嵌入现有大模型的微调流程中，对解决LLM自我纠错、自我奖励机制中的'知行不一'问题具有极高的实践指导价值。方法不仅提升了生成质量，还保持了验证器的准确性，适用于需要高可靠性推理与指令遵循的工业级大模型训练场景。

### 社区活跃度 (评分: 8.5/10)
论文聚焦大模型自我一致性与对齐这一当前学术界与工业界的热点问题，时效性极强。作者团队包含知名NLP学者，来源权威可信。其提出的频率校正视角为解决LLM自我验证偏差提供了新范式，预计将在LLM对齐与自我博弈训练领域产生重要影响。

## 项目链接
https://arxiv.org/abs/2607.02668
