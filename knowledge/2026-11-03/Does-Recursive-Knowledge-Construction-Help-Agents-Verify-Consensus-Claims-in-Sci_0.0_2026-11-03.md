# Does Recursive Knowledge Construction Help Agents Verify Consensus Claims in Science?

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-03  
**来源：** rss  

## 项目描述
arXiv:2610.40906v1 Announce Type: new Abstract: Recent scientific agents build knowledge recursively by retrieving evidence, constructing an intermediate state, and judging whether that state contains sufficient information. These agents are evaluated end-to-end, usually without ground truth, so the effect of each design choice is unknown. Here, we examined two design axes: (1) what the recursion builds (the state of evidence) and (2) what controls it (the judge that decides when to stop). To measure them, we defined consensus scientific claim verification and measured these effects on this task, where a system must establish a claim's consensus stance from the open literature. We built a new consensus claim dataset, ProClaim-eval, including 718 claims with SUPPORT and REFUTE gold labels from five expert-curated databases spanning molecular biology, nuclear physics, and astronomy. Our instrument, ProClaim, persists an evidence state outside the model's context, so each axis can be studied with the other held fixed. Against verification systems and general-purpose agent harnesses, ProClaim ranks among the top three, with a significant advantage over the harnesses. We found that the evidence state improves performance over in-context accumulation, and it also matters what is stored in it. In addition, a trained judge that reads the evidence state performs better than fixed-round stopping. A judge trained separately and never exposed to ProClaim-eval achieves the highest agreement with the gold labels on three of five subsets, where it matches the off-the-shelf Claude Sonnet~4.6 judge and outperforms Claude Haiku~4.5. Our results support recursively maintaining a structured evidence state outside the model's context as an effective design for verifying claims in scientific agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.40906
