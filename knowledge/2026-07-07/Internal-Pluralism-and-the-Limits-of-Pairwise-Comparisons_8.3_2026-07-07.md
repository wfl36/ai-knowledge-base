# Internal Pluralism and the Limits of Pairwise Comparisons

**评分：** 8.3  
**状态：** 正常  
**标签：** AI对齐, 偏好学习, RLHF, 决策规则, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02672v1 Announce Type: new Abstract: Local pairwise comparisons are a standard tool for learning how people want decision rules to work, e.g., in participatory design or alignment. However, their use builds in two strong assumptions: that local comparisons are sufficient evidence about how a person wants an automated decision rule to behave, and that people can always answer those comparisons decisively. We investigate how these assumptions may be compromised under internal pluralism: the idea that an individual evaluates decision rules according to multiple authoritative priorities about how the rule should behave. We provide a formal model of such pluralistic preferences over decision rules, which then lets us identify two distinct failures of forced local pairwise comparison data. First, priorities such as proportionality, egalitarianism, and equal treatment are inherently global: what they imply in one case can depend on what happens elsewhere, so local comparisons may fail to capture them. Second, even when priorities are representable locally, tension between strongly-held priorities can generate internal conflict, producing potentially costly behavioral distortions when comparisons are forced. We then use our model to investigate the alternative -- allowing people to report indecision -- and our findings suggest that doing so can considerably reduce the number of queries needed to learn preferences accurately. We conclude by describing how our model points toward preference-learning methods that elicit these priorities directly, yielding more faithful and interpretable accounts of what people value.

## 综合总结
本文挑战了AI对齐和参与式设计中广泛使用的局部成对比较方法的基础假设，提出了'内部多元主义'概念，指出个体评估决策规则时依赖多重权威优先级。通过形式化模型，作者揭示了强制成对比较的两大缺陷：一是比例性、平等性等全局优先级无法被局部比较捕捉；二是优先级间的冲突会导致内部矛盾和行为扭曲。研究进一步表明，允许个体表达'未决定'不仅能减少行为扭曲，还能显著降低准确学习偏好所需的查询次数，并倡导开发直接引出优先级的偏好学习方法，以获得更忠实、可解释的价值表征。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文具有极高的理论深度与洞见性，直接挑战了当前AI对齐与偏好学习（如RLHF）中广泛使用的局部成对比较方法的底层假设。作者创新性地提出了'内部多元主义'的形式化模型，严谨地论证了强制成对比较在两种情况下的失效：一是比例性、平等主义等全局优先级无法被局部比较捕捉；二是多重优先级间的张力会导致内部冲突与行为扭曲。该分析直击当前偏好学习范式的方法论软肋，论证严密且具有范式转移的启发性。

### 实用性 (评分: 7.5/10)
对AI从业者（尤其是对齐数据标注与RLHF流程设计者）具有重要参考价值。论文证明了允许标注者报告'未决定'能显著减少查询次数并提升偏好准确性，这为改进现有偏好数据收集流程提供了直接且低成本的实践指导。然而，由于论文侧重于形式化模型与理论推演，关于如何具体设计'直接引出优先级'的交互界面与算法机制，仍需工程实践层面的进一步转化与探索。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，AI对齐与大模型偏好学习是当前AI领域的核心痛点，对RLHF局限性的反思正成为社区热点。作为arXiv上的最新学术论文，来源具有较高权威性与可信度。其指出的成对比较缺陷触及了当前主流对齐范式的根本，有望在AI安全与对齐社区引发广泛讨论与后续研究。

## 项目链接
https://arxiv.org/abs/2607.02672
