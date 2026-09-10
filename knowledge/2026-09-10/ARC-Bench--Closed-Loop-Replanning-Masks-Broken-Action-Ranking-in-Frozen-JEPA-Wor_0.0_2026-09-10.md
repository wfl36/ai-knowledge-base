# ARC-Bench: Closed-Loop Replanning Masks Broken Action Ranking in Frozen JEPA World Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-10  
**来源：** rss  

## 项目描述
arXiv:2609.05461v1 Announce Type: new Abstract: Reward-free latent world models plan by scoring candidate actions with distances in a frozen latent space: an action is preferred if its predicted future embedding lands closer to the goal embedding. This silently assumes that latent closeness is action-rankable, i.e., that ordering candidates by latent distance agrees with ordering them by true cost. We audit this assumption directly. We introduce ARC-Bench, a no-leak, fixed-candidate protocol that measures whether frozen JEPA-style objectives rank candidate actions correctly, and apply it to official released JEPA-WM checkpoints across navigation and manipulation-style control. The assumption fails, severely and structurally: on the official manipulation audits the top-scored candidate is almost always suboptimal, and the same inversion appears in the maze domains. A controlled visual-backbone extension shows that the defect persists when DINOv2 is replaced by video-pretrained V-JEPA 1 and V-JEPA 2 encoders at ViT-L/ViT-G scale. Provenance, undertraining, matched-budget backbone controls, and metric-circularity controls rule out trivial explanations. We then explain why this defect has stayed invisible: closed-loop replanning masks it. When we reduce the planner's replanning frequency, success collapses in both a navigation and a manipulation domain, and the episodes rescued by frequent replanning are enriched for severe first-plan ranking failures in the PointMaze first-plan diagnostic. Closed-loop success rates therefore systematically overstate the rankability of frozen latent representations. ARC-Bench supplies the measurement, and the masking mechanism the explanation, for methods that adapt, amortize, or replan around latent-space planners without directly auditing released JEPA-WM action rankability.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.05461
