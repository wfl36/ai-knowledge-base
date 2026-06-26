# Reducing Conversational Escalation in Large Language Model Dialogue with Nonviolent Communication Constraints

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 安全对齐, 人机交互, 提示工程, 论文  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26106v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used in emotionally charged situations involving interpersonal conflict, frustration, and distress. While prior safety research has focused on preventing explicit harms such as toxic or policy-violating content, less attention has been paid to conversational behaviors that may unintentionally escalate conflict. In this paper, we investigate whether LLMs can be guided toward more de-escalating dialogue behavior through lightweight prompt-level constraints derived from Nonviolent Communication (NVC). We reformulate NVC principles as process-oriented guidelines that discourage blame attribution, emphasize attention to users' emotional experiences, and encourage clarification before advice. Using a dual-agent simulation framework across multiple instruction-tuned models and user resistance levels, we show that NVC-constrained prompting consistently reduces conversational escalation and stabilizes interactions with highly resistant users. These results suggest that simple communication constraints can meaningfully improve the trustworthiness of LLM dialogue in conflict-prone settings.

## 综合总结
本文研究了LLM在情绪激动场景下无意中加剧冲突的问题，提出将非暴力沟通（NVC）原则转化为轻量级提示约束，以引导模型产生降级冲突的对话行为。通过双智能体模拟框架验证，该方法能有效减少对话升级并稳定与高抵抗用户的交互，为提升LLM在易冲突环境中的可信度提供了简单且高效的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
将非暴力沟通（NVC）原则转化为过程导向的提示级约束，视角新颖。采用双智能体模拟框架进行评估，论证严谨，为LLM在冲突场景下的行为研究提供了新的方法论，但在模型内在机制的理论剖析上略显不足。

### 实用性 (评分: 9.0/10)
提出的NVC约束为轻量级提示方案，无需模型重训即可直接应用于现有系统，落地成本极低。对客服、心理辅导、争议调解等易冲突场景具有极高的实用价值和指导意义。

### 社区活跃度 (评分: 8.0/10)
聚焦LLM安全与对齐领域中被忽视的'无意冲突升级'问题，填补了传统安全研究仅关注毒性内容的空白，话题时效性强。arXiv论文来源可信，对提升AI系统社会信任度有积极影响。

## 项目链接
https://arxiv.org/abs/2606.26106
