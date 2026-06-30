# Developmental Trajectories of Situation Modeling and Mentalizing in Transformer Language Models

**评分：** 7.2  
**状态：** 正常  
**标签：** 大模型, 心智理论, 认知科学, 评估, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28524v1 Announce Type: new Abstract: Recent work suggests that Large Language Models (LLMs) are sensitive to the belief states of agents described by text, as measured by the false belief task (FBT), yet persistent concerns of construct validity remain. We adopt a **developmental perspective**, tracing the pattern of mental state reasoning behavior -- and likely **preconditions** for this behavior -- across multiple training stages in the Olmo2 and Pythia language model suites. We find that above-chance FBT performance depends both on model size and sufficient training volume, emerges relatively late in pretraining, and is most improved by post-training interventions (SFT, DPO) in the condition most diagnostic of mentalizing (False Belief, Implicit). However, FBT performance is fragile: consistent with past work, the use of non-factive verbs (e.g., thinks) increases false belief attributions even in the True Belief condition. To contextualize these findings, we track the emergence of **situation modeling**: the ability to report on basic factual properties of a described scene. Situation modeling accuracy generally precedes and exceeds FBT accuracy, yet situational representations also prove surprisingly incoherent in certain respects: when asked about the knowledge states of the Antagonist agent -- who always knows the item's true location -- Olmo2 13b is consistently influenced both by the Target agent's knowledge state and the presence of non-factive verbs. Together, these results suggest that larger, sufficiently trained models build partially coherent situation models in a developmentally appropriate sequence, yet display surprising fragility -- highlighting the value of developmental and stress-testing approaches for evaluating LLM capabilities.

## 综合总结
本文从发展心理学视角追踪了Transformer语言模型在训练过程中情境建模与心智化能力的发展轨迹。研究发现，模型在错误信念任务（FBT）上的表现依赖于规模和训练量，且在后训练阶段提升显著，但这种能力十分脆弱，易受非事实动词等因素干扰。同时，情境建模能力虽先于心智化出现，但其表征仍存在不连贯性。这表明当前大模型仅构建了部分连贯的情境模型，凸显了采用发展性与压力测试方法评估LLM认知能力的重要性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
采用发展心理学视角，系统追踪了LLM（OLMo2和Pythia）在预训练及后训练阶段情境建模与心智化能力的涌现规律。研究不仅验证了模型规模与训练量对错误信念任务（FBT）表现的影响，还深入揭示了非事实动词导致的脆弱性及情境表征的不连贯性（如受其他代理知识状态干扰），论证严谨，对LLM认知能力的本质提供了深刻洞见。

### 实用性 (评分: 5.0/10)
研究属于基础认知与AI交叉领域，对工程实践的直接落地指导有限。但其揭示的LLM心智推理脆弱性，对设计高可靠性Agent交互系统、评估模型真实理解能力具有重要参考价值，提醒从业者在涉及复杂多角色状态推理的任务中需谨慎依赖当前LLM的输出。

### 社区活跃度 (评分: 8.0/10)
LLM是否具备心智理论是当前AI社区极具争议和关注的热点话题。该论文基于开源模型套件进行全训练周期追踪，方法扎实，结论对破除“LLM已具备人类级ToM”的过度乐观具有较高影响力，来源可信度高，话题时效性强。

## 项目链接
https://arxiv.org/abs/2606.28524
