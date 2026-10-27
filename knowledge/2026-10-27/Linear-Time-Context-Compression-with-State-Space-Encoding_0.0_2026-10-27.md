# Linear-Time Context Compression with State-Space Encoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-27  
**来源：** rss  

## 项目描述
arXiv:2610.33006v1 Announce Type: new Abstract: Transformer-based large language models (LLMs) impose substantial computation and memory costs as context sizes increase, motivating methods that compress a context into a shorter representation before inference. Existing soft-prompt compression methods typically use the same Transformer backbone as used in the target model, where producing the compressed representation leads to significant latency overheads. This restricts them to the offline setting where context is compressed once and then reused across many queries. We propose the Boa Compressor, a plug-and-play online context compressor built on a Mamba state-space model (SSM) that encodes arbitrary-length context in a single linear-time pass, producing a representation on which we condition a frozen target LLM. The SSM is trained by distillation, matching the next-token logit distribution from the LLM ingesting the full context (as teacher) to the same LLM ingesting the compressed representation (as the student). At equal compression ratios, Boa matches or surpasses the performance of existing state-of-the-art offline compression baselines, while being an order of magnitude faster than Transformer-based implementations, thereby reducing end-to-end latency rather than adding compression time overhead. We demonstrate that Boa also scales well to longer contexts and to compression ratios as aggressive as 16x. By enabling effective compression that is cheap enough to run on every query at inference time, Boa becomes a practical and general tool for efficient long-context inference.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.33006
