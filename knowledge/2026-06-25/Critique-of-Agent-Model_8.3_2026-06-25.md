# Critique of Agent Model

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 大模型, 自主系统, 世界模型, 论文, 观点  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.23991v1 Announce Type: new Abstract: What is an agent? What constitutes agency? With the rise of Large Language Model (LLM) systems marketed as ``coding agents'', ``AI co-scientists'', and other ``agentic" tools that promise to drive up productivity, and at the same time, ``existential" concerns such as AI escaping human control with destructive power under a speculative ``machine agency" against humans, it has become essential to clarify where automation ends and agency begins, both for building capable systems and for understanding whether and what to fear. Drawing on Descartes' grounding of agency in independent thought, and on portrayals of autonomous beings in science fiction, we survey the current landscape of AI agents, and analyze agent architectures along five dimensions: goal, identity, decision-making, self-regulation, and learning. Specifically, we argue that genuine agency requires these structures to be \emph{internalized within the system itself} rather than assembled through external scaffolding. This distinction between \emph{agentic} systems, whose competence resides in engineered workflows, and \emph{agentive} systems, whose capabilities (including social interaction) arise endogenously, defines the boundary between systems designed for prescribed tasks, and those capable of operating in the open world with true autonomy. Building on this analysis, we propose the Goal-Identity-Configurator (GIC) architecture for a general-purpose agent model, combining hierarchical goal decomposition, identity evolution, simulative reasoning grounded in a separately trained world model, learned self-regulation, and self-directed learning from both real and simulated experience. Furthermore, we share insight on the auditability, controllability, and safety of agentive systems that possess greater autonomy and ``agency", but remain under human oversight.

## 综合总结
本文深刻批判了当前AI Agent概念的模糊与滥用，借鉴哲学与科幻，区分了依赖外部工程的'agentic'系统与具备内生自主性的'agentive'系统，指出真正的agency必须内化。基于此，提出了包含目标、身份、配置器等维度的GIC架构作为通用自主智能体蓝图，并探讨了高自主性系统的可控性与安全性，为Agent领域的长远发展提供了重要的理论基石。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
从哲学（笛卡尔）与科幻视角深刻剖析了Agent的本质，创新性地提出了'agentic'（基于外部工程工作流）与'agentive'（内生自主能力）的关键区分，指出真正的agency必须内化于系统而非依赖外部脚手架。基于此提出GIC（Goal-Identity-Configurator）架构，融合层次化目标分解、身份演化、基于世界模型的模拟推理等五大维度，理论深度与前瞻性极强。

### 实用性 (评分: 6.5/10)
对Agent概念的澄清对行业纠正当前'工作流即Agent'的误区有重要指导意义，但所提出的GIC架构及'agentive'系统（如身份演化、内生自我调节与自导向学习）在当前技术条件下落地难度极大，更多作为长期研究蓝图，短期内的工程实践参考价值有限。

### 社区活跃度 (评分: 9.5/10)
话题紧扣当前AI Agent热潮与AI失控焦虑，对厘清自动化与自主性的边界具有高度时效性。作者Eric Xing为知名AI学者，权威性极高，该论文对Agent领域的概念正名、未来发展方向及安全治理标准的制定具有潜在的重大影响力。

## 项目链接
https://arxiv.org/abs/2606.23991
