# Stabilizing language models under continual learning via condition-anchored distillation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-07  
**来源：** rss  

## 项目描述
arXiv:2610.06940v1 Announce Type: new Abstract: Continual adaptation of language models can change their output distribution on prompts learned earlier, while retaining every old prompt-answer pair may be undesirable or impossible. We study condition-anchored generative distillation (CAGD): retain a small set of old prompts, use a frozen previous model to reconstruct completions and generation states, and match its predictive distributions while learning the next task. The formulation separates three roles that ordinary replay conflates: conditions select the behavior to protect, teacher generations locate relevant states, and soft targets specify how predictions may change. For autoregressive language generation, teacher-rollout distillation admits an exact chain-rule decomposition of sequence divergence. For masked-diffusion language modeling, our implementation directly controls local denoising drift on teacher-generated completions. In continual adaptation of a 219M masked diffusion language model, CAGD reduces four-task final held-out loss from 2.927 to 1.114 in one task order and from 2.168 to 0.891 in exact reverse. The same soft targets lower final average loss by 0.055 over hard replay when teacher-generated support is held identical. The direction persists on fresh facts and natural instructions across SMDM and Qwen3. On GSM8K, Qwen adaptation preserves answer-format compliance, but exact-match retention is seed-mixed at 0.6B and worsens at 1.7B. These results support condition-anchored functional preservation as a common design principle across the tested language-generation objectives.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.06940
