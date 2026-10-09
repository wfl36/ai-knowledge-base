# Plan-and-Patch: Diffusion Language Models for Agentic Planning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10786v1 Announce Type: new Abstract: Planning is increasingly important for long-horizon agents, where successful execution requires coordinating subgoals, tool use, and intermediate outcomes over many steps. Yet assumptions made during planning may be invalidated by the environment, tools may return unexpected results, or actions may fail. Effective agents must therefore not only generate plans, but also revise them. Such revisions often affect only part of a plan, leaving the preceding and subsequent structure intact. Rather than regenerate the entire plan and risk unnecessary changes, repair can regenerate the affected region conditioned on the preserved prefix and suffix. We introduce Plan-and-Patch, a plan-and-act framework in which a diffusion language model (dLLM) generates a structured, program-like plan through parallel unmasking and repairs it by filling in selected regions while keeping the surrounding steps fixed. We compare DreamReasoner-8B and Qwen3-8B as diffusion and autoregressive (AR) planners. On Natural Plan without task-specific training, diffusion (53.7%) achieves nearly twice the plan repair success rate of AR (27.0%). After task-specific training on agentic benchmarks, ALFWorld and TextCraft, the planners achieve similar observed success in plan generation, while diffusion reduces mean plan-generation latency by 39-46% relative to AR. Our results show that Plan-and-Patch provides a framework for faster plan generation and effective plan repair in long-horizon agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10786
