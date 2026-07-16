# Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models

**评分：** 7.5  
**状态：** 正常  
**标签：** Agent, 强化学习, 安全对齐, 世界模型, RLHF, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.13172v1 Announce Type: new Abstract: We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available. In the context of safety-critical environments, we consider traditional reinforcement learning impractical and resort to the resource of human input. We introduce DROPJ, a human-centred method for both safe training and deployment. We first learn a world model (a learned simulator) from a dataset of prior real-world trajectories. A human then plays the game in this learned simulator to extract several informative simulated trajectories. From these, we sample pairs of simulated trajectory segments and elicit from a human their preference over these segments, as well as a reason (justification) for their choice. We then train a reward model from these justified preferences and use it, together with the world model, to directly deploy the agent using model predictive control. Running real-user experiments, we find that generating informative simulated trajectories from a user significantly reduces the computational cost during training compared to other strategies, and can also improve the performance during deployment. In the context of training within a learned simulator, we show that the use of preferences rather than other types of feedback substantially improves the performance during deployment. We further demonstrate that safety justifications accompanying preferences can significantly enhance safety or prioritise user-prescribed aspects of safety associated with them during deployment.

## 综合总结
本文提出DROPJ方法，针对未知动态和无明确奖励函数的安全关键场景，通过世界模型生成模拟轨迹，结合人类的偏好及理由训练奖励模型，并利用模型预测控制（MPC）实现智能体的安全训练与直接部署。实验表明，该方法有效降低了训练计算成本，且偏好反馈及附带的安全理由能显著提升部署阶段的安全性和性能。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出DROPJ方法，创新性地将世界模型、人类偏好反馈与理由相结合，解决未知动态和无奖励函数下的安全强化学习问题。其技术亮点在于不仅获取人类的偏好，还提取偏好的'理由'，增强了奖励模型对安全约束的捕捉能力；同时利用世界模型结合模型预测控制（MPC）实现策略的直接部署，避免了传统强化学习训练中的不稳定性，论证逻辑严密，方法闭环完整。

### 实用性 (评分: 7.5/10)
对安全关键型场景（如自动驾驶、机器人控制等）具有较高参考价值。利用世界模型减少真实环境交互风险，MPC直接部署对工程实践友好。但该方法依赖人类在模拟器中交互并提供带理由的偏好数据，数据获取成本较高，在复杂高维环境下的可扩展性仍需进一步验证，限制了其在大规模场景下的快速落地。

### 社区活跃度 (评分: 7.0/10)
安全强化学习与基于人类反馈的对齐技术（RLHF）是当前AI社区的核心热点。论文发布于2026年，时效性强，紧扣大模型与智能体安全对齐的前沿趋势。将'理由'引入偏好反馈以提升安全性，为RLHF技术提供了新的演进方向，虽尚处学术验证阶段，但具备引起学术界和工业界关注的潜力。

## 项目链接
https://arxiv.org/abs/2607.13172
