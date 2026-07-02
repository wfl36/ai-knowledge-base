# A Contextual-Bandit Oversight Game with Two-Sided Informational Asymmetry

**评分：** 7.5  
**状态：** 正常  
**标签：** AI安全, 对齐, 监督博弈, 人机协同, 强化学习, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00155v1 Announce Type: new Abstract: We study runtime human oversight of an AI agent when private information runs in both directions: the human privately knows her reward function, while the AI privately knows the quality of the action it proposes. This is the kind of asymmetry that arises naturally when an autonomous robot or software agent has inspected a situation its human supervisor cannot directly assess. Building on Cooperative Inverse Reinforcement Learning (CIRL) and the Oversight Game, we introduce a contextual-bandit team game with two-sided asymmetric information and a play/ask/trust/oversee interface. The bandit structure removes physical state transitions and thereby yields exact one-shot characterizations that would remain conjectural in the full POMDP setting, though the common belief remains a dynamically controlled state across rounds. We give two one-shot characterizations, a team optimum and a behaviorally natural myopic rule, whose gap is a slab of avoidable harm: a region in which the AI privately knows the proposed action is harmful and shutdown would help, yet a myopic human, trusting her prior, declines to oversee. We show this gap is the price of non-credible oversight communication, and give a partial analysis of how it resolves dynamically over repeated rounds through passive learning and active signaling with a one-period-lagged oversight response.

## 综合总结
本文研究了双边信息不对称下（人类私有奖励，AI私有动作质量）的运行时人类监督AI代理问题。基于CIRL与监督博弈，作者构建了上下文赌博机团队博弈模型及play/ask/trust/oversee接口，通过精确的一次性特征刻画，揭示了团队最优与近视规则间的'可避免伤害'差距：即AI私知动作有害且关闭有益，但近视人类因信任先验拒绝监督的区域。文章证明此差距为非可信监督沟通的代价，并分析了多轮交互中通过被动学习与主动信号动态化解该问题的机制，为AI安全与对齐提供了重要的理论洞见。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
文章在AI对齐与监督的理论研究上具有较高深度与创新性。作者巧妙地结合了合作逆向强化学习(CIRL)与监督博弈，引入了双边信息不对称（人类私有奖励函数，AI私有动作质量）的上下文赌博机模型。通过移除物理状态转移，模型得出了在完整POMDP中难以证明的精确一次性特征，并严谨地推导出了'可避免的伤害'区域及其本质（非可信监督沟通的代价），理论论证扎实且洞见深刻。

### 实用性 (评分: 6.5/10)
对AI安全机制设计的从业者有重要的启发意义，特别是提出的play/ask/trust/oversee接口和揭示的'近视人类拒绝监督已知有害AI动作'的盲区，能直接指导人机交互与监督协议的设计。但由于模型基于简化的上下文赌博机结构（去除了物理状态转移），距离复杂的现实物理环境（如自动驾驶、机器人控制）的直接工程落地还有一定距离，需要进一步的模型扩展。

### 社区活跃度 (评分: 7.5/10)
AI安全、对齐与可控性是当前大模型与Agent爆发背景下的核心热点议题，话题时效性极强。文章来源于arXiv学术预印本平台，具备较高的学术规范与可信度。尽管是单一作者且偏向纯理论探索，但其对'非可信监督代价'的定性与动态解决机制的分析，在AI对齐理论社区中具有引发关注和讨论的潜力。

## 项目链接
https://arxiv.org/abs/2607.00155
