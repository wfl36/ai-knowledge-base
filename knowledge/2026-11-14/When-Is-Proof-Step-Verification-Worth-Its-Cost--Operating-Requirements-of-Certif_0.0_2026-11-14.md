# When Is Proof-Step Verification Worth Its Cost? Operating Requirements of Certify-or-Decline Verification for Open-Weight Mathematical Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-14  
**来源：** rss  

## 项目描述
arXiv:2611.14794v1 Announce Type: new Abstract: Proof-step verification rewrites a solver's answer into typed steps and uses LLM judges to certify or decline. We evaluate this pipeline on open-weight models across GPQA, AIME-2025, and a MATH-500 subset. Certification raises answer-key-match precision by 31 percentage points on the strong GPQA configuration and 46 on AIME, while answering only 35% and 21% of attempts. On near-ceiling MATH-500, gains are at most 5 points at a loss of 13-27 points of coverage. An output-token-matched self-consistency selector obtains 82.9% precision at 35% coverage, compared with the verifier's pooled 87.6% (paired difference: +4.8 points, 95% interval [-8.2, 18.5]). A diagnostic sample reveals a distinct failure mode: 52 of 88 completed problems end in invalid proof construction without ever reaching a judge. Finally, external-LLM acceptance of rendered certified chains is 61.0-67.6%, compared with 87.6% answer-key match. These audits lack human or formal-kernel ground truth. Open-weight auditor pairs show near-zero chance-corrected agreement, which measures consistency rather than accuracy against proof truth. These results motivate separate reporting of execution failures, selected-answer precision, and independently assessed proof validity. We provide per-configuration results and evaluation details in the supplement.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.14794
