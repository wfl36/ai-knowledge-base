# HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs

**评分：** 7.0  
**状态：** 正常  
**标签：** RAG, 知识图谱, 图推理, 大模型, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14095v1 Announce Type: new Abstract: Retrieval Augmented Generation (RAG) has proven to be a widely successful process at improving the quality of outputs from a Large Language Model (LLM) for wider context. However, RAG systems typically retrieve context from flat document stores, which struggles when queries require hierarchical or relational reasoning across structured knowledge. I present HG-RAG (Hierarchy-Guided RAG), a framework that performs graph-traversal over a hierarchical knowledge graph to deliver structured context to a language model. My retrieval pipeline resolves a named entity anchor from the query, then expands context upward through parent nodes, laterally through relational neighbors, and downward through child nodes when needed. I evaluate HG-RAG against a dense retrieval baseline across three world scales (18-800 nodes) with four query types: local fact, hierarchical, neighborhood, and multi-hop. Results show HG-RAG consistently outperforms the flat baseline on hierarchical, relational, and multi-hop reasoning tasks, while reducing hallucination and maintaining locality coherence.

## 综合总结
本文提出了HG-RAG框架，通过在层次化知识图谱上进行图遍历（向上追溯父节点、横向检索关系邻居、向下深入子节点）来增强RAG系统的结构化推理能力。实验表明，该方法在层次、关系和多跳推理任务上优于扁平检索基线，有效降低了幻觉并保持了局部连贯性，为结构化知识库的RAG应用提供了新思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
针对扁平RAG在层次和关系推理上的不足，提出了基于层次知识图谱的图遍历检索框架HG-RAG。其向上追溯父节点、横向检索关系邻居、向下深入子节点的上下文扩展策略设计合理，具有一定的技术新颖性；但评估规模较小（18-800节点），对大规模图谱的可扩展性和复杂图结构的鲁棒性论证不足，整体研究深度中等偏上。

### 实用性 (评分: 7.5/10)
对处理结构化知识库（如企业本体库、层级目录）的RAG开发者具有较高参考价值，图遍历检索策略可直接指导工程实践。但落地前提是需要预先构建高质量的层次化知识图谱，这在实际业务中构建与维护成本较高，且受限于当前评估规模，大规模工业级应用的性能表现有待验证。

### 社区活跃度 (评分: 6.5/10)
RAG与知识图谱结合（GraphRAG）是当前大模型领域的热点方向，话题时效性极强。但该论文为arXiv预印本，且为单人作者，尚未经过同行评审，实验评估数据集规模偏小，来源权威性与学术可信度一般，短期内影响力有限。

## 项目链接
https://arxiv.org/abs/2607.14095
