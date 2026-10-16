# Jev-as-a-Judge for RAG Claim Verification: Confidence-Gated Cascading Between a Non-Generative Verifier and a Frontier LLM

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20634v1 Announce Type: new Abstract: Retrieval-augmented generation asks one question at volume: does this evidence support this claim? The answer is one bit, yet most pipelines obtain it from a text generator and pay generation prices for the prose wrapped around it. We compare a non-generative decision model, which returns a typed value from a declared enumeration together with a native probability and no text, against a frontier LLM configured as an engineer would deploy it for binary classification. Both answer the same 495 human-labelled claims from LLM-AggreFact, so every comparison is within-item. We report three things. First, the two systems are statistically indistinguishable on the metric this task is conventionally scored by, a paired difference of -0.56 points, Jev minus Astra, at a 187-fold cost difference. Second, that tie carries almost no information about deployment: the systems disagree on 15.2% of claims, and the cheaper one admits 23.2% of the claims annotators marked unsupported against the frontier model's 14.1%. A component whose job is to catch unsupported claims should be judged on that rate, and the conventional headline hides it. Third, because the errors differ they compose: routing the claims the cheap model is confident about and escalating the rest reaches 74.10 at USD 2.92 per thousand claims against 73.83 at USD 8.93, with the threshold chosen out of fold. But a matched random-escalation control at in-sample thresholds, spending the same budget by coin flip, does as well, so what buys the saving is the escalation share and not the probability that picks what to escalate. Measured against the cheap model it is built from, the cascade costs 61-fold more for 0.83 points, 95% CI [-3.36, 4.86], and it is the more permissive guard of the two. Equal accuracy conceals unequal errors. All predictions, prompts, pricing and code are released.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20634
