# Agentic World Modeling for Agent Test-time Scaling without Environment Replica

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-03  
**来源：** rss  

## 项目描述
arXiv:2610.40927v1 Announce Type: new Abstract: Test-time scaling (TTS) improves large language model agents by sampling and selecting among multiple candidate trajectories, but common realizations assume that these trajectories can be executed in parallel. This assumption breaks in realistic deployments, where enterprise workspaces and cloud services are shared and persistent, costly or infeasible to replicate, and actions may introduce irreversible side effects or cross-trajectory interference. Existing generative world models avoid direct execution, but typically compress environment state into a single prompt, limiting their ability to reliably simulate transitions under partial observability. Instead, we introduce Agentic World Modeling (AWM), which reformulates next-observation prediction as a multi-turn evidence-acquisition task. For each hypothetical action, an agentic simulator adaptively queries the real environment through safe read-only interfaces, reasons over the returned evidence, and uses executable computation to construct the resulting observation without mutating shared state. Integrated with trajectory-level TTS, AWM enables parallel exploration over a single shared environment. Across $\tau$-bench, AppWorld, and OfficeBench, AWM outperforms a single-shot simulation baseline by 40.07% on average, and surpasses a trained world-model baseline by 12.36% on average. These results establish interactive, read-grounded simulation as a practical foundation for safe and scalable agentic test-time scaling in shared, non-resettable environments.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.40927
