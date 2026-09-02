# RePro: Proof-Verified Benchmark Rewriting for Reliable Evaluation of LLM Mathematical Problem Solving

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 推理, 数学, 基准评估, 数据污染, 自动定理证明, 论文  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00062v1 Announce Type: new Abstract: Data contamination undermines the reliable evaluation of large language models (LLMs) on mathematical problem solving. While rewriting-based evaluation mitigates memorization, existing methods lack guarantees of problem validity and answer correctness. We propose Proof-Verified Benchmark Rewriting (RePro), the first framework to integrate Lean-oriented neural automated theorem provers (ATPs) into benchmark rewriting, which rewrites problems and regenerates answers with correctness ensured by Lean-verified proofs. Experiments on GSM8K and MATH show that RePro's retained rewritten instances achieve 100% well-definedness, feasibility, and answer correctness, while existing methods still produce invalid or incorrect instances. Moreover, several models exhibit accuracy drops on proof-verified rewritten benchmarks, suggesting that their performance is sensitive to surface-level and structural variations and may partly reflect memorization effects. Our source code and data are available at https://github.com/AI4Engi/RePro.

## 综合总结
RePro 提出首个基于 Lean 神经定理证明器的数学基准重写框架，通过形式化证明确保重写后问题的正确性，在 GSM8K 和 MATH 上实现 100% 正确性保证，揭示了现有 LLM 在数学基准上可能存在的记忆效应。方法新颖且对数学推理评估领域具有重要参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出 RePro 框架，首次将 Lean 导向的神经自动定理证明器(ATP)集成到基准重写流程中，通过形式化证明验证保证重写后问题的良定义性、可解答性与答案正确性，方法新颖且论证严谨。100% 的正确性保证与现有方法的对比实验设计合理，技术深度较高。

### 实用性 (评分: 7.5/10)
对从事 LLM 数学推理评估的研究者具有较高参考价值，提供了一套可复现的基准重写工具与数据(已开源)，能有效缓解数据污染问题。但框架依赖 Lean 证明生态，对非形式化验证背景的从业者门槛较高，且适用场景局限于数学问题。

### 社区活跃度 (评分: 7.0/10)
数据污染是 LLM 评估领域的热点问题，话题时效性强。作者来自高校研究团队并在 arXiv 发布，来源可信。但论文为预印本且发表日期标注 2026 年(可能为系统异常)，未经同行评审，引用与社区影响力尚待观察。

## 项目链接
https://arxiv.org/abs/2609.00062
