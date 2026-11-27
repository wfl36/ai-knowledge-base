# Irreducible Governance Structure for Autonomous Agent Systems: Fair Allocation, Strategy-Proofness, and Multi-Scale Composition

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-27  
**来源：** rss  

## 项目描述
arXiv:2611.31284v1 Announce Type: new Abstract: Autonomous agent governance is commonly framed as a problem of enforcing correct execution. However, in multi-agent systems, an equally fundamental question precedes execution: which agents are allowed to act. In this paper, we show that allocation is not an auxiliary concern but a structural component of governance. When multiple agents compete for execution under constrained resources, any allocation mechanism introduces unavoidable trade-offs between fairness, efficiency, and resistance to strategic manipulation. We formalize this through a set of impossibility results, including Sybil amplification and the incompatibility of desirable allocation properties. We then show that these allocation constraints cannot be resolved within a single layer of control. Instead, they propagate across the system, interacting with execution atomicity, state enforcement, and behavioral drift. This leads to a multi-scale governance structure composed of four orthogonal dimensions: temporal (atomicity), state (enforcement), behavioral (drift monitoring), and population (allocation). Our main result is an irreducibility theorem: under finite observability, no governance architecture can collapse these dimensions without loss of correctness or stability. Allocation, in particular, acts as a first-class constraint that prevents simplification of the governance stack. We validate these results through a series of analytical constructions and empirical ablations, showing that removing or approximating any layer leads to systematic failure modes. This work reframes agent governance as a structural problem: not only how actions are executed, but how access to execution is determined, and why these decisions impose irreducible architectural requirements.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.31284
