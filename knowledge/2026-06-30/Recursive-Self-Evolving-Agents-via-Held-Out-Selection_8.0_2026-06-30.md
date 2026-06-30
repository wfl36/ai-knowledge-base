# Recursive Self-Evolving Agents via Held-Out Selection

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, 自我进化, 大模型, 经验学习, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28374v1 Announce Type: new Abstract: LLM agents are increasingly improved without weight updates by evolving a natural-language artifact, such as reflections, workflows, playbooks, cheatsheets, or optimized prompts, that conditions a frozen policy. Such methods are typically reported as wins on the single benchmark where they help. We study them apples-to-apples and surface a sharper picture. We introduce RSEA, a Recursive Self-Evolving Agent that carries a compact three-layer natural-language state: an imperative strategy, reusable skills, and a procedural playbook. Across generations, RSEA rewrites all three layers from its own trajectories and commits a candidate only if it does not regress on a disjoint held-out split, using a strict keep-better gate. Across four diverse benchmarks, ALFWorld, GAIA, (\tau)-bench, and WebShop, and six faithful baselines, ReAct, Reflexion, GEPA, AWM, ACE, and Dynamic Cheatsheet, all evaluated on one shared local backbone, we find three main results. First, no artifact universally wins. RSEA is the strongest single-pass method on ALFWorld, reaching 69.3% compared with 64.6% for ReAct (McNemar (p=0.015)), and reaches 79.4% with retry, the best overall result. However, concrete-workflow induction, represented by AWM, is best on the strong-backbone tool-use tasks. Second, unguarded context evolution is high-variance and unsafe. Dynamic Cheatsheet, which curates context online without a held-out gate, is near-best on ALFWorld at 70.7%, yet collapses on WebShop, with a score of 0.14 compared with 0.43 for ReAct. Third, RSEA's strict held-out selection is what makes recursive self-evolution monotone-safe: it never significantly underperforms the base agent on any benchmark and falls back to vanilla ReAct when evolved context would hurt.

## 综合总结
本文提出RSEA（递归自演化Agent），通过三层自然语言状态（策略、技能、剧本）和严格的留出选择门控机制，解决了LLM Agent在无权重更新自我进化中的不稳定和退化问题。跨4个基准和6个基线的实验表明，无防护的上下文演化具有高风险性，而RSEA的严格门控能确保演化过程的单调安全，且在ALFWorld等任务上达到SOTA。该研究为构建安全、稳定的自学习Agent提供了重要的工程指导和理论依据。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文深入研究了LLM Agent在不更新权重的情况下通过自然语言工件（如反思、工作流等）进行演化的方法。提出了RSEA（递归自演化Agent），采用三层自然语言状态（策略、技能、剧本），并创新性地引入了严格的留出选择门控机制，确保演化过程的单调安全性。研究通过跨4个基准和6个基线的严谨对比实验，揭示了无防护上下文演化的高风险性以及不存在通用最优工件的结论，论证严谨，洞见深刻。

### 实用性 (评分: 8.0/10)
RSEA提出的“留出选择门控”机制对工程实践具有极高的参考价值，有效解决了Agent在自我进化过程中因上下文污染导致的性能崩溃问题，实现了“不退化则保留，退化则回退”的安全策略。其三层状态设计也为Agent的记忆和经验管理提供了清晰的架构模板，可直接指导开发者构建更稳定、可落地的自学习Agent系统。

### 社区活跃度 (评分: 7.5/10)
Agent的自我进化与记忆管理是当前大模型领域的热点话题。该论文针对现有方法在跨场景下表现不稳定甚至崩溃的痛点，提出了具有单调安全保证的解决方案，具有很高的时效性和现实意义。其基于严格对比实验得出的结论对社区具有很好的警示和指导作用，来源权威性较高。

## 项目链接
https://arxiv.org/abs/2606.28374
