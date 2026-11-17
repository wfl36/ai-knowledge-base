# LoRAWeaver: Directional Adapter Routing in LoRA Representation Space

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-17  
**来源：** rss  

## 项目描述
arXiv:2611.17340v1 Announce Type: new Abstract: Large language models are expensive to update through full retraining. Parameter-efficient fine-tuning reduces the cost of adaptation, but repeated adaptation creates a growing pool of task-specific LoRA adapters. This pool complicates adapter selection during inference. Existing routing and encoder-based methods often require retraining when new adapters are added, which limits their use in dynamic settings. This paper treats adapter routing as a representation alignment problem in the adapter-output space. The proposed training-free method selects adapters by matching adapter-conditioned query representations against task prototypes using cosine similarity. Experiments with LLaMA-2-7B and LLaMA-2-13B on a 48-task FLAN-v2 benchmark and on out-of-distribution tasks show that the method outperforms training-free baselines in the cross-task setting and approaches a trained retrieval encoder without learning a router. An ablation confirms the benefit of directional alignment in the adapter-output space.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.17340
