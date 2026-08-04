# AgentMemBench: A Systematic Benchmark for Evaluating Long-Term Memory Management Strategies in Conversational AI Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-04  
**来源：** rss  

## 项目描述
arXiv:2608.00009v1 Announce Type: new Abstract: Long-term memory remains a critical bottleneck for conversational AI agents, whose finite context windows cannot support coherent recall across thousands of turns. We present AgentMemBench, a unified, reproducible benchmark evaluating five memory management strategies under identical conditions: in-context windowing (ICW), external key-value store (EKV), graph-based episodic memory (GEM), compression-based summarisation (CBS), and web-augmented memory (WAM). All are assessed across three public datasets covering long-term multi-session dialogue (LoCoMo), task-oriented document grounding (MultiDoc2Dial), and persona-grounded multi-session chat (MSC), using Recall@k, MRR, nDCG@k, Answer F1, an LLM-judge Faithfulness score, Memory Footprint, and Latency over 491 annotated question turns. Generation and judging both use Qwen2.5-7B-Instruct (4-bit), with greedy decoding for determinism. Our results show that (1) EKV dominates on every quality axis (macro Recall@5 0.792, MRR 0.677, F1 0.156, Faithfulness 0.354); (2) long-range recall is decisive: on LoCoMo, where the gold turn lies many sessions back, ICW, WAM, GEM, and CBS retrieve almost nothing (Recall@5 <= 0.005) while EKV alone reaches 0.573, showing that recency windows, summaries, and entity graphs collapse at long horizons and only dense retrieval scales; (3) CBS is the runner-up on retrieval (0.556); (4) WAM equals ICW on in-corpus recall by construction, since external results carry no in-corpus provenance; and (5) EKV's recall advantage carries a footprint cost (~5,100 vs ~300 tokens for ICW/WAM), an explicit accuracy-efficiency trade-off. We additionally evaluate two published memory systems (MemGPT/Letta, HippoRAG) against the same harness, and release all code, environment, and result artefacts for full reproducibility.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.00009
