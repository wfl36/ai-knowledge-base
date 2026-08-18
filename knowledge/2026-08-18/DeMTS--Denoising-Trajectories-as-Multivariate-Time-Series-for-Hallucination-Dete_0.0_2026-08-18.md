# DeMTS: Denoising Trajectories as Multivariate Time Series for Hallucination Detection in Diffusion Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-18  
**来源：** rss  

## 项目描述
arXiv:2608.14632v1 Announce Type: new Abstract: Diffusion large language models (D-LLMs) have emerged as a promising paradigm for text generation. However, similar to autoregressive LLMs, D-LLMs remain vulnerable to hallucinations, where fluent outputs may contain factually incorrect or unsupported content. Although existing hallucination detection methods for D-LLMs attempt to leverage uncertainty trajectories of the denoising process to better identify hallucination signals, they typically compress the trajectories along either the temporal or token dimension, overlooking the useful information encoded in the complete two-dimensional token-step structure. Consequently, they may fail to capture hallucination-relevant patterns, such as inconsistent convergence and cross-token fault propagation, leading to suboptimal detection performance. To bridge this gap, we propose a D-LLM hallucination detection framework that formulates the Denoising trajectories as Multivariate Time Series over learnable latent variables (DeMTS for short). DeMTS employs a trajectory-preserving token-to-variable assignment module to convert token signals into stable latent variables. Based on these variables, we propose dynamic multivariate temporal modeling to progressively integrate inter-variable dependency modeling with temporal encoding for hallucination prediction. Extensive experiments on two D-LLMs backbones and three benchmarks demonstrate that DeMTS outperforms existing hallucination detection methods while maintaining strong robustness, efficiency, and cross-task transferability.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.14632
