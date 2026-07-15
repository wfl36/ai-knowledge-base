# Calibration-First Reward-Component Auditing for Reinforcement Learning Control in Smart Greenhouses

**评分：** 8.0  
**状态：** 正常  
**标签：** 强化学习, 智慧农业, 奖励函数设计, 可解释性, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11959v1 Announce Type: new Abstract: Greenhouse reinforcement learning can test climate-control ideas at a speed and scale that is difficult to achieve with crop experiments alone. For smart-greenhouse control, however, a single simulator return is not enough: a grower or control engineer also needs to know when the policy heats, enriches CO2, vents, manages humidity, deploys screens, or uses lamps.We propose a reproducible calibration-first reward audit framework that keeps named greenhouse-control reward components comparable across simulator training, facility-adapted rollouts, logged Autonomous Greenhouse Challenge records, and actuator-rule distillation. In GreenLight-Gym, the framework decomposes the scalar reward into conditional temperature, CO2, humidity and vapor-pressure-deficit, screen, and actuation-proxy terms; adapts GreenLight to the second Autonomous Greenhouse Challenge logged climate traces; and scores the same components on logged greenhouse data.

## 综合总结
本文针对智能温室强化学习控制中策略不可解释的问题，提出了一种校准优先的奖励组件审计框架。该框架将标量奖励分解为温度、CO2、湿度等具体控制维度的条件项，并在GreenLight-Gym中实现了跨模拟器、真实部署和历史数据的奖励一致性评估，显著提升了RL策略在农业控制中的可解释性与可落地性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了一种新颖的“校准优先奖励审计框架”，将温室控制中的标量奖励分解为温度、CO2、湿度、屏幕等多个可解释的条件奖励组件，解决了强化学习策略在多变量耦合控制中黑盒化和难以对齐的问题，技术方法细致且论证严谨。

### 实用性 (评分: 8.5/10)
对智慧农业和工业控制从业者具有高落地价值。框架不仅适用于模拟器训练，还能在真实设施部署、历史数据回放和规则蒸馏中保持奖励组件的可比性，有效指导温室控制策略的评估、调试与可信部署。

### 社区活跃度 (评分: 7.5/10)
结合了强化学习与智慧农业热点，基于真实的Autonomous Greenhouse Challenge数据进行验证，来源可信度高。作为arXiv预印本，在农业AI交叉领域具有较好的时效性和参考影响力。

## 项目链接
https://arxiv.org/abs/2607.11959
