# Same Facts, Different Diagnosis: Measuring and Mitigating Narrative Anchoring in Clinical Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-31  
**来源：** rss  

## 项目描述
arXiv:2607.27384v1 Announce Type: new Abstract: Large language models used for clinical diagnostic reasoning are sensitive to sociolinguistic register, not just clinical content. We term this failure mode Narrative Anchoring: identical clinical facts expressed in different registers cause diagnostic outputs to diverge. Unlike prior demographic-bias work, which manipulates explicit identity tokens such as race or income, our benchmark isolates register as the sole channel of variation, with no demographic marker present in any form. We construct a dataset of 1,000 USMLE clinical vignettes, each rewritten into three sociolinguistically distinct personas under an independently audited fact-preservation guarantee, verified by a separate model that never sees the generation prompt. Across seven language models spanning three architecture families and scales, Narrative Anchoring is statistically significant under direct prompting in every model tested, with a Narrative Anchoring Gap of 0.064 to 0.151. Chain-of-thought reasoning and explicit debiasing instructions reduce the bias only partially, and their apparent gains are frequently confounded by accuracy collapse. We introduce NarrativeShield, a three-agent pipeline that structurally extracts and verifies clinical facts before diagnostic reasoning begins, reducing the Narrative Anchoring Gap to near-zero ($-0.004$ to $0.037$) and achieving the lowest rate of severely unstable decisions (DSS $<$ 0.8) of any method across all models, at a modest and mechanistically expected accuracy cost for most models. A stress test using a non-instruction-tuned base model shows that executing a debiasing intervention at all is gated by zero-shot instruction-following ability, not prompt content alone. We release our dataset, human-validated for fact preservation, as a standalone resource for studying register-based clinical bias.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.27384
