# Cost-Effective Automated Judging of Natural-Language Mathematical Proofs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-04  
**来源：** rss  

## 项目描述
arXiv:2608.00004v1 Announce Type: new Abstract: Grading natural-language mathematical proofs is a recurring cost in evaluating math-reasoning systems, and frontier LLM judges are expensive. We ask whether cheap open-weight models can serve as reliable judges given a candidate proof, a ground-truth proof, and a human-grading rubric. On a 200-instance validation sample of IMO-GradingBench, three cheap judges (GPT-OSS 120B, DeepSeek-V4 Flash, Gemma-4 31B) agree with human pass/fail decisions at rates statistically indistinguishable from Claude Opus 4.7 and Gemini 3.1 Pro, at up to $100\times$ lower cost. We had expected a majority vote of the three to be the best budget option; it matched the frontier but did not improve on its strongest member. Extending to the full 1000-instance benchmark and exploring consensus rules, we found that requiring unanimous agreement (all-three-pass) reaches the highest pass-agreement and precision and, on four replicate runs, the smallest run-to-run spread. The headline finding is that cheap judges are competitive with the frontier at one to two orders of magnitude lower cost; as a deployable default we recommend all-three-pass, with the caveat that this rule was identified post-hoc and warrants independent replication.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.00004
