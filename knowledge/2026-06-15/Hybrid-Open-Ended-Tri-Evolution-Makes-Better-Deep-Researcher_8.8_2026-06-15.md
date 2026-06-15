# Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 深度研究, 强化学习, 自主进化, 多智能体协作, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13710v1 Announce Type: new Abstract: Deep research and agent evolution serve as de-facto tasks for AI agents in real-world applications toward artificial general intelligence. The former enables autonomous retrieval and integration of information in open-ended environments to tackle open-ended research tasks, yet it is constrained by the static parametric deep research capabilities of agent systems. The latter allows agents to autonomously interact with the environment to gain experiences that evolve model capabilities. However, its effectiveness has been widely validated only on verifiable tasks with standard answers, leaving a gap with open-ended research tasks. To bridge these two critical tasks, we propose the Hybrid Open-Ended Tri-Evolution (HOTE) framework, which leverages hybrid-mode reinforcement learning to facilitate the collaborative evolution of a proposer, solver and judge based on web-scale knowledge, moving toward autonomous evolving agents in open-ended tasks and environments. Extensive experiments on three long-form deep research benchmarks demonstrate that the 8B model trained via HOTE surpasses the strongest static open 8-32B models as well as those trained by state-of-the-art deep research training methods with less time overhead, and further verify that the evolution of all three modules in HOTE is indispensable.

## 综合总结
本文提出HOTE（Hybrid Open-Ended Tri-Evolution）框架，旨在解决深度研究受限于静态参数能力以及Agent进化仅适用于可验证任务的痛点。HOTE利用混合模式强化学习，基于网络规模知识驱动Proposer、Solver和Judge三个模块协同进化，实现开放式任务中的自主进化。实验表明，经HOTE训练的8B模型在长文本深度研究基准上超越了8-32B的静态开源模型及现有SOTA方法，且验证了三模块进化的不可或缺性，为低成本、高能力的自主进化研究Agent提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出HOTE框架，巧妙地将‘深度研究’与‘Agent进化’结合，解决了Agent进化仅限于可验证任务的痛点。引入Proposer-Solver-Judge三元协同进化机制与混合模式强化学习，理论框架完整，论证严谨（证明了三者不可或缺）。8B模型超越8-32B静态模型及SOTA方法，技术深度与观点新颖性极高。

### 实用性 (评分: 8.5/10)
针对长文本深度研究任务，HOTE使8B小模型性能超越8-32B大模型，对工业界降低推理成本、提升Agent能力极具参考价值。Proposer-Solver-Judge架构符合业界多Agent协作范式，易于迁移落地，但混合模式RL及web-scale知识的应用存在一定工程门槛。

### 社区活跃度 (评分: 9.0/10)
‘Deep Research’与‘Agent Evolution’是当前AI社区迈向AGI的核心热点话题。该论文直击开放式任务中Agent进化的关键空白，8B超越大模型的结果极具话题性与影响力。arXiv首发，作者团队背景扎实，来源可信度高，时效性与权威性兼备。

## 项目链接
https://arxiv.org/abs/2606.13710
