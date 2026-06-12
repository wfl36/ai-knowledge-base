# Arbor: Tree Search as a Cognition Layer for Autonomous Agents

**评分：** 9.2  
**状态：** 正常  
**标签：** Agent, 多智能体, 推理优化, 树搜索, 系统优化, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12563v1 Announce Type: new Abstract: Arbor is a multi-agent framework that introduces structured tree search as a cognition layer for autonomous agents operating in large, stateful action spaces. Prior autonomous optimization systems operate on isolated targets with stateless evaluation. Arbor instead maintains an explicit search tree of scored hypotheses that serves as the shared working memory across agents, evolving with every measurement, treating failures as diagnostic signal that reshapes subsequent exploration, and expanding as prior successes shift the bottleneck distribution. We validate Arbor on full-stack LLM inference optimization, a domain where achieving peak performance has historically required coordinated effort from engineering teams across the application, framework, compiler, kernel, and hardware stack. Arbor pairs an Orchestrator agent, which drives optimization by delegating to Domain Specialists across the inference stack, with a Critic agent that safeguards stability through root-cause analysis, introspection, and measurement validation -- a checks-and-balances architecture where neither agent can unilaterally drive the system. Agent capabilities are decomposed into hard skills (domain expertise) and soft skills (coordination protocols that determine how contributions compose), enabling fully autonomous multi-day campaigns. Arbor achieves up to 193% inference throughput-latency Pareto improvement over vendor-optimized baselines, while a single agent without the harness plateaus at +33% throughput improvement and crashes irrecoverably within hours. Arbor generalizes to multiple generations of hardware platform, and run-to-run variance is within 2 percentage points demonstrating that the method is hardware-agnostic and reproducible.

## 综合总结
本文提出了 Arbor，一个将结构化树搜索作为认知层的多智能体框架，用于解决大状态动作空间下的自主优化问题。不同于以往的无状态评估，Arbor 维护显式的带评分假设搜索树作为共享工作记忆，将失败转化为诊断信号指导后续探索。在全栈 LLM 推理优化场景中，Arbor 采用 Orchestrator-Critic 制衡架构，实现了多天全自主稳定优化。实验表明，相比厂商优化基线，Arbor 实现了高达 193% 的推理吞吐量-延迟 Pareto 提升，且跨硬件泛化性强、可复现性高，而单智能体不仅提升有限且极易崩溃。该工作为复杂系统优化提供了极具潜力的 Agent 架构范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
将结构化树搜索作为多智能体的共享认知层，突破了传统自主优化系统无状态评估的局限。通过显式搜索树将失败转化为诊断信号重塑探索方向，结合 Orchestrator-Critic 制衡架构与硬软技能解耦机制，在极具挑战的全栈 LLM 推理优化场景中展现了极深的技术洞察与严谨的系统工程逻辑。

### 实用性 (评分: 9.5/10)
针对 LLM 推理优化这一业界核心痛点，提供了可落地的全栈自主优化方案。其多智能体制衡架构、硬软技能解耦及搜索树记忆机制，不仅适用于推理优化，对编译器自动调优、芯片设计探索、分布式系统配置等复杂工程实践同样具有极高的架构参考价值与复用潜力。

### 社区活跃度 (评分: 9.0/10)
LLM 推理成本与优化是当前 AI 社区最迫切的需求之一，话题时效性极强。作者团队具备深厚的系统与硬件背景，实验对比详实（对比厂商基线与单智能体，验证跨硬件泛化与可复现性），数据极具说服力，预计将在 AI 系统与 Agent 社区产生重要影响。

## 项目链接
https://arxiv.org/abs/2606.12563
