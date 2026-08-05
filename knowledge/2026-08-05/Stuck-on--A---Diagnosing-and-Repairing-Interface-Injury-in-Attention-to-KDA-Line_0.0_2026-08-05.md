# Stuck on "A": Diagnosing and Repairing Interface Injury in Attention-to-KDA Linearization of a 0.6B Language Model

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02689v1 Announce Type: new Abstract: We convert 21 of 28 full-attention layers of Qwen3-0.6B-Base into KDA (Kimi Delta Attention) linear-attention layers on a single consumer-grade GPU budget, and ask a simple question: what exactly does the conversion break? After surgery, hidden-state alignment and end-to-end KL distillation drive the student close to its teacher in perplexity, yet multiple-choice accuracy stays near random chance (25-29% vs. the teacher's 50.6% on C-Eval). Using a four-permutation diagnostic that rotates answer options while holding content fixed, we show the model sticks to option labels (predicting "A" 81% of the time; 106/161 questions keep the same label under all four rotations) rather than following answer content -- an interface injury that standard distillation metrics cannot see. A 1,000-step format-targeted completion-only KL stage repairs the interface (+12.48 points on C-Eval, label-stickiness roughly halved), after which persona SFT and one round of on-policy DPO preserve benchmark scores within noise. We release code, weights, recipes, and the full audit trail, and distill the engineering lessons -- including an FP32-master failure mode in which bf16 optimizer updates are silently swallowed -- that made convergence possible at this budget.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02689
