# Training Therapeutic Judges and Multi-Agent Systems for Human-Aligned Mental Health Support

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, Agent, 心理健康, 对齐, 评估, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30887v1 Announce Type: new Abstract: Large language models show promise for mental health support, yet therapeutic quality improves only when evaluation functions as an actionable control signal rather than a passive metric. We introduce a framework that formulates therapeutic response generation as a decision-refinement problem driven by multi-dimensional, human-aligned evaluation. In Stage I, we introduce TheraJudge, an open-source therapeutic evaluator trained via preference-based optimization on human-annotated data to produce reliable judgments across 7 psychological dimensions. In Stage II, we introduce TheraAgent, which operationalizes TheraJudge's evaluations through a coordinated refinement process with specialized Critic, Coach, and Therapist roles that translate evaluative signals into targeted response revisions. Empirically, TheraJudge achieves strong agreement with clinician ratings, with intraclass correlation coefficients (ICC = 0.87-0.95), surpassing supervised baselines and strong closed-source judges, particularly on critical dimensions such as Safety, Relevance, and Empathy. Acting on these evaluations, TheraAgent yields a +0.43 improvement in human-rated therapeutic quality (on a 5-point scale) under blind evaluation, with 96\% clinician inter-rater reliability. Low-quality responses ($\leq 3$) improve by +2.45 points with a 94\% recovery rate, demonstrating targeted correction of unsafe outputs. Overall, our results indicate that effective alignment of mental-health LLMs stems from acting on human-aligned evaluation, rather than relying solely on stronger generation. We release code at https://github.com/vis-nlp/TheraAlign.

## 综合总结
本文提出了一种基于人类对齐评估的心理健康支持大模型框架。该框架包含开源的治疗评估器TheraJudge（在7个心理维度上与临床医生评分高度一致，超越闭源模型）和多智能体系统TheraAgent（通过Critic、Coach、Therapist角色将评估信号转化为回复修改）。实验表明，该框架能显著提升治疗质量（盲评+0.43），对低质量/不安全回复的恢复率达94%。研究证明，在敏感领域，基于人类对齐评估的执行比单纯增强生成能力更有效。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出将治疗性回复生成视为由多维人类对齐评估驱动的决策细化问题，创新性地将评估从被动指标转化为主动控制信号。构建了TheraJudge（基于偏好优化的7维心理评估器）和TheraAgent（包含Critic、Coach、Therapist角色的多智能体协同细化系统），技术路径清晰且论证严谨，实验数据详实（ICC达0.87-0.95，低质量回复恢复率94%）。

### 实用性 (评分: 9.0/10)
对AI医疗和心理健康领域的从业者具有极高的落地指导价值。开源了代码和评估器，提供了一套可直接复用的“评估-反馈-修正”工程范式，尤其在纠正不安全输出（低质量回复提升+2.45分）方面表现卓越，适用于所有对安全性和同理心要求极高的敏感对话场景。

### 社区活跃度 (评分: 8.5/10)
紧扣大模型对齐、多智能体和AI心理健康等前沿热点。研究团队来自学术机构，开源代码极大增强了可信度与可复现性。其“评估即控制”的理念及在关键维度上超越闭源模型的结果，对当前依赖强生成能力的社区主流思路形成了有力补充，具有较高的行业话题性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.30887
