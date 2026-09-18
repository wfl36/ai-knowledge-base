# Subliminal Prompting Beyond Static Geometry: Causal Depth and Multi-Token Confounds

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-18  
**来源：** rss  

## 项目描述
arXiv:2609.19149v1 Announce Type: new Abstract: Subliminal learning shows that language models can transmit a hidden trait through outputs that appear unrelated to it. One proposed explanation, token entanglement, links animal and number tokens through the model's output vocabulary. Yet existing measurements answer different questions: whether outputs co-vary, fixed output vectors align, an answer can be read from a hidden state, or that state causally controls the answer. We measure each separately in a fixed animal-number prompting protocol. From Llama-3.1-8B to 70B, fixed output-vector similarity predicts behavior less well: the paired mean correlation change is -0.080 (95% CI [-0.127, -0.035]). A fixed output-head readout shows no resolved change in normalized depth AUC. To test control, we copy the temporary answer-position state from one number prompt into another at five depths and measure which prompt the final animal score follows. Donor-control AUC rises from 0.254 to 0.540, a paired change of +0.286 (95% CI [+0.272, +0.300]), with increases for all 18 concepts. The contrast remains with exactly eight transformer blocks remaining, while specificity and identity controls remain small or exact. In two Qwen models, scoring every digit in sequence does not recover the positive one-token association. Per-token averaging instead creates a positive pooled association that disappears after controlling number width, revealing a length confound. Thus, fixed geometry, observational readability, causal timing, and multi-token measurement are distinct properties of this frozen prompting channel. They constrain token-level explanations but do not identify the mechanism of training-time trait transfer.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.19149
