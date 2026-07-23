# NEXUS: Structured Runtime Safety for Tool-Using LLM Agents

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 大模型, 安全, 运行时监控, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19356v1 Announce Type: new Abstract: Tool-using LLM agents increasingly execute high-impact actions, making runtime safety monitoring essential. We present NEXUS (Neural EXecution Utility and Safety), a structured-plan safety monitor that applies a formal intervention policy to select among four actions: allow, block, request confirmation, or request revision. NEXUS combines deterministic safety rules, argument-level inspection, and a calibrated logistic-regression risk score for graded escalation. On a 128-instance synthetic benchmark, NEXUS achieves an F1 score of 0.949 and a 4-class intervention accuracy of 0.6406, outperforming rule-only intervention selection by 27.3 percentage points. It also improves over rule-only on R-Judge (F1 = 0.861 vs. 0.849), matches rule-only on AgentHarm due to threat-model limits, and achieves 0% ASR at 99% control allow on IPI. On the rule-blind NEXUS-Stress benchmark, NEXUS reaches an F1 score of 0.881, highlighting the difficulty of fine-grained intervention routing. With 0.205 ms median latency, NEXUS adds under 0.1% overhead to typical agent loops. Code, benchmarks, and the calibrated risk scorer are publicly released.

## 综合总结
本文提出NEXUS，一种针对工具调用LLM Agent的结构化运行时安全监控框架。该框架融合确定性规则与校准的逻辑回归风险评分，实现允许、阻止、确认、修订的四级动态干预。实验表明其在合成基准上F1达0.949，较纯规则方法提升显著，且运行延迟极低（<0.1%开销），为Agent安全落地提供了高可用、易集成的工程解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出NEXUS结构化运行时安全监控框架，创新性地将确定性安全规则、参数级检查与校准的逻辑回归风险评分相结合，实现了允许、阻止、请求确认、请求修订的四级分级干预机制。实验论证严谨，在合成基准上F1达0.949，较纯规则方法提升27.3个百分点，但在部分对抗场景（如AgentHarm）受限于威胁模型表现一般，风险评分模型（逻辑回归）的复杂度与泛化上限仍有探索空间。

### 实用性 (评分: 9.0/10)
极具工程落地价值。针对Agent执行高风险动作的安全痛点，提供了细粒度且符合实际业务逻辑的干预策略。其极低的延迟（0.205ms，开销<0.1%）确保了不会成为Agent执行循环的性能瓶颈，且代码与基准完全开源，可直接作为安全护栏组件集成至现有LLM Agent框架中。

### 社区活跃度 (评分: 8.5/10)
Agent安全与对齐是当前大模型应用落地的核心关注点，话题时效性极强。该工作开源了代码、基准及校准模型，为社区提供了可复现的基线和评估标准，影响力潜力较大；但作者团队相对新兴，在极端对抗场景下的泛化能力仍需社区进一步验证与迭代。

## 项目链接
https://arxiv.org/abs/2607.19356
