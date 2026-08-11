# Flow-by-Flow:Content-Judgment Bypass for Governing AI Output in High-Loss Domains

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-11  
**来源：** rss  

## 项目描述
arXiv:2608.07474v1 Announce Type: new Abstract: Prior work showed that human-in-the-loop oversight becomes structurally untenable in high-loss domains when AI output velocity V exceeds human cognitive capacity C_max. The operative constraint, however, is not V alone but V x L, where L denotes per-item cognitive load. L consists of triage, judgment, and response, which respond asymmetrically to AI capability improvement. Triage cost does not decline as models become more capable, because semantic indeterminacy is inherent in general-purpose design. Response cost is invariant to accuracy improvements. Only judgment cost faces downward pressure, and this pressure often operates by inducing omission rather than genuine reduction. Capability improvement therefore restructures L rather than reducing it. Governance mechanisms based on evaluating whether AI output is correct either delegate that evaluation to AI and inherit hallucination risk, or delegate it to humans and face the V x L ceiling. We propose Flow-by-Flow, a governance paradigm that controls supervisory load without evaluating content. A cognitive cost score based on formal, countable features imposes nonlinear costs on high-volume production, while an institutional capacity cap keeps processing volume within C_max. We derive four design invariants for any content-judgment-bypass exceedance pathway: no content judgment, no scalable consumption of examiner capacity, identity-bound per-application friction, and no batch clearance. One reference implementation is discussed to show that these invariants are jointly satisfiable, while its practical difficulties are explicitly acknowledged. An illustrative Monte Carlo analysis across 1,000 parameter draws suggests that composite multi-metric flow control outperforms supervision reinforcement alone in 90.8% of trials.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.07474
