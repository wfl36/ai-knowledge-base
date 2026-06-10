# Supervised Fine-tuning with Synthetic Rationale Data Hurts Real-World Disease Prediction

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 监督微调(SFT), 推理, 疾病预测, 论文  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10279v1 Announce Type: new Abstract: Supervised fine-tuning with synthetic rationale data is widely assumed to improve language model performance on clinical prediction tasks by teaching models not just what to predict but why. We test this assumption on five-year Alzheimer's disease and related dementias (ADRD) prediction from longitudinal health histories. Across a large-scale controlled experiment of 504 configurations, we find that rationale-based SFT consistently and substantially hurts prediction performance relative to label-only fine-tuning. The degradation persists across model families and data scales, and is not resolved by using a reasoning-oriented base model. Crucially, the failure is not explained by poor rationale quality: human expert annotation confirms that the generated rationales are medically accurate and faithfully grounded in patient-specific evidence, and few-shot experiments show that the same rationales improve performance when used as inference-time demonstrations rather than training targets. We identify the root cause as a structural conflict between narrative plausibility and discriminative optimization. We hope our work paves the path toward a more precise understanding of when and how rationale-based supervision helps and when it does not, guiding the responsible development of language models for high-stakes clinical prediction.

## 综合总结
该论文挑战了'使用合成理由数据进行SFT能提升临床预测性能'的普遍假设。通过对阿尔茨海默病预测任务进行504种配置的大规模实验，发现基于理由的SFT反而持续显著地降低了预测性能。研究排除了模型家族、数据规模和理由质量（经专家验证为医学准确）等因素，指出根本原因在于'叙事合理性与判别式优化之间的结构性冲突'。关键发现是，同样的理由作为推理时演示能提升性能，而作为训练目标则有害。该研究为高风险临床预测中如何正确使用理由数据提供了重要指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该研究具有极高的技术深度与洞见，挑战了当前普遍认为'基于合成理由数据的SFT能提升模型推理与预测性能'的假设。通过504种配置的大规模严谨对照实验，不仅证实了Rationale-based SFT在临床判别任务中的性能退化，且通过排除了模型家族、数据规模、基础模型推理能力及理由质量（经人类专家验证）等干扰因素，精准定位了根本原因：'叙事合理性与判别式优化之间的结构性冲突'。此外，通过对比SFT与推理时少样本演示的效果差异，进一步深化了对大模型学习机制的理解，论证极其严密。

### 实用性 (评分: 8.5/10)
对医疗AI及大模型落地从业者具有极高的避坑与指导价值。研究明确警示：在疾病预测等高风险判别式任务中，不应盲目使用理由数据进行监督微调，否则会显著损害模型性能。同时提供了实践出路：同样的理由数据作为推理时的上下文演示有效，而作为训练目标则有害。这一结论可直接指导临床NLP模型的微调策略选择，避免算力与资源的无效浪费。

### 社区活跃度 (评分: 8.5/10)
话题时效性强，直击当前大模型领域'思维链/理由数据微调'的热点与痛点。来源为arXiv论文，实验规模庞大且有人类专家背书，可信度高。该成果对医疗AI社区及大模型推理研究方向具有显著的纠偏与启发作用，有望引发关于'生成式推理与判别式优化边界'的广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.10279
