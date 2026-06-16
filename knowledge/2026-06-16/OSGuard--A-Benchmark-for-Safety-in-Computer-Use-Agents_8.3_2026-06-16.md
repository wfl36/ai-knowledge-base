# OSGuard: A Benchmark for Safety in Computer-Use Agents

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, Computer-Use, 安全性, 评估基准, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15034v1 Announce Type: new Abstract: Computer-use agents are increasingly evaluated by whether they complete realistic desktop and web tasks. However, task success alone can miss failures in which an agent reaches the nominal goal through an unsafe shortcut. We introduce OSGuard, a dual-granularity benchmark suite for evaluating safety in computer-use agents under benign, unchanged user instructions. OSGuard contains an action-level benchmark for local guardrail decisions and a risk-augmented execution suite for end-to-end evaluation. The action-level benchmark consists of contextualized proposed actions labeled as allowed, unrelated, or unsafe, each judged relative to the original instruction and current interface state. The execution suite contains manually constructed OSWorld-derived task variants in which the original task remains achievable, but the environment is modified to introduce latent hazards such as destructive overwrites, etc. Each variant is paired with augmented evaluators that retain the original task-success criterion while adding explicit state-based safety invariants, allowing us to distinguish safe completions from unsafe completions that satisfy the nominal task objective. Our experimental results on OSGuard show that current multimodal guardrails can perform well on isolated action judgments, while risk-augmented execution exposes remaining gaps between local oversight and reliable end-to-end safety. This dual-granularity design enables more precise diagnosis of whether models can both recognize unsafe proposed actions and improve full-task safety when deployed as guardrails.

## 综合总结
本文提出了OSGuard，一个用于评估计算机使用代理安全性的双粒度基准。它包含动作级护栏基准和风险增强执行套件，旨在发现代理通过不安全捷径完成任务的隐患。实验表明，现有护栏在孤立动作判断上表现尚可，但在端到端风险执行中仍存在显著安全漏洞，为Agent安全评估与护栏部署提供了重要诊断工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了OSGuard双粒度基准，创新性地将安全性评估拆分为动作级判断与风险增强的端到端执行评估。该研究精准识别了现有评估仅关注任务成功率的盲点（即通过不安全捷径达成目标），并基于OSWorld构建了带有安全不变量的任务变体，论证严谨，实验深刻揭示了局部监督与全局端到端安全之间的差距。

### 实用性 (评分: 8.0/10)
对Computer-Use Agent开发者和安全护栏构建者具有极高的实操参考价值。该基准不仅能评估代理是否完成任务，更能精准诊断其是否在执行中引入了破坏性操作（如覆盖重要文件），可直接用于Agent安全对齐与护栏模块的迭代优化。

### 社区活跃度 (评分: 8.5/10)
Computer-Use Agent是当前大模型落地的核心前沿方向，其安全性是制约应用的关键痛点。该研究基于权威OSWorld环境构建，来源可信，切中行业急需解决的安全隐患问题，具有极强的时效性与社区影响力。

## 项目链接
https://arxiv.org/abs/2606.15034
