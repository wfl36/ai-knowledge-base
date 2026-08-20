# Compiler-Guided Adaptive Proof Search with Cross-Model Synergy on Context-Dependent Theorem Proving

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-20  
**来源：** rss  

## 项目描述
arXiv:2608.18084v1 Announce Type: new Abstract: Theorem proving in real-world Lean 4 projects is challenging because proofs often depend on project-specific context. While iterative refinement can use compiler errors to repair failed proofs, reusing failed attempts requires careful search control: some proofs provide better starting points than others, and later revisions may degrade a partially correct proof. We propose a compiler-guided proof search framework that balances exploration and exploitation. It explores diverse starting points through dual-model generation and stagnation-triggered resampling, while exploiting promising proof states through current-best refinement guided by compiler-grounded pairwise comparison. Experiments on seven real-world Lean 4 projects from miniCTX-v2 show that our method achieves a better effectiveness--efficiency tradeoff than pass@k baselines. Within the pass@32 budget, our method improves average pass rate by 12.8 percentage points while reducing LLM calls by 21.9%.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.18084
