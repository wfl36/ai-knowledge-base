# Synthetic Contrastive Reasoning for Multi-Table Q&A

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, 多表问答, 合成数据, 偏好对齐, 论文  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05382v1 Announce Type: new Abstract: Multi-table question answering requires models to retrieve relevant evidence, link schemas, and perform compositional reasoning across relational tables. Existing multi-table Q&A resources typically provide questions and final answers but lack reasoning supervision that explains how answers are derived. To address this gap, we construct a synthetic contrastive reasoning-trace dataset for MMQA by generating validated positive traces and plausible negative traces with heterogeneous LLMs. We then use the resulting preference pairs to fine-tune open-weight LLMs with Contrastive Preference Optimization (CPO). Across Qwen3-14B, Mistral-8B, and Llama-3.1-8B, CPO achieves absolute average improvements over Q&A supervised fine-tuning ranging from 9.7%-16.3%, with gains up to 21 percentage points on MMQA. Ablations show that heterogeneous positive and negative trace generators strengthen the contrastive signal, and automated as well as human evaluations indicate that the generated pairs are largely faithful, coherent, and meaningfully contrastive.

## 综合总结
本文提出一种针对多表问答的合成对比推理方法，利用异构LLM生成正负推理轨迹构建偏好数据集，并通过CPO微调开源大模型。实验表明，该方法相比传统SFT取得了最高21个百分点的显著提升，消融与评估证实了数据的高质量与对比信号的有效性，为结构化数据推理和合成数据构建提供了极具价值的实践范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对多表问答缺乏推理监督的问题，创新性地提出利用异构LLM生成正负推理轨迹构建合成对比数据集，并结合对比偏好优化（CPO）微调模型。实验在多个开源模型上验证了该方法的有效性，消融实验和人工评估进一步证实了异构生成器对增强对比信号及数据质量的积极作用，技术论证严谨且具有深度。

### 实用性 (评分: 8.0/10)
该研究为解决复杂结构化数据问答中的推理过程监督缺失提供了可操作的工程实践方案。利用异构LLM生成对比偏好数据并使用CPO微调的方法，不仅适用于多表问答，也可广泛迁移至其他缺乏中间推理标注的领域，对RAG和结构化数据处理从业者具有极高的参考价值。

### 社区活跃度 (评分: 7.5/10)
论文聚焦于多表问答、合成数据生成及模型对齐等当前AI社区的热点方向。作为arXiv上的最新研究，其实验设计规范、数据质量评估全面，具备较高的学术可信度，对相关领域的后续研究和应用具有较好的启发意义。

## 项目链接
https://arxiv.org/abs/2606.05382
