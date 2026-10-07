# WavePrune: One period is often enough for RoPE

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-07  
**来源：** rss  

## 项目描述
arXiv:2610.06963v1 Announce Type: new Abstract: Rotary Position Embedding (RoPE) encodes token positions by rotating each two-dimensional channel of the query and key vectors at a channel-specific frequency, making the attention logits invariant to a common shift of positions. However, this rotation is periodic, and it leads to position aliasing where relative positions separated by a full rotation period become hard to tell apart. To address this, we propose WavePrune, which restricts each channel to its first rotation period. We show that it removes the distractions in attention maps created by position aliasing and improves overall long-context performance. Specifically, WavePrune raises the HELMET score on four of five models we test without any extra tuning (e.g., 35.7 -> 40.0 on Qwen3-8B). When pretraining models from scratch, WavePrune also achieves lower validation loss at extrapolated lengths than pretraining without it. Because WavePrune restricts each channel to a sliding window, it induces a fine-grained sparsity that our hardware-aligned CUDA kernels exploit for 1.15x prefill and 1.24x decoding speedups over FlashAttention-2 at 32K context. Together, these results show that RoPE's periodic structure, widely regarded as essential, is largely redundant beyond the first rotation period.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.06963
