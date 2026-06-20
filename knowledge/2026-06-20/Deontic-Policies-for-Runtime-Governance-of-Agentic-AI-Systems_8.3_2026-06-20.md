# Deontic Policies for Runtime Governance of Agentic AI Systems

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, AI安全, 智能体治理, 道义逻辑, 论文  
**更新日期：** 2026-06-20  
**来源：** rss  

## 项目描述
arXiv:2606.19464v1 Announce Type: new Abstract: Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. This includes specifying what agents are permitted and prohibited from doing, what they areobliged to do after certain actions (e.g., notify the CISO), under what conditions a standing obligation may be waived, and which rules take precedence when policies conflict. This governance problem exceeds what current policy engines provide. Systems such as XACML, Rego, and Cedar address only the permit/prohibit subset of this governance structure. They do not provide obligation lifecycle management, meta-policy conflict resolution, dispensations that waive obligations in specific circumstances, and ontological reasoning over domain class hierarchies commonly found in applications such as healthcare, cybersecurity, or data privacy. We propose AgenticRei, which realizes key governance requirements such as obligations, dispensations, policy conflict resolutions, and reasoning over policies, as well as the basic permit/prohibit constraints. We use a deontic policy language built on the Rei framework, expressed as OWL (Web Ontology Language) and evaluated at runtime by a high-performance logic engine entirely outside the LLM. The same pipeline governs both tool invocations by the agent and agent-to-agent messages. We show through examples that deontic policies capture governance constraints around security and privacy that mostly cannot be expressed in current production engines. Our approach composes naturally with industry-standard frameworks like A2AS.

## 综合总结
本文提出AgenticRei框架，利用道义策略语言解决LLM智能体运行时治理问题。该框架突破了传统策略引擎仅支持'允许/禁止'的限制，引入了义务、豁免、策略冲突解决及本体推理等高级治理能力，并通过OWL表达与LLM外部的高性能逻辑引擎进行运行时评估，同时支持工具调用和智能体间消息治理，可与A2A等标准框架无缝集成，为企业级AI安全与合规提供了全新的解决思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对LLM驱动的自主智能体在安全、隐私和合规方面的新挑战，创新性地引入了道义逻辑策略，超越了传统策略引擎（如XACML、Rego、Cedar）仅支持'允许/禁止'的局限。提出的AgenticRei框架基于Rei构建，使用OWL表达，并在LLM外部通过高性能逻辑引擎进行运行时评估，实现了义务生命周期管理、元策略冲突解决、豁免机制以及本体推理，技术深度与理论严谨性极高。

### 实用性 (评分: 7.5/10)
对企业级AI从业者具有极高的参考价值。随着智能体自主性增强，传统的认证和访问控制已不足以应对复杂的合规需求。AgenticRei提供了可落地的架构模式（在LLM外部进行治理），且能与A2A等行业标准框架自然组合。不过，道义逻辑和OWL的使用对常规工程团队有一定的学习门槛，落地实施需配套工具链支持。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击当前及未来Agentic AI系统治理的核心痛点。作者团队在语义网和智能体领域具有权威性，且论文契合A2A等智能体协作协议爆发的行业趋势，对AI安全与治理社区具有显著的前瞻引导影响力。

## 项目链接
https://arxiv.org/abs/2606.19464
