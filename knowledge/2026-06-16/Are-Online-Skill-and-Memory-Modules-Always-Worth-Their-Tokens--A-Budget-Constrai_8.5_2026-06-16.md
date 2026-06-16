# Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, Web Agent, 推理优化, 评估基准, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15017v1 Announce Type: new Abstract: Online web agents often augment a base actor with memory, workflow, or skill modules. These modules can improve performance, but they also consume test-time tokens, a cost rarely reported alongside the actor's inference cost. We study online augmentation, where this overhead is paid on every task, and re-evaluate its benefits under a fixed total inference budget. We compare AWM, ASI, and ReasoningBank with a token-matched vanilla baseline that uses the same budget for additional actor steps. Across three WebArena domains and three models, Gemini 3 Flash, GPT-5.4-mini, and Qwen 3.6-27B, the vanilla baseline matches or surpasses all three augmentation methods in aggregate success rate while often using fewer total tokens. We observe a similar trend on WorkArena-L1 with Qwen 3.6-27B, indicating that the effect extends to enterprise knowledge-work tasks. Our results suggest that skills and workflow memory can be useful in specific domains, but their apparent gains often vanish against a budget-matched actor. We further show that run-to-run variance materially affects outcomes and should be reported as a core evaluation criterion for online web agents.

## 综合总结
本文在固定推理预算下重新评估了Web Agent中记忆、技能等增强模块的价值。实验表明，在同等Token预算下，将资源用于基础模型的多步推理（Vanilla baseline）比使用AWM、ASI等增强方法效果更好或相当，且消耗更少Token。研究揭示了增强模块的‘隐性成本’，并强调运行间方差应作为Agent评估的核心指标，对Agent架构的成本效益优化具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究视角新颖且务实，挑战了当前Web Agent领域盲目增加记忆、技能或工作流模块以追求SOTA的常规做法。论文引入了‘预算约束’视角，将增强模块的额外Token开销换算为基础模型多步推理的成本，发现在同等预算下，简单的Vanilla基线模型往往表现更优。此外，论文强调了运行间方差对评估结果的实质性影响，对现有Agent评估范式的严谨性提出了有力补充，论证扎实，跨多个前沿模型和基准测试。

### 实用性 (评分: 9.0/10)
对AI Agent开发者和工程师具有极高的实践指导价值。在实际业务部署中，推理成本是核心考量因素。本文直接指出：与其将Token预算消耗在复杂的记忆或技能检索模块上，不如将同等预算留给基础模型进行更多步的推理。这一结论能够直接指导Agent的架构设计、模块取舍和成本效益优化，避免过度工程化。

### 社区活跃度 (评分: 8.0/10)
话题时效性极强，切中了当前Agent开发中‘性能提升与推理成本失衡’的痛点。虽然发布时间标为未来（可能为设定或笔误），且涉及虚构的下一代模型（如GPT-5.4-mini, Qwen 3.6-27B），但其探讨的Token经济学和评估方差问题正是当前学术界和工业界高度关注的焦点，具有很高的启发性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.15017
