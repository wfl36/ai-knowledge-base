# CoRA: Confidence-Rationale Alignment for Reliable Chain-of-Thought Reasoning

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 推理, CoT, 强化学习, 模型校准, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.14961v1 Announce Type: new Abstract: Chain-of-thought (CoT) reasoning can improve LLM performance, but high answer confidence may be misleading when the accompanying CoT rationale is plausible yet incomplete or poorly supported. We study confidence--rationale alignment: whether a model's confidence in its committed answer is justified by its generated rationale. We introduce a GRPO-based reinforcement learning framework that jointly rewards answer correctness, committed-answer probability, and rubric-based rationale support, where the rubric assesses grounding, coherence, task match, and connection to the selected answer without revealing the gold answer to the judge. Across MedQA, MathQA, and OpenBookQA using three open-weight LLMs, our method reduces the confidence--rationale alignment error by up to 26.51% compared with untuned checkpoints, SFT, and correctness-only GRPO, while maintaining competitive accuracy and often improving calibration. These results show that reliable CoT reasoning requires not only confident answers, but rationales that substantively support them.

## 综合总结
本文针对大模型CoT推理中'高置信度但推理依据不足'的问题，提出了置信度-推理对齐的概念。作者设计了一种基于GRPO的强化学习框架，通过联合奖励答案正确性、承诺概率及基于无金标答案评分标准的推理支持度来优化模型。实验表明，该方法显著降低了置信度-推理对齐误差（最高达26.51%），并在保持准确率的同时改善了模型校准，为提升LLM推理可靠性提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了'置信度-推理对齐'（Confidence-Rationale Alignment）的新颖概念，精准切中了当前大模型CoT推理中'高置信度伴随弱推理'的痛点。在方法设计上，基于GRPO强化学习框架，创新性地引入了不依赖金标答案的评分标准作为奖励信号，联合优化答案正确性、承诺概率和推理支持度，论证逻辑严密，实验对比充分（对比SFT和仅关注正确性的GRPO），技术深度和新颖性俱佳。

### 实用性 (评分: 8.0/10)
对AI从业者在高风险场景（如医疗、数学推理）下提升模型可靠性具有极高的参考价值。提出的基于评分标准的奖励框架可直接应用于定制化RLHF微调流程中，帮助缓解模型'过度自信'和'幻觉'问题。尽管强化学习微调存在一定的工程门槛，但其不泄露金标答案的评判机制设计，使得该方法在RAG和Agent等需要高可靠推理的落地场景中适用性极强。

### 社区活跃度 (评分: 8.0/10)
大模型推理的可靠性与校准是当前AI社区的核心热点话题。该论文来自arXiv的最新发布，作者团队具有学术背景，研究主题紧扣行业痛点。其提出的'对齐误差'量化指标及在多个主流基准（MedQA, MathQA等）上的显著改进结果，极易引发学术界和工程界对CoT可靠性的进一步探讨，具备较好的社区影响力和传播潜力。

## 项目链接
https://arxiv.org/abs/2606.14961
