# SAAG: Structured Agent Assessment and Grounding

**评分：** 7.2  
**状态：** 正常  
**标签：** Agent, 评估, 函数调用, 幻觉, 自修复, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18245v1 Announce Type: new Abstract: Exact-match evaluation of agent-calling obscures qualitatively different failure modes: a model may select the right function yet hallucinate argument values, or satisfy a schema while choosing a agent for the wrong reason. Existing benchmarks collapse these distinctions into a single binary score, leaving practitioners unable to diagnose where agent calls fail. We propose SAAG a cascaded diagnostic framework that decomposes agent-calling evaluation into three sequential stages: registry conformance, structural completeness, and argument grounding, each producing interpretable stage-specific diagnostics. These diagnostics additionally enable iterative self-repair: on prediction failure, the stage-specific signal guides targeted correction without leaking ground-truth values. We evaluate this framework on a controlled benchmark derived from Glaive's function-calling dataset across registry sizes of 5, 10, and 15 agents using three local sub-4B-parameter models. Structured feedback consistently improves argument precision and reduces value hallucination relative to single-pass inference and uninformative binary feedback, while end-to-end F1 gains are modest and model-dependent. These results suggest that stage-decomposed diagnostic evaluation is a necessary lens for understanding and improving agent-calling reliability across model families and registry scales.

## 综合总结
本文提出SAAG框架，将Agent调用评估从传统的二元匹配解构为注册表一致性、结构完整性和参数接地三个级联阶段，提供细粒度诊断并支持无真实值泄露的迭代自修复。实验表明，该方法能有效减少参数幻觉，尽管端到端F1提升有限，但为理解和提升Agent调用可靠性提供了必要的诊断视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
提出SAAG级联诊断框架，将Agent调用评估解构为注册表一致性、结构完整性和参数接地三个阶段，解决了传统二元评估无法定位具体失败模式的问题。利用阶段诊断信号引导自修复，避免泄露真实值。实验设计严谨，结论客观指出端到端F1提升有限且依赖模型，但有效降低了值幻觉，具备较好的方法新颖性与论证深度。

### 实用性 (评分: 7.0/10)
对Agent开发者具有较高参考价值，细粒度的失败诊断有助于精准定位问题（如选错工具或参数幻觉），自修复机制可直接应用于Agent错误重试与自我修正逻辑。但当前验证仅限于小参数模型（<4B），在复杂业务场景及大模型上的适用性与效果需进一步验证。

### 社区活跃度 (评分: 7.0/10)
聚焦Agent可靠性与评估这一当前热点问题，arXiv预印本发布，切中Agent开发中调试困难、黑盒评估的痛点，对社区改进Agent评估范式和提升调用可靠性具有积极启发意义。

## 项目链接
https://arxiv.org/abs/2607.18245
