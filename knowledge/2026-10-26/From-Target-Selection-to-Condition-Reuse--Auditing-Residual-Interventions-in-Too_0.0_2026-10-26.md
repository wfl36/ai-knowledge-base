# From Target Selection to Condition Reuse: Auditing Residual Interventions in Tool-Use Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-26  
**来源：** rss  

## 项目描述
arXiv:2610.31686v1 Announce Type: new Abstract: Activation interventions can make a language model produce a target answer, but can the model use the intended condition in other computations? We study this question in Qwen3.5-27B on tool-use tasks where time or permissions determine eligibility and selection. Across 32 fresh worlds, two case-specific residual-writing variants raise familiar target-selection correctness from 35/128 to 119/128 and from 33/128 to 114/128. Yet these gains disappear when familiar facts and identifiers are recombined within the same selection task, while selection of previously rewarded identifiers increases. The gains persist across output formats but yield little improvement in independent judgments about whether a candidate is eligible or should be selected. Internal edits can nevertheless change how a source fact affects a judgment: in a prespecified secondary comparison, an early-layer source patch changes 50/64 judgments when that source is used, with one adverse change among 64 cases where it is not. This selective effect does not ensure correct complete actions. Together, these results separate target-selection control, condition-sensitive judgments, and complete-action correctness. Evaluating how an edited state is used, rather than only its trained answer, exposes these differences.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.31686
