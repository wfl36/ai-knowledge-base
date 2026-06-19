# Where to Place the Query? Unveiling and Mitigating Positional Bias in In-Context Learning for Diffusion LLMs via Decoding Dynamics

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 扩散模型, 上下文学习, 位置偏差, 解码动力学, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19349v1 Announce Type: new Abstract: While In-Context Learning (ICL) is extensively studied in Autoregressive (AR) LLMs, its mechanism within Diffusion Large Language Models (dLLMs) remains largely unexplored. Unlike AR models restricted by unidirectional causal masking, dLLMs intrinsically utilize bidirectional attention, offering extensive spatial flexibility for query placement. Unfortunately, current practices conventionally inherit AR-style trailing-query templates, often overlooking the structural paradigm shift. This paper presents a comprehensive analysis unveiling that query position is actually a first-order variable in dLLMs. Through empirical decoupling, we demonstrate that positional variance impacts generation quality on par with example semantic quality. Internally, this positional sensitivity stems from a spatial ``Recency Effect'' in attention flow and task-dependent shifts in decoding trajectories. To mitigate this instability without ground-truth labels, we reveal that traditional single-step confidence ($C_{decoded}$) fails in dLLMs. Instead, we propose Average Confidence ($\overline{C}$), a novel metric tracking the iterative decoding process. By establishing the foundational spatial ICL baselines, we introduce Auto-ICL, a training-free adaptive routing strategy that dynamically optimizes query placement, robustly approaching oracle performance across heterogeneous reasoning and perception tasks.

## 综合总结
本文针对扩散大语言模型中的上下文学习（ICL）机制展开研究，揭示了查询位置是影响dLLMs生成质量的一阶变量，打破了自回归模型遗留的尾部查询范式。研究深入剖析了位置敏感性的内部机制（空间近因效应与解码轨迹偏移），指出传统单步置信度在dLLMs中失效，并提出平均置信度（$\overline{C}$）新指标。基于此，本文提出免训练的自适应路由策略Auto-ICL，动态优化查询位置，在多项任务中逼近oracle性能，为dLLMs的ICL实践提供了重要理论基础与工程方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文具有极高的研究深度与新颖性，首次系统性地揭示了扩散大语言模型中上下文学习（ICL）的查询位置偏差问题，打破了自回归（AR）模型遗留的尾部查询惯性思维。研究深入剖析了其内部机制，指出位置敏感性源于注意力流的空间‘近因效应’及解码轨迹的任务依赖偏移，并严谨地论证了传统单步置信度在dLLMs中的失效，创新性地提出了基于迭代解码过程的平均置信度（$\overline{C}$）指标，逻辑闭环完整。

### 实用性 (评分: 8.5/10)
对dLLMs从业者具有极高的实践指导价值。提出的Auto-ICL策略为免训练方案，可直接嵌入现有dLLMs推理流程中，通过动态优化查询位置显著提升生成质量。该研究不仅为dLLMs的提示词工程和模板设计提供了新准则，也为解决无真实标签下的模型不稳定性提供了可落地的工程方案。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，dLLMs作为大模型领域的前沿方向，其ICL机制研究正处于探索期。本文直击当前dLLMs研究中的核心痛点，来源为arXiv预印本，虽未经同行评审，但其反直觉的发现与有效的解决方案有望重塑dLLMs领域的ICL实践范式，具备较高的潜在学术影响力与社区关注度。

## 项目链接
https://arxiv.org/abs/2606.19349
