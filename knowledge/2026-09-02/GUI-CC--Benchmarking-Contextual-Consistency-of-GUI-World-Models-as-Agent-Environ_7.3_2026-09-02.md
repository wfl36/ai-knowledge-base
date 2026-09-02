# GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments

**评分：** 7.3  
**状态：** 正常  
**标签：** GUI Agent, 世界模型, 基准测试, 评估方法, 多模态, Agent  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00048v1 Announce Type: new Abstract: GUI world models are increasingly evaluated as one-step next-screen predictors, yet their intended use is often as multi-step environments for GUI agents. This mismatch leaves a key requirement under-tested: generated states must remain contextually consistent when they are repeatedly reused for future interaction. We introduce GUI-CC, a benchmark that evaluates contextual consistency of GUI world models as agent environments rather than isolated next-screen predictors. GUI-CC contains two complementary tracks: an offline reference-action track that rolls models along real mobile GUI trajectories, and an online agent-loop track that lets fixed probing agents interact with model-generated UIs. We construct 500 offline trajectory tasks from GUIOdyssey and 200 emulator-verified online tasks across 30 mobile apps. GUI-CC evaluates transition fidelity, transition plausibility, contextual consistency, and task progress. Experiments show that plausible single-step generation does not guarantee reliable environment simulation: current models often produce usable-looking screens while failing to preserve task-relevant context or support executable multi-step rollouts.

## 综合总结
GUI-CC是一个针对GUI世界模型上下文一致性的评估基准，揭示了当前模型在单步生成可信但多步环境模拟不可靠的关键问题。论文提出了双轨评估框架（离线+在线），通过700个任务覆盖30个移动应用，从转换保真度、可信度、上下文一致性和任务进度四个维度系统评估模型作为代理环境的适用性。研究对GUI Agent领域具有重要的诊断价值和方向指引意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文提出了GUI-CC基准，敏锐地指出了当前GUI世界模型评估中的关键错位问题——即单步下一屏预测能力与多步代理环境需求之间的脱节。技术贡献包括双轨评估设计（离线参考动作轨和在线代理循环轨），覆盖转换保真度、可信度、上下文一致性和任务进度四个维度。方法论上具有严谨性，构建了500个离线轨迹任务和200个经模拟器验证的在线任务，并揭示了'可信的单步生成不等于可靠的环境模拟'这一重要现象。实验设计系统，但创新性主要体现在评估视角的转换而非底层模型架构的突破。

### 实用性 (评分: 7.0/10)
该基准对GUI代理和GUI世界模型的研究者具有直接参考价值，明确指出了现有评估协议的不足，为后续模型开发提供了更贴合实际使用场景的评估标准。离线+在线双轨设计、跨30个移动应用的覆盖范围使基准具有较好的泛化性。然而，benchmark的实际落地需要研究者适配新的评估流程，且对模型开发方向的指导作用相对有限（更多是诊断工具而非解决方案）。对从事GUI Agent研发和评估的从业者较为实用。

### 社区活跃度 (评分: 7.5/10)
话题聚焦于GUI Agent和世界模型的评估前沿，是当前AI Agent领域的热点方向之一。作者团队具有学术背景（来自高校/研究机构），论文发布于arXiv，标注为2026年发布（疑为预印本或时间标注异常）。GUI世界模型作为代理环境是新兴且受关注的研究课题，话题时效性强。但作为新发表的基准论文，其社区影响力和引用积累尚需时间验证，权威性处于建立阶段。

## 项目链接
https://arxiv.org/abs/2609.00048
