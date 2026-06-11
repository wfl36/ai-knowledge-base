# Knowing When to Ask: Self-Gated Clarification for Hierarchical Language Agents

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 推理, 大模型, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11349v1 Announce Type: new Abstract: In hierarchical reasoning, failures often originate at intermediate decision points where the agent commits to a wrong branch without recognizing that it lacks critical information. Rather than treating clarification as an external uncertainty trigger, we propose ACTION-RATING, a formulation that places it inside the agent's action space on a shared ordinal scale with navigation, so that asking competes directly with acting at every decision point and help-seeking becomes observable at intermediate states. Two structurally distinct information-seeking modes emerge from the agent's own ratings: mandatory (no viable branch) and opportunistic (residual uncertainty despite a leading candidate). On Harmonized Tariff Schedule classification (30,000-node taxonomy, three benchmarks, 9~LLMs across 4 families), we observe a regime shift from mandatory to opportunistic clarification, with Information-Seeking Effectiveness (ISE), a local diagnostic defined as the fraction of help interactions followed by a correct next navigation step (not a final-task metric), rising from 50% to 74%. Three diagnostic contrasts fail to reproduce this structure. A separability test shows that the information-seeking pattern (mode split, ISE ranking) persists when answer quality is degraded (-18.8% accuracy), supporting an empirical separation between where an agent seeks help and the quality of the help it receives. Under the controlled answer channel, accuracy gains reach +16.2% at 10-digit; we read this as an upper bound on what better localization could unlock, not a deployment estimate.

## 综合总结
该论文提出ACTION-RATING方法，将澄清提问内化为层级语言Agent动作空间的竞争选项，而非外部触发。通过在3万节点关税分类任务上的实验，揭示了从强制性到机会性澄清的机制转变，并定义ISE指标验证了信息寻求的有效性提升（50%至74%）。可分离性测试证明了寻求帮助的位置与帮助质量的独立性，受控环境下准确率提升达16.2%。该研究为解决Agent层级推理中的盲目决策问题提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
将澄清机制从外部触发内化为动作空间的竞争选项，提出ACTION-RATING方法，深刻揭示了层级推理中的决策失败根源。区分强制性与机会性信息寻求模式，并通过ISE指标和可分离性测试严谨论证了寻求帮助位置与帮助质量的独立性，研究深度与论证逻辑极佳。

### 实用性 (评分: 8.0/10)
对构建复杂层级决策Agent（如法律、医疗、复杂分类系统）具有高参考价值，直接解决了中间状态“盲目决策”的痛点。但在实际落地中，如何保证“机会性提问”获取的高质量反馈仍是一大挑战，且当前实验主要基于特定分类法，泛化到通用Agent仍需工程适配。

### 社区活跃度 (评分: 8.5/10)
探讨Agent在层级推理中的主动提问机制，切中当前大模型Agent研究的热点与痛点。论文实验设计扎实（跨4个家族9个LLM，3万节点分类法），数据详实，arXiv发布具备较高学术可信度。对未来Agent架构设计具有启发意义。

## 项目链接
https://arxiv.org/abs/2606.11349
