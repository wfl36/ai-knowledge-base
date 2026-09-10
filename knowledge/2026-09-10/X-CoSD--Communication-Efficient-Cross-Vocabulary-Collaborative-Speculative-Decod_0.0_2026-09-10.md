# X-CoSD: Communication-Efficient Cross-Vocabulary Collaborative Speculative Decoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-10  
**来源：** rss  

## 项目描述
arXiv:2609.09166v1 Announce Type: new Abstract: This paper investigates collaborative speculative decoding (CoSD), a distributed large language model (LLM) inference framework in which an on-device small language model (SLM) drafts candidate tokens and a server LLM verifies them. Existing CoSD methods assume a shared vocabulary between the SLM and the LLM and incur substantial communication load because residual resampling requires token distribution exchange between the user device and the edge server. To address these limitations, we propose cross-vocabulary CoSD (X-CoSD), a lossless and communication-efficient CoSD framework for heterogeneous SLM-LLM vocabularies. X-CoSD is built on hybrid resampling (HR), which splits residual resampling across the common-vocabulary region on the device and the LLM-only region on the server, so that distribution transmission is required only for the common-vocabulary region. We further propose X-CoSD-E, an enhanced variant based on server resampling with device verification (SR-DV), in which the server sends only replacement candidates sampled from the server LLM and their corresponding probabilities for local verification at the device. We prove that both X-CoSD and X-CoSD-E preserve the server LLM distribution, and experiments show that they significantly improve token generation speed while maintaining generation quality comparable to that of the server LLM.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.09166
