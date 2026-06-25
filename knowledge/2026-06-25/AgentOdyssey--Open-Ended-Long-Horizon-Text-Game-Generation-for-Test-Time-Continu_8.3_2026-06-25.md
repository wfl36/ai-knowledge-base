# AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 持续学习, 测试时学习, 评估基准, 文本游戏, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.24893v1 Announce Type: new Abstract: For agents to learn continuously from interaction with the world at test time, they must be able to explore effectively, acquire new world knowledge and skills, retain relevant episodic experiences, and plan over long horizons. To evaluate these key abilities of test-time continual learning agents, we introduce AgentOdyssey, a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Critically, AgentOdyssey goes beyond the conventional machine learning assumption that learning does not occur at test time by placing agents in a continuous, long-horizon setting that interleaves learning and inference throughout deployment. We further propose a multifaceted evaluation methodology that measures not only game progress but also offers diagnostic tests on world knowledge acquisition, episodic memory, object and action exploration, action diversity, and model cost. We evaluate diverse agent paradigms in the generated games. Our experimental results reveal critical limits in agents' key abilities, as well as factors that influence their meaningful horizon. Although performance scales with stronger base models, even the top agent remains far below human performance, leaving substantial headroom for improvement. Among agent mechanisms, we find that short-term memory benefits multiple agent paradigms and is an important component of agent test-time training.

## 综合总结
本文提出了AgentOdyssey，一个针对'测试时持续学习'Agent的新型评估框架，通过程序化生成开放式文本游戏模拟长期交互环境，打破了传统'测试时不学习'的ML假设。研究设计了多维度诊断评估方法，实验揭示当前最强Agent在长期任务中远低于人类水平，存在严重能力瓶颈，并验证了短期记忆是测试时训练的重要组件。该工作为Agent的持续学习与长程规划研究提供了关键基准与发展方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该论文提出了极具前瞻性的'测试时持续学习'概念，打破了传统机器学习'测试时不学习'的固有范式。通过程序化生成开放式文本游戏构建了AgentOdyssey评估框架，并设计了涵盖知识获取、情景记忆、探索能力等多维度的诊断评估方法，论证严谨，实验深刻揭示了当前Agent在长期交互中的关键能力瓶颈及短期记忆对测试时训练的重要性，研究深度与新颖性极高。

### 实用性 (评分: 7.5/10)
AgentOdyssey为Agent研究人员和开发者提供了系统性的评估基准，其多维诊断指标能有效指导Agent架构设计（如短期记忆机制的引入、测试时训练策略的优化）。但开放式文本游戏与测试时持续学习目前更多处于学术探索阶段，距离工业界复杂真实场景的大规模落地应用尚有距离，实际适用范围主要聚焦于前沿研发与学术评测。

### 社区活跃度 (评分: 8.5/10)
探讨的话题极具时效性，'测试时计算/学习'与'Agent长期记忆'是当前大模型与Agent社区的核心热点。作者团队包含Daniel Khashabi等知名学者，来源权威性高（arXiv预印本）。该研究明确指出当前最强模型远低于人类水平，为社区指出了明确的改进空间与挑战，具有较高的影响力和话题引发潜力。

## 项目链接
https://arxiv.org/abs/2606.24893
