# AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance

**评分：** 9.2  
**状态：** 正常  
**标签：** Agent, 大模型, EDA, HLS, 芯片设计, 代码重构, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30949v1 Announce Type: new Abstract: High-Level Synthesis (HLS) provides a fast path from concepts to silicon, but converting real-world software into synthesizable HLS code remains challenging due to restrictive language support and the gap between software and hardware programming practices. Existing automated and LLM-based refactoring approaches partially address this problem, yet they often lack flexibility, struggle to scale, and incur high computational costs. We introduce AgRefactor, an LLM-based multi-agent workflow for refactoring software into HLS-compatible programs. AgRefactor incorporates a self-evolving memory system that accumulates and retrieves factual and strategic knowledge across tasks, improving robustness and efficiency on unseen programs. To reduce cost and enhance scalability, it integrates automated refactoring tools, enabling agents to balance LLM-driven rewrites with efficient tool-based transformations. On 9 out of 11 challenging real-world benchmarks, which are 5-10x longer than the most complex cases studied in prior work, AgRefactor outperforms or matches the state-of-the-art automated refactoring tool and a strong LLM-based baseline built on the same framework backbone. Further agentic performance optimization yields a 6.51x geometric mean speedup over the SoTA pragma tuning tool and a 1.20x speedup over optimized open-source designs with less than 20% extra resources. AgRefactor is fully-automated and open-sourced.

## 综合总结
本文提出AgRefactor，一个基于LLM的多智能体工作流，旨在解决软件代码向HLS兼容代码转换的难题。该系统通过自进化记忆机制积累知识，并协同LLM与自动化重构工具以降低成本、提升可扩展性。在更具挑战性的基准测试中，AgRefactor在兼容性上超越SOTA，并在性能优化上实现6.51x的显著加速。项目由领域权威团队发布且完全开源，为芯片设计自动化提供了极具价值的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出AgRefactor，一种基于LLM的多智能体工作流，用于软件到HLS代码的重构。创新性地引入自进化记忆系统以积累跨任务的事实与策略知识，并协同LLM重写与传统自动化重构工具，兼顾灵活性与效率，在复杂长代码基准上显著超越现有SOTA方法，技术深度与新颖性极高。

### 实用性 (评分: 9.5/10)
针对HLS开发中软件与硬件编程范式差异大、重构困难的痛点，提供全自动且开源的解决方案。不仅实现代码兼容，还能带来6.51x的几何平均性能加速，对FPGA/芯片设计工程师具有极高的直接应用与落地价值。

### 社区活跃度 (评分: 9.0/10)
由UCLA Jason Cong等FPGA/HLS领域权威学者发布，来源可信度极高。结合当前火热的Agent技术与传统EDA/HLS痛点，极具时效性和行业影响力，且项目已开源，有望在软硬件协同设计社区产生广泛影响。

## 项目链接
https://arxiv.org/abs/2606.30949
