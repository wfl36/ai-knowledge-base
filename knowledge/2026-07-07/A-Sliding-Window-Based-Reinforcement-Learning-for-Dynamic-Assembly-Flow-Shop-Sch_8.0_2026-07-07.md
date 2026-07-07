# A Sliding-Window-Based Reinforcement Learning for Dynamic Assembly Flow Shop Scheduling with Multi-Product Delivery

**评分：** 8.0  
**状态：** 正常  
**标签：** 强化学习, 调度, 图神经网络, 智能制造, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02941v1 Announce Type: new Abstract: Multi-product kitting delivery imposes significant challenges for real-time scheduling in hybrid manufacturing systems that integrate processing and assembly, as dynamic order arrivals simultaneously alter supply dependencies and the set of feasible job-machine assignments. This paper proposes a sliding-window-based reinforcement learning (SWRL) framework for end-to-end online scheduling in the flexible assembly flow shop scheduling problem with complex kitting constraints. The problem is formulated as a heterogeneous graph-based Markov decision process that captures the dual-layer kitting structure and the tail-product bottleneck dynamics that produce a sparse reward landscape. To address the resulting challenges, SWRL integrates a sliding-window filtering mechanism that filters inactive nodes and prioritizes kitting-critical operations, a spatiotemporal graph encoding network that tracks bottleneck shifts across consecutive decision states, and a dynamic action mapping module with a constrained waiting strategy that adapts to the changing action space under variable topologies. Experiments on real-world instances from a home appliance manufacturer demonstrate that SWRL achieves consistent tardiness reductions over classical dispatching rules and existing deep reinforcement learning methods, and exhibits robust performance across varying resource configurations, order loads, and arrival concentrations.

## 综合总结
本文提出了一种基于滑动窗口的强化学习（SWRL）框架，用于解决具有多产品成套交付约束的动态装配流水车间调度问题。通过构建异构图MDP模型，结合滑动窗口过滤、时空图编码和动态动作映射模块，有效克服了稀疏奖励和动态动作空间难题。在真实家电制造数据上的实验表明，该方法在降低延迟和鲁棒性上均优于传统规则和现有深度强化学习方法，对智能制造领域的动态调度实践具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文针对柔性装配流水车间中多产品成套交付的动态调度问题，创新性地提出了基于滑动窗口的强化学习（SWRL）框架。技术深度体现在将问题建模为异构图MDP以捕捉双层成套约束与尾产品瓶颈，并针对性地设计了滑动窗口过滤机制、时空图编码网络及动态动作映射模块，有效解决了稀疏奖励与动态动作空间的挑战，方法设计与论证严谨。

### 实用性 (评分: 8.5/10)
研究具有很高的落地参考价值。不仅基于家电制造企业的真实实例进行了验证，证明其在降低延迟和应对不同资源/订单配置时的鲁棒性，其提出的滑动窗口过滤和动态动作映射机制也可直接指导其他复杂制造场景下的在线调度系统开发，适用范围广。

### 社区活跃度 (评分: 7.5/10)
话题属于AI与运筹优化、智能制造交叉领域的热点，具有强时效性。作者团队包含优化领域知名学者Qingfu Zhang，保证了研究的权威性与可信度。尽管RL用于调度已非全新概念，但针对成套约束与动态拓扑的深度定制方案对工业界和学术界均有较大参考价值。

## 项目链接
https://arxiv.org/abs/2607.02941
