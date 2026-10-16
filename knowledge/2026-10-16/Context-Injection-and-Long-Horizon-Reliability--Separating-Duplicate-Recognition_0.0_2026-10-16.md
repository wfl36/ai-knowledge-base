# Context Injection and Long-Horizon Reliability: Separating Duplicate Recognition, Local Processing, and Counter Tracking

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20633v1 Announce Type: new Abstract: Long-horizon failures of language models are usually measured as end-task success or as a horizon length. We instead score, step by step, three components of a 400-step ledger task in which every step is easy in isolation and the model's own answers are re-injected into its context: recognising a record already seen 5 to 300 steps earlier, processing the current record locally, and writing a counter incremented at every step. On Qwen3-8B (non-thinking, 20 seeds, replicated on a second machine and backend), with every step scored component by component, two results hold. First, duplicate-recognition errors rise late in the episode -- from 0.0019 to 0.011 per step at risk across step 200 -- while the counter makes no error in 8,000 steps and local processing is descriptively stable; the rise combines long-distance recall errors and rising false alarms. Second, a block of irrelevant content inserted before each step makes the counter fail in 20 of 20 seeds on each machine, against none without it, while its effect on local processing is much smaller and not distinguishable from none. Three pre-registered follow-ups probe the counter. Its value depends on the value present in the response history: a corrupted value persists without correction in every seed, and an exact external reminder, repeated before each message, re-aligns it within one to two steps. Under the irrelevant block, no counter error was observed when an exact compact reminder of the state, supplied externally by an oracle, preceded each message (0 of 20 seeds with an error, against 15 without it), and this reminder outperformed a length-matched neutral text; whether a single reminder suffices was not conclusive, and the absence of damage to the other components was not established. An aggregate or exclusive error classification can hide the difference we report.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20633
