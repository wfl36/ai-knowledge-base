# MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-06  
**来源：** rss  

## 项目描述
arXiv:2610.02260v1 Announce Type: new Abstract: Flow matching models excel at generative modeling, and many downstream applications require their samples to satisfy prescribed constraints, such as observed measurements and physical laws. However, existing constrained samplers often face a trade-off: \textit{enforcing constraints can substantially displace samples from the pretrained data distribution}. To address this trade-off, we introduce \textbf{MintFlow}, a training-free constrained sampling framework that formulates constraint enforcement as a minimal intervention on the pretrained flow trajectory. MintFlow seeks the minimal perturbation of an intermediate flow state such that its subsequent evolution under the pretrained flow field satisfies the target constraint. By minimally perturbing the flow state while keeping the pretrained flow field unchanged, MintFlow enforces the constraint while minimizing unnecessary deviation from the pretrained distribution. An adjoint formulation yields a closed-form expression for this perturbation, eliminating expensive iterative optimization. Furthermore, MintFlow adaptively selects the intervention time to balance the required perturbation magnitude with its amplification by the remaining flow. Across a range of tasks in generative vision and physical system modeling, MintFlow achieves competitive constraint satisfaction while preserving the pretrained generative distribution substantially better than state-of-the-art constrained methods.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.02260
