# Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning

**评分：** 9.4  
**状态：** 正常  
**标签：** 大模型, MoE, Mamba, Agent, 长上下文, 推理, 论文, 工程实践  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15007v1 Announce Type: new Abstract: We introduce Nemotron 3 Ultra, a 550 billion total and 55 billion active parameter Mixture-of-Experts Hybrid Mamba-Attention language model. We pre-trained Nemotron 3 Ultra on 20 trillion text tokens, then extended the context length to 1M tokens, and post-trained using Supervised Fine Tuning (SFT), Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD). Nemotron 3 Ultra is our most capable model yet, employing multiple key technologies - LatentMoE, Multi Token Prediction (MTP), NVFP4 pre-training, multi-environment RLVR, MOPD, and reasoning budget control. Nemotron 3 Ultra achieves up to ~6x higher inference throughput as compared to state-of-the-art publicly available LLMs while attaining on-par accuracy. The state-of-the-art accuracy, high inference throughput, and 1M token context length make Nemotron 3 Ultra ideal for long-running autonomous agentic tasks. We open-source the base, post-trained, and quantized checkpoints, along with the training data and recipe on HuggingFace.

## 综合总结
NVIDIA 发布 Nemotron 3 Ultra，这是一个 550B 总参/55B 激活参数的 MoE 混合 Mamba-Transformer 模型。该模型融合了 LatentMoE、MTP、NVFP4 等前沿技术，支持 1M 超长上下文，并在后训练中引入多教师同策略蒸馏 (MOPD) 和推理预算控制。相比现有 SOTA 公开 LLM，其推理吞吐量提升约 6 倍且准确率持平，非常适合长时序自主 Agent 任务。项目全面开源了模型权重、训练数据及配方。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
创新性地结合了 Mamba 与 Transformer 的混合架构及 MoE 机制，在 550B 总参数、55B 激活参数规模上实现了线性推理复杂度与强表征能力的统一。引入 LatentMoE、多 Token 预测 (MTP)、NVFP4 量化预训练及多教师同策略蒸馏 (MOPD) 等前沿技术，在架构设计、训练范式与推理控制上展现了极高的研究深度与工程创新。

### 实用性 (评分: 9.5/10)
极具落地价值。55B 激活参数结合约 6 倍的吞吐量提升，大幅降低了推理成本；1M 长上下文与推理预算控制机制完美契合长时序自主 Agent 任务需求。此外，全面开源模型权重、训练数据及配方，为从业者提供了从预训练到后训练的完整实践参考，适用范围广泛。

### 社区活跃度 (评分: 9.5/10)
由 NVIDIA 官方庞大团队发布，来源权威性极高。聚焦 MoE、Mamba、长上下文与 Agent 推理等当前 AI 社区最热门前沿方向，时效性极强。作为 Nemotron 系列的最强版本，其开源策略与卓越性能必将对开源大模型及 Agent 生态产生重大且深远的影响。

## 项目链接
https://arxiv.org/abs/2606.15007
