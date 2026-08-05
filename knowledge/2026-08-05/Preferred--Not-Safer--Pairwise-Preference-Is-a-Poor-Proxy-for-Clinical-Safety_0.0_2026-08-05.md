# Preferred, Not Safer: Pairwise Preference Is a Poor Proxy for Clinical Safety

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02617v1 Announce Type: new Abstract: We evaluate whether clinician pairwise preferences provide a reliable signal of clinical safety in large language model (LLM) evaluation using expert feedback from MOOVE (Massive Open Online Validation and Evaluation), a clinician-led platform collecting blinded pairwise preferences alongside multi-criterion rubric ratings. Clinicians assign scores on a discrete $[-2, +2]$ scale, where negative values indicate clinically unsafe or misleading content. Using 26{,}804 pairwise judgments across outputs from 13 LLMs, contributed by more than 736 clinicians across 28+ countries, we find that clinician preference is a poor proxy for safety-critical performance. Models ranking highly under pairwise preference can still exhibit substantial rates of clinically meaningful failures ($\leq -1$) on dimensions such as \emph{Harmlessness} and \emph{Accuracy}. These failures are unevenly distributed across specialties, creating domain-specific ``no-go zones'' not visible in aggregate rankings or single-number leaderboards. We further analyze contributing factors including prompt length, refusal and escalation behavior, and the relative contributions of safety-critical versus surface-level features. A substantial fraction of preference votes carry no positive safety signal, while feature decomposition shows that surface-level characteristics explain slightly more preference variation than safety-critical rubric differences. Finally, we introduce a clinically adjusted preference ranking combining pairwise preference with rubric-derived feedback, producing a more safety-aware ordering than raw Bradley--Terry strength alone. Our findings support evaluation practices that separate preference from safety, report safety-critical failure rates directly, and incorporate clinically grounded adjustments when ranking LLMs for clinical decision making.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02617
