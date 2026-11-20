# DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-20  
**来源：** rss  

## 项目描述
arXiv:2611.21925v1 Announce Type: new Abstract: Speculative-diffusion decoding uses a small parallel drafter model to generate b draft tokens in one forward pass, which then undergo parallel verification via a larger target model. Faster inference can be achieved when multiple draft tokens pass verification simultaneously. Recent parallel draft architectures (DFlash, DSpark) improve draft quality by conditioning on rich features computed by the target, through a mechanism known as feature encoding. However, standard feature encoding mechanisms have three limitations: (1) they are lossy, applying encoding projections that are destructive to the underlying target feature-space via a discovered effect known as residual mixing, (2) they are memory-less, with no record of previously processed proposals, and (3) they utilize features sampled uniformly from across the target layers, omitting important hidden states. To address these issues, we propose Mixture-of-Features Attention (MoFA), a lightweight feature-encoding approach equipped with a working memory that encodes previously rejected proposals. Leveraging MoFA, rejection memory, and a set of further enhancements, including 2-tap causal convolutions, prefix-only cross-attention, and non-uniform target layer selection, the final architecture, DNeo, achieves 1.3x faster generation speed than SoTA (DFlash-2) without impacting drafter footprint or generation quality. DNeo marks a new state of the art in high quality, fast LLM inference.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.21925
