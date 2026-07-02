# Solution space path planning for supporting en-route air traffic control

**评分：** 7.7  
**状态：** 正常  
**标签：** 路径规划, 人机协同, 空管系统, 决策支持, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00064v1 Announce Type: new Abstract: As technology advances, many path-planning algorithms have been proposed for Air Traffic Management, yet their operational adoption in tactical control remains limited, revealing a misalignment between algorithmic design priorities and air traffic controllers' needs. This underscores the need for decision-support solutions that are inherently interpretable, computationally efficient, and explicitly designed for human use. Focusing on this design challenge, this study develops a conflict-free path-planning algorithm for en-route Air Traffic Control (ATC) designed to be compatible with two guiding considerations: (1) the interpretability and flexibility offered by solution-space displays, which motivate constructing an algorithm that exposes all feasible safe actions and accommodates shifting optimization goals; and (2) the decision logic controllers naturally apply when enforcing operational constraints, such as separation standards, maneuverability limits, waypoint minimization, and routing practicality. Centered on these principles, the algorithm integrates three intent-based conflict detection methods -- distance-based, time-interval-based, and zone-based -- within a solution-space framework to identify conflict-free paths in computationally efficient ways. Additionally, vertex-based and edge-based search nodes are proposed for solution space path planning (SSPP), resulting in two variants -- SSPPV and SSPPE, respectively, which are evaluated in terms of computational speed and solution quality. Empirical results show that SSPPV paired with zone-based conflict detection achieves the best performance, computing paths in 3.69 ms on average in operational-relevant scenarios based on the Delta sector of the Maastricht Upper Area Control Centre (MUAC) using a 5 nmi grid.

## 综合总结
本文针对航路空中交通管制中路径规划算法难以在实际战术控制中落地的问题，提出了一种基于解空间框架的无冲突路径规划算法（SSPP）。该算法结合了解空间显示的可解释性与空管员的实际决策逻辑，集成了基于距离、时间间隔和区域的三种冲突检测方法，并提出了SSPPV和SSPPE两种搜索变体。实验表明，SSPPV结合基于区域的冲突检测在真实扇区场景中表现最佳，平均计算时间仅3.69毫秒，充分满足实时决策支持需求，对空管自动化系统的工程实践具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文针对传统空管路径规划算法与实际战术控制需求脱节的问题，提出了一种基于解空间框架的无冲突路径规划算法（SSPP）。技术上的亮点在于将算法设计与人类认知（解空间显示的可解释性）及空管员实际决策逻辑（间隔标准、机动性限制等）深度融合，并创新性地集成了三种基于意图的冲突检测方法（基于距离、时间间隔和区域），提出了SSPPV和SSPPE两种搜索变体。论证严谨，实验基于真实空域数据（MUAC Delta扇区）验证了算法在计算效率和求解质量上的表现，但底层搜索机制仍属于传统图搜索的变体，范式级突破有限。

### 实用性 (评分: 8.5/10)
该研究对空管决策支持系统的工程落地具有极高的参考价值。文章直击传统算法'好用但不实用'的痛点，强调算法的可解释性和对动态优化目标的兼容性，非常契合人机协同系统的实际需求。SSPPV结合区域冲突检测平均3.69毫秒的计算速度完全满足战术控制的实时性要求，算法设计直接考虑了航路点最小化和路由实用性等业务约束，可直接指导新一代空管自动化系统的研发与部署。

### 社区活跃度 (评分: 7.0/10)
空中交通管理自动化与人机协同决策是航空及安全关键系统领域的持续热点。该论文来自arXiv预印本平台，使用了欧洲Maastricht Upper Area Control Centre (MUAC)的真实场景数据进行验证，来源具有较高的行业可信度。虽然该成果在垂直的空管/航空领域内具有较强的影响力和应用前景，但受限于领域壁垒，在更广泛的AI社区中破圈影响力相对一般。

## 项目链接
https://arxiv.org/abs/2607.00064
