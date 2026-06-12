# ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 工具学习, 评估基准, 大模型, 论文, 框架  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12451v1 Announce Type: new Abstract: Large language models deployed as agents over large tool catalogs face a critical tool-retrieval bottleneck. As embedding-based retrieval approaches rely on compact encoders that may under-capture specialized tool semantics, parametric tool retrieval addresses this by encoding each tool as a virtual token appended to the LLM vocabulary, fine-tuned in two stages (memorization then retrieval SFT) to use the LLM as a retriever, achieving strong performance on standard ToolBench retrieval benchmarks. Yet these benchmarks use verbose, fully-specified queries, and their evaluation applies constrained decoding that restricts outputs to valid token paths, neither reveals whether the model actually understands its tools. We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark. Applying ToolSense to ToolBench (~47k tools) and evaluating five parametric model training configurations reveals a knowledge-retrieval dissociation: on RRB queries, several configurations collapse by ~50-64 percentage points compared to fully-specified ToolBench benchmarks, falling below the embedding-model baseline. Additionally, despite strong retrieval performance, some models score near-random on factual probes, suggesting a knowledge-retrieval dissociation. We open-source the ToolSense framework and the ToolBench diagnostic benchmarks at https://github.com/SAP/toolsense.

## 综合总结
本文提出 ToolSense，一个用于审计 LLM 参数化工具知识的开源诊断框架。针对当前参数化工具检索在 ToolBench 上表现虚高的问题，ToolSense 能自动生成包含真实模糊查询(RRB)、多选探测(MCQ)和问答探测(QA)的基准。实验揭示了显著的‘知识-检索分离’现象：在模糊查询下模型性能暴跌50-64个百分点甚至低于传统基线，且在事实探测中接近随机猜测，证明现有模型并未真正理解工具语义。该研究为 Agent 工具调用能力的评估提供了更真实、严谨的测试手段。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
研究深度出色，创新性地揭示了参数化工具检索中存在的‘知识-检索分离’现象，打破了模型检索表现好即代表理解工具的错觉。通过设计三级模糊查询(RRB)、MCQ和QA探测基准，严谨地论证了现有模型在受限解码和完全指定查询下的性能虚高问题，对现有评估体系形成了有力补充和挑战。

### 实用性 (评分: 8.5/10)
可落地性极强，ToolSense 作为一个开源的自动化诊断框架，允许开发者输入任意工具目录即可生成定制化的评估基准。这为构建 LLM Agent 的工程师提供了直接可用的测试工具，能有效检验微调后的模型是否真正掌握了工具语义，避免在真实模糊场景下的灾难性失效。

### 社区活跃度 (评分: 8.2/10)
话题时效性极高，LLM Agent 与工具调用是当前AI领域的核心热点。来源为 arXiv 论文且由 SAP 团队开源，具有较高的权威性和可信度。该研究直击当前主流 ToolBench 评估的痛点，有望推动社区建立更真实、严格的工具检索评估标准，具备较强的影响力潜力。

## 项目链接
https://arxiv.org/abs/2606.12451
