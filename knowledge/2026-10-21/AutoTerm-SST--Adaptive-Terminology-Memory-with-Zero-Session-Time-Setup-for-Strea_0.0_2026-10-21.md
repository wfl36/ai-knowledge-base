# AutoTerm-SST: Adaptive Terminology Memory with Zero Session-Time Setup for Streaming Speech Translation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26865v1 Announce Type: new Abstract: Retrieval-augmented speech translation improves rare terminology, but systems such as RASST still assume that users provide a glossary before each session. That assumption is inconvenient for live talks, while merging every domain into one growing glossary eventually places too many irrelevant terms in the same retrieval and prompt competition. We present AutoTerm-SST, an interactive system that removes session-time glossary upload and domain selection. It organizes a large offline terminology catalog into topic slices, matches recent streaming translation context to bilingual slice prototypes, and activates a compact multi-slice working set under fixed retrieval and prompt budgets. On five ACL and five ESO oncology talks, AutoTerm matches a known-domain reference in terminology accuracy (88.3% vs. 88.1%) and mWER-resegmented BLEU (45.09 vs. 45.19), while requiring no domain input. Compared with a one-million-entry merged glossary, it improves terminology accuracy by 3.9 points and BLEU by 2.30. Routing plus four-slice retrieval remains lightweight: the complete system runs at 0.406 RTF, and the vLLM host sustains 32 real-time sessions. The live demo exposes active slices and retrieved terminology as the topic changes, providing zero-setup terminology-aware streaming translation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26865
