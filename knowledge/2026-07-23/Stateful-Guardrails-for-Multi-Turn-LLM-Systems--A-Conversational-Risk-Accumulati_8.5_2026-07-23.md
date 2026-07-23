# Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 安全, 多轮对话, Agent, 基准测试, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19361v1 Announce Type: new Abstract: Most safety guardrails for large language models (LLMs) evaluate each prompt-response pair in isolation, which misses failures that arise only over a dialogue as benign turns compose into harm. We term this Conversational Risk Accumulation (CRA): gradual intent drift, fragmented assembly of prohibited instructions, and sensitivity build-up from repeated disclosures. We propose a session-layer CRA Framework that tracks three trajectory signals: semantic drift from a session anchor, a sensitivity-weighted information accumulation graph over extracted entities, and a compliance-gradient signal capturing increasing willingness to comply. For scoring, we provide (i) an unsupervised convex fusion for attribution and ablations, and (ii) CRA-Net DA, a compact learned trajectory model trained with family-adversarial objectives to reduce length and topic-coverage confounds. To benchmark CRA, we release CRA-Bench v0.1 (1,200 eight-turn sessions across three threat families with topic-matched benign twins), CRA-Bench v0.2 (LLM-paraphrased variants to reduce template artifacts), and an extended 5-family set (2,000 sessions adding persona priming and context stuffing). We introduce a trajectory-native evaluation protocol with session-level splits, mixed-set threshold calibration, Trajectory AUROC, turns-to-detection, calibrated false-positive metrics, bootstrap confidence intervals, leave-one-family-out diagnostic stress tests, and synthetic-to-human transfer checks. Claims focus on within-distribution session scoring on CRA-Bench and human-transfer subsets.

## 综合总结
本文针对大模型多轮对话中因良性意图组合而导致的安全失效问题，提出了会话风险累积（CRA）框架。该框架突破了传统单轮孤立检测的局限，通过追踪语义漂移、敏感性加权信息累积图和合规梯度三个轨迹信号来评估多轮对话风险。同时，作者提出了无监督凸融合和紧凑的CRA-Net DA模型进行风险评分，并发布了多版本CRA-Bench基准及严谨的轨迹原生评估协议，为多轮对话安全防护提供了重要的理论、模型与评测基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文精准识别了当前LLM安全领域单轮孤立评估的盲区，创新性地提出了会话风险累积（CRA）概念。在方法论上，构建了包含语义漂移、信息累积图和合规梯度三个维度的轨迹信号体系，并提供了无监督凸融合与抗干扰的CRA-Net DA模型两种评分路径。评估体系极其严谨，引入了轨迹原生评估、留一族诊断压力测试及合成到人类迁移检查，研究深度与论证严谨度极高。

### 实用性 (评分: 8.5/10)
多轮对话安全是当前Agent和复杂对话系统落地的核心痛点。该框架提出的会话层状态追踪机制可直接作为中间件集成至现有LLM应用架构中，CRA-Net DA作为紧凑模型也具备工程部署潜力。同时，发布的CRA-Bench及评估协议为行业提供了标准化的多轮安全测试工具。但在超长上下文场景下，信息累积图的实时计算可能面临性能挑战，需进一步工程优化。

### 社区活跃度 (评分: 8.0/10)
多轮对话越狱是当前AI安全社区高度关注的前沿话题，该研究具有极强的时效性。作者不仅开源了多版本、大规模的CRA-Bench基准，且评估设计考虑了主题匹配的良性对照和模板伪影消除，极大提升了基准的可信度与权威性，对推动多轮对话安全评估标准化具有重要影响力。

## 项目链接
https://arxiv.org/abs/2607.19361
