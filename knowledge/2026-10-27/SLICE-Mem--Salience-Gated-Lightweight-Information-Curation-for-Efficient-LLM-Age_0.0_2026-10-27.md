# SLICE-Mem: Salience-Gated Lightweight Information Curation for Efficient LLM Agent Memory

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-27  
**来源：** rss  

## 项目描述
arXiv:2610.33015v1 Announce Type: new Abstract: Long-term memory enables large language model (LLM) agents to maintain personalized and temporally coherent interactions, but repeated LLM inference for memory admission, extraction, and organization introduces substantial cost and latency. We present SLICE-Mem, a lightweight memory framework that combines salience-guided admission and predicate-centered information extraction. A compact classifier identifies user turns worth retaining, and a semantic-dependency-based extractor converts admitted turns into concise memory entries. This online pipeline requires no generative LLM calls, while cross-entry reconciliation is deferred to an offline consolidation stage. We evaluate SLICE-Mem on the weekly subset of Memora and LongMemEval-S using 8B and 30B Qwen backbones for memory construction and consolidation on both benchmarks. Compared with the generative-memory baseline MemOS under the Qwen3-30B configuration, SLICE-Mem's online pipeline achieves 46.60 versus 46.68 FAMA (Forgetting-Aware Memory Accuracy) on Memora Weekly and 56.8% versus 59.3% accuracy on LongMemEval-S, while reducing total LLM token consumption by 92.4% and 99.5%, respectively. These results demonstrate that SLICE-Mem can preserve useful evidence for long-term memory with substantially less reliance on LLM-based memory construction.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.33015
