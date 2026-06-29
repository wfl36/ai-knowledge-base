# Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 大模型, 世界模型, 幻觉缓解, 规划, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27806v1 Announce Type: new Abstract: World models for language agents come in two useful forms. An agent-based world model calls an LLM API and reasons flexibly in language, but its errors appear as hallucinated state changes that are hard to score with ordinary regression losses. A parameterized world model is a trained transition predictor; its errors are easier to measure with quantities such as NodeMSE, delta accuracy, and validity accuracy, but it is usually weaker as a standalone planner. We compare these two families on four graph-structured planning benchmarks and introduce operational hallucination metrics for the agent-based case. The comparison motivates \textbf{Grounded Iterative Language Planning} (GILP), which trains only a small parameterized backbone and combines it with API-based agent reasoning. The backbone supplies valid actions, predicted state deltas, risk, and value; the LLM drafts an action and imagined delta; and a consistency gate asks for revision when the two disagree. On real GPT-4o-mini calls, GILP reduces hallucinated-state rate from 0.176 to 0.035. In calibrated simulator ablations, it raises success from 0.668 to 0.838 while adding only ~22% extra LLM calls.

## 综合总结
本文针对LLM Agent在规划任务中的幻觉传播问题，提出了GILP（Grounded Iterative Language Planning）混合架构。该框架将小型参数化世界模型与LLM推理相结合，通过参数化主干提供有效动作和预测状态增量，并引入一致性门控机制，在LLM起草内容与主干预测不一致时触发修订。实验表明，GILP在GPT-4o-mini上将幻觉状态率从0.176大幅降至0.035，并将任务成功率从0.668提升至0.838，仅增加约22%的LLM调用，为构建高可靠性、低成本的Agent系统提供了极具落地价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文深入比较了基于智能体和参数化的两类世界模型在规划任务中的优劣，创新性地提出了GILP框架，将小型参数化世界模型与LLM推理相结合，并引入一致性门控机制来校验和修正LLM的输出。实验论证严谨，在降低幻觉传播（率从0.176降至0.035）和提升成功率（0.668提升至0.838）上效果显著，技术深度与新颖性俱佳。

### 实用性 (评分: 9.0/10)
对Agent开发者具有极高的实践指导价值。GILP通过小模型做状态预测与校验、大模型做起草的协同模式，在大幅缓解幻觉问题的同时，仅增加了约22%的LLM调用开销。这种轻量级参数化模型+LLM的混合架构，为构建高可靠性、低成本的复杂规划Agent提供了可直接落地的工程范式。

### 社区活跃度 (评分: 8.5/10)
直击当前LLM Agent领域的核心痛点——幻觉问题，话题时效性极强。作为arXiv上的最新研究，结合GPT-4o-mini等主流大模型进行验证，来源可信度高，其提出的混合架构思路对Agent社区具有重要的启发和影响力。

## 项目链接
https://arxiv.org/abs/2606.27806
