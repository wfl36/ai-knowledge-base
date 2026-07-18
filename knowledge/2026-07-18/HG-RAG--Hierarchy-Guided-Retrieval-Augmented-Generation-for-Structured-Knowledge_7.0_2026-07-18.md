# HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs

**评分：** 7.0  
**状态：** 正常  
**标签：** RAG, 知识图谱, 图推理, 论文  
**更新日期：** 2026-07-18  
**来源：** rss  

## 项目描述
arXiv:2607.14095v1 Announce Type: new Abstract: Retrieval Augmented Generation (RAG) has proven to be a widely successful process at improving the quality of outputs from a Large Language Model (LLM) for wider context. However, RAG systems typically retrieve context from flat document stores, which struggles when queries require hierarchical or relational reasoning across structured knowledge. I present HG-RAG (Hierarchy-Guided RAG), a framework that performs graph-traversal over a hierarchical knowledge graph to deliver structured context to a language model. My retrieval pipeline resolves a named entity anchor from the query, then expands context upward through parent nodes, laterally through relational neighbors, and downward through child nodes when needed. I evaluate HG-RAG against a dense retrieval baseline across three world scales (18-800 nodes) with four query types: local fact, hierarchical, neighborhood, and multi-hop. Results show HG-RAG consistently outperforms the flat baseline on hierarchical, relational, and multi-hop reasoning tasks, while reducing hallucination and maintaining locality coherence.

## 综合总结
本文提出HG-RAG框架，针对传统RAG在扁平文档检索中难以处理层次和关系推理的痛点，通过在层次化知识图谱上进行图遍历（向上溯源、横向关联、向下展开）来获取结构化上下文。实验表明，该方法在层次、关系和多跳推理任务上优于扁平检索基线，能有效减少幻觉并保持局部一致性，对GraphRAG的工程实践具有较好参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
提出基于层次化知识图谱的图遍历检索策略（向上溯源父节点、横向关联邻居、向下展开子节点），有效弥补了传统扁平RAG在关系与层次推理上的不足，思路清晰且具备针对性；但实验规模偏小（18-800节点），在超大规模图谱上的算法扩展性与复杂度论证略显不足。

### 实用性 (评分: 7.5/10)
其“锚点定位+三向扩展”的检索策略对构建知识图谱RAG系统具有直接的工程参考价值，易于在Neo4j等图数据库中落地实现；但前提是需要预先构建高质量的层次化知识图谱，这在实际业务中构建成本较高，适用场景主要局限于具备明确层级关系的领域。

### 社区活跃度 (评分: 6.5/10)
RAG与知识图谱结合（GraphRAG）是当前AI领域的热点方向，话题时效性强；但该文为arXiv预印本且为单人作者，缺乏同行评审，且实验验证规模有限，来源权威性与社区影响力目前处于中等水平。

## 项目链接
https://arxiv.org/abs/2607.14095
