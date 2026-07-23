# Multi-Mask Diffusion Language Models for Few-Step Generation

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 扩散模型, 掩码扩散, 少步生成, 离散扩散, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19686v1 Announce Type: new Abstract: Masked diffusion models (MDMs) are a promising family of language generators, but achieving high-quality few-step generation remains challenging. In MDMs, all forward trajectories collapse to a single fully masked state, leaving no terminal entropy for consistency-style few-step generation. While recent few-step alternatives based on uniform-state diffusion avoid this degeneracy, it becomes harder to distinguish clean tokens from noise than MDMs, which usually harms modeling quality and training efficiency. In this work, we propose a multi-mask diffusion model (MultiMDM) that preserves the masking structure towards few-step generation. In the forward process, each clean token is first pushed towards a designated mask and then gradually mixes over the mask set. As a result, the backward process has a drafting capability by predicting a designated mask before refining to a clean token. We derive a closed-form ELBO training objective for MultiMDM that supports continual training from pretrained MDMs. In addition, we formulate a purely discrete-state consistency distillation scheme, with a shared-Gumbel coupling to reduce pathwise entropy. Experiments on pretraining and distillation show that MultiMDM provides an effective foundation for principled few-step generation.

## 综合总结
本文提出多掩码扩散模型，通过引入多掩码集和起草能力，解决了传统掩码扩散模型无法进行少步生成的理论限制。推导了闭式ELBO目标并支持从预训练模型持续训练，同时提出共享Gumbel耦合的离散一致性蒸馏方案。该研究在理论和工程上为离散扩散语言模型的高效少步生成提供了坚实基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出多掩码扩散模型，创新性地解决了传统MDM因终端熵为零而无法进行一致性少步生成的理论瓶颈，同时避免了均匀状态扩散中噪声与信号难以区分的问题。推导了闭式ELBO训练目标及纯离散状态一致性蒸馏方案（含共享Gumbel耦合），理论严谨且方法新颖。

### 实用性 (评分: 8.5/10)
支持从预训练MDM进行持续训练，降低了模型迁移与训练成本；提出的少步生成机制和一致性蒸馏方案能显著提升离散扩散语言模型的推理速度，对大语言模型的快速生成与工程部署具有极高的参考价值。

### 社区活跃度 (评分: 9.0/10)
发布于2026年7月，时效性极强；作者团队包含顾全全、应乐兴等知名学者，学术权威性高；离散扩散语言模型及少步生成是当前AI社区的前沿热点，预计将引发广泛关注与后续研究。

## 项目链接
https://arxiv.org/abs/2607.19686
