# Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-03  
**来源：** rss  

## 项目描述
arXiv:2607.28636v1 Announce Type: new Abstract: LLMs increasingly serve as automated judges, but their judgments remain vulnerable to cognitive biases. Existing mitigations mostly rely on prompt-driven debiasing, which is brittle across bias types, or human evaluation, which does not scale. We study \emph{Chain-of-Models} (CoM), an automated audit pipeline in which a second model inspects the first model's reasoning trace before producing the final judgment. The key design question is whether the auditor should be the same model, a same-family model, or a different-family model. Across 9 models from 6 families, 4 cognitive biases, and 4 factual datasets, we find that auditor identity matters in two ways. First, standalone bias resistance does not predict audit effectiveness: Kimi-K2.5 is the strongest standalone model on several biases, yet is a weak auditor for Qwen2.5-72B's biased traces. Second, the best auditor is bias-specific: GPT-4o is strongest on bandwagon, authority, and distraction, while GLM-5 is strongest on sycophancy. We operationalize these findings with a per-bias auditor selection rule that, given the bias type, scores candidates along functional diversity, per-bias standalone resistance, and calibrated audit effectiveness. Under a calibration/test split, the selector reaches the highest accuracy across the four biased slices ($0.884$ vs.\ $0.824$ for the strongest single fixed auditor and $0.805$ for the no-audit baseline). We release data, configurations, and an LLM-agent skill at https://anonymous.4open.science/r/chain-of-models-B585 .

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.28636
