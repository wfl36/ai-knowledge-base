# Large Behavior Model: A Promptable Digital Twin of the Retail Customer

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 数字孪生, 推荐系统, RAG, 强化学习, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06993v1 Announce Type: new Abstract: Customer behavior modeling underpins recommendation, marketing, and decision support, yet existing approaches either optimize predictive accuracy without explaining decisions or simulate users without grounding them in real behavioral data. We present the Large Behavioral Model (LBM) that learns customer decision making directly from large-scale retail transactions through a unified Person-Environment formulation. Customer state is represented by a behavioral profile derived from historical purchases, while product context is incorporated through retrieval-augmented generation. The model is trained using continued pre-training on verbalized behavioral data, supervised fine-tuning for decision generation, and reinforcement learning with verifiable rewards for evidence-based calibration. We evaluate the proposed framework on purchase prediction, hard-negative discrimination, basket completion, promotion response, and cross-domain voucher redemption. The model consistently outperforms frontier general-purpose language models on in-domain retail tasks while demonstrating strong zero-shot and fine-tuned transfer across retailers and decision domains. Ablation studies show that continued pre-training is the primary driver of behavioral generalization, retrieval is most effective when applied during both training and inference, and reinforcement learning improves reliance on explicit behavioral evidence over generic language-model priors. These results demonstrate that behavioral knowledge encoded in transaction histories can be effectively learned by language models, providing a scalable foundation for customer digital twins and behavior simulation.

## 综合总结
本文提出大型行为模型（LBM），通过持续预训练、SFT和强化学习三阶段范式，将大规模零售交易数据转化为语言模型可学习的行为知识，并结合RAG引入产品上下文。实验表明，LBM在零售决策任务上显著超越通用大模型，具备优秀的零样本与跨域迁移能力，为客户数字孪生和行为模拟提供了可扩展的落地基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出大型行为模型（LBM），通过统一的“人-环境”公式将客户状态与产品上下文结合。技术路线上创新性地采用了言语化行为数据的持续预训练（CPT）、决策生成的监督微调（SFT）以及基于可验证奖励的强化学习（RL）三阶段范式，并结合RAG增强产品上下文。消融实验论证严谨，清晰揭示了CPT是行为泛化的主要驱动力、RAG在训练与推理双重生效、RL能有效修正语言模型先验以依赖显式行为证据。

### 实用性 (评分: 9.0/10)
针对零售场景的购买预测、促销响应、购物篮补全等核心业务痛点，提供了可落地的客户数字孪生解决方案。模型不仅在域内任务上超越通用大模型，还展现出强大的零样本与跨域微调迁移能力，对电商、零售行业的推荐系统升级与精准营销实践具有极高的指导价值和广泛的适用范围。

### 社区活跃度 (评分: 8.5/10)
作为2026年最新发布的研究，紧扣大模型垂直领域应用与数字孪生热点。证明了交易历史中的行为知识可被语言模型有效学习并超越前沿通用模型，对工业界构建垂直领域智能体/数字孪生具有较强启发性和可信度，预计将在AI+零售社区产生显著影响力。

## 项目链接
https://arxiv.org/abs/2607.06993
