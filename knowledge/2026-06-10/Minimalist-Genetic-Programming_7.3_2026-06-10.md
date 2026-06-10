# Minimalist Genetic Programming

**评分：** 7.3  
**状态：** 正常  
**标签：** 符号回归, 程序归纳, 遗传编程, 进化计算, 论文  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10237v1 Announce Type: new Abstract: Genetic programming (GP) is based on two important insights. First, that any learning task can fundamentally be posed as a program induction problem, where the goal is to construct a symbolic hierarchical model that is expressed as a syntax tree. Second, to pose this task as a search problem, and use evolution to locate the desired model. Since it was proposed, GP has produced notable results in a wide range of tasks and problem domains. This work presents an alternative view by modifying the second core insight of GP, posing the problem as a syntactic derivation task instead. In particular, this paper presents Minimalist Genetic Programming (MGP), an algorithm that like GP is biologically inspired, but instead of evolution it takes inspiration from the Minimalist Program to human language, in which syntax is understood as an optimal solution to the problem of linking two other mental systems. In minimalism, the core computational process is a binary set formation operator called $MERGE$, than can be used to incrementally construct complex syntactic structures using a simple Markovian process. MGP is able to discover the core building blocks of the symbolic expressions, and to incrementally combined them using $MERGE$. The proposed system is benchmarked on symbolic regression tasks that are known to be difficult to solve with standard GP systems because of the propensity for bloat. Results show that when a proper lexicon of atomic syntactic objects are chosen, MGP is able to consistently produce the exact ground truth model on a set of symbolic regression where standard GP struggles to do the same. The insights provided by minimalism are shown to be relevant to the problem of program induction, and should be explored further based on the potential exhibited by MGP in this work.

## 综合总结
本文提出极简遗传编程（MGP），颠覆了传统GP的进化搜索范式，将其重构为基于语言学最简方案的句法推导任务。通过引入MERGE算子，MGP能以马尔可夫过程逐步构建符号表达式，有效克服了标准GP的代码膨胀问题，并在符号回归任务中成功还原了精确的真实模型，为程序归纳提供了突破性的新视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了突破性的跨学科视角，将传统遗传编程（GP）的核心逻辑从'进化搜索'重构为'句法推导'。受语言学最简方案启发，引入MERGE算子通过马尔可夫过程构建句法结构，理论新颖且论证严谨，在解决GP长期存在的代码膨胀问题上展现了显著的技术深度。

### 实用性 (评分: 6.5/10)
对符号回归和程序归纳从业者具有较高的参考价值，提供了一种避免代码膨胀并生成精确可解释符号模型的新路径。但在实际落地中，算法性能依赖于'合适词汇表'的选择，需要一定的先验知识，目前适用范围主要局限于符号回归任务，泛化性有待进一步验证。

### 社区活跃度 (评分: 7.0/10)
程序合成与符号回归在当前AI可解释性需求下仍具时效性。论文来源于arXiv，作者在GP领域具有一定可信度。虽然语言学最简方案的引入相对小众，但其颠覆性的思路有望在进化计算和符号AI社区引发关注与讨论。

## 项目链接
https://arxiv.org/abs/2606.10237
