# Regimes: An Auditable, Held-Out-Gated Improvement Loop Demonstrated on LongMemEval with ActiveGraph

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, 自我改进, 事件溯源, 长上下文, 工程实践  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10241v1 Announce Type: new Abstract: Autonomous improvement loops are hard to trust because the improvement process is usually external scaffolding bolted onto the agent: failures go unlogged, diagnoses cannot be replayed, and promote-or-discard decisions land in a side database rather than the agent's own history. We show that an event-sourced agent runtime removes that friction and turns controlled improvement into a first-class workflow. When the agent's state is a deterministic projection of an append-only event log, failures are recorded, a run replays exactly from its log, candidate patches scope to typed pipeline seams, gates are auditable, and every promotion or discard is itself an event. We demonstrate this with Regimes, a loop on the ActiveGraph runtime that diagnoses failed evaluations, proposes a repair at a pipeline point, and promotes it only after static checks, sandbox execution, in-sample evaluation, and held-out validation. The loop is target-agnostic: the same control flow runs against different tasks through a common interface. On LongMemEval-S the dominant failure is not retrieval but reconciliation: the evidence is already in the assembled context, yet the reader answers incorrectly. Across five seeded held-out splits, Regimes discovers reader-prompt repairs that improve final held-out accuracy by +0.05 to +0.10 in four splits and +0.01 in one over-promotion split; two splits are individually significant (seed 5 unadjusted for its sequential promotion structure), and the pooled count is descriptive only, since the splits share one 500-question pool. The durable contributions are ActiveGraph as an auditable substrate that makes controlled improvement loops tractable, the held-out-gated loop it supports, the failure-regime taxonomy routing each failure to a pipeline location (whose marginal value over an unrouted baseline is the primary open question), and the prompt-as-discovery-probe hypothesis.

## 综合总结
本文提出了一种基于事件溯源的智能体运行时 ActiveGraph，将受控的自我改进过程转化为可审计、可重放的一等公民工作流，解决了传统 Agent 改进循环缺乏透明度的问题。在此基础上构建了 Regimes 循环，通过诊断失败、提出修复并经过静态检查、沙盒执行及严格的留出验证后才进行提升。在 LongMemEval-S 上的实验表明，该机制能有效发现并修复阅读器提示词，使留出集准确率提升 0.05-0.10，并揭示了长文本记忆中'协调'而非'检索'是主要失败模式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
本文在技术深度上表现出色，创新性地将事件溯源架构引入智能体运行时，将状态转化为确定性的追加日志投影，从而解决了自主改进循环中不可重放、不可审计的痛点。提出的 Regimes 循环通过严格的静态检查、沙盒执行和留出验证门控机制，显著提升了 Agent 自我改进的严谨性。实验在 LongMemEval-S 上揭示了'协调失败而非检索失败'是主要瓶颈，并实现了 0.05-0.10 的留出集准确率提升，论证严谨，但提升幅度的局限性和分类法边际价值的未确定性稍减其惊艳感。

### 实用性 (评分: 7.5/10)
对 AI 工程师和架构师具有很高的实践指导价值。事件溯源和可审计的 Agent 运行时设计为企业级高可靠 Agent 系统提供了可行的架构范式。留出门控机制和针对 pipeline 环节的修复策略，可直接应用于 Prompt 优化和 RAG 系统的调试中。不过，ActiveGraph 运行时的迁移成本和'目标不可知'接口的通用性在实际落地时仍需针对具体业务场景进行适配。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，Agent 的自我改进与可审计性是当前 AI Agent 基础设施领域的核心痛点与前沿方向。作者 Yohei Nakajima 作为 BabyAGI 的创作者，在 Agent 社区具有极高的影响力和号召力，文章来源为 arXiv，具备良好的权威性与可信度，预计将在 AI 工程圈引发对 Agent 可靠性架构的广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.10241
