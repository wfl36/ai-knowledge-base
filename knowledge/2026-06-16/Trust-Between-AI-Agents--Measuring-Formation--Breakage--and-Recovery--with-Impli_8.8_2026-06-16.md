# Trust Between AI Agents: Measuring Formation, Breakage, and Recovery, with Implications for Governing Multi-Agent Systems

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 多智能体系统, 信任机制, 治理, 评估, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.14923v1 Announce Type: new Abstract: As language-model agents increasingly work in teams, each agent must decide how much to trust its teammates. Yet we lack a standard way to measure trust between AI agents. We propose a behavioral measure based on costly verification. In a cooperative survival game, checking a teammate's work consumes resources, while trusting a wrong answer can be fatal. Relative to a memoryless version of the same model, reduced verification provides an observable measure of trust. Using this framework, we study trust formation, breakage, and recovery across six frontier model snapshots. When paired with a consistently reliable teammate, four snapshots (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.1, and Gemini 3.1 Pro) reduce verification by roughly 60-85%, whereas two smaller snapshots show little or no such adjustment. Failures reverse this discount, but models differ in how they respond. Some concentrate renewed scrutiny on the culprit, while others become more cautious toward the entire team. Recovery is slower than formation, and clustered failures sustain suspicion far longer than the same number of failures spread apart. These differences have practical consequences. Models that form trust verify less, decide more quickly, and achieve higher payoffs in our environment. By contrast, persistent over-verification is associated with indecision rather than safety. Our results show that trust dispositions can be measured before deployment and suggest that calibration, rather than maximal suspicion, should be the central concern in the governance of multi-agent AI systems.

## 综合总结
本文提出了一种基于'昂贵验证'的AI智能体间信任行为测量框架，通过合作生存游戏量化信任的形成、破裂与恢复。研究发现，大模型更易形成信任且收益更高，信任恢复慢于形成，且过度验证会导致决策低效。该研究证明信任倾向可在部署前测量，并指出多智能体系统治理应关注信任校准而非最大怀疑，为多智能体协作与治理提供了重要理论与实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文创新性地提出基于'昂贵验证'的AI智能体间信任行为测量框架，将抽象的信任量化为验证频率的降低。研究深入剖析了信任形成、破裂与恢复的动态过程，发现大模型更易形成信任，且信任恢复慢于形成，聚集失败比分散失败影响更持久。论证严谨，揭示了不同模型在信任破裂后的差异化反应（针对犯错者vs泛化全队），具有很高的理论深度与新颖性。

### 实用性 (评分: 8.5/10)
研究为多智能体系统的部署前评估提供了实用工具，证明智能体的信任倾向可被提前测量。更重要的是，指出'过度验证等同于犹豫不决而非安全'，为从业者设计多智能体协作机制提供了关键指导：应追求信任的合理校准而非一味防范，从而有效提升系统决策效率和整体收益。

### 社区活跃度 (评分: 9.0/10)
多智能体协作与治理是当前AI领域的核心前沿，该研究切中痛点，极具时效性。论文对下一代前沿模型（如GPT-5.1、Claude Opus 4.6等）的信任表现进行了基准测试，来源权威。其关于多智能体治理应从'最大怀疑'转向'信任校准'的结论，对学术界和工业界均具有深远的启示和影响力。

## 项目链接
https://arxiv.org/abs/2606.14923
