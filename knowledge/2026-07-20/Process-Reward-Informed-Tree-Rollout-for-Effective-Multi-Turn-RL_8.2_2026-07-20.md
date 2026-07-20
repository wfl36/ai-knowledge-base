# Process Reward Informed Tree Rollout for Effective Multi-Turn RL

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, Agent, 强化学习, 过程奖励, 推理, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15610v1 Announce Type: new Abstract: Reinforcement learning (RL) has become a key approach for training LLM agents, yet popular methods such as GRPO/RLOO rely on multiple independently sampled complete trajectories for advantage estimation. In long-horizon agentic tasks, such a uniform rollout strategy can waste budget on uninformative dead-end attempts, while promising intermediate states do not receive sufficient exploration. The multi-turn structure of agentic trajectories, with interleaved actions and observations, naturally supports organizing a trajectory group as a tree, where each turn serves as a decision point for exploration. This perspective reframes effective exploration as the problem of deciding where to branch. We propose Process-Scorer Guided Adaptive Tree Rollout (PATR), a quality-aware rollout framework for multi-turn agent RL. PATR uses task-appropriate process feedback to score partial trajectories, selectively branches from promising states, reuses shared prefixes, and conservatively stops degenerate paths to reduce wasted sampling. The resulting rollout groups remain compatible with standard policy optimization while providing more efficient exploration under the same training budget. We evaluate PATR on FrozenLake and the challenging SWE-Bench, which is largely unexplored by prior tree-rollout agent RL methods. Experiments show that PATR improves performance by up to +5.0 points on SWE-Bench and +9.3 points on FrozenLake, highlighting process-guided tree rollouts as an effective strategy for scalable multi-turn RL.

## 综合总结
本文针对LLM Agent在长周期多轮强化学习中采样效率低下的问题，提出了PATR（Process-Scorer Guided Adaptive Tree Rollout）框架。该方法将多轮轨迹建模为树结构，利用过程反馈对部分轨迹评分，实现从高潜力状态选择性分支、复用共享前缀并提前终止退化路径。实验表明，在同等训练预算下，PATR在FrozenLake和SWE-Bench上分别取得了+9.3和+5.0的显著性能提升，为可扩展的多轮Agent RL提供了高效的探索策略。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了新颖的PATR框架，将多轮Agent轨迹建模为树结构，并创新性地引入过程奖励来指导树状Rollout的分支与剪枝。该方法有效解决了GRPO/RLOO等传统独立采样方法在长周期任务中探索效率低下、预算浪费的问题，理论视角的转换（从独立轨迹到树状决策分支）具有较高洞见，且与标准策略优化兼容，论证严谨。

### 实用性 (评分: 8.0/10)
对Agent和RL从业者具有极高的参考价值。PATR框架无需颠覆现有策略优化算法，即可显著提升采样效率和训练效果。在SWE-Bench这类高难度、长周期的真实代码修复任务上取得+5.0的提升，证明了其在复杂工程场景下的落地潜力，能够直接指导多轮Agent的RL训练流程优化并节省算力预算。

### 社区活跃度 (评分: 8.0/10)
强化学习与Agent的结合是当前大模型领域的前沿热点，而过程奖励模型(PRM)与树搜索也是备受关注的范式。本文在极具挑战性和权威性的SWE-Bench基准上取得了显著突破，且该领域此前鲜有树状Rollout RL方法的探索，具备很强的时效性与话题度，预计将在Agent RL社区产生较好影响力。

## 项目链接
https://arxiv.org/abs/2607.15610
