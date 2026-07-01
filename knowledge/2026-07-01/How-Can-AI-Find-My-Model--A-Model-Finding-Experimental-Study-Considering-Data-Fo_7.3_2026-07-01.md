# How Can AI Find My Model? A Model-Finding Experimental Study Considering Data Formats, Embeddings, and Retrieval Strategies

**评分：** 7.3  
**状态：** 正常  
**标签：** 信息检索, 嵌入模型, RAG, 建模与仿真, 模型发现, 论文, 实验研究  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30846v1 Announce Type: new Abstract: Discovering simulation models for reuse remains a fundamental challenge in Modeling and Simulation (M&S). When many models coexist, identifying those that align with a given modeling intent remains difficult. Recent advances in Artificial Intelligence (AI), particularly retrieval-based approaches, offer a promising pathway to operate at this semantic layer. In this paper, we present an experimental study investigating the impact of data representation, transformer-based embedding models, and retrieval strategies on the discovery of simulation models using natural language queries. We evaluated performance across multiple query types using standard information retrieval metrics, including recall@5 and nDCG@5. Results show that data representation matters, open-source embedding models can achieve high performance, and reranking methods are important, especially as query complexity increases. This work provides a baseline for AI-driven model discovery and discusses its role in advancing toward AI-driven composability and interoperability.

## 综合总结
本文是一项关于利用AI检索技术发现仿真模型的实验研究。作者系统评估了数据格式、嵌入模型和检索策略对自然语言查询模型发现的影响，结果表明数据表示至关重要，开源嵌入模型表现优异，且重排序在复杂查询中不可或缺。该研究为AI驱动的模型发现建立了基线，并为提升模型复用与互操作性提供了实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
该研究系统性地评估了数据表示格式、基于Transformer的嵌入模型以及检索策略（尤其是重排序机制）对自然语言查询发现仿真模型的影响。虽然未提出全新的AI基础算法，但通过严格的实验设计（使用recall@5和nDCG@5等标准IR指标）在建模与仿真（M&S）领域建立了AI驱动模型发现的基线，论证严谨，对数据表示和检索策略的深度分析具有一定的技术洞见。

### 实用性 (评分: 8.0/10)
对建模与仿真领域的从业者及系统开发者具有极高的参考价值。研究明确指出了开源嵌入模型即可实现高性能，且在查询复杂度增加时重排序方法至关重要，这为构建模型检索系统、模型资产库及提升模型复用性提供了直接的工程实践指导。

### 社区活跃度 (评分: 7.0/10)
研究结合了当前热门的检索增强（RAG/IR）技术与垂直领域的模型发现问题，具有较好的时效性。arXiv作为来源具备学术可信度，且探讨了AI驱动的组合与互操作性，符合当前AI向系统化、工程化发展的大趋势；但受限于建模与仿真（M&S）的垂直领域属性，在更广泛的AI社区中的影响力相对受限。

## 项目链接
https://arxiv.org/abs/2606.30846
