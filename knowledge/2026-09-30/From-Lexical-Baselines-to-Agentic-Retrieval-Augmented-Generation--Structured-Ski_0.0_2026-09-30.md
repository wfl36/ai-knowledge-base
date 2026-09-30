# From Lexical Baselines to Agentic Retrieval-Augmented Generation: Structured Skill and Responsibility-Level Extraction with the SFIA Framework

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35806v1 Announce Type: new Abstract: Automated skill extraction underpins workforce planning, yet most systems represent skills as flat labels with no notion of the responsibility level at which a skill is practiced. The Skills Framework for the Information Age (SFIA) captures exactly this dimension, defining 147 professional skills across seven responsibility levels, but no automated LLM-based extraction targeting SFIA has been reported. We formalize the task as structured prediction of (skill, level) pairs from free text and ask three questions: how accurately can text be mapped onto SFIA's closed vocabulary, which strategies reliably predict the level alongside the skill, and do agentic designs improve on simpler retrieval and prompting? We evaluate five strategies (a lexical baseline, dense retrieval with LLM reranking, a zero-shot schema-constrained LLM, single-agent agentic RAG, and a three-agent retriever--matcher--verifier crew) against expert-mapped European ICT role profiles, all drawing on an SFIA~9 corpus built by a fully automated agentic pipeline that we release. Retrieval-based matching identifies the most skills while generative strategies are markedly more precise; only strategies assigning the level as an explicit decision predict it reliably, with similarity-based selection more than twice as inaccurate; and the crew doubles latency without improving accuracy, so added agent roles do not automatically benefit closed-taxonomy matching. These results provide the first reproducible baseline for structured, level-aware skill extraction against SFIA.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35806
