# Benchmarking the Personalization Capabilities of Large Language Models

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, Agent, 个性化, 评估基准, 贝叶斯说服, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20471v1 Announce Type: new Abstract: Personalization, the act of varying a message to induce action from a specific receiver while keeping sender, channel, and time fixed, has a long tradition in psychology and marketing as a two-party problem in which sender and receiver have independent objectives. Large language models remove the bounded-inventory constraint of classical retrieval-and-ranking approaches by generating a continuum of message variants conditioned on inferred receiver state, raising the question of how well current models perform personalization in the classical sense. Existing LLM personalization benchmarks measure sender-side adaptation, in which the receiver is the same user the model is serving. The two-party question, whether a generated message induces its intended action in a third party, has been investigated only through A/B tests and small-scale human studies that cannot be re-run against a new model on demand. We adapt the Bayesian Persuasion framework of Kamenica and Gentzkow (2011) to generative agents and instantiate the formulation in sales, where receiver actions are routinely logged against the outreach that induced them. We release SDR-Bench, a public corpus of 6,279 customer success stories spanning 22 industries and approximately 200 enterprises, served through a temporally constrained simulation that prevents future-data leakage. Across frontier LLMs and deep-research agents, we observe a consistent personalization plateau and on a Fortune 100 tech cohort no model statistically separates successful from unsuccessful outreach. A field deployment with 12 professional sales representatives validates the framework, with 48 percent of model-generated content rated immediately useful and senior-expert agreement at Pearson 0.82. We release SDR-Arena and SDR-Bench publicly to support reproducible study of generative personalization at scale.

## 综合总结
本文将贝叶斯说服框架引入LLM评估，从两方博弈视角重新审视大模型的个性化能力，指出传统基准仅衡量单边适应的局限性。研究构建并开源了SDR-Bench与SDR-Arena，发现当前前沿LLM在个性化任务上存在'停滞'，无法有效区分成功与失败的触达。该框架在专业销售实地部署中验证了实用性，为LLM在营销等领域的个性化应用提供了全新评估范式与实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
将贝叶斯说服框架引入生成式智能体，从两方博弈（发送者与第三方接收者）视角重新定义和评估LLM的个性化能力，突破了传统单边适应的评估局限。研究揭示了当前前沿模型在第三方说服任务上存在的'个性化停滞'现象，理论视角新颖，论证严谨且具有深刻的洞见。

### 实用性 (评分: 9.0/10)
研究聚焦销售场景的落地应用，开源了SDR-Bench和SDR-Arena，填补了生成式个性化缺乏可复现评估基准的空白。通过12名专业销售代表的实地部署验证，48%的模型生成内容被评为立即有用，专家一致性达0.82，对营销和销售领域的LLM应用具有极高的实践指导价值。

### 社区活跃度 (评分: 8.5/10)
针对LLM个性化评估的痛点提出新基准并开源，话题时效性强。揭示当前大模型在复杂个性化任务上的局限性（财富100强队列中无法区分成功与失败触达），对社区认知有重要纠偏作用，来源权威且具备引发广泛讨论的潜力。

## 项目链接
https://arxiv.org/abs/2607.20471
