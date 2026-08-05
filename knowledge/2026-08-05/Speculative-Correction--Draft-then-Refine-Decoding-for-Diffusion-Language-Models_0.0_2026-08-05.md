# Speculative Correction: Draft-then-Refine Decoding for Diffusion Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02625v1 Announce Type: new Abstract: Diffusion language models (DLMs) can revise tokens bidirectionally, but standard decoding procedures often adapt them to left-to-right generation by producing text block by block. We study a simple plug-and-play inference pattern: first generate a complete draft, then refine the full response using bidirectional diffusion. Using LLaDA2.1-Flash and LLaDA2.1-Mini, we evaluate two configurations. In Flash-Flash, the same Flash model serves as both drafter and refiner, testing whether an existing model can improve its own block-autoregressive output through global refinement. In Mini-Flash, inspired by speculative decoding, we introduce speculative correction: Mini drafts a full response, and Flash revises it as an editable initialization. Flash-Flash improves GSM8K-384 accuracy from 0.848 to 0.899 while running 1.20 times faster than the selected Flash block-autoregressive baseline, and improves MBPP-384 from 0.545 to 0.693. Latency-window-matched Flash-only controls indicate that these gains persist after targeted tuning of block-autoregressive decoding. Causal ablations indicate that completed drafts provide useful initializations: refinement from a fully masked span performs poorly, full global refinement provides a clear additional gain on GSM8K, and local refinement captures much of the gain on MBPP and MATH. Mini-Flash provides useful quality-latency trade-offs, including MATH-384 performance of 0.294 versus 0.300 for Flash while running 2.17 times faster. These results support a Pareto-frontier interpretation rather than the claim that the heterogeneous cascade uniformly matches Flash quality. Overall, same-model draft-and-refine provides evidence that bidirectional refinement is a useful decoding primitive for DLMs, while speculative correction demonstrates a training-free route to fast DLM generation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02625
