# ITNet: A Learnable Integral Transform That Subsumes Convolution, Attention, and Recurrence

**评分：** 9.3  
**状态：** 正常  
**标签：** 架构统一, 积分变换, 多模态, 大模型, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19538v1 Announce Type: new Abstract: Convolutional networks, recurrent networks, and transformers each encode different inductive biases -- locality, sequential memory, and content-dependent pairwise interaction -- and have remained mathematically distinct since their inception. We show that this fragmentation reflects not a fundamental diversity in how signals should be processed, but rather incomplete views of a single underlying mathematical object: a learnable integral transform. We introduce the Integral Transform Network (ITNet), a unified architecture built around a learnable kernel that depends jointly on positions and features. This kernel is implemented as a small neural network, specifically an MLP, that models pairwise interactions, enabling the model to adapt its behavior from data. We show that convolution, self-attention (including multi-head), and autoregressive recurrence (including LSTM, GRU, S4, and Mamba) arise as special cases under appropriate parameterizations, and that ITNet is a universal approximator of continuous operators. To make this practical, we develop tiled kernel fusion, importance-weighted Monte Carlo integration, and learned low-rank factorization, enabling efficient and scalable computation. A single ITNet architecture with a shared operator and lightweight modality-specific encoders matches or exceeds specialized baselines on ImageNet-1K , GLUE, ModelNet40, VQA\,v2 and NLVR2. The results demonstrate that a single learned interaction mechanism can recover the behavior of all three architectural families from data.

## 综合总结
本文提出ITNet，通过可学习的积分变换将卷积、注意力和循环网络三大基础架构在数学上统一，证明它们均为ITNet的特例。为解决计算问题，引入了核融合与蒙特卡洛积分等高效算子。实验表明，单一ITNet架构在ImageNet、GLUE等多个跨模态基准上匹配或超越专用模型，展示了极强的架构统一与泛化潜力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
从数学底层出发，提出可学习的积分变换(ITNet)，将卷积、注意力及循环机制（含LSTM/GRU/S4/Mamba等）统一为特定参数化下的特例，并证明了其作为连续算子通用近似器的性质，理论深度与论证严谨性极高。

### 实用性 (评分: 9.0/10)
提出了分块核融合、重要性加权蒙特卡洛积分等工程优化方法解决计算瓶颈，单一架构配合轻量级编码器即可在CV、NLP、3D及多模态等五大基准上超越专用模型，对工业界降本增效和统一架构部署具有极大实践指导价值。

### 社区活跃度 (评分: 9.5/10)
直击当前AI社区“架构碎片化”痛点，将最热门的Transformer与Mamba等SSM架构统一，话题时效性与前瞻性极强；若实验结论可复现，将对下一代基础模型的设计范式产生深远且颠覆性的影响。

## 项目链接
https://arxiv.org/abs/2606.19538
