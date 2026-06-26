# Investigating LLM's Problem Solving Capability -- a Study on Statics Questions

**评分：** 6.5  
**状态：** 正常  
**标签：** 大模型, 推理, 多模态, 评估, 工程教育  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26103v1 Announce Type: new Abstract: Large Language Models (LLMs) have rapidly influenced many aspects of society, particularly education, due to their demonstrated ability to complete assignments and examinations across a wide range of subjects. Although prior studies have examined the educational impact of LLMs, much of the existing work relies on public or open problem datasets and lacks topic-specific analysis. In engineering education, especially within mechanical engineering, systematic investigations of LLM performance on specific problem types remain limited. Instead of using traditional methods that directly ask textbook questions to an LLM tool, our study adopts a model distillation process to evaluate LLM capabilities in solving statics problems. By distilling ChatGPT, we extracted 25 text-only statics questions and further constructed two additional datasets by adding diagrams and modifying their numerical values. Experimental results show that while LLMs perform well on text-only statics problems, their accuracy decreases when diagrams are introduced and the problems require multi-step reasoning. Further analysis suggests that this performance drop is not primarily caused by limitations in image recognition, but rather by difficulties in multi-step reasoning and in consistently applying extracted visual information across successive solution stages.

## 综合总结
本研究针对LLM在机械工程静力学问题上的解题能力进行了评估。研究摒弃了传统的直接提问方式，通过蒸馏ChatGPT提取了25道纯文本静力学题目，并扩展出含图表和修改数值的数据集。实验表明，LLM在纯文本问题上表现良好，但引入图表和多步推理后准确率显著下降。深入分析发现，性能下降的主要原因不是图像识别缺陷，而是多步推理困难及在连续解题阶段一致应用视觉信息的能力不足。该研究为提升LLM在工程领域多模态复杂推理能力提供了重要启示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
该研究在方法论上有所创新，摒弃了直接使用教科书题目的传统方法，采用模型蒸馏提取静力学问题，并系统性地构建了纯文本、含图表和修改数值的三类数据集。研究深度较好，不仅指出了LLM在引入图表后准确率下降的现象，还进一步剖析了下降的根本原因并非图像识别能力不足，而是多步推理和跨步骤应用视觉信息的困难，论证较为严谨。

### 实用性 (评分: 6.5/10)
对工程教育领域的从业者和LLM应用开发者有明确的参考价值。研究揭示了当前LLM在处理多模态工程问题（尤其是需要多步推理的静力学问题）时的局限性，为开发更强大的工程辅助计算工具指明了优化方向（即需重点攻克多步推理和视觉信息一致性应用）。但研究样本量较小（仅25题蒸馏提取），适用范围有限。

### 社区活跃度 (评分: 6.0/10)
话题聚焦于LLM在垂直领域（机械工程/静力学）的解题能力评估，属于当前AI+教育的热点分支。虽然arXiv发布时间标为2026年（可能是年份笔误或虚拟时间），但研究基于ChatGPT蒸馏，具有较好的时效性和可信度。不过，该研究属于特定细分领域的评估性工作，影响范围相对局限，缺乏广泛的破圈影响力。

## 项目链接
https://arxiv.org/abs/2606.26103
