# Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 长期记忆, 多跳推理, 知识图谱, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19359v1 Announce Type: new Abstract: Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured. We make three contributions. First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations. Second, we present Profile-Graph Memory (ProGraph), a two-layer memory architecture combining (i) profile expansion -- substring-matched traversal of entity names that naturally appear in LLM-written profile narratives, a minimal alternative to explicit knowledge-graph construction -- and (ii) compression residuals -- exact dates, quantities, and named items co-extracted with each profile update at zero extra API cost. Third, a full-grid ablation shows cross-benchmark mechanism specialization: profile expansion drives multi-hop reasoning (-22.6pp on MemHop when removed) while compression residuals drive precision recall (-8.6pp on LoCoMo when not co-extracted), with cross-effects under 3pp within a single architecture. ProGraph averages 80.1% on MemHop (matching the FullContext reference) and 78.4% on LoCoMo (exceeding FullContext by 11.3pp), outperforming Mem0, A-Mem, HippoRAG, and RAG on both. We release MemHop, ProGraph, and baseline implementations.

## 综合总结
本文针对LLM Agent长期记忆中多跳关联评估缺失的问题，提出了多跳记忆基准MemHop和双层记忆架构ProGraph。ProGraph通过叙事配置文件中的子串匹配隐式遍历实体（替代显式知识图谱），并结合零成本的压缩残差保留精确信息。实验证明该架构在多跳推理和精确召回上机制特化，在MemHop和LoCoMo基准上均显著优于现有主流方法，且工程实现极简，具有极高的落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
提出了一种新颖的双层记忆架构ProGraph，巧妙地通过LLM生成叙事中的子串匹配遍历替代显式知识图谱构建，并结合压缩残差机制保留精确信息。同时构建了多跳记忆基准MemHop填补了评估空白，全网格消融实验严谨地揭示了不同机制在多跳推理和精确召回上的特化作用，技术深度与新颖性俱佳。

### 实用性 (评分: 9.2/10)
对Agent开发者具有极高的实践指导价值。ProGraph避免了显式知识图谱的高昂构建与维护成本，采用极简的子串匹配和零额外API成本的压缩残差提取，易于在现有Agent框架中实现。在多跳推理和长期对话基准上显著优于Mem0、HippoRAG等现有方案，可直接应用于个人助理、社交模拟等需要复杂长期记忆的Agent场景。

### 社区活跃度 (评分: 8.5/10)
紧扣当前LLM Agent长期记忆的研究热点，与Mem0、HippoRAG等近期热门工作直接对比并展现出优越性能。论文承诺开源基准和代码，增强了结果的可复现性与可信度，其极简且高效的实现路径预计将在Agent记忆系统社区产生较大影响力。

## 项目链接
https://arxiv.org/abs/2607.19359
