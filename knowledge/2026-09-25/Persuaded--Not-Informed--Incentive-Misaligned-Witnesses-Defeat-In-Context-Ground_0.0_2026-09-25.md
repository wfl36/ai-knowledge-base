# Persuaded, Not Informed: Incentive-Misaligned Witnesses Defeat In-Context Grounding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-25  
**来源：** rss  

## 项目描述
arXiv:2609.28854v1 Announce Type: new Abstract: Language-model agents increasingly answer questions over customer-relationship management (CRM) records, such as whether to qualify a sales lead. We identify a failure mode not addressed by a stronger model: when the context contains an assertion by a party with an incentive toward optimism - here the sales representative, a witness recorded in the CRM - the model treats the assertion as evidence and clears deals the company's own records deem unacceptable. Across 100 lead-qualification tasks from CRMArena-Pro, the representative asserts an acceptable timeline in every call and an acceptable budget in 76; on the 31 tasks where such an assertion contradicts the price list and installation policy, a model reading only the transcript clears the deal in 29 of 31 cases. The signature is consistent across seven models from four providers (misled on 87-97%); scale and explicit reasoning confer no resistance. Only 3 of 35 genuine failures involve no assertion: the failure is persuasion, not missing information. We contribute a diagnostic method rather than an architecture: (i) a bucket analysis that separates persuasion from information gaps, (ii) a same-information control showing that supplying the records to the model lowers strict accuracy from 41 to 18 while raising recall - precision collapses - and (iii) a compute-step control that holds extraction fixed and varies only who computes Budget and Timeline. The margin ranges from 42 points on an inexpensive model to 2-5 points on models that already compute correctly; on the strongest models the arms are within confidence intervals, so the pattern is a consistent direction and a soundness property, not a proved performance floor. We pre-specify a generalization test that returns a negative result, characterize the precondition (a policy exactly specified in the inputs), and release all evaluation artifacts.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.28854
