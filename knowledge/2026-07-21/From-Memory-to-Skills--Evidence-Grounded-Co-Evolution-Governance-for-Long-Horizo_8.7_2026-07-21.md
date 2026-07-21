# From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 大模型, 记忆系统, 技能进化, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16621v1 Announce Type: new Abstract: Existing memory systems for long-horizon LLM agents often retrieve prior traces as passive context rather than converting them into executable capabilities. In this paper, we propose MSCE, a training-free Memory--Skill Co-Evolution framework that organizes agent experience into grounded step traces, reusable procedural policies, and declarative environmental cognition. MSCE crystallizes evidence-backed L2 policies with positive estimated gain into callable skills that retain evidence links, applicability boundaries, decision guidance, verification rules, and reliability estimates. It further introduces reflection-weighted value backfilling, which propagates sparse terminal feedback through dense local self-reflections to produce evidence-calibrated trace values for governing memory and skill evolution. Experiments on EvoAgentBench and LoCoMo demonstrate that MSCE significantly outperforms state-of-the-art skill-augmented and memory-driven agent baselines, exhibiting strong cross-domain transferability and lifelong-evolution capabilities.

## 综合总结
本文提出免训练的记忆-技能协同进化框架MSCE，解决了现有长周期LLM Agent记忆系统仅被动检索而无法转化为可执行能力的痛点。MSCE将经验组织为步骤轨迹、程序策略和环境认知，并将有正收益的策略结晶为带证据和边界的可调用技能；同时引入反思加权价值回填机制，利用局部自反思传播稀疏反馈以校准轨迹价值。实验表明MSCE显著优于现有基线，具备强大的跨域迁移与终身进化能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文针对长周期LLM Agent记忆系统仅作为被动上下文检索的痛点，创新性地提出免训练的记忆-技能协同进化框架（MSCE）。其技术深度体现在：1) 将经验从轨迹提升为可执行的L2策略技能，并保留证据链接、适用边界与可靠性估计；2) 引入反思加权价值回填机制，巧妙地通过密集的局部自反思传播稀疏终端反馈，实现证据校准的轨迹价值评估。实验在EvoAgentBench和LoCoMo上显著超越SOTA，论证严谨，具备高度新颖性。

### 实用性 (评分: 8.5/10)
框架设计为免训练（training-free），极大降低了工程部署与算力成本，对从业者具有极高的参考价值。将记忆转化为具备验证规则和适用边界的可调用技能，直接解决了Agent在复杂环境中重复犯错和能力无法沉淀的工程痛点。其跨域迁移和终身进化能力也表明该框架可广泛应用于自动化运维、长周期游戏、个人助理等需要长期交互的Agent场景。

### 社区活跃度 (评分: 8.5/10)
长周期Agent的记忆与进化是当前AI Agent领域的核心前沿热点，话题时效性极强。论文在权威基准EvoAgentBench和LoCoMo上验证了其有效性，来源可信度高。提出的从被动记忆到主动技能的范式转移，若能被开源社区广泛采纳，将对Agent基础设施的演进产生显著影响力。

## 项目链接
https://arxiv.org/abs/2607.16621
