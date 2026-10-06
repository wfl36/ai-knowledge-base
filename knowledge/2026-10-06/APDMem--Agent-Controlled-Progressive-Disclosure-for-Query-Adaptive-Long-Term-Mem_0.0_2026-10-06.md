# APDMem: Agent-Controlled Progressive Disclosure for Query-Adaptive Long-Term Memory

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-06  
**来源：** rss  

## 项目描述
arXiv:2610.02472v1 Announce Type: new Abstract: Personalized LLM assistants must recover sparse evidence from long conversation histories across queries of varying complexity. We introduce APDMem (Agent-controlled Progressive Disclosure Memory), a hierarchical long-term memory architecture that applies progressive disclosure to memory retrieval. Rather than relying on a flat memory store or fixed retrieval granularity, APDMem represents conversation history as four progressively detailed layers: thematic summaries, personalized key facts, turn-level evidence notes, and raw messages. At inference time, a controller applies progressive disclosure to the memory hierarchy: it first reads high-level summaries and drills into finer evidence only when needed. This creates an adaptive cost-fidelity trade-off: simple queries can terminate early, while complex temporal, multi-hop, or exact-evidence queries trigger deeper inspection. A note synthesizer converts retrieved evidence into a query-focused structure that consolidates facts, orders events, and flags contradictions before final answer generation. Experiments on LongMemEval show that APDMem achieves strong performance for long-context memory reasoning while accessing only 8% of the total conversations.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.02472
