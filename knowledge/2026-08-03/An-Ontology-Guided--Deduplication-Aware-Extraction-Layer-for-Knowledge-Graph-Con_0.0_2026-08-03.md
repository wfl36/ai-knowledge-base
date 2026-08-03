# An Ontology-Guided, Deduplication-Aware Extraction Layer for Knowledge Graph Construction from Heterogeneous Documents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-03  
**来源：** rss  

## 项目描述
arXiv:2607.28662v1 Announce Type: new Abstract: Large language models extract entities and relationships from unstructured documents fluently but inconsistently: type vocabularies fracture across documents, the same person surfaces under several name variants, relationships duplicate, and distinct individuals who share a name risk silent conflation. This paper presents the design, implementation, and empirical refinement of a production extraction layer that converts a live document stream into a validated knowledge graph aligned to a formal ontology. The system consumes document metadata from Kafka, routes PDF, spreadsheet, Office, and image content through handlers built for each format, and extracts entities and relationships in two passes using a locally hosted Qwen3.5-9B model tuned on the ontology. Its distinguishing component is ontology-guided extraction: the relevant slice of a curated ontology is retrieved live from a graph database by embedding similarity and injected into the extraction prompt, reducing catalog overhead by about 94 percent relative to static domain slices. Extracted results then pass through a refinement pipeline of five stages: deterministic cleaning, merging across chunks, a second pass for relationships, six deduplication algorithms that require no model inference, and an embedding resolution subsystem whose conflict guard no similarity score can override. Evaluation on intelligence corpora improved search recall from roughly 70 to 95 percent with no false merges, and corrected seven classes of silent quality defect, ranging from a bug that truncated source text by a single character to the systematic duplication of entities that carried title prefixes.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.28662
