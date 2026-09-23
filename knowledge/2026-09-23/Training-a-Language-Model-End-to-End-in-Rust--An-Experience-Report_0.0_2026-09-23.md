# Training a Language Model End-to-End in Rust: An Experience Report

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.25008v1 Announce Type: new Abstract: I pretrained a language model end-to-end in Rust - alone, with no team, no PyTorch, and no Python in the training path - for $164 in rented GPU time. I report that as an achievement, not a recommendation: the more useful contribution is a measured failure taxonomy of the two leading Rust ML frameworks, Candle and Burn, as training (not inference) backends in 2026. I document five Candle defects, including fused kernels that silently produce no gradient, and three Burn defects, including a backward pass at roughly 3% of theoretical GPU throughput and a kernel-fusion path that segfaults mid-training at multi-billion-parameter scale. Every one passed ordinary loss-curve inspection; none announced itself. I describe the verification discipline that caught six such silent failures, centered on a gradient-flow arbiter: a test that runs one forward/backward pass and asserts every trainable parameter receives a finite, nonzero gradient, generalizable to any framework. The trained model (roughly 0.4B parameters, Bangla-first) shows strong Bangla language-modeling signal - a per-token negative log-likelihood of 0.93 against 12.60 for a random-initialized twin - while scoring at chance on English commonsense multiple-choice, the expected outcome of a deliberately small, Bangla-weighted budget (about 2 billion tokens, 54.6 hours, one rented H100). I also report a tokenizer-fertility trap in Bengali script: naive byte-level tokenization collapsed Bangla to roughly 1.4 characters per token against English's 3.9, silently inverting the corpus's language balance; fixing it reached roughly 4.1. To my knowledge, this is among the first documented end-to-end LM pretraining runs in pure Rust. After this run I moved training to PyTorch and kept Rust for on-device serving: in my hands, Rust is not yet a competitive place to train a language model, though it may be a good place to serve one.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.25008
