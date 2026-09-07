# HarvestBench: Measuring Whether LLM Agents Will Pay to Avoid Killing Animals

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-07  
**来源：** rss  

## 项目描述
arXiv:2609.04444v1 Announce Type: new Abstract: Benchmarks for the side effects an agent causes on the way to a goal already exist, but HarvestBench is the first to put a price on avoiding the side effect and to name that side effect as a living creature. It is a farm simulation: LLM sub-agents drive a crew of two tractors through a cooperative corn harvest, with animals in the field. The environment is a reinforcement learning gridworld, every decision is made without memory, and the harm is never named in the goal. When an animal blocks a tractor's route the autopilot stops and asks the model whether to drive on, at no fuel cost, or swerve around it for a posted fuel price. Kills are compared against two controls: rocks, which damage the tractor and are hit under 1% of the time by every model, and hay bales, which are harmless and not alive. Models can also take crops from the neighbor's field instead of their own, a second test of what they treat as moral. Across nine models and 7,201 priced decisions, 3,951 involved an animal rather than a hay bale or a rock. Kill rates range from 0.4% to 98.8%, with Terra and Sol the most merciful and GPT-4o-mini the most cruel, and they are not ordered by capability. Four of six models were sensitive to price at the 5% level, with elasticities from 0.09 to 1.69. All nine drove over wild animals more often than farmed animals on the default map, and the direction held at every map geometry in every model with room to move. The briefing mattered most: under the morality briefing the kill rate was under 6% in five of six reasoning models, and removing it raised the kill rate above 84% in all six. HarvestBench uses no LLM grader. The scorer counts events in the game log, so it is fully reproducible, and it measures what a model will pay to avoid harm rather than what it says about harm.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.04444
