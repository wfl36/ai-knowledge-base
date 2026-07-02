# From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents

**评分：** 8.4  
**状态：** 正常  
**标签：** Agent, 多智能体, 语言涌现, 记忆架构, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00233v1 Announce Type: new Abstract: How do two agents invent a shared language from scratch? In a Lewis signaling game, a sender and receiver must coordinate on a code using only their interaction history. We study five memory architectures across varying channel configurations with LLM agents and find that memory architecture matters more than channel capacity. Agents with a persistent private notebook benefit from surplus channel capacity and avoid the high-capacity collapse seen in stateless agents, achieving the most reliable coordination ($0.867 \pm 0.023$ at capacity = 25). Stateless agents peak at moderate capacity and then degrade as the vocabulary grows beyond what a rolling context window can track The notebook externalizes learned conventions, freeing agents from having to re-derive codes each round. An information bottleneck-inspired argument predicts an optimal capacity equal to the number of objects. Instead, the bottleneck (capacity = 8) proves to be a fragility point, and surplus capacity is generally better. We show that channel capacity alone cannot predict coordination; memory architecture determines whether agents turn interaction history into stable conventions, and both dimensions are needed to understand how signals become language.

## 综合总结
本文研究了 LLM Agent 在 Lewis 信号博弈中从零构建共享语言的过程，对比了五种记忆架构在不同通道配置下的表现。研究发现，记忆架构比通道容量更能决定协调效果：带有持久私有笔记本的 Agent 能有效外化约定，避免无状态 Agent 在高容量下的性能崩溃，实现最可靠的协调。此外，实验反直觉地发现，信息瓶颈理论预测的最优容量反而是脆弱点，过剩容量通常表现更好。该研究揭示了记忆架构在将交互历史转化为稳定约定中的决定性作用，为多 Agent 通信与协作机制设计提供了重要启示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
研究将 LLM Agent 引入经典的 Lewis 信号博弈，系统性地对比了五种记忆架构对语言涌现的影响。其核心洞见在于挑战了基于信息瓶颈理论的传统预测，实证表明理论预测的最优容量反而是脆弱点，过剩通道容量表现更优；且记忆架构（特别是外化约定的私有笔记本）比通道容量更能决定协调成功率，论证严谨且具有反直觉的新颖性。

### 实用性 (评分: 7.8/10)
对多智能体系统架构设计具有直接指导意义。研究证实，在 Agent 协作中，单纯增加上下文窗口（通道容量）会导致无状态 Agent 的性能退化，而引入持久化外部记忆（如私有笔记本）能更有效地固化通信协议，这为解决 LLM 多轮交互中的上下文遗忘和通信爆炸问题提供了可落地的架构参考。

### 社区活跃度 (评分: 8.5/10)
论文发布于 2026 年 7 月，时效性极强。多智能体协作与通信是当前 AI 社区的核心热点，作者团队包含知名学者，研究结合了经典博弈论与现代 LLM 架构，对理解大模型社会性涌现极具启发性，预计将在 Agent 研究圈层产生较高影响力。

## 项目链接
https://arxiv.org/abs/2607.00233
