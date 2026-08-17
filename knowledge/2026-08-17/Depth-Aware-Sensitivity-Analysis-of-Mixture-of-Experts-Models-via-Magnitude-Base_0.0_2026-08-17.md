# Depth-Aware Sensitivity Analysis of Mixture-of-Experts Models via Magnitude-Based Expert Masking

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** rss  

## 项目描述
arXiv:2608.13565v1 Announce Type: new Abstract: Mixture-of-Experts (MoE) architectures scale large language models (LLMs) while preserving computational efficiency through sparse activation. Despite their widespread adoption, the relative importance of individual MoE layers remains insufficiently characterized, particularly for model compression. This paper presents a systematic layer-wise sensitivity analysis of the Qwen3.6-35B-A3B model (40 MoE layers, 256 experts per layer, top-8 routing) using magnitude-based expert masking on the XLCoST cross-lingual code translation benchmark. We conduct a multi-phase study spanning 100, 300, and 500 prompt evaluation scales across three H100 GPU servers. Our central finding is that layer sensitivity is strongly depth-dependent: early layers (0-9) and middle layers (10-29) are highly fragile to expert masking, while late layers (30-39), and especially very-late layers (35-39), tolerate aggressive masking of low-magnitude experts. Flat all-layer masking at 30% retains only 150/300 Good+Similar outputs at 300-prompt scale, whereas late-focused policies retain 249-255/300 while masking 640-1,145 experts. On a later 500-prompt held-out validation slice, the narrow very-late policy (layers 35-39 @ 50%) achieves the strongest quality/masked-expert tradeoff among tested candidates, retaining 419/500 Good+Similar outputs while masking only 640 of 10,240 total experts. We additionally characterize top-k routing width reduction from 8 to 6 active experts per token, which shows a large observed wall-clock reduction on a 100-prompt probe with no Good+Similar loss, though it does not yet compose cleanly with aggressive expert masking. These findings provide an empirical foundation for depth-aware MoE expert masking and establish a practical path toward physical weight surgery, activation-based expert scoring, and training-based recovery.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.13565
