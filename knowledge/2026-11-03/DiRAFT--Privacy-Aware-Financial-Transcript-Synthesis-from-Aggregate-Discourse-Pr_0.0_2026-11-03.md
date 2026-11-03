# DiRAFT: Privacy-Aware Financial Transcript Synthesis from Aggregate Discourse Priors

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-03  
**来源：** rss  

## 项目描述
arXiv:2610.40938v1 Announce Type: new Abstract: Using customer conversations to train and evaluate financial language models raises confidentiality concerns because non-public financial facts can remain after direct identifiers are masked. Synthetic transcripts offer an alternative data source, but their discourse fidelity and residual confidentiality risks require assessment. We introduce DiRAFT (Discourse Realization from Aggregate First-order Transitions), which extracts financial concept graphs and records the order in which concepts are first introduced. It pools adjacent concept transitions across training records and samples new graph plans from aggregate transition, starting-concept, and plan-length priors. A discourse layer guides text realization without supplying an individual source passage or graph. We assess privacy-related risks through two complementary evaluations: corpus-level structural overlap and source-grounded checks for specific non-public investor facts. The structural assessment covers two financial corpora and three generation backends. The confidential-fact assessment uses human review of 1,400 investor-call outputs across seven strategies and two backends. We also evaluate transition fidelity, content recoverability, and trajectory diversity. Stochastic sampling provides a favorable balance between transition fidelity and structural overlap, with consistent advantages over greedy and top-3 on investor calls. The confidential-fact assessment likewise detects fewer matches for stochastic sampling than these alternatives on both backends covered by the fact assessment. These complementary assessments provide empirical evidence on residual confidentiality risks without establishing a formal guarantee.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.40938
