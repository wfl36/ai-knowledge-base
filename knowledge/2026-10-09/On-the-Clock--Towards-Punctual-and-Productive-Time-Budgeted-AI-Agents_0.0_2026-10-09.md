# On the Clock: Towards Punctual and Productive Time-Budgeted AI Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10833v1 Announce Type: new Abstract: We study whether small LLM agents can operate effectively under explicit wall-clock time budgets by both respecting the allocated runtime and using available time productively. We evaluate Qwen3.6-27B on five competitions from MLE-Bench Lite and Qwen3-4B on Zork I (Jericho), two agentic benchmarks where additional computational time can meaningfully improve performance. In the simplest setting, where the budget is stated only in the prompt, agents fail to translate the stated budget into controlled use of time. These failures arise from gaps in time awareness, since the harness provides no timing feedback, but also because they cannot reliably anticipate the duration of actions, and do not have a learned mapping from available time to an appropriate strategy. We investigate two complementary classes of interventions: harness-based mechanisms that expose timing information and enforce deadlines, and reinforcement learning with budget-aware rewards. Injecting timing information through the harness substantially improves budget adherence for Qwen3.6-27B without measurable loss in performance, while enforcement hooks tighten adherence further. RL with GRPO achieves near-perfect budget adherence on Zork I and generalizes to held-out budgets not seen during training, but does not improve task performance over the untrained harness on MLE-Bench. Once agents are made to respect the budget, they still fail to use additional time to improve task performance. RL-trained policies learn when to stop but often fill extra time with repeated actions, and GRPO training on multiple budgets tends to collapse toward the strategy learned for the shortest budget. Our results reveal a gap between time adherence and productive time allocation, which remains a central challenge for budget-conditioned agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10833
