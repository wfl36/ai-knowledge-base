# EntropyMoE: Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06398v1 Announce Type: new Abstract: Recent byte-level large language models (LLMs) have made tokenizer-free modeling increasingly competitive by grouping bytes into dynamically sized patches. However, existing byte-patch architectures still apply the same dense feed-forward computation to every patch. This uniform computation cannot adapt model capacity to variations in patch semantics and granularity. We address this limitation with EntropyMoE, a Mixture-of-Experts (MoE) architecture designed for dynamic byte patches. EntropyMoE replaces the dense feed-forward modules in the global patch Transformer with Top-K expert layers. Each dynamic patch serves as the basic unit of expert routing, and its byte coverage determines its contribution to workload accounting. The router selects experts directly from patch entropy, using the same granularity signal that underlies dynamic patch construction to organize sparse computation. Patch entropy and length jointly define the feature space for regulating expert specialization. Experiments show that EntropyMoE achieves the lowest held-out bits-per-byte among matched dense and sparse baselines while maintaining comparable downstream accuracy. These results establish patch entropy as an effective routing coordinate for sparse conditional computation and extend Mixture-of-Experts modeling beyond tokenizer-based representations.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06398
