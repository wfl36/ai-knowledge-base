# Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-Use Agents on Atlassian Workflows

**评分：** 7.3  
**状态：** 正常  
**标签：** Agent, RLVR, Tool-Use, 强化学习, 大模型, 论文  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01465v1 Announce Type: new Abstract: Large language models are trained to predict the next token, not to act inside a specific API. In niche enterprise SaaS workflows -- where success means hitting the right endpoint with the right nested arguments in the right order -- this objective mismatch shows up as silent failures: dropped required fields, hallucinated tools, or early stops after a single read. We ask whether Reinforcement Learning with Verifiable Rewards (RLVR), applied directly in the target environment, closes the gap. As a proof of concept we build a suite of five synthetic environments emulating the Jira REST v3 and Confluence v2 APIs at schema fidelity; rewards are computed entirely from the tool-call trace, with no live API, no learned judge, and no human label in the loop. Scoring prompted Qwen3-1.7B and Qwen3.5-4B on the same checkers that drive GRPO training, we find that on the four scenarios whose rewards are non-degenerate the RL-trained policy lifts average reward from a 4B-baseline range of 0.35--0.92 to 0.95--1.00, with the largest single gain on Confluence page creation ($0.35 \rightarrow 1.00$). We position this as a preliminary step toward outcome-optimised small models for niche enterprise APIs, and foreground two limitations a workshop reader should weigh: hand-crafting verifiable rewards does not scale beyond the handful of endpoints reported here, and one of our five scenarios (ticket-transition) has a saturating reward shape that the prompted 4B already maxes out.

## 综合总结
本文针对大模型在企业SaaS API（如Jira/Confluence）调用中因“下一个token预测”目标不匹配导致的静默失败问题，提出使用RLVR进行端到端优化。作者构建了5个高保真合成环境，完全基于工具调用轨迹计算可验证奖励，无需人工或模型裁判。实验表明，经过RLVR训练的Qwen小模型在4个场景中平均奖励从0.35-0.92显著提升至0.95-1.00。尽管效果显著，但作者坦承手工构建奖励函数难以规模化，且部分场景存在奖励饱和问题，这仍是迈向企业级小模型优化的初步探索。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
本文精准指出了大模型在特定企业API调用中存在的目标不匹配问题（下一个token预测 vs 精确动作执行），并创新性地采用RLVR（带可验证奖励的强化学习）在目标环境中直接优化。研究构建了高保真的合成环境，奖励完全基于工具调用轨迹自动计算，避免了LLM裁判或人工标注的偏差。实验论证严谨，Qwen小模型在4个场景下奖励从0.35-0.92跃升至0.95-1.00，证明了该范式在垂直API场景的有效性。但作为概念验证，手工构建可验证奖励的扩展性受限，技术深度仍有进一步提升空间。

### 实用性 (评分: 6.5/10)
对于从事企业SaaS集成（特别是Atlassian生态）和Agent开发的从业者具有较高的参考价值，证明了小模型通过RLVR在特定垂直API上可以实现接近完美的执行率，避免了通用大模型的幻觉和遗漏字段问题。然而，其可落地性受限于手工编写奖励函数的低效性，难以直接推广到拥有成百上千端点的复杂企业系统中，且目前仅在合成环境中验证，距离真实生产环境的复杂状态与异常处理仍有距离。

### 社区活跃度 (评分: 7.5/10)
RLVR是当前大模型与Agent训练的前沿热点，结合企业级SaaS工作流（Jira/Confluence）具有极强的现实应用时效性。作为arXiv预印本，学术可信度良好，但作者明确指出这仅是workshop级别的概念验证，且存在明显的扩展性局限，目前的行业影响力和权威性相对有限。

## 项目链接
https://arxiv.org/abs/2607.01465
