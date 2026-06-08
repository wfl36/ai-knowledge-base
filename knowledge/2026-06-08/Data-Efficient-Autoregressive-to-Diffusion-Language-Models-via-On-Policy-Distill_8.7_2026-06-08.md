# Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 扩散语言模型, 知识蒸馏, 自回归模型, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06712v1 Announce Type: new Abstract: We study the transformation of autoregressive models (ARLMs) into diffusion language models (DLMs). Rather than pretraining from scratch, prior work replaces the causal attention in ARLMs with bidirectional attention and then trains the resulting model using a DLM objective. However, these approaches incur two distribution shifts. First, transitioning from a next-token prediction objective to a DLM objective can discard knowledge acquired by the ARLM during training. Second, standard DLMs suffer from a train-inference mismatch, as the training loss is defined on randomly masked sequences rather than the trajectories encountered at inference produced by confidence-based decoding. To address both challenges, we introduce an On-Policy Diffusion Language Model (OPDLM) in which On-Policy Distillation (OPD) is employed for ARLM-to-DLM transformation. Specifically, OPDLM is trained via self-OPD, where the student, an ARLM with bidirectional attention, generates its own trajectories, and the teacher, the original frozen ARLM, distills its knowledge by providing target logits on these trajectories. By training directly in an on-policy manner, OPDLM eliminates the train-inference mismatch in DLMs, while distillation from the original model enhances knowledge retention from the ARLM. Empirical results demonstrate that OPDLM requires 15x to 7,000x fewer training tokens with strong performance across a wide variety of tasks. OPDLM avoids the prohibitive cost of DLM pretraining and positions DLM transformation as a form of ARLM post-training.

## 综合总结
本文提出OPDLM框架，通过在线策略蒸馏(OPD)解决ARLM向DLM转换中的分布偏移与训练-推理不匹配问题。该方法将DLM转换视为ARLM的后训练，在保留原模型知识的同时，将所需训练token减少了15至7000倍，极大降低了DLM的构建成本，为高效开发扩散语言模型提供了突破性方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深入分析了自回归语言模型(ARLM)向扩散语言模型(DLM)转换过程中的两大分布偏移问题（目标偏移与训练-推理不匹配），创新性地提出了在线策略蒸馏(OPD)框架OPDLM。通过让学生模型（双向注意力ARLM）生成自身推理轨迹，并由教师模型（原始冻结ARLM）提供目标logits进行蒸馏，有效解决了上述问题。技术路径巧妙结合了强化学习中的on-policy思想与知识蒸馏，论证严谨且具有较高的技术深度。

### 实用性 (评分: 8.5/10)
该方法将DLM的构建从昂贵的从头预训练转变为高效的ARLM后训练，仅需极少量的训练数据（减少15x至7000x倍）即可实现优异性能。这为从业者利用现有开源ARLM快速、低成本地构建DLM提供了极具实用价值的工程指导，落地门槛大幅降低，适用范围广泛。

### 社区活跃度 (评分: 8.5/10)
扩散语言模型(DLM)作为突破自回归架构限制的新方向备受学术界和工业界关注，但高昂的预训练成本制约了其发展。该论文提出的极低成本转换方案直击社区痛点，来源可信，且在数据效率上的巨大提升有望重塑DLM的构建范式，具有很高的时效性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.06712
