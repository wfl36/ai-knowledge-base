# SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-07  
**来源：** rss  

## 项目描述
arXiv:2608.05204v1 Announce Type: new Abstract: LLM-agent ecosystems are rapidly growing around reusable skills: mixed-modality packages of metadata, natural-language instructions, code, tools, references, and operational workflows. As skills become marketplace artifacts, auditing their reuse is no longer the same problem as ordinary code clone detection. Existing detectors target single-modality source code or whole-package similarity, yet skill reuse evidence is distributed across authored text, implementation fragments, and operational structure. As a result, they can miss reuse that preserves only one part of a skill. We present SKILLTRACE, a multi-trace provenance auditing framework for LLM-agent skill reuse. SKILLTRACE extracts three provenance traces: Expression, Implementation, and Operational. It represents the Operational Trace as a Skill Operational Graph (SOG) that captures activation, procedure, and resource-flow structure. An LLM assists only the Operational-trace extraction, once at ingestion; at audit time SKILLTRACE compares cached traces deterministically, calibrates each trace against same-function strict negatives, and reports which trace supports a reuse decision. On SKILLTRACE-BENCH, with 820 transformed reuse positives over 100 marketplace anchors and 751 negative controls, SKILLTRACE achieves AUROC 0.938 and F1 0.898. A 36,446-skill wild audit further shows that trace-attributed evidence surfaces actionable reuse review queues beyond repository-level baselines.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.05204
