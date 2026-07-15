# In-Context Reinforcement Learning under Non-Stationarity: A Survey

**评分：** 8.3  
**状态：** 正常  
**标签：** 强化学习, 上下文学习, Agent, 非平稳环境, 综述  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11906v1 Announce Type: new Abstract: The development of decision-pretrained transformers, algorithm distillation, long-context meta-RL, and retrieval-augmented agents has renewed interest in in-context reinforcement learning (ICRL): the ability of a pretrained or fine-tuned decision model to infer latent task rules and improve future behavior from interaction context, without test-time parameter updates. This line of work asks when trial-and-error evidence, rewards, transitions, demonstrations, feedback, or retrieved experience can make learning-like computation happen inside the context window. However, existing surveys of ICRL mainly organize the field around pretraining objectives, architectures, context formats, evaluation protocols, and theoretical mechanisms, while the non-stationary setting remains comparatively underexamined. In changing environments, accumulated context is not merely more evidence about a fixed task: the reward specification, transition kernel, observation channel, action interface, constraint model, or demonstration and memory distribution can fall out of alignment with the current regime. Previously useful context can therefore become stale, misleading, or useful again when an old regime returns. We survey non-stationary ICRL as the problem of adapting through context while deployed policy parameters remain fixed: the policy must infer both the current decision rule and which parts of its accumulated evidence still support that rule. We define non-stationary ICRL, relate it to meta-RL, decision sequence modeling, retrieval-augmented RL, value- and model-aware ICRL, and reward-feedback agents, and organize the literature along three questions: what changes, how the change unfolds, and how observable the change is to the agent.

## 综合总结
本文是一篇关于非平稳环境下上下文强化学习（ICRL）的综述。针对现有ICRL研究多假设平稳环境而忽视环境动态变化的局限，文章首次系统定义了非平稳ICRL问题，指出策略需在参数固定的情况下，通过上下文推断当前决策规则并识别有效历史证据。文章将该问题与元强化学习、检索增强RL等联系起来，并从变化内容、变化动态过程及变化可观察性三个核心维度对现有文献进行了系统梳理，为构建能适应复杂动态现实环境的智能体提供了重要的理论框架和研究方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
文章精准抓住了上下文强化学习（ICRL）在非平稳环境下的核心痛点，即历史累积上下文不仅可能失效，甚至可能产生误导。将非平稳ICRL形式化定义为‘在策略参数固定下，推断当前决策规则及有效历史证据’的问题，并从变化内容、变化动态过程及变化可观察性三个维度解构文献，具有极高的理论深度和学术洞见，填补了该细分领域的理论框架空白。

### 实用性 (评分: 7.5/10)
现实世界中的强化学习场景（如自动驾驶、金融交易、人机交互）普遍存在非平稳性，本文提出的问题框架对开发具有持续适应能力的Agent（特别是RAG增强的智能体）具有明确的工程指导意义。它能帮助从业者在设计上下文窗口和记忆机制时，更好地处理上下文过期与冲突问题，但作为综述其直接落地需结合具体算法。

### 社区活跃度 (评分: 8.5/10)
结合Decision Transformer和Algorithm Distillation的ICRL是当前大模型与强化学习交叉领域的热点前沿，而非平稳性是其走向真实应用必须跨越的障碍，话题极具时效性和研究价值。arXiv平台发布，作者系统梳理了该新兴子领域，对社区后续研究具有显著的引领和启发作用。

## 项目链接
https://arxiv.org/abs/2607.11906
