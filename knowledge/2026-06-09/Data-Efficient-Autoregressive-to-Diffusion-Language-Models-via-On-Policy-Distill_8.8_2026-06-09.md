# Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation

**评分：** 8.8  
**状态：** 正常  
**标签：** 扩散语言模型, 自回归模型, 知识蒸馏, 模型转换, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06712v1 Announce Type: new Abstract: We study the transformation of autoregressive models (ARLMs) into diffusion language models (DLMs). Rather than pretraining from scratch, prior work replaces the causal attention in ARLMs with bidirectional attention and then trains the resulting model using a DLM objective. However, these approaches incur two distribution shifts. First, transitioning from a next-token prediction objective to a DLM objective can discard knowledge acquired by the ARLM during training. Second, standard DLMs suffer from a train-inference mismatch, as the training loss is defined on randomly masked sequences rather than the trajectories encountered at inference produced by confidence-based decoding. To address both challenges, we introduce an On-Policy Diffusion Language Model (OPDLM) in which On-Policy Distillation (OPD) is employed for ARLM-to-DLM transformation. Specifically, OPDLM is trained via self-OPD, where the student, an ARLM with bidirectional attention, generates its own trajectories, and the teacher, the original frozen ARLM, distills its knowledge by providing target logits on these trajectories. By training directly in an on-policy manner, OPDLM eliminates the train-inference mismatch in DLMs, while distillation from the original model enhances knowledge retention from the ARLM. Empirical results demonstrate that OPDLM requires 15x to 7,000x fewer training tokens with strong performance across a wide variety of tasks. OPDLM avoids the prohibitive cost of DLM pretraining and positions DLM transformation as a form of ARLM post-training.

## 综合总结
本文提出OPDLM框架，通过在线策略蒸馏(OPD)解决自回归语言模型(ARLM)向扩散语言模型(DLM)转换中的双重分布偏移问题。该方法让学生模型生成轨迹并由原始ARLM教师模型进行在线蒸馏，不仅消除了训练-推理不匹配，还保留了ARLM知识。实验表明，OPDLM在保持强性能的同时，所需训练token减少15至7000倍，将DLM转换重新定义为ARLM的后训练过程，极大降低了DLM的构建成本。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
深入剖析了自回归语言模型(ARLM)向扩散语言模型(DLM)转换中的双重分布偏移问题（目标转换导致的知识遗忘与训练-推理不一致），创新性地提出在线策略蒸馏(OPD)框架OPDLM。通过让学生模型生成自身推理轨迹并由冻结的ARLM教师模型进行在线蒸馏，有效消除了上述偏移，技术路径新颖且论证严谨。

### 实用性 (评分: 8.5/10)
对工业界极具落地价值。该方法将DLM转换视为ARLM的后训练阶段，大幅降低了DLM的预训练成本（所需训练token减少15至7000倍），使得现有大规模ARLM能够低成本、高保真地转换为具备双向建模能力的DLM，为从业者提供了一条高效、可操作的模型升级路径。

### 社区活跃度 (评分: 9.0/10)
发布于2026年，属于极早期前沿研究。扩散语言模型作为突破自回归限制的重要方向备受关注，该论文由知名学者参与，其提出的“后训练转换”范式和数据效率的大幅提升，有望在AI社区引发广泛讨论和后续研究，时效性与权威性俱佳。

## 项目链接
https://arxiv.org/abs/2606.06712
