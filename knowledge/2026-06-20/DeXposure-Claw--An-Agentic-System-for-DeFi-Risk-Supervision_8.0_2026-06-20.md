# DeXposure-Claw: An Agentic System for DeFi Risk Supervision

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, DeFi, 风险监管, 图神经网络, 时间序列, 论文  
**更新日期：** 2026-06-20  
**来源：** rss  

## 项目描述
arXiv:2606.19501v1 Announce Type: new Abstract: Decentralized finance exposes supervisors to fast-moving, networked credit risks. General-purpose LLM agents fit this setting poorly: they over-read weak evidence and recommend high-stakes interventions, while existing evaluations offer no regulator-aligned way to measure the resulting false alarms. We introduce DeXposure-Claw, a forecast-grounded agentic supervision system that routes LLM decisions through structured evidence: (1) DeXposure-FM, a graph time-series foundation model, forecasts future exposure networks; (2) deterministic monitors and stress scenarios then turn those forecasts into typed alerts, attribution signals, and scenario evidence; and (3) data-health and confidence gates constrain escalation before DeXposure-Claw emits auditable supervisory tickets with rationales. We further develop DeXposure-Bench, a six-axis evaluation harness, whose decision axis scores tickets against a regulator-aligned absolute-loss ground truth and an explicit false-intervention rate. Experiments on five years of weekly real data fully support our system. Code is at https://github.com/EVIEHub/DeXposure-Claw.

## 综合总结
本文提出DeXposure-Claw，一个面向DeFi风险监管的代理系统。针对通用LLM在监管场景下易产生高误报的缺陷，该系统通过图时间序列基础模型预测风险敞口，结合确定性监控与置信度门控机制，约束LLM仅基于强证据进行干预，并输出可审计的监管票据。同时，作者开发了六轴评估基准DeXposure-Bench，引入监管对齐的绝对损失和误报率指标。基于5年真实数据的实验验证了系统的有效性，为LLM在高风险金融场景的可靠应用提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对通用LLM在DeFi风险监管中易受弱证据干扰导致高误报的问题，创新性地提出了DeXposure-Claw系统。该系统将LLM决策与结构化证据路由结合，通过图时间序列基础模型（DeXposure-FM）预测风险敞口，并利用确定性监控和置信度门控约束LLM的升级干预，显著提升了决策的严谨性与可控性。同时提出的DeXposure-Bench评估基准，首次引入监管对齐的绝对损失和误报率指标，填补了该领域评估体系的空白。

### 实用性 (评分: 8.0/10)
对DeFi协议和金融监管机构具有极高的实践指导意义。系统通过门控机制有效降低了误报带来的不必要干预成本，输出的可审计监管票据符合实际合规需求。基于5年真实数据的验证和开源代码/评估基准，使得风控从业者可以直接参考或复用其架构进行DeFi风险监控系统的开发与评估。

### 社区活跃度 (评分: 7.5/10)
结合了当前两大热点——AI Agent与DeFi，切中了LLM在金融等高风险领域落地的核心痛点（幻觉与误报）。作者团队来自学术界，且开源了代码与基准测试，具备较高的权威性和社区传播潜力。虽然发布时间标注为2026年略显异常，但其探讨的议题极具时效性与现实意义。

## 项目链接
https://arxiv.org/abs/2606.19501
