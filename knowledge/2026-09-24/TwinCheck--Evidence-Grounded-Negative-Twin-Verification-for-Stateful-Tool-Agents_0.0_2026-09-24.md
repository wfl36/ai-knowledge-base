# TwinCheck: Evidence-Grounded Negative-Twin Verification for Stateful Tool Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-24  
**来源：** rss  

## 项目描述
arXiv:2609.26911v1 Announce Type: new Abstract: A single locally plausible tool call can derail an otherwise successful agent trajectory. Suspicion alone does not justify intervention, because the replacement itself can introduce the very failure verification is meant to prevent. We introduce TwinCheck, an inference-time verification policy that considers replacement only when the trace satisfies an evidence condition tied to a trace-local failure hypothesis. It constructs a trace-grounded counterfactual alternative, a negative twin, and replaces the agent's proposal only if the twin passes structural checks and the pairwise verifier prefers it in both candidate orders. For paired evaluation, exact replay holds the agent's parsed responses and actions fixed until the first accepted replacement, separating intervention effects from resampling. In the primary analysis of 159 multi-turn BFCL V4 tasks with complete exact-replay pairs, the complete policy raises task success for GPT-5.6 Sol from 45.3% to 58.5% (95% task-bootstrap CI [8.2, 18.8]), with no observed success-to-failure regressions. Together, these findings recast execution-boundary repair as a constrained comparison, making the counterfactual action itself the object of verification.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.26911
