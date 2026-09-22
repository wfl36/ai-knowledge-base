# Summarize, Judge, Refine: Decoupled Content Understanding and Policy Learning for Multimodal Content Moderation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.22094v1 Announce Type: new Abstract: Content moderation systems traditionally entangle multimodal understanding with policy-specific classification, requiring full pipeline retraining for every policy change and suffering from label scarcity since multimedia cannot be meaningfully augmented. We propose Summarize-Judge-Refine (SJR), a two-model architecture that decouples these concerns via a natural language interface: a multimodal Content Model produces structured text summaries, and a text-only Policy Model classifies them against policy definitions. An iterative co-training loop refines the Content Model via GRPO to produce policy-relevant summaries, while text-space augmentation generates adversarial summary variants---an augmentation pathway impossible on raw multimedia---enabling few-shot policy bootstrap. Every decision is grounded in a human-readable summary, providing interpretability as a structural byproduct. On misleading advertisement detection, SJR achieves +23.6\% relative non-misleading F1 over a zero-shot chain-of-thought baseline, outperforming end-to-end SFT, STaR/RFT, and RLFT. Notably, a variant trained on zero real violating examples---with all positive-class data synthetically generated---matches the full-data model within 0.2\% relative on violating F1, demonstrating that new policies can launch without any real violation data.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.22094
