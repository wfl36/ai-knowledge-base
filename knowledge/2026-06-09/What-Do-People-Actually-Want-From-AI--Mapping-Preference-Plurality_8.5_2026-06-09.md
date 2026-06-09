# What Do People Actually Want From AI? Mapping Preference Plurality

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 对齐, RLHF, 价值观, 偏好, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06674v1 Announce Type: new Abstract: Large Language Models (LLMs) are often fine-tuned through Reinforcement Learning from Human Feedback (RLHF) to align with people's preferences and values. However, this method has known limitations: it aggregates conflicting preferences, often relies on unrepresentative samples, and uses only binary comparisons. Analysing 1,500 open-ended responses from the PRISM dataset across 75 countries, we examine what people actually want from AI systems and reveal concrete failures of current methods. We find that different people want different things: most values are requested by fewer than a quarter of respondents, with truthfulness the sole exception at 49%. Furthermore, the same words hide divergent meanings: when people describe what they mean by "truthfulness", they reveal distinct, potentially incompatible, epistemological bases, as some ask for sourced claims, some for expert opinions, and some even ask for unpopular views. Certain capabilities, namely how human-like a model behaves, and some features, like AI guardrails, are outright controversial, with some desiring them and others rejecting them. We additionally find that people often use contextual distinctions (what AI should do "by default" versus "if requested") that binary comparisons cannot capture. These findings expose fundamental problems in current alignment practices. When 49% request truthfulness but define it differently, this is unlikely to be captured by a single reward model. The persistence of high hallucination rates in well-funded models, despite users' clear demands for accuracy, suggests that current methods fail to identify actual preferences. This paper sheds light on the situated, contested, imperfect signals that are currently being flattened into universal preference models, a practice others have characterised as epistemic violence.

## 综合总结
该论文基于全球75国的实证数据，揭示了当前RLHF对齐范式的根本缺陷：单一奖励模型无法捕捉人们偏好的多元性、相同价值观词汇背后的语义分歧以及情境化需求。研究指出，将异质偏好压平为普遍模型不仅导致高幻觉率等技术问题，更可能构成“认知暴力”，为重构AI对齐范式提供了重要的实证依据与反思。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文基于75个国家1500份开放式回答的实证分析，深刻揭示了当前RLHF对齐范式的根本缺陷：偏好聚合掩盖了多元需求，相同价值观词汇（如“真实性”）背后存在不可兼容的认识论分歧，且二元比较无法捕捉情境化偏好。论证严谨，将技术缺陷上升到“认知暴力”的哲学高度，研究深度与洞见极佳。

### 实用性 (评分: 7.5/10)
虽然论文侧重于揭示问题而非提供现成解决方案，但其发现对AI对齐工程师和产品经理具有极高的实践指导意义。它明确指出了单一奖励模型的失效原因，为未来开发情境感知的对齐方法、多奖励模型架构以及更精细化的AI护栏设计提供了关键的避坑指南和方向指引。

### 社区活跃度 (评分: 9.0/10)
论文直击当前大模型发展中最核心的“对齐”痛点，话题极具时效性和争议性。基于全球代表性数据集（PRISM）的结论具有高度权威性，对当前由少数样本定义“普遍偏好”的行业现状构成了有力挑战，预计将在AI伦理和对齐研究社区引发广泛讨论与共鸣。

## 项目链接
https://arxiv.org/abs/2606.06674
