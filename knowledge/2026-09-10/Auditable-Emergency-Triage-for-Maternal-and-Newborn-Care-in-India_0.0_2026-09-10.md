# Auditable Emergency Triage for Maternal and Newborn Care in India

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-10  
**来源：** rss  

## 项目描述
arXiv:2609.09356v1 Announce Type: new Abstract: At Noora Health, our nurses answer more than 50,000 medical queries per month on our WhatsApp-based service that provides caregivers with on-demand support. Their most time-critical task is emergency triage: deciding which queries need immediate in-person attention. To support them, we built a system that uses a large language model (LLM) to classify whether a message is an emergency and provide a rationale for interpretability. But the system was opaque: analyzing mistakes meant reading reasoning chains for each message, which is infeasible at our scale. Prompt changes meant re-running a full evaluation to prevent regressions, which was both costly and operationally challenging. Clinicians follow a decision tree to make this call, but it was never documented or passed to the model, which relied on a flat list of danger signs. To address these issues, we decomposed triage into two steps: an LLM extracts canonical symptoms and patient context from the query using a clinician-authored vocabulary, and a deterministic rule engine captures the scenarios that indicate an emergency. We show that the new system raised recall from 0.565 to 0.810 and F1 from 0.606 to 0.702, with structured rules driving most of the accuracy gains while the decomposition provides auditability: clinical experts can inspect each stage of the new system to see whether the query was mistranslated, symptoms were incorrectly extracted, patient context was wrongly inferred, or the necessary rules were missing. They can add new rules independently without causing regressions and avoid running costly evaluations. Since deployment, the new system has triaged 152,421 patient queries and flagged 28,535 (18.7%) as emergencies. The over-escalation rate has been 17.8%, without any increase in missed emergencies. Clinicians have also added 48 new rules since deployment, evidence of the faster correction loop we set out to build.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.09356
