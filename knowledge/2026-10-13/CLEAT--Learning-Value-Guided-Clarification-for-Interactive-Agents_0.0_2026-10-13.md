# CLEAT: Learning Value-Guided Clarification for Interactive Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-13  
**来源：** rss  

## 项目描述
arXiv:2610.12655v1 Announce Type: new Abstract: LLM agents can execute increasingly complex tasks, but effective assistance also requires aligning their actions with goals and constraints that users may leave unstated. We study this problem as interactive intent alignment through clarification. Yet clarification is useful only when the agent can turn the answer into better decisions. As training changes how the agent handles incomplete information and uses additional answers, the same clarification can become more or less useful. We introduce CLEAT (CLarification through valuE-guided Agent co-Training), a framework that co-trains a clarification-value controller and the task policy from shared interaction outcomes. We formulate residual query value to measure the task utility gained by asking rather than proceeding under the current policy, and estimate it through paired rollouts from the same interaction history. These paired returns train the controller to predict clarification value and the task policy to select useful questions and act on the answers. The controller guides subsequent rollout collection, while outcomes from the updated agent provide new value labels that allow clarification guidance to adapt as the agent learns. With Qwen3-4B, CLEAT achieves the highest mean score in all ten evaluation settings across four benchmarks. Gains over the strongest baseline reach 13.2 and 6.5 percentage points on UserGym Travel and IN3 underspecification judgment accuracy, respectively. Ablations show that co-training improves the task policy even when the controller is removed at inference, while adapting clarification guidance to the evolving policy yields further gains.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.12655
