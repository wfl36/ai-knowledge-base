# SANA: What Matters for QA Agents over Massive Data Lakes?

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, 数据湖, 评估框架, 问答系统, 数据分析, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13904v1 Announce Type: new Abstract: Exploratory question answering (EQA) over data lakes requires an LLM agent to discover relevant sources, analyze retrieved data, and adapt its actions based on intermediate results. End-to-end accuracy alone cannot distinguish failures in search, planning, data analysis, or the agent's Action Policy: its decisions about what to do next and when to submit an answer. We present SANA (Search Agent Navigation Ablation framework), a diagnostic ablation framework that transforms EQA tasks into runtime profiles containing gold source sequence, sanitized subquestions, and execution records. SANA uses these profiles to construct idealized search, planning, and data-analysis tools, allowing each component to be ablated; the residual gap is diagnostic evidence for policy failures. To illustrate SANA as a reusable evaluation framework, we adapted two recent EQA benchmarks, LakeQA and KramaBench, and evaluated lightweight and mid-sized agents under fixed prompts, budgets, data lakes, and runtimes. Across both benchmarks, data analysis is a consistent bottleneck while planning is less so. Search is a major limitation in LakeQA's large data-lake setting, but less so for the smaller-scale KramaBench. SANA thus deconstructs end-to-end task accuracies into a diagnosis of where data-lake agents fail, and allows for systematic comparisons of progress in search, planning, data analysis, and agent design.

## 综合总结
本文提出了SANA框架，用于诊断数据湖探索性问答（EQA）Agent的失败原因。该框架通过构建理想化的搜索、规划和数据分析工具进行消融实验，将端到端准确率解构为组件级诊断证据。在LakeQA和KramaBench上的实验表明，数据分析是Agent的主要瓶颈，而搜索能力在大规模数据湖中限制显著。该研究为Agent的精细化评估和优化提供了重要的方法论支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了SANA诊断消融框架，创新性地将EQA Agent的端到端准确率解构为搜索、规划和数据分析三个组件的归因分析。通过构建理想化工具进行控制变量消融实验，为Agent策略失败提供了细粒度的诊断证据，方法论严谨且具有较高的技术深度。

### 实用性 (评分: 7.5/10)
对开发数据湖QA Agent的从业者具有较高参考价值，能帮助开发者精准定位Agent性能瓶颈（如搜索召回不足、规划错误或数据分析能力弱），从而进行针对性优化。但框架的部署需要构建黄金源序列等先验数据，实际落地存在一定的实施成本和门槛。

### 社区活跃度 (评分: 8.0/10)
针对数据湖探索性问答这一高时效性热点领域，填补了Agent组件级评估方法的空白。论文来源于arXiv，学术可信度良好，其得出的“数据分析是持续瓶颈”等反直觉结论对社区后续Agent设计方向具有较强指导意义和影响力。

## 项目链接
https://arxiv.org/abs/2606.13904
