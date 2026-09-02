# Discrete-Time MDP Modeling for Multi-Item Capacitated Lot Sizing with Stochastic Demand Timing

**评分：** 5.2  
**状态：** 待复核  
**标签：** 运筹学, 强化学习, MDP, 遗传算法, 生产计划, 库存优化, 论文  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00004v1 Announce Type: new Abstract: This paper studies a finite-horizon multi-item capacitated lot-sizing problem in which demand quantities are deterministic, while demand-arrival periods are stochastic. Each demand occurs once within a known time window and must be satisfied no later than its deadline. The proposed model makes production and allocation decisions at the demand level, allowing it to represent capacity competition, demand-specific backlog, and allocation-dependent inventory dynamics. The stochastic problem is formulated as a discrete-time Markov decision process (DTMDP), including the state space, feasible actions, transition kernel, and one-period cost function. To isolate the computational effect of stochastic timing, each stochastic instance is first compared with a deterministic counterpart in which each arrival distribution is replaced by its most likely arrival period. This comparison shows that stochastic timing substantially increases the number of states, the number of transitions, solution time, and memory pressure. A genetic algorithm (GA) is then proposed for the stochastic-timing problem. The GA searches over feasible state-feedback policies and evaluates each policy exactly under the DTMDP transition model. Computational experiments on 330 benchmark instances show that the GA remains close to the exact stochastic solution whenever the latter is available, with an average optimality gap of about $3.44\%$. On the difficult benchmark instances, comprising 90 test cases, the GA remains below the $5\%$ optimality-gap threshold and achieves an average optimization speedup of $6.89 \pm 1.41$ at the $95\%$ confidence level. For instances that cannot be solved exactly on the available hardware, an empirical Bellman-time regression is used to estimate the missing exact resolution time and extrapolate the expected GA speedup.

## 综合总结
本文研究有限 horizon 多品种产能批量确定问题中需求到达时机随机的情况，将其形式化为离散时间 MDP，并提出基于遗传算法的策略搜索方法。实验在 330 个基准实例上验证了 GA 相对精确随机解的接近度（平均最优性差距 3.44%）和在困难实例上的加速比（约 6.89 倍）。工作属于运筹学与 MDP 结合的较为扎实的工程型研究，问题建模清晰、实验充分，但方法新颖性有限，社区影响力较小。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文将多品种产能批量确定问题中需求到达时机的随机性建模为离散时间MDP，状态/动作/转移核/代价的构建较为系统完整。通过与确定性对应实例对比，量化了随机时机带来的状态空间膨胀问题，并设计了在可行状态反馈策略空间上搜索的遗传算法，配合DTMDP精确评估策略。方法上属于将经典运筹学问题与MDP框架结合的较为标准的做法，新颖性有限；GA用于策略搜索、经验Bellman时间回归外推计算时间等做法有一定工程合理性但缺乏理论深度。

### 实用性 (评分: 5.0/10)
对从事库存管理、生产计划、供应链优化的从业者有一定参考价值，尤其是处理需求到达时机不确定的多品种批量问题时提供了可复现的MDP建模思路和GA求解方案。但应用场景较为窄众（运筹学/生产计划领域），对更广泛的AI从业者直接指导意义有限。330个基准实例的实验规模和最优性差距（3.44%、5%以内）的报告增加了结果可信度，但缺少开源代码或可落地系统细节。

### 社区活跃度 (评分: 4.0/10)
话题属于运筹学与强化学习交叉的传统领域，并非当前AI社区的热点方向（LLM、Agent、多模态等）。来源为arXiv预印本（编号2609.00004，时间标注2026年9月，疑为元数据异常），无顶会接收信息，权威性和影响力有限。受众集中在生产与运营管理、确定性/随机优化交叉的小众学术社区，时效性一般。

## 项目链接
https://arxiv.org/abs/2609.00004
