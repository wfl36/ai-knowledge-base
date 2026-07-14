# Silent Failures in Quantized LLM Reasoning: A Taxonomy-Based Analysis of Hollow Convergence and Failure Mode Shifts

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 量化, 推理, 评估, 失败模式, 论文, 实证研究  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09999v1 Announce Type: new Abstract: We show that post-training quantization can silently alter how large language models reason even when task accuracy is preserved. Using a six-category failure taxonomy validated by two independent human annotators (Cohen's $\kappa$ = 0.906), we classify 30,000 chain-of-thought outputs from five instruction-tuned LLMs (3B--14B parameters) across three quantization precisions (FP32, FP16, NF4) and four reasoning benchmarks. We find that while accuracy is robust across precisions (maximum 3.1 pp drop), Hollow Convergence (correct answers reached through incomplete or unverifiable reasoning) shows a significant size-dependent shift under NF4, dropping sharply for the two smallest models tested but remaining invariant for models at 12B parameters and above. This effect is also benchmark-specific: GSM8K is categorically immune while LogiQA and ARC-Challenge show the largest shifts. Furthermore, under NF4, Shortcut Collapse rises from 44% to 78% of wrong-answer failures in LLaMA 3.2-3B while Confidence Snowballing collapses from 15.8% to near zero, a qualitative shift invisible to accuracy metrics. Finally, we show Hollow Convergence cannot be reliably detected from surface-level text features (best F1 = 0.53), establishing it as a deployment-relevant failure mode that standard evaluation pipelines cannot catch.

## 综合总结
本文深入研究了后训练量化对大语言模型推理过程的隐性影响，提出了“空洞收敛”（Hollow Convergence，即通过不完整或不可验证的推理得出正确答案）的概念。通过对3万条CoT输出进行六类失败模式分类，研究发现尽管量化（NF4）对准确率影响微小，但会导致小模型的空洞收敛显著下降，且不同基准测试表现不一（GSM8K免疫，LogiQA/ARC受影响大）。此外，NF4量化引发了从“信心雪球”到“捷径崩溃”的定性偏移。研究证明这些隐性失败无法通过表面文本特征检测，揭示了标准评估流水线在量化模型部署中的严重盲区。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了“空洞收敛”这一新颖概念，揭示了后训练量化在保持任务准确率的同时悄然改变LLM推理过程的深层机制。研究构建了六类失败模式分类法，并通过严格的人工标注（Cohen's κ=0.906）和大规模CoT输出分析，论证了NF4量化下不同规模模型和基准测试的失败模式偏移（如Shortcut Collapse激增、Confidence Snowballing消失），技术深度与论证严谨度极高。

### 实用性 (评分: 8.5/10)
对LLM部署实践具有高度指导意义。研究明确指出标准准确率指标无法捕捉量化带来的推理质量降级，特别是小模型在NF4下的“空洞收敛”和捷径崩溃现象。这警示从业者在评估量化模型（尤其是3B-8B级别）时，必须超越表面准确率，深入审查推理链的完整性与可验证性，对关键推理场景的模型量化部署具有直接参考价值。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，直击当前大模型轻量化部署中的痛点。量化（尤其是NF4）是社区关注的核心技术，而该研究指出常规评估体系的盲区，极易引发广泛讨论与后续研究。arXiv预印本发布，结论对现有评估范式构成挑战，具有较高的社区影响潜力。

## 项目链接
https://arxiv.org/abs/2607.09999
