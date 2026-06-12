# Deployment-Centered Evaluation: Predicting Query-Level Rejection Risk in a Clinical LLM System

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 评估体系, 医疗AI, 部署评估, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12702v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly integrated into clinical systems, making it essential to evaluate the real-world utility of these systems. However, static benchmarks tend to measure correctness rather than user acceptance, aggregate performance across queries, and require densely annotated datasets -- leading to major blind spots for evaluating clinical systems. In this work, we perform a deployment-centered evaluation of an LLM system embedded within electronic health records at an academic medical center, where user feedback is sparse but closely reflects the deployment conditions. Specifically, we train a pre-response classifier that estimates the risk that a future interaction will result in the user rejecting the LLM response, based on query content and deployment-specific context available before generation. We conduct a prospective analysis of our model over 4.5 months of user feedback, finding that our prediction model achieves an AUROC of 0.719. Further, we estimate the benefit of such predictions in two downstream use cases (guardrail triggering and abstention). Our key conceptual insight is that making use of deployment-specific context (i.e., the provider type, department name, language model used for response), as opposed to only query content, improves the ability to predict whether the user will reject the system output. Altogether, our empirical case study demonstrates the feasibility of predicting user rejection using deployment-specific context, opening the door to targeted guardrails.

## 综合总结
本文针对临床LLM系统在真实世界中的评估盲区，提出以部署为中心的评估方法。研究在学术医疗中心的EHR系统中，训练了一个预响应分类器，利用查询内容及部署上下文（如科室、医生类型等）来预测用户拒绝LLM输出的风险。4.5个月的前瞻性研究表明，引入部署上下文能显著提升预测效果（AUROC 0.719），并可用于下游的安全护栏触发和模型拒答机制，为高风险场景下的LLM安全部署提供了极具实操性的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出了一种以部署为中心的评估范式，从传统的静态基准测试（侧重正确性）转向预测真实世界中的用户接受度。技术上，通过训练“预响应分类器”，结合查询内容和部署特定上下文（如提供者类型、科室、模型版本），实现了在LLM生成前对用户拒绝风险的预测。4.5个月的前瞻性分析证明了该方法的有效性（AUROC 0.719），核心洞见在于：引入部署上下文比单纯依赖查询内容更能显著提升拒绝风险的预测能力。

### 实用性 (评分: 9.0/10)
具有极高的落地参考价值。该研究直接解决了LLM在医疗等高风险场景部署时的安全性与可用性痛点。通过在生成前预测拒绝风险，系统可以提前触发安全护栏或选择拒答，从而避免潜在的医疗风险和不良体验。该方法不仅适用于临床，其利用上下文预测拒绝风险的思路可广泛迁移至各类企业级LLM应用中，指导开发者构建更稳健的防御机制。

### 社区活跃度 (评分: 8.5/10)
话题极具时效性，LLM的真实世界评估与对齐是当前AI社区关注的核心痛点。作者团队包含知名学者（如Nigam Shah, Sanmi Koyejo），学术背景强大。研究基于真实的电子病历系统进行了长达4.5个月的前瞻性验证，数据来源和结论极具权威性与可信度，对医疗AI和LLM评估社区有重要的示范意义和影响力。

## 项目链接
https://arxiv.org/abs/2606.12702
