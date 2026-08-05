# MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02613v1 Announce Type: new Abstract: Edge-deployed personal memory assistants must handle private interpersonal conversations on-device with open-weight models. Yet, existing memory benchmarks often under-test the combination of activity-dense interaction, ego-centric perspective, and coherent multi-session worlds. MemArena fills these gaps with a single-world conversational benchmark built with its MASim agent simulator, for 50 agents over 15 days (10.3M dialog-text tokens, 24.1K text-only ego-observed tokens/agent/day). With the interaction history, it co-generates ground truth over six recall, reasoning, and trustworthiness evaluation dimensions. We evaluate five open-weight readers with Vanilla context, BM25-RAG, Oracle retrieval, Memobase, and MemSearch as memory backends. Three results stand out: (1) Memory-backend choice matters more for content accuracy: At Qwen3-0.6B, Memobase-to-MemSearch gains +32.5/+19.2 pp, exceeding MemSearch reader scaling (+10.6/+6.8 pp). (2) Permission-aware access fails universally, with Oracle leaking heavily and other backends too timid to disclose. (3) Search latency bites only at very small reader: on a Spark GB10 edge node, memory-search adds a moderate and fixed 87/7/48 ms (BM25-RAG/Memobase/MemSearch) that composes a small part of TTFT for most reader-backend combinations. Code, the MASim simulator, and the MemArena-L benchmark will be released upon acceptance.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02613
