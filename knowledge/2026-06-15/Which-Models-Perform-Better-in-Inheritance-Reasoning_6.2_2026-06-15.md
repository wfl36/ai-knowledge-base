# Which Models Perform Better in Inheritance Reasoning?

**评分：** 6.2  
**状态：** 正常  
**标签：** 大模型, 推理, 法律AI, 评估, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13751v1 Announce Type: new Abstract: This paper presents the participation of team PSL in the QIAS 2026 Shared Task on Arabic Islamic inheritance reasoning. The task evaluates the ability of large language models to solve inheritance cases that require legal interpretation, multi-step reasoning, and precise numerical computation. We compare \textit{commercial} and \textit{open-source} models under a unified prompting strategy to assess their effectiveness in structured legal reasoning with minimal task-specific adaptation. \\ Our results show a clear gap in reliability between the two model families. Commercial models demonstrate stronger performance in identifying eligible heirs, applying exclusion rules, and maintaining consistency across reasoning steps. In contrast, open-source models exhibit greater instability, particularly in cases involving dependent legal decisions and fractional share adjustments. The best performance is achieved by \textit{Gemini 2.5 Flash}, with an MRE of $0.989$.

## 综合总结
本文介绍了团队在QIAS 2026阿拉伯伊斯兰继承推理共享任务中的工作，通过统一提示策略评估了商业与开源大模型在法律解释、多步推理和数值计算上的表现。结果表明，商业模型（尤其是Gemini 2.5 Flash，MRE达0.989）在识别继承人、应用排斥规则及推理一致性上显著优于开源模型，后者在依赖性法律决策和分数份额调整上存在明显不稳定性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
论文在统一提示策略下对比了商业与开源大模型在阿拉伯伊斯兰继承法推理任务上的表现，揭示了商业模型在多步法律推理、排斥规则应用及推理一致性上的优势，以及开源模型在依赖性决策和分数调整上的不稳定性。但整体研究方法属于常规基准测试与对比分析，缺乏底层技术或方法论的创新，研究深度中等。

### 实用性 (评分: 5.5/10)
研究对法律AI领域的从业者具有参考价值，特别是在涉及复杂规则、多步逻辑和精确数值推理的场景下，为商业与开源模型的选择提供了实证依据。但由于任务领域（伊斯兰继承法）高度特定且规则复杂，其结论的直接适用范围较窄，通用落地性受限。

### 社区活跃度 (评分: 7.0/10)
文章发布于2026年，测试了Gemini 2.5 Flash等最新模型，时效性极强；作为QIAS 2026共享任务的参赛作品，具备一定的学术可信度与严谨性；但在更广泛的AI社区中，因领域较为小众（阿拉伯伊斯兰继承法），整体影响力和关注度相对有限。

## 项目链接
https://arxiv.org/abs/2606.13751
