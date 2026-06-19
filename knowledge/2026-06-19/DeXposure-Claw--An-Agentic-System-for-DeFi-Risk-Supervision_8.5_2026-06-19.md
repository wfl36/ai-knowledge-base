# DeXposure-Claw: An Agentic System for DeFi Risk Supervision

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, DeFi, 风险监管, 图时间序列, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19501v1 Announce Type: new Abstract: Decentralized finance exposes supervisors to fast-moving, networked credit risks. General-purpose LLM agents fit this setting poorly: they over-read weak evidence and recommend high-stakes interventions, while existing evaluations offer no regulator-aligned way to measure the resulting false alarms. We introduce DeXposure-Claw, a forecast-grounded agentic supervision system that routes LLM decisions through structured evidence: (1) DeXposure-FM, a graph time-series foundation model, forecasts future exposure networks; (2) deterministic monitors and stress scenarios then turn those forecasts into typed alerts, attribution signals, and scenario evidence; and (3) data-health and confidence gates constrain escalation before DeXposure-Claw emits auditable supervisory tickets with rationales. We further develop DeXposure-Bench, a six-axis evaluation harness, whose decision axis scores tickets against a regulator-aligned absolute-loss ground truth and an explicit false-intervention rate. Experiments on five years of weekly real data fully support our system. Code is at https://github.com/EVIEHub/DeXposure-Claw.

## 综合总结
本文提出了DeXposure-Claw，一种面向DeFi风险监管的智能体系统。针对LLM在金融监管中易产生误报的问题，该系统通过图时间序列基础模型预测风险暴露网络，结合确定性监控与置信度门控机制，约束LLM决策并生成可审计的监管工单。同时，论文提出了面向监管的评估基准DeXposure-Bench，引入误干预率等指标。基于五年真实数据的实验验证了系统的有效性，为高风险领域的AI监管落地提供了极具参考价值的范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文针对通用大模型在DeFi监管中易过度解读弱证据并导致误报的问题，提出了基于预测的智能体系统DeXposure-Claw。其技术创新点在于将图时间序列基础模型（DeXposure-FM）与确定性监控、压力测试场景及置信度门控机制相结合，约束LLM的决策升级，并创新性地提出了面向监管的六轴评估框架DeXposure-Bench，引入了绝对损失真值和误干预率指标，论证严谨，研究深度较高。

### 实用性 (评分: 8.5/10)
该系统对DeFi领域的风险监管具有极高的落地价值。通过生成可审计的监管工单及归因信号，直接契合了金融监管的实际需求。其开源代码和基于五年真实数据的验证进一步提升了工程实践的参考价值。此外，将LLM与确定性规则结合以约束高风险决策的思路，对其他强监管行业（如传统金融、医疗）也具有广泛的借鉴意义。

### 社区活跃度 (评分: 8.0/10)
DeFi风险监管与AI Agent是当前学术界与工业界高度关注的前沿交叉领域，话题时效性极强。论文来源于arXiv，且基于五年真实周度数据进行实验验证，来源与结论具有较高可信度。该工作为去中心化金融的自动化监管提供了新范式，有望在金融科技与AI交叉社区产生显著影响力。

## 项目链接
https://arxiv.org/abs/2606.19501
