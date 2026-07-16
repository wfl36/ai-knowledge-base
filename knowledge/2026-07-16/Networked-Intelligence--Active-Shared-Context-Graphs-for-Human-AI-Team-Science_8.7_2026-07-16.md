# Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science

**评分：** 8.7  
**状态：** 正常  
**标签：** AI for Science, 多智能体协作, 人机协同, 网络化智能, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.13220v1 Announce Type: new Abstract: Most AI-for-science systems focus on scaling a single reasoning process through better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user. However, challenging scientific problems are rarely solved by one reasoner alone. They are solved by teams whose members bring different priors, experimental backgrounds, tacit knowledge, and domain-trained intuitions. The open problem is therefore not only how to scale models, but how to cultivate networked intelligence: scaling the connections between humans and AI systems so that a result or hypothesis produced in one context reaches another person, agent, instrument, or robot that can act on it. We introduce Mycelium, an active shared workspace that automatically connects researchers and AI agents as a multi-user co-scientist. As human users and agents work, the system captures important observations and hypotheses, tracks how they relate to the team's evolving model, and routes them to the person or agent whose next decision they can inform. We evaluate Mycelium in its first empirical test, a biological multi-omics campaign in which routed shared context turned a local analytical finding into a cross-expert mechanistic constraint and ultimately into an experimental design. We also give networked intelligence a computational account as sparse conditional computation over distributed scientific contexts. This account distinguishes when a scaled standalone agent can match the network from when independent expertise and non-mergeable contexts make the network irreducible.

## 综合总结
本文提出“网络化智能”概念，指出解决复杂科学问题需从扩展单一模型转向扩展人机连接。作者开发了Mycelium系统，作为多用户与AI代理的主动共享工作空间，实现观察假设的捕获、关联与智能路由。在生物多组学实验中验证了其将局部发现转化为跨领域实验设计的有效性。此外，论文从计算理论角度定义了网络化智能，并论证了在存在不可合并上下文时网络智能的不可约性，为构建下一代人机团队科研系统提供了重要理论基础与工程范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文跳出了单智能体扩展的局限，提出“网络化智能”概念，创新性地将人机团队协作建模为分布式科学上下文上的稀疏条件计算。理论推导中关于“不可约网络”的界定，深刻揭示了独立专业知识和不可合并上下文在复杂科学问题中的必要性，论证严谨且具深度。

### 实用性 (评分: 8.0/10)
Mycelium系统为构建多用户、多Agent协作的科研平台提供了具体架构参考，其“捕获-追踪-路由”的机制可直接指导AI for Science工程实践。但在通用场景下，上下文的自动抽取与精准路由面临较高工程挑战，落地需深度定制。

### 社区活跃度 (评分: 9.0/10)
多智能体与人机协同是当前大模型领域的核心演进方向，该文极具时效性。作者团队阵容庞大且具备深厚科研背景，结合真实生物多组学实验进行验证，极大提升了成果的权威性与可信度，对科研社区有重要启发意义。

## 项目链接
https://arxiv.org/abs/2607.13220
