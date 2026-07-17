# Automatically Evolving Prompt Guidelines for Task-Specific Optimization

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 提示工程, 推理, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14105v1 Announce Type: new Abstract: For Large Language Models to reliably answer user queries, users must clearly specify requirements, context, and constraints. In practice, however, user queries are often underspecified, forcing models to infer unstated assumptions that may misalign with the actual user intent. Existing prompt engineering guidelines aim to mitigate this issue, they are typically generic and task-agnostic, limiting their practical utility. Additionally, existing guidelines are formed manually and in a non-systematic way. To this end, we study prompt guideline optimization: the problem of automatically generating task-specific guidelines that help write better-specified prompts for a given task and model. Our key observation is that existing (completed) task examples (aka reference answers) often implicitly encode the missing information required to complete underspecified queries, including behavioral constraints, contextual assumptions, and evaluation criteria. We therefore propose AGOPS, an automatic approach that evolves task-specific guidelines via an optimization scheme that involves a prompt LLM writer, a solver LLM and prompt evolution, which maximize downstream effectiveness on a set of examples (user queries with reference answers). At inference time, our guidelines help users write well-specified prompts, boosting the effectiveness of LLMs. We show across mathematical reasoning, medical question answering, and coding tasks, that prompt underspecification leads to major drops (up to 95.3%) in downstream task performance (compared to well-specified prompts) and, perhaps more importantly, that this drop can hardly be recovered by existing prompt optimization techniques. Users following AGOPS guidelines can regain this loss (increasing performance between 15.5 to 81.7% on average) consistently across all benchmarks.

## 综合总结
本文针对LLM用户提示词欠规范导致性能严重下降的问题，提出AGOPS框架，通过自动进化生成任务特定的提示指南。实验表明，提示欠规范可导致性能下降高达95.3%，且现有优化技术难以弥补，而遵循AGOPS生成的指南可平均恢复15.5%至81.7%的性能，为大模型提示工程提供了全新的自动化优化范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了一种自动进化任务特定提示指南的新方法AGOPS，突破了传统通用且手动的提示工程限制。该方法创新性地从已有的参考答案中挖掘隐含的行为约束和上下文假设，并结合LLM编写器、求解器和进化算法进行自动化迭代优化。论证严谨，不仅量化了提示欠规范对性能的毁灭性影响（最高下降95.3%），还指出了现有提示优化技术在应对欠规范提示时的失效，充分验证了AGOPS的有效性。

### 实用性 (评分: 8.0/10)
针对用户提示词欠规范这一普遍痛点，AGOPS提供了一种高度可落地的自动化解决方案。生成的任务特定指南可直接指导普通用户编写高质量提示词，在数学推理、医疗问答、编程等垂直场景具有广泛适用性，能有效提升LLM应用的下游任务表现，大幅降低非专业用户使用大模型的门槛。

### 社区活跃度 (评分: 8.0/10)
论文聚焦大模型应用落地的核心痛点——提示词规范问题，切中当前AI社区的热点与难点。arXiv首发，来源可信。其揭示的欠规范提示导致的性能断崖及现有优化方法的无力，对从业者和研究者具有强烈的警示意义，提出的自动化进化指南新范式预计将在社区引发广泛关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.14105
