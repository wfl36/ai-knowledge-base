# ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch

**评分：** 9.0  
**状态：** 正常  
**标签：** 大模型, Agent, 调度系统, 特征工程, DPO, 论文, 工程实践  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18803v1 Announce Type: new Abstract: Bringing Large Language Models (LLMs) into industrial ride-hailing dispatch as semantic feature extractors over platform-scale behavioral logs is a compelling but under-explored data systems problem. Production matching pipelines remain dominated by structured numerical features, yet decisive behavioral signals (e.g., a driver's habitual aversion to certain regions) are inherently contextual and naturally expressible as LLM-generated user profiles. However, scaling such profiling to a live, millisecond-latency dispatcher faces three intertwined constraints rarely addressed together: on a platform with millions of daily orders, logs exceed any LLM's context window by orders of magnitude; most users are long-tail, with too few interactions for per-user profiling; and surface-fluent profiles do not necessarily improve downstream prediction utility. We present ProfiLLM, an agentic LLM data pipeline that operationalizes utility-aligned user profiling for production matching systems through two modules. (1) Tool-Augmented Global Knowledge Mining equips an LLM agent with 27 analytical tools to mine platform-scale data, producing reusable global knowledge, adaptive user clustering rules, and region-level supply-demand priors. (2) Utility-Aligned Profile Exploration generates multiple candidate profiles per cluster, evaluates them via a lightweight downstream utility proxy, iteratively refines the best candidates and constructs preference pairs for DPO fine-tuning. Deployed on DiDi's production dispatcher, ProfiLLM achieves up to +6.14% relative AUC improvement in outcome prediction, up to +4.35% GMV gain in dispatching simulation, and consistent improvements in a 14-day online A/B test including +0.47% GMV, +0.33% Completion Rate, and -0.82% Cancel-Before-Accept rate.

## 综合总结
本文提出ProfiLLM，解决LLM在网约车调度系统中落地时面临的日志超长、长尾用户稀疏和画像效用不对齐三大挑战。通过构建包含工具增强全局知识挖掘和效用对齐画像探索的Agentic数据管道，结合DPO微调，使LLM生成的语义画像能有效提升下游预测效用。该方法在滴滴生产系统部署，线上A/B测试实现GMV和完单率等核心指标的显著提升，为LLM改造传统工业调度系统提供了极具价值的实践范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文精准识别了LLM在工业级调度系统落地时的三大痛点：超长日志超出上下文、长尾用户交互稀疏、表面流畅的画像未必提升下游效用。提出的ProfiLLM通过工具增强的全局知识挖掘和效用对齐的画像探索（结合DPO微调）两个模块，巧妙地绕过了上下文限制和长尾稀疏问题，特别是引入轻量级效用代理来闭环优化LLM生成画像的下游价值，方法设计严谨且具有深度创新。

### 实用性 (评分: 9.5/10)
极高的落地价值。论文不仅在滴滴的生产调度系统中进行了实际部署，还给出了完整的离线评估与14天线上A/B测试结果（GMV +0.47%，完单率 +0.33%等）。其针对毫秒级延迟、长尾用户和特征工程的方法论，可直接复用或借鉴至外卖、打车、电商等其他具有海量行为日志和供需匹配特征的工业级推荐与调度系统中。

### 社区活跃度 (评分: 9.0/10)
LLM改造传统搜推广/调度系统是当前业界高度关注的热点。本文作者来自滴滴，基于真实千万级订单的生产环境进行验证，来源权威且可信度极高。线上业务指标的显著提升对工业界社区具有强烈的吸引力和示范效应，有望引发传统匹配系统向语义化、Agent化演进的新一轮实践热潮。

## 项目链接
https://arxiv.org/abs/2606.18803
