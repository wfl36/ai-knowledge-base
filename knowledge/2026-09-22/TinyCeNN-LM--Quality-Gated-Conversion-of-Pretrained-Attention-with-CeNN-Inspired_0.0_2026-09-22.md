# TinyCeNN-LM: Quality-Gated Conversion of Pretrained Attention with CeNN-Inspired Cellular-Recurrent Layers

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.21139v1 Announce Type: new Abstract: Replacing attention in a pretrained language model is a compatibility problem: a plausible substitute may alter representations expected by later layers. TinyCeNN-LM introduces a \emph{quality-gated post-training conversion} framework using CeNN-inspired cellular-recurrent layers with bounded local processing, compact recurrent memory, routing, fusion, and accept-or-rollback validation. Three implementations are studied: Integrated Memory, MemoryFusion, and PDelta3-GDN2-CLVR+Local32. Strict PDelta3 conversion accepts a layer only when representation and NLL criteria pass fixed thresholds. On SmolLM2-135M, layers 0-2 are accepted with cumulative $\Delta\mathrm{NLL}=+0.01209$, while layer 3 is rejected despite acceptable NLL because representation fidelity fails. On Qwen3.5-0.8B, full-attention layers 3, 7, and 11 are accepted with final $\Delta\mathrm{NLL}=+0.02073$. Integrated Memory keeps perplexity within $-0.07\%$ to $+0.93\%$ while reducing total cache by up to $6.01\%$. A sampled 200-item downstream sanity check gives $28.5\%$--$32.0\%$ overall accuracy for converted Qwen releases. The results support conservative, quality-gated structural conversion rather than universal attention replacement or speedup.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.21139
