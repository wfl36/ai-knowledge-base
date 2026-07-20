# Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 推理, AI4Science, 评测基准, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15766v1 Announce Type: new Abstract: Large language models (LLMs) excel at answering pre-specified questions, yet their ability to navigate the open-ended, pre-conclusion stage of discovery remains largely unmeasured. We introduce Prospective Hypothesis Discovery (PHD), which asks models to autonomously construct grounded, discriminative, and testable hypothesis spaces from inconclusive evidence, including anomalous observations and fragmented records, to guide subsequent investigation. To evaluate this capability, we introduce HypoArena, comprising HypoData, a benchmark of 988 cases across six scientific and analytical domains, and HypoEval, an evaluation framework for open-ended hypothesis sets. To construct HypoData at scale, we propose Retrospective Context Regression, a Forge--Audit pipeline that reconstructs pre-conclusion contexts from completed expert documents by removing explicit conclusions, target hypotheses, and retrospective causal attributions while preserving the factual substrate. Because PHD admits multiple valid outputs, HypoEval combines bidirectional pairwise judgments with Bradley--Terry--Davidson aggregation for ranking and six-dimensional rubric scoring for diagnosis. Experiments on 15 frontier LLMs reveal clear capability stratification and model-dependent effects of structured analytical skills, with gains for several lower-performing models on HypoArena but regressions for other systems, including a top-performing model. Compared with absolute rubric scoring, arena evaluation resolves finer-grained differences among models, with aggregated rankings showing strong agreement with human experts and an independent judge. Together, these results support treating PHD as a distinct target for evaluating how LLMs formulate investigative directions when final conclusions are withheld. Our code and data are publicly available at github.com/SKYLENAGE-AI/HypoArena and github.com/SKYLENAGE-AI/HypoArena.

## 综合总结
本文提出了“前瞻性假设发现”（PHD）任务，旨在评估LLM在缺乏明确结论时，从不完整证据中自主构建可测试假设的能力。为此，作者构建了HypoArena基准（包含HypoData数据集和HypoEval评估框架），并创新性地提出了回顾性上下文回归方法来生成评测数据。对15个前沿LLM的实验揭示了模型在假设发现能力上的分层及结构化分析技能的差异化影响，该基准与人类专家评估高度一致，为AI科学发现能力的评测树立了新标准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了“前瞻性假设发现”（PHD）任务，填补了LLM在开放式、结论前阶段发现能力的评测空白。创新性地设计了Retrospective Context Regression和Forge-Audit管道来构建HypoData基准，并开发了结合Bradley-Terry-Davidson聚合与六维评分的HypoEval框架，方法论严谨且具有深度。

### 实用性 (评分: 8.5/10)
为AI4Science和复杂分析领域提供了极具价值的评测工具。HypoArena基准及数据构建方法可直接用于评估和训练模型在不确定证据下生成假设的能力，对开发具备真正科学发现潜力的LLM具有强实践指导意义。

### 社区活跃度 (评分: 9.0/10)
切中当前LLM从“被动回答”向“主动探索”演进的热点趋势。作者团队权威，代码与数据完全开源，且实验覆盖15个前沿模型，与人类专家评估高度一致，具备成为该领域核心基准的潜力。

## 项目链接
https://arxiv.org/abs/2607.15766
