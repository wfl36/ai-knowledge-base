# Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-28  
**来源：** rss  

## 项目描述
arXiv:2608.24988v1 Announce Type: new Abstract: Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, preservation tracks the training data: steering degrades when optimisation pressure contradicts the targeted behaviour and persists otherwise, with refusal ablation losing 64% of its effect on average under SFT. Mechanistically, however, the weight edit survives almost untouched even where behaviour reverts: mean vector recovery is $\rho = 0.004$, and the fine-tuning update along the steering direction is near-orthogonal to its pre-edit weight pattern (mean $\cos\theta = 0.074$). When steered behaviour degrades, fine-tuning does not achieve it by dismantling or reversing the steering mechanism itself. Embedded steering is therefore mechanistically durable but functionally vulnerable, and requires behavioural re-validation after downstream training.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.24988
