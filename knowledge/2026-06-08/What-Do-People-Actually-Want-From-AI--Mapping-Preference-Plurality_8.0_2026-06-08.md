# What Do People Actually Want From AI? Mapping Preference Plurality

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 对齐, RLHF, 偏好学习, 论文, 实证研究  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06674v1 Announce Type: new Abstract: Large Language Models (LLMs) are often fine-tuned through Reinforcement Learning from Human Feedback (RLHF) to align with people's preferences and values. However, this method has known limitations: it aggregates conflicting preferences, often relies on unrepresentative samples, and uses only binary comparisons. Analysing 1,500 open-ended responses from the PRISM dataset across 75 countries, we examine what people actually want from AI systems and reveal concrete failures of current methods. We find that different people want different things: most values are requested by fewer than a quarter of respondents, with truthfulness the sole exception at 49%. Furthermore, the same words hide divergent meanings: when people describe what they mean by "truthfulness", they reveal distinct, potentially incompatible, epistemological bases, as some ask for sourced claims, some for expert opinions, and some even ask for unpopular views. Certain capabilities, namely how human-like a model behaves, and some features, like AI guardrails, are outright controversial, with some desiring them and others rejecting them. We additionally find that people often use contextual distinctions (what AI should do "by default" versus "if requested") that binary comparisons cannot capture. These findings expose fundamental problems in current alignment practices. When 49% request truthfulness but define it differently, this is unlikely to be captured by a single reward model. The persistence of high hallucination rates in well-funded models, despite users' clear demands for accuracy, suggests that current methods fail to identify actual preferences. This paper sheds light on the situated, contested, imperfect signals that are currently being flattened into universal preference models, a practice others have characterised as epistemic violence.

## 综合总结
本论文基于PRISM数据集的跨国家实证分析，揭示了当前RLHF对齐范式的根本缺陷：人们的需求存在高度多样性，同一价值观（如真实性）背后隐藏着不兼容的认识论基础，且偏好具有强烈的情境依赖性。研究指出，将复杂、争议性的偏好信号扁平化为单一奖励模型不仅无法捕捉真实诉求，甚至可能构成'认知暴力'，亟需向多元化、情境化的对齐范式转变。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文直击当前大模型对齐技术（RLHF）的核心痛点，通过实证分析深刻揭示了偏好同质化假设的缺陷。研究不仅指出了偏好的多样性（仅真实性超半数，其余均低于25%），更深入剖析了同一概念（如真实性）背后的认识论分歧，以及情境依赖（默认vs请求）对二元比较机制的挑战，论证严谨，对现有对齐范式构成了强有力的理论冲击。

### 实用性 (评分: 7.0/10)
虽然论文未提供直接替代RLHF的现成工程方案，但对AI对齐从业者具有极高的警示和启发价值。它明确指出了单一奖励模型的失效场景，为未来对齐技术的发展指明了方向，如情境化对齐、多奖励模型架构、个性化RLHF以及细粒度的偏好标注，有助于避免资源浪费在无效的扁平化对齐上。

### 社区活跃度 (评分: 8.5/10)
RLHF的局限性及AI价值观对齐是当前大模型领域的核心议题，该研究基于75国1500份真实反馈，数据来源权威且具全球代表性。论文指出的'认知暴力'（epistemic violence）等观点极具话题性，极易在AI伦理、技术社区及社会学界引发广泛讨论，时效性与影响力兼具。

## 项目链接
https://arxiv.org/abs/2606.06674
