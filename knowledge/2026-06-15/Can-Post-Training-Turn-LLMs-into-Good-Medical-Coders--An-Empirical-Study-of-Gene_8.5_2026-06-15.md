# Can Post-Training Turn LLMs into Good Medical Coders? An Empirical Study of Generative ICD Coding

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 强化学习, 后训练, ICD编码, 论文, 实证研究  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13940v1 Announce Type: new Abstract: Automated International Classification of Diseases (ICD) coding is a core medical-coding task for billing, epidemiology, and clinical decision support. Generative large language models (LLMs) are often reported as weak medical coders, but this finding mainly comes from inference-time settings such as prompting, retrieval, reranking, or tool use, leaving the role of task-specific post-training underexplored. We present a controlled empirical study of post-training for generative ICD coding, comparing discriminative baselines with LLM coders across prompting, supervised fine-tuning, and reinforcement learning under a common protocol and metric set. To our knowledge, this is the first study to evaluate RL-based post-training for generative LLM coders in ICD coding. We further introduce PHI, a diagnostic curriculum that extends GRPO to refine missed-code cases. Our results show that prompting-only evaluation substantially underestimates the potential of LLMs for ICD coding. SFT provides the main capability jump, GRPO further improves code-set prediction beyond SFT, and PHI provides targeted gains on macro-level performance. These findings suggest that the main bottleneck is not the generative formulation alone, but how the model is adapted and optimized for full-taxonomy recall. We release our code, data splits, and checkpoints at https://github.com/AlexandreWANG915/LLM4ICD.

## 综合总结
本文针对“生成式大模型在ICD医疗编码中表现不佳”的普遍认知，系统性地研究了后训练的作用。研究首次将基于RL的后训练应用于生成式ICD编码，并提出了扩展GRPO的PHI诊断课程。实验表明，仅用提示词评估严重低估了LLM潜力，SFT带来核心能力跃升，GRPO进一步提升预测表现，PHI则针对性优化宏观指标。该研究指出瓶颈在于模型的全分类召回优化方式而非生成式架构本身，并已开源全部资源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究具有较高新颖性与深度，首次系统性地评估了强化学习（RL）在后训练阶段对生成式ICD医疗编码的作用，并创新性地提出了PHI诊断课程来扩展GRPO算法。实验设计严谨，在统一协议和指标下对比了判别式基线与LLM在提示、SFT和RL下的表现，论证了LLM在医疗编码表现不佳的瓶颈在于适应与优化方式，而非生成式架构本身。

### 实用性 (评分: 9.0/10)
对医疗AI从业者具有极高的落地指导价值。研究不仅打破了'LLM不擅长医疗编码'的刻板印象，还提供了一条清晰、可复现的模型优化路径（Prompt -> SFT -> GRPO -> PHI）。同时，作者开源了代码、数据划分和模型检查点，极大降低了工业界在医疗账单、临床决策支持等场景的应用与复现门槛。

### 社区活跃度 (评分: 8.0/10)
话题紧扣大模型后训练与垂直领域应用的热点，时效性强。挑战了现有仅依赖提示词评估的普遍认知，对学术界和工业界重新审视LLM在专业任务上的潜力具有启发意义。作为arXiv新发论文，其开源策略增强了可信度，虽长期影响力有待验证，但短期内必将在医疗信息学社区引发关注。

## 项目链接
https://arxiv.org/abs/2606.13940
