# Deontic Policies for Runtime Governance of Agentic AI Systems

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, AI安全, 治理, 道义逻辑, 知识表示, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19464v1 Announce Type: new Abstract: Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. This includes specifying what agents are permitted and prohibited from doing, what they areobliged to do after certain actions (e.g., notify the CISO), under what conditions a standing obligation may be waived, and which rules take precedence when policies conflict. This governance problem exceeds what current policy engines provide. Systems such as XACML, Rego, and Cedar address only the permit/prohibit subset of this governance structure. They do not provide obligation lifecycle management, meta-policy conflict resolution, dispensations that waive obligations in specific circumstances, and ontological reasoning over domain class hierarchies commonly found in applications such as healthcare, cybersecurity, or data privacy. We propose AgenticRei, which realizes key governance requirements such as obligations, dispensations, policy conflict resolutions, and reasoning over policies, as well as the basic permit/prohibit constraints. We use a deontic policy language built on the Rei framework, expressed as OWL (Web Ontology Language) and evaluated at runtime by a high-performance logic engine entirely outside the LLM. The same pipeline governs both tool invocations by the agent and agent-to-agent messages. We show through examples that deontic policies capture governance constraints around security and privacy that mostly cannot be expressed in current production engines. Our approach composes naturally with industry-standard frameworks like A2AS.

## 综合总结
本文针对LLM驱动的自主智能体在企业治理中面临的义务、豁免和策略冲突等复杂挑战，提出了基于道义逻辑的治理系统AgenticRei。该系统使用OWL表达基于Rei框架的策略，并在LLM外部的高性能逻辑引擎中运行时评估，突破了传统策略引擎仅支持允许/禁止的局限，实现了对工具调用和智能体间消息的全面治理，并与A2A等行业标准兼容。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深刻指出了当前LLM Agent治理仅停留在允许/禁止的二元约束层面的局限性，创新性地引入道义逻辑来处理义务、豁免及策略冲突等复杂企业治理需求。基于Rei框架和OWL本体语言构建AgenticRei系统，将治理逻辑完全外置于LLM并由高性能逻辑引擎执行，既保证了推理的严谨性，又避免了LLM自身的幻觉和越狱风险，理论深度与新颖性兼具。

### 实用性 (评分: 8.0/10)
提出的AgenticRei系统为解决企业级Agent合规与安全问题提供了极具参考价值的架构，其外置逻辑引擎的部署方式及与A2A标准的兼容性增强了工程可行性。但基于OWL和道义逻辑的实现方式对开发团队在知识表示与推理方面的门槛较高，短期内大规模普及存在一定挑战，更适合对合规要求极高的医疗、网络安全等特定场景先行落地。

### 社区活跃度 (评分: 9.0/10)
论文直击当前AI领域最紧迫的Agent安全与治理痛点，时效性极强。作者团队在语义网与知识表示领域具有深厚背景，且提出的治理方案与业界最新的A2A（Agent-to-Agent）标准天然契合，对学术界和工业界的Agent安全框架演进具有显著的引导和示范作用。

## 项目链接
https://arxiv.org/abs/2606.19464
