# LLM Hallucination Detection via Low-rank Multilinear Decomposition

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-28  
**来源：** rss  

## 项目描述
arXiv:2610.36191v1 Announce Type: new Abstract: Large language models (LLMs) frequently generate fluent yet factually incorrect responses, raising concerns about their reliability. Recent hallucination detectors increasingly exploit internal representations, but extracting informative signals from high-dimensional hidden states remains challenging. Existing approaches often rely on selected activations or pooling-based compression, potentially overlooking discriminative information distributed across Transformer layers, feature modes, and tokens. We propose LOTUS (Low-rank Order-statistic TUcker-based Subspace learning), a multilinear low-rank decomposition framework for hallucination detection that extracts compact representations from LLM hidden states while reducing dependence on labeled data. Our approach first summarizes variable-length token representations using complementary statistical descriptors that capture peak activations, activation distributions, and cross-layer changes. We then leverage low-rank multilinear decomposition to extract compact representations that capture the underlying structure of LLM hidden states, which are subsequently used to train a lightweight hallucination classifier. Experiments across multiple LLMs and question-answering benchmarks demonstrate improved hallucination detection performance over recent state-of-the-art baselines.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.36191
