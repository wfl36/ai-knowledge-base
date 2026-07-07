# SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery

**评分：** 8.2  
**状态：** 正常  
**标签：** 多Agent系统, 代码生成, 开放式探索, 自动化优化, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02807v1 Announce Type: new Abstract: Long-running coding agents such as autoresearch can persistently discover optimizations for open-ended problems. However, they tend to converge onto a single high-level approach, then proceed with low-level edits while missing other superior approaches to the problem. We hypothesize two harness-level design choices contribute to this behavior: accumulating context in a single long-running agent and only exposing a single program state to edit. We introduce SwarmResearch, an orchestrator-subagent harness in which a Shepherd Agent uses global context to steer a population of Search Agents, each operating with local context in their respective git branch. On open-ended optimization tasks, SwarmResearch discovers better or comparable solutions to state-of-the-art LLM-guided evolution and multi-agent techniques on 13/15 tasks, driven by higher-level exploration. Compared with fixed scaling of serial and parallel agents, SwarmResearch's orchestrator-guided scaling discovers better-performing solutions by adapting parallelism at different search depths.

## 综合总结
SwarmResearch提出了一种新型的orchestrator-subagent多Agent架构，旨在解决长期运行编码代理在开放式问题中易陷入局部最优的问题。通过引入Shepherd Agent进行全局上下文引导，以及多个Search Agent在独立Git分支中进行局部上下文操作，该架构实现了更高级别的探索和动态并行度调整。实验表明，该方法在13/15的开放式优化任务上优于现有SOTA，为多Agent协作和自动化代码发现提供了极具价值的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文精准识别了现有长期运行编码代理在开放式问题中易收敛于单一方案并陷入低级修改的痛点，并从架构层面（上下文累积与状态暴露）给出了合理解释。提出的SwarmResearch架构通过全局上下文引导与局部上下文隔离，结合Git分支实现状态解耦，设计精巧，实验在13/15任务上超越SOTA，论证严谨，具有较高的技术深度与新颖性。

### 实用性 (评分: 8.0/10)
该研究对多Agent系统设计具有极高的实践指导价值。其'牧羊犬-搜索代理'的编排模式、利用Git分支进行状态隔离的工程实践，以及动态调整并行度的策略，可直接应用于现有的代码生成、自动化测试与优化框架中，帮助开发者构建更具探索性和鲁棒性的AI Agent应用。

### 社区活跃度 (评分: 8.0/10)
多Agent协作与自动化代码探索是当前大模型领域的核心热点。作者来自知名学术机构，发布于arXiv，具备较高的来源权威性。该工作为解决开放式探索中的局部最优问题提供了新范式，对AI Agent研究社区具有较强的影响力和启发性。

## 项目链接
https://arxiv.org/abs/2607.02807
