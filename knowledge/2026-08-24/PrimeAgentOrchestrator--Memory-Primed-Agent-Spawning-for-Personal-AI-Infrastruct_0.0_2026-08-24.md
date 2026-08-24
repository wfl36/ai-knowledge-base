# PrimeAgentOrchestrator: Memory-Primed Agent Spawning for Personal AI Infrastructure

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-24  
**来源：** rss  

## 项目描述
arXiv:2608.20342v1 Announce Type: new Abstract: Large language model (LLM) coding agents start each session with an empty context window, discarding accumulated knowledge from prior work. We present PrimeAgentOrchestrator (PAO), a system that spawns new instances of Claude Code -- Anthropic's terminal-based coding agent -- pre-loaded with relevant memories compiled from the user's existing personal databases. At spawn time, PAO queries two independently-operated memory backends in parallel (a PostgreSQL entity-observation database and a Cloudflare Worker semantic search index), fuses results using backend-specific retrieval strategies, and delivers the compiled briefing via filesystem injection that exploits the host agent's configuration auto-read behavior. PAO manages the full agent lifecycle including trust pre-seeding, readiness polling with error detection, and adaptive terminal text injection. We report on four months of regular deployment (December 2025 through March 2026) as an experience report, documenting three generations of context delivery mechanisms, the failure modes that motivated each redesign, and the engineering tradeoffs of bridging heterogeneous memory systems rather than building a unified one.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.20342
