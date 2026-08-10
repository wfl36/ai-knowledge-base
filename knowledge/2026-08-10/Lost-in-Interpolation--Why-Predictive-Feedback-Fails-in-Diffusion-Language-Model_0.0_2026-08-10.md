# Lost in Interpolation: Why Predictive Feedback Fails in Diffusion Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06529v1 Announce Type: new Abstract: Soft-masking accelerates the convergence of Masked Diffusion Language Models (MDLMs). Existing formulations build this blend with linear interpolation (LERP) in the raw embedding space, which implicitly treats that space as Euclidean. We analyze the embedding space of MDLMs and find that the mask and predicted-token embeddings maintain a near-constant angle of (\approx 73^\circ) throughout training, while embedding norms remain essentially flat across vocabulary-frequency rank. These indicate a hyperspherical geometry, for which LERP is the wrong interpolation primitive. We introduce Spherical Soft-Masking (S-SM), a drop-in replacement that aggregates the top-(k) predictions with a Fr'echet mean on the hypersphere and blends this mean with the mask direction using spherical linear interpolation (SLERP), then restores the native mask norm. We evaluate S-SM on continued pre-training of a released 169M-parameter MDLM checkpoint across a wide range of inference-time step budgets, SLERP feedback avoids the training degradation that LERP feedback induces and delivers MAUVE gains of up to 2x over the vanilla MDLM baseline and 27.5-56.1% over TopK/LERP at various sampling budgets, alongside consistently lower generative perplexity (16.9-19.6% over the baseline), while leaving output entropy and convergence essentially unchanged.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06529
