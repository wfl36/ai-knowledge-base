# Generative Ontology Induction: Domain-Agnostic Schema Discovery from Document Corpora Using Large Language Models

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 知识图谱, 本体工程, 结构化抽取, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16201v1 Announce Type: new Abstract: Ontology engineering remains a critical bottleneck in knowledge-intensive AI systems. Existing automated approaches either depend on predefined schemas, operate within narrow domains, or produce unstructured outputs unsuitable for downstream pipelines. We introduce Generative Ontology Induction (GOI), a domain-agnostic framework that induces a generative blueprint - entities, dimensions, properties, relationships, and constraints - from a corpus of examples and exports it as a typed graph (six node types, seven edge types) in YAML/JSON. We introduce the Node Coverage Score, a novel evaluation metric that measures the fraction of structural ontology nodes (classes, properties, and dimensions) appearing in generated outputs. A controlled generative validation on four contrasting ontologies - a familiar Software Services Invoice schema, a custom Job Description Ontology, a confidential Pain-Management Clinical Visit Record Ontology, and a Professional Services Contract & Statement of Work Ontology - shows that GOI-prompted generation covers 95-100% of the structural backbone in every case; a generic three-field template holds at 97.8% on the invoice schema but drops to 52.2% on the Job Description Ontology, 62.2% on the Pain-Management ontology, and 78.3% on the Professional Services Contract ontology. The structural coverage holds regardless of how familiar the document type is to the model.

## 综合总结
本文提出了一种名为生成式本体归纳（GOI）的领域无关框架，利用大语言模型从文档语料库中自动发现并提取实体、维度、属性、关系和约束，生成结构化的类型化图（YAML/JSON格式）。同时提出了Node Coverage Score新指标来评估结构覆盖率。在四个不同领域的本体（发票、职位描述、临床记录、合同）上的实验表明，GOI能实现95-100%的结构骨干覆盖率，且不受文档类型对模型熟悉度的影响，显著优于通用模板方法，有效解决了知识密集型AI系统中的本体工程瓶颈。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出了生成式本体归纳（GOI）框架，创新性地利用大语言模型从非结构化语料中自动提取包含实体、维度、属性、关系和约束的结构化本体，并输出为具有6种节点和7种边类型的类型化图（YAML/JSON）。同时提出了Node Coverage Score这一新颖评估指标，用于衡量生成本体对结构骨干的覆盖程度。实验设计严谨，在四个差异显著的本体上进行验证，证明了方法的有效性及对领域熟悉度的鲁棒性，技术深度与论证严谨度较高。

### 实用性 (评分: 9.0/10)
本体工程一直是知识密集型AI系统落地的关键瓶颈，该框架具有极高的可落地性。其领域无关特性和结构化输出格式（YAML/JSON）可直接无缝接入下游知识图谱构建、RAG系统增强及企业数据治理流水线。实验覆盖了发票、招聘、医疗和合同等典型业务场景，证明了其在垂直领域自动化知识抽取与模式发现中的广泛适用性和实用价值。

### 社区活跃度 (评分: 7.5/10)
利用大模型进行自动化知识工程是当前AI社区的热点方向，该论文紧扣痛点，时效性强。论文发布于arXiv，具有一定可信度，但作者为单一学者，缺乏大型机构背书，其提出的方法和指标在社区内的广泛影响力尚需后续实际应用和引用的检验。

## 项目链接
https://arxiv.org/abs/2607.16201
