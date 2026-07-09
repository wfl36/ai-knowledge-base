# Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 推理, ARC-AGI, 程序合成, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06764v1 Announce Type: new Abstract: Recent progress on ARC-AGI-1 from disclosed architectures has come broadly from two regimes: heavy test-time compute over frontier models (evolutionary search, exhaustive sampling, extended chain-of-thought), or benchmark-specific training in which small models are fine-tuned on ARC data, often with task-specialized architectures. We study a third regime: an open-weight model in non-thinking mode (DeepSeek V3.2) under a strict budget, with no ARC-specific fine-tuning. We study what is recoverable through architecture alone, building agentic harnesses that decompose pattern-discovery and program-synthesis stages explicitly. First, we introduce an Explorer-Definer Pipeline that separates pattern discovery from executable transformation synthesis, implemented as a two-stage agent pipeline. Next, we present the Reflective Orchestrator, which augments the pipeline with autonomous exploration of new transformations when previous hypotheses fail on training pairs. On the ARC-AGI-1 public 400-task evaluation set, the pipeline reaches 57.50% pass@2 at \$0.25 per task, and the orchestrator reaches 67.25% pass@2 at \$0.62 per task. Together these architectures lift a 15.50% one-shot baseline by ~52 points without benchmark-specific training or heavy test-time compute. Furthermore, the orchestrator-driven lift tests a falsifiable diagnostic the pipeline produces; unbiased pass@k analysis suggests the pipeline is generation-bound, not selection-bound (selection via training-pair accuracy captures ~95% of the candidate ceiling) and predicts that significant improvement requires broader generation, not better ranking. The orchestrator implements this prediction via adaptive re-exploration and confirms it (unbiased pass@1 lift +9.81 pp, matching selection-mediated pass@2 lift). An additional pipeline ablation identifies its think tool as a significant component, with removal reducing pass@2 by 5.75 pp.

## 综合总结
本文针对ARC-AGI-1基准，提出了一种无需特定微调且低成本的Agent架构方案。不同于现有的重测试时计算或微调范式，作者基于DeepSeek V3.2构建了显式解耦模式发现与程序合成的Explorer-Definer Pipeline，以及具备自主反思与重探索能力的Reflective Orchestrator。该方法在极低成本下将one-shot基线提升了约52个百分点，达到67.25%的pass@2。此外，研究通过严谨的诊断分析揭示了系统受限于生成而非选择，并通过Orchestrator验证了该假设，为抽象推理任务提供了极具价值的架构参考与理论洞见。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了区别于“重度测试时计算”和“特定基准微调”的第三种范式，通过纯架构设计挖掘开放权重模型的潜力。其核心创新在于构建了显式解耦模式发现与程序合成的Explorer-Definer Pipeline，以及具备自主反思与重探索能力的Reflective Orchestrator。更深刻的是，研究不仅停留在工程实现，还通过无偏pass@k分析提出了可证伪的诊断结论：系统瓶颈在于生成而非选择，并通过Orchestrator的自适应重探索成功验证了该假设，展现了极高的论证严谨性与研究深度。

### 实用性 (评分: 8.0/10)
对从业者具有极高的实践指导价值。在极低成本（单任务0.62美元）且无需任何ARC特定微调的前提下，将基线提升了约52个百分点。这种将复杂推理任务解耦为‘探索-定义-反思’的Agent架构设计，以及利用训练集进行假设证伪的机制，可直接迁移至其他需要抽象推理、代码生成和复杂问题求解的落地场景中，显著降低了对大模型算力和微调数据的依赖。

### 社区活跃度 (评分: 8.5/10)
ARC-AGI-1作为评估AGI抽象推理能力的核心基准，一直是学术界和工业界关注的焦点。本文在未使用前沿闭源模型和重度计算的情况下取得了极具竞争力的成绩，话题时效性强。其‘低成本、零微调、强架构’的路线对当前普遍依赖暴力搜索的社区风气提供了有力的反证，来源权威，结论具有很高的可信度与启发意义，预计将在AI推理与Agent社区产生显著影响。

## 项目链接
https://arxiv.org/abs/2607.06764
