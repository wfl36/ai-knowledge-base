# LoRA-Diffusion: Parameter-Efficient Fine-Tuning via Low-Rank Trajectory Decomposition

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-14  
**来源：** rss  

## 项目描述
arXiv:2608.12328v1 Announce Type: new Abstract: Parameter-efficient fine-tuning methods such as LoRA have transformed the adaptation of large autoregressive language models, enabling task-specific customization with substantially fewer trainable parameters. However, these methods have not been successfully extended to diffusion-based language models, which generate text through iterative denoising rather than sequential token prediction. We propose LoRA-Diffusion, a parameter-efficient fine-tuning approach that applies low-rank decomposition to the denoising trajectory instead of model weights. Unlike weight-based LoRA, which modifies individual transformation matrices, our method learns low-rank perturbations to the entire diffusion path from noise to output. We introduce trajectory-level low-rank adapters that modify each denoising step, step-adaptive rank allocation across diffusion phases, and compositional multi-task learning that allows merging task-specific modules at inference without retraining. On SST-2, QNLI, and MRPC, we report token-level denoising validation accuracy over five random seeds. LoRA-Diffusion achieves the highest mean performance on SST-2 and strong performance on QNLI and MRPC. Joint multi-task training further shows that LoRA-Diffusion achieves the highest token-level accuracy among the evaluated methods. The approach reduces per-task storage compared with full fine-tuning and establishes a parameter-efficient fine-tuning framework for diffusion language models.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.12328
