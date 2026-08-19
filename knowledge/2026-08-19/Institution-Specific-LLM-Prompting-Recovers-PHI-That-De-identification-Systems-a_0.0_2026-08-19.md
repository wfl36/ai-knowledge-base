# Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-19  
**来源：** rss  

## 项目描述
arXiv:2608.17051v1 Announce Type: new Abstract: Secondary use of electronic health records requires de-identification, yet existing systems miss \emph{institutionally situated} protected health information (PHI) such as hospital abbreviations, building names, and internal codes whose status is locally determined. We ask whether large language models (LLMs) with in-context learning (ICL) can close this gap and control the precision--recall trade-off. On 100 annotated pediatric oncology notes (5,322 PHI spans) from Texas Children's Hospital, we benchmarked eight LLMs against two purpose-built systems (Stanford TiDE, OpenMed PII) and two pattern-based baselines. Each LLM ran under three prompts of increasing specificity: (1) a HIPAA-aligned baseline, (2) baseline plus the institutional PHI categories it missed, and (3) prompt 2 plus instructions against over-redacting clinical content. We then compared 14~multi-agent and ensemble configurations against the best single prompt, with recall the primary safety metric. LLMs outperformed the purpose-built systems (best F1=0.918$\pm$0.001 vs.\ TiDE 0.779), with advantages concentrated in contextual categories. Naming the missed categories recovered 79\% (48/61) of them, and discouraging over-redaction restored precision. No agentic architecture beat calibrated single-pass prompting (F1 0.906--0.907), but LLM outputs surfaced 414~candidate annotation gaps; re-annotation confirmed 227~PHI spans, against which the final prompt reached recall=0.981 (F1=0.907$\pm$0.002). Well-calibrated ICL resolves both the institutional PHI gap and the precision--recall trade-off in one LLM call per note. LLMs cost more to run than traditional methods, but that cost buys a way to audit the reference standard. LLMs are a legitimate, adaptable alternative to purpose-built de-identification systems; institution-specific prompt development should be the primary adaptation strategy.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.17051
