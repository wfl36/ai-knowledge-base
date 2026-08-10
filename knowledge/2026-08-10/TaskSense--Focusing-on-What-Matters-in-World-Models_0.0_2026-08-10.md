# TaskSense: Focusing on What Matters in World Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06544v1 Announce Type: new Abstract: World models for visual control typically learn compact latent states by reconstructing observations, implicitly encouraging representations to preserve information across the entire visual input. However, task-relevant content often occupies only a small fraction of the observation, while background clutter and distractors consume valuable representational capacity. This mismatch between visual reconstruction and control objectives biases latent representations to model task-irrelevant visual content, diluting learning signals for control-relevant features and severely degrading downstream performance under visual distractions. We introduce TaskSense, a task-centric world modeling framework that enforces task relevance before latent encoding through a differentiable stochastic spatial attention mechanism conditioned on the previous latent state. To steer attention toward control-relevant regions, we augment training with an auxiliary inverse-dynamics objective. Rather than reconstructing the full observation, the world model reconstructs only the attended regions, encouraging latent representations to preserve task-relevant information while discarding irrelevant visual content. The decoder is further conditioned on the sampled attention map, enabling consistent reconstruction despite stochastic attention. Compared with the DreamerV3 baseline, TaskSense maintains competitive performance on the DeepMind Control Suite while consistently outperforming DreamerV3 on the Distracting Control Suite, demonstrating substantially improved robustness to visual distractions. Qualitative analysis further confirms that the learned attention, guided by inverse-dynamics supervision, consistently localizes control-relevant regions while suppressing irrelevant visual content.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06544
