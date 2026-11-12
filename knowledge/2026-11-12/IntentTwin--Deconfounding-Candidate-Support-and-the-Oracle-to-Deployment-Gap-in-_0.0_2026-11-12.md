# IntentTwin: Deconfounding Candidate Support and the Oracle-to-Deployment Gap in Offline Web Behavior Prediction

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-12  
**来源：** rss  

## 项目描述
arXiv:2611.12918v1 Announce Type: new Abstract: Offline web-behavior benchmarks frequently insert the demonstrated action into a finite candidate set and then measure reranking. We show that this protocol can create a candidate-support confound: when the target is outside training support while all distractors are sampled from that support, support membership identifies the gold action without modeling behavior. We formalize this effect with support-identifiability rate (SIR), construct support-balanced candidate sets, and evaluate a target-free dual-path proposer that combines support retrieval with open-vocabulary DOM/LM proposals. On filtered OPeRA (4,282/469/992 train/dev/test steps), the original protocol has SIR 1.0000 on target-OOV rows and a support-only rule reaches 1.0000 OOV Exact@1. Support balancing reduces SIR to 0.0000; the strongest conditional reranker obtains 0.7214 overall Exact@1, 0.7988 on IV rows, and 0.5668 on OOV rows. The target-free dual-path system reaches Proposal Recall@16 0.6915 and end-to-end Exact@1 0.5212, compared with oracle conditional Exact@1 0.7450. On Mind2Web, the same audit yields SIR 0.2380 and an oracle-to-proposal gap of 0.2125. A 200-row semantic audit labels 0.7150 of exact-key OOV targets as semantically novel, 0.2450 as locator/string variation, and 0.0400 as ambiguous (Cohen's $\kappa=0.8173$). These measurements show why support composition must be controlled alongside candidate accuracy when offline results are used to reason about deployment.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.12918
