# Dream at SemEval-2026 Task 13: SALSA for Single-Pass Machine-Generated Code Detection

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 代码检测, OOD泛化, 分类, 论文, 评测  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.25102v1 Announce Type: new Abstract: Large language models have transformed code generation, raising concerns around authorship, assessment integrity, and software trust. SemEval-2026 Task 13 Subtask A operationalizes detection as binary classification over code snippets, with a particular emphasis on out-of-distribution (OOD) generalization across unseen programming languages and application domains. We propose a SALSA-style formulation, Single-pass Autoregressive LLM Structured Classification, that maps each class to a dedicated output token and trains the model to emit a single-token label in a structured response. Rather than engineering hand-crafted features or decision rules, this formulation delegates the authorship decision to the model. To improve OOD robustness, we combine balanced sampling across languages with parameter-efficient fine-tuning and conservative training (low learning rate, single epoch) to avoid overfitting to the training domain. Our best system achieves OOD $F_1 = 0.789$ on the official leaderboard, substantially outperforming the CodeBERT baseline ($F_1 = 0.305$).

## 综合总结
本文针对SemEval-2026 Task 13机器生成代码检测任务，提出SALSA单次自回归结构化分类方法，将分类转化为单token生成。通过结合平衡采样、参数高效微调和保守训练，有效提升了模型在跨语言和跨领域上的OOD泛化能力，在官方排行榜上取得0.789的OOD F1分数，显著优于CodeBERT基线。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出SALSA风格的分类方法，将二分类转化为单token自回归生成，无需手工特征；结合平衡采样、参数高效微调(PEFT)和保守训练策略有效解决OOD泛化问题，在SemEval-2026任务中大幅超越基线。

### 实用性 (评分: 8.5/10)
针对机器生成代码检测的OOD痛点（跨语言/跨领域），提出单次推理方案，兼顾了检测效果与推理效率，对代码审查、学术诚信等场景具有高落地价值。

### 社区活跃度 (评分: 9.0/10)
基于SemEval-2026权威评测任务，关注LLM代码生成带来的信任与合规问题，具有极高的时效性和社区关注度。

## 项目链接
https://arxiv.org/abs/2606.25102
