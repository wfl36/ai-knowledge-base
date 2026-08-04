# Role Steering of Language Models for Social Simulations

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-04  
**来源：** rss  

## 项目描述
arXiv:2608.00023v1 Announce Type: new Abstract: Social simulations built from language-model agents need role-conditioned behavior that can be checked before agents are placed into a simulated population. We introduce an activation-steering screening workflow for role-conditioned agents: define a role profile, extract a role-specific direction, sweep four steering coefficients, evaluate role-profile alignment, and pass or flag each candidate configuration. On OLMo-3-7B-Instruct, we apply the workflow to a mixed 275-role inventory with 228 role-agnostic questions, GPT-4.1-mini prompted role references, and GPT-4.1-mini judges. Role-specific directions receive higher judged role-profile alignment than an assistant-axis directional control from prior persona-vector work, with mean overall scores of 63.2 versus 41.1 across the tested grid. They also preserve high lexical diversity, while the control drops sharply at larger coefficients. The role-level screen is the main practical output: most roles improve as steering increases, but 38 roles decline across all six measured dimensions, showing why simulation builders should choose coefficients per role rather than deploy a uniform high-strength setting. We make our code and evaluation artifacts available at https://anonymous.4open.science/r/anonymous-research-code-5F03/.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.00023
