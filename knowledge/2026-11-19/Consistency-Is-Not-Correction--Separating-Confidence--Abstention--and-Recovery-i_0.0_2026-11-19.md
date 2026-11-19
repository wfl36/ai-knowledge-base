# Consistency Is Not Correction: Separating Confidence, Abstention, and Recovery in LLM Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-19  
**来源：** rss  

## 项目描述
arXiv:2611.21651v1 Announce Type: new Abstract: A controller that resamples an answer, escalates to a larger model, or abstains is usually justified by a confidence signal. Three claims about such a signal do not follow from one another: it ranks answers (discrimination), it supports withholding some of them (selective prediction), and it changes an answer for the better (correction utility). We give an exact decomposition of the third into gated recoveries minus gated harms, which bounds whether a comparison can succeed before it is run: a gate that only replaces a proposal can act only where the base policy was already wrong, so the initial error count caps the discordant pairs any correct gate can produce. When that cap falls below the count a paired test needs, the experiment cannot return a positive result for a working mechanism, nor distinguish one from a gate that never fired. We measure all three targets on two model scales and find the bound binds. In a small-model suite a perturbation-agreement verifier reaches within-policy AUROC 0.990 (95% interval [0.95, 1.00]) while every episode outcome matches single-sample decoding at 4.32 times the call count. In a controlled 840-episode study no verifier replaced the proposal on any of the 60 GSM8K decisions, so that comparison tested nothing; the entire GSM8K gain across six controllers is one task, and it is the task whose identical temperature-zero repeats disagreed, making it the one answer the service does not reproduce. On the diagnostic set the gate could reach four errors while the test needed six, so even a perfect gate had no significant result available. We report two checks that would have caught this before any budget was spent, and show that tie handling in rankings, tied selection cutoffs, and unequal output limits each move a headline number in the same dataset. The binding constraint on this literature is measurement resolution, not the choice of signal.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.21651
