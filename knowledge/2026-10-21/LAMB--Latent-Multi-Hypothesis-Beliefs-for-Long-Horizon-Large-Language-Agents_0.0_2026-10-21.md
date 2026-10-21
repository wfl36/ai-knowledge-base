# LAMB: Latent Multi-Hypothesis Beliefs for Long-Horizon Large Language Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26955v1 Announce Type: new Abstract: Long-horizon language agents require compact memories that retain interaction evidence while preserving competing hypotheses about unobserved states. Although effective, many belief-state methods encode memory in discrete natural language, where repeated compression can omit evidence or prematurely discard plausible alternatives. We introduce LAMB, a recurrent framework for latent multi-hypothesis beliefs. A Common--Delta factorization combines a shared Common state for interaction evidence with weighted Delta components for competing hypotheses. Relative evidence from action-outcome predictions guides recurrent hypothesis updates without generating textual memory. A context-conditioned readout exposes hypotheses separately to the policy through a fixed-token belief prefix in the default configuration. The belief modules and policy are jointly trained using action imitation and auxiliary state, outcome, and observation-discrimination objectives. Across ALFWorld, BabyAI, ScienceWorld, and Crafter, LAMB matches or outperforms PABU, improving ALFWorld SR@30 and ScienceWorld success by 6.0 and 22.0 percentage points, respectively, and Crafter achievement progress by 26.37 points. On ALFWorld, it also reduces the redundant-action rate by 17.70 percentage points. These results support latent multi-hypothesis beliefs as compact memory for effective long-horizon decision making

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26955
