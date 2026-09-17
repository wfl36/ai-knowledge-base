# GVD: Governed Versioning and Deduplication for Document Repositories

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-17  
**来源：** rss  

## 项目描述
arXiv:2609.17696v1 Announce Type: new Abstract: Document repositories evolve continuously. Guidelines and policies are revised, superseded, and re-uploaded, so the same content recurs in different wording and newer versions refine or contradict earlier ones. These inconsistencies belong to the growing collection rather than to any single document, yet existing work treats versioning, duplicate detection, and contradiction detection as isolated pairwise tasks and stops once a pair is labeled. We present GVD (Governed Versioning and Deduplication), a framework that unifies cross-document version linking with rule-level conflict resolution under an auditable update policy. Incoming documents are assigned to version families through bidirectional rule alignment, and their rules are compared against the family memory to identify duplicates, contradictions, asymmetric refinements, and new knowledge, with Counterfactual Span Probing (CSP) resolving related pairs that inference misclassifies as neutral. Relation-specific policies suppress duplicates and escalate only consequential changes for review, retaining version lineage as an audit trail. The pipeline runs fully locally, with no large language model. On 120 enterprise documents processed as 140 ingestions across 59 version families, GVD reaches an F1 of 0.97 for version-family construction and 0.94 for rule-level consistency, with CSP raising rule consistency from 0.90 to 0.94.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.17696
