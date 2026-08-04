# Empowering Cross-Domain Sequential Recommendation with Hybrid Tokenization and Serial-Parallel Decoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-04  
**来源：** rss  

## 项目描述
arXiv:2607.28659v1 Announce Type: new Abstract: Cross-domain sequential recommendation (CDSR) aims to model users' dynamic interest transitions and sequential patterns across multiple domains. Recently, generative recommendation (GR) has emerged. It first learns semantic identifiers (SIDs) from item semantics and formulates recommendation as autoregressive generation. However, existing methods face two critical issues: (1) they ignore collaborative correlations across domains during tokenization, and (2) they adopt inefficient decoding strategies, such as beam search, during generation, which hinders real-time deployment. To address these limitations, we propose GenCDSR, an effective and efficient generative framework for CDSR. Specifically, we design a cross-domain hybrid tokenization mechanism with a multi-tower architecture to jointly capture cross-domain commonalities and domain-specific distinctions through hierarchical shared-specific and fine-grained codebooks. Furthermore, we develop a cross-domain serial-parallel decoding strategy that leverages the hierarchical SID structure to partially parallelize generation, significantly reducing inference latency while preserving generation consistency. Experiments on three public datasets show that GenCDSR achieves an average accuracy improvement of 1.5 percent and an average inference latency reduction of 85.1 percent compared with state-of-the-art baselines. The implementation code and datasets are available online: https://github.com/Applied-Machine-Learning-Lab/RecSys2026_GenCDSR.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.28659
