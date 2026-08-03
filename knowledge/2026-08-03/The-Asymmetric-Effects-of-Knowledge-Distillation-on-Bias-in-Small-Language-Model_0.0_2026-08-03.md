# The Asymmetric Effects of Knowledge Distillation on Bias in Small Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-03  
**来源：** rss  

## 项目描述
arXiv:2607.28639v1 Announce Type: new Abstract: We show that knowledge distillation in small instruction-tuned language models has asymmetric effects on bias. On unambiguous tasks (BBQ-disambig), response-based distillation from a Gemma-2-9B teacher improves context-following: for the most biased baseline (SmolLM2-1.7B-Instruct), it cuts the context-overriding error rate from 44% to 24%. On ambiguous tasks (BBQ-ambig), the same distillation destroys per-item refusal calibration: 15% of items where the baseline correctly abstained instead receive stereotype answers, even when overall refusal rate is preserved. The pattern reproduces on a second student family (OLMo-2-1B-Instruct), with silence-loss of 8% and filled-silence accounting for 89% of new bias. Across the full 28-configuration grid, the magnitudes of silence-loss and filled-silence are uncorrelated (Spearman $\rho=0.19$, n.s.), indicating that the two effects arise from distinct mechanisms. Aggregate stereotype metrics (CrowS-Pairs, overall BBQ Stereotype Reliance Score) average over both effects and conceal the per-item harm. We trace the calibration loss to a data-side mechanism: an audit of four training corpora finds <0.5% refusal-as-answer-shape. Supervised fine-tuning (SFT) with refusal injection either breaks parsing or over-corrects into a trivial-refuser regime (refusal rate 99.8%, disambig accuracy 0.2%) that aggregate metrics would call perfectly calibrated. We propose Per-Condition Calibration Diagnosis (PCCD), a three-step protocol that evaluates refusal calibration, context-following, and capability preservation. PCCD catches both the asymmetric harm and the trivial-refuser failure mode that aggregate evaluations miss.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.28639
