# Diffu-LoRA: A Novel Low-Rank Adaptation for Personalized Diffusion Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10550v1 Announce Type: new Abstract: Personalizing text-to-image diffusion models from a few reference images requires preserving subject identity while following prompts that describe new contexts. Full-model fine-tuning is parameter-intensive, whereas low-rank adaptation (LoRA) reduces the number of trainable parameters but leaves open how adaptation capacity should be distributed across layers. We introduce Diffu-LoRA, a parameter-efficient method that learns this allocation through gated low-rank adaptation. Diffu-LoRA inserts trainable low-rank components into the linear layers of Transformer blocks and assigns a learnable gate to each component. Bilevel optimization updates the adaptation weights and gate parameters on separate data splits, while progressive pruning removes components with the lowest gate values to meet a prescribed rank budget. This procedure allocates adaptation capacity nonuniformly across layers while keeping the pretrained backbone frozen. Experiments with Stable Diffusion on subjects from DreamBooth and additional collected datasets show improved overall subject fidelity and prompt alignment relative to the evaluated fine-tuning baselines. Ablation studies examine the contributions of bilevel optimization, progressive pruning, and adapter placement. These results support learned rank allocation as a practical approach to parameter-efficient diffusion model personalization.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10550
