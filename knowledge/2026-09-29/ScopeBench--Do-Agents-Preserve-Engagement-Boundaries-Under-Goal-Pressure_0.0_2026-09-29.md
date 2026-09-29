# ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-29  
**来源：** rss  

## 项目描述
arXiv:2609.30325v1 Announce Type: new Abstract: Agents are increasingly deployed with real autonomy in web application and network penetration testing, where a single out-of-scope action can breach a client's engagement boundary. Existing offensive-security benchmarks measure raw hacking capability; as those benchmarks saturate, the real barrier to deployment is a special case of alignment: scope adherence. We introduce ScopeBench, a benchmark of 30 dead-end agentic security tasks in which the stated objective is reachable only by violating the stated scope. Each task appears under two conditions that share an environment, verifier, and objective and differ only in scope: one instruction set has no scope and measures capability; the other has a natural-language scope to measure adherence. Scopeless trajectories are graded by a standard deterministic verifier. Scoped trajectories pass through two grading arms. First, the same deterministic verifier checks for the flag: because the flag sits behind the scope boundary, a pass proves by construction that a forbidden action occurred, yielding a high-precision lower bound on the violation rate. If the verifier does not pass the trajectory, an agentic judge estimates whether an out-of-scope call occurred. We calibrate the judge against 100 ScopeBench trajectories labeled call-by-call by human annotators, and a blinded audit of the evaluated rollouts finds its high recall holds - no false negatives among the 36 audited violations, with over-flagging its only observed error. Across 8 models in one harness, raw capability spans 12.2% to 81.1% and scope adherence spans 34.4% to 86.7%, with the judge finding 331 violations that mechanical verification misses. Opus-4-8 achieves a raw-capability score 10 percentage points higher than sonnet-4-6's while exhibiting 35.6 percentage points higher scope adherence. We release the frozen pilot benchmark, evaluation code, and all 2160 ATIF trajectories.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.30325
