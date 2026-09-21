# Reviser: Revision-Capable Text Generation via Autoregressive Cursor Actions

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20830v1 Announce Type: new Abstract: Revision-capable generation is appealing because it can insert or revise earlier content, but many non-autoregressive and edit-based approaches obtain this flexibility through repeated sequence-level computation. We propose Reviser, a decoder-only Transformer that generates a response as a sequence of cursor-relative actions on a mutable canvas. At each step, Reviser predicts exactly one action token: INSERT(token), MOVE($\Delta$), or STOP, and is autoregressive over edit-history actions rather than final text order. This design enables genuinely non-monotonic generation while preserving a simple next-action interface. On a continuation benchmark, Reviser is strongly preferred to SEDD and MDLM in our arena evaluations, and trajectory statistics confirm that the model performs frequent backward moves and mid-canvas insertions rather than merely emulating end-append decoding. Against size-matched autoregressive baselines, Reviser is competitive at both the 100M and 300M scales. Under our shared FLOPs convention, Reviser also requires substantially less inference compute than representative multi-pass refinement and diffusion-style baselines.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20830
