# Cross-Prompt Reuse of Entity-Replacement Responses

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-04  
**来源：** rss  

## 项目描述
arXiv:2611.00352v1 Announce Type: new Abstract: With model weights fixed, we measure how much of an entity-replacement response transfers between English factual questions, beyond whether answers change. We add the hidden-state change from two source questions to a target question about the same entity, comparing the predicted log-probability shift between two relations' published answers, given known answer prefixes, with the measured one. Hidden reuse injects the aligned change at 50% depth before the target's remaining layers; direct reuse adds source output-score changes. With other-relation sources, hidden reuse removes 45% and 49% of no-change error on 0.5-1B Qwen and Llama. Gemma-2-2B removes 22% and passes one of three comparisons in plain text without its default beginning-of-sequence (BOS) token. A later protocol restoring it yields 58-68%, passing every comparison on three cohorts. Larger checkpoints, chat format and new entities show replication and format- or cohort-dependent failures. On small plain-format checkpoints, other-relation hidden reuse mainly reproduces the shift both relations' questions share, without reliably lowering relation-selective error. With target-relation sources, hidden reuse's post hoc advantage over direct reuse is 0.2-0.9 nats outside chat format, unconfirmed and not replacement-specific. The same relation-neutral change at both questions' entity tokens lowers relation-selective error more than random or other-replacement changes, indicating receiving-question dependence.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.00352
