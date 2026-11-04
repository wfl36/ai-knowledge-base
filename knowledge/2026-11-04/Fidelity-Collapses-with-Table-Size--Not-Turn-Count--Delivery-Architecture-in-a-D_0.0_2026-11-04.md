# Fidelity Collapses with Table Size, Not Turn Count: Delivery Architecture in a Deployed Tool-Using Agent

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-04  
**来源：** rss  

## 项目描述
arXiv:2611.00442v1 Announce Type: new Abstract: When a multi-turn agent delivers a tool's structured records into the model's context and re-emits them each turn, every turn can corrupt data the tool computed correctly. We measure this in a production award-travel agent: two architectures over identical frozen payloads, lineage-matched prompts and sampling, differing only in delivery architecture. SYNTHESIS feeds full record sets into the planner's context and answers follow-ups in-head; BYPASS, the deployed system, keeps records in session state, translates follow-ups into arguments for a deterministic filter, and delivers rows over a typed side channel. Across 24 dialogues (339 scored turns per condition), BYPASS scores 92.3% of turns fully correct, SYNTHESIS 45.7% (paired gap +46.6pp [+35.7, +57.1]). Varying delivered-table size by capture date, SYNTHESIS collapses from near-perfect at 10 rows or fewer to 8% or less beyond about 74 rows. On a content-controlled prefix ladder the collapse threshold orders by model capability, from under 10 rows (GPT-4o-mini) to about 198 or more (Gemini 2.5 Pro), while BYPASS stays size-flat for all four models. The collapse is expensive: beyond 100 rows, where almost no SYNTHESIS answer is correct, each correct one costs roughly 200x BYPASS's flat \$0.012. Practitioners converged on typed side-channel delivery for rendering, not correctness; we show it was, unknowingly, also a correctness decision.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.00442
