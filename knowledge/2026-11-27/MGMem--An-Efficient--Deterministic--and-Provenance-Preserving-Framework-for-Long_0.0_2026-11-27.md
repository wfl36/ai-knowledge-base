# MGMem: An Efficient, Deterministic, and Provenance-Preserving Framework for Long-Horizon Agent Memory

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-27  
**来源：** rss  

## 项目描述
arXiv:2611.33174v1 Announce Type: new Abstract: Long-horizon Large Language Model (LLM) agents need persistent memory that surfaces the right past interaction at the right time across thousands of turns. Many systems index by invoking generative LLMs to rewrite history into summaries, facts, or knowledge graphs--a step that is (a) costly (thousands of generative calls per build), (b) non-deterministic (undermining reproducibility and giving inconsistent answers across runs), and (c) provenance-erasing (the reader sees synthesized text, not the original turn). We propose MGMem, a framework with no generative indexing calls that replaces this step with a deterministic discriminative-parser pipeline: recurring mentions across sessions are organized into an incidence graph, question mentions are resolved by a subject-conditioned three-stage resolver, and raw dialogue episodes are returned to the reader. On English multi-session dialogue QA, MGMem outperforms matched-protocol baselines on LoCoMo without generative indexing calls; on the full LongMemEval-S, it remains competitive overall and leads or ties on single-session types among local retrieval comparisons. Code: https://github.com/junhong-h/MGMem

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.33174
