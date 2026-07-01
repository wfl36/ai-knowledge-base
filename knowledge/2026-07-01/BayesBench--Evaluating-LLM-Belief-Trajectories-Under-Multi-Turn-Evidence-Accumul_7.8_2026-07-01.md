# BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, 推理, 评估, 论文, 基准测试  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30850v1 Announce Type: new Abstract: Large language models (LLMs) are typically deployed in multi-turn conversations, where each turn provides new evidence that should reduce epistemic uncertainty about their environment. Acting rationally then requires inferring the unobserved quantities that govern it and updating beliefs about them as evidence accumulates. Yet most evaluations only score the model's final-turn answer in a single-turn format, leaving this process unexamined. We ask how closely LLMs' belief updates match those of a rational Bayesian reasoner in multi-turn settings, and introduce BayesBench, a suite of simulation environments that probe this across three progressively complex tasks: (i) Bayesian estimation, where the model infers an unknown parameter from sequential evidence; (ii) Bayesian prediction, where the model turns inferred beliefs about a latent variable into outcome forecasts; and (iii) latent-framed Bayesian prediction, where observations are filtered through a user-persona framing, requiring joint inference over the latent state and the persona. Across seven LLMs (3B--70B), scaling improves latent inference and evidence accumulation, with updates occasionally matching the Bayesian posterior. However, these gains do not reliably carry over to downstream prediction, exposing a gap between inferring latent structure and using it to rationally update beliefs about the target outcome.

## 综合总结
该论文提出了BayesBench基准，用于评估大语言模型在多轮证据积累下的信念更新轨迹。针对现有评估仅关注单轮最终答案的局限，BayesBench通过三个逐渐复杂的贝叶斯推理任务探究LLM与理性贝叶斯推理器的匹配度。实验表明，尽管模型规模扩大提升了潜在推断能力且偶尔能匹配贝叶斯后验，但这种增益未能可靠地传递到下游预测，揭示了LLM在推断潜在结构与利用其进行理性预测之间存在显著差距。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文视角新颖，将大模型在多轮对话中的行为与理性贝叶斯推理器进行对标，提出了‘信念轨迹’和‘证据积累’下的评估框架。通过设计三个逐步复杂的任务（贝叶斯估计、贝叶斯预测、潜在框架贝叶斯预测），严谨地剖析了LLM在推断潜在结构与利用其更新下游预测信念之间的脱节问题，研究深度与论证逻辑俱佳。

### 实用性 (评分: 7.0/10)
BayesBench为评估和优化LLM在多轮交互中的动态推理能力提供了标准化的测试基准，对Agent及多轮对话系统的开发者具有较高参考价值。然而，其模拟环境基于理想化的贝叶斯推理设定，与复杂的真实业务场景存在距离，直接指导工程落地的适用范围相对受限。

### 社区活跃度 (评分: 8.0/10)
多轮对话中LLM的推理一致性和信念更新能力是当前大模型与Agent领域的核心痛点，该研究切中时效性热点。作为arXiv新发文，由多位学者合作完成，揭示了模型规模扩大并未解决推断到预测的转化Gap这一关键发现，具备较高的学术影响力和社区讨论潜力。

## 项目链接
https://arxiv.org/abs/2606.30850
