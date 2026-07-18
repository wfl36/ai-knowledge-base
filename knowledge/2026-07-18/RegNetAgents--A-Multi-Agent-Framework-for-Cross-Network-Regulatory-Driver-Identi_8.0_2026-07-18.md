# RegNetAgents: A Multi-Agent Framework for Cross-Network Regulatory Driver Identification in Cancer Genomics

**评分：** 8.0  
**状态：** 正常  
**标签：** 多智能体, 癌症基因组学, 基因调控网络, 生物信息学, 论文  
**更新日期：** 2026-07-18  
**来源：** rss  

## 项目描述
arXiv:2607.14097v1 Announce Type: new Abstract: We introduce RegNetAgents, an AI-oriented multi-agent framework for structured, query-driven regulatory candidate identification across heterogeneous gene regulatory networks. The system enables unified analysis of bulk tumor and single-cell-derived ARACNe networks by integrating TCGA-derived cancer networks with large-scale single-cell regulatory networks from the GREmLN project. For a given focal gene, the framework performs dual-network classification, cancer gene filtering using OncoKB annotations, and mode-of-action (MoA) assignment for tumor-derived regulatory relationships. Candidates are ranked by evidence consistency across networks (Both, TCGA-only, GREmLN-only). The system is implemented as a multi-agent LangGraph DAG workflow, accessible through a unified Python API and Model Context Protocol (MCP) client, operating as a downstream analytical layer over precomputed regulatory networks rather than a network inference method. Across eleven breast cancer (BRCA) and twelve colorectal cancer (COAD) focal genes, RegNetAgents identifies candidate regulators significantly enriched for OncoKB-annotated cancer genes. TCGA-derived candidates show strong enrichment (Stouffer Z = 6.69 for BRCA and 6.95 for COAD), while GREmLN-derived candidates also demonstrate significant enrichment (Z = 5.51 for BRCA and 7.06 for COAD; all p < 0.0001). No enrichment is observed in housekeeping or non-driver control gene sets, supporting signal specificity. An extended module enables structured evaluation of oncogenic potential, druggability, clinical relevance, and network vulnerability, supporting end-to-end interpretation from candidate identification to biological hypothesis generation. RegNetAgents establishes an interpretable AI framework for cross-network regulatory candidate identification in cancer genomics.

## 综合总结
RegNetAgents是一个基于多智能体（LangGraph DAG）的AI框架，用于在异构基因调控网络（TCGA和GREmLN）中识别癌症调控候选基因。该框架通过双网络分类、OncoKB癌症基因过滤及MoA分配，实现了跨网络的候选因子排序，并在乳腺癌和结直肠癌中验证了其富集特异性。系统提供Python API和MCP客户端，支持从候选识别到成药性、临床相关性评估的端到端解释，为癌症基因组学研究提供了高可落地性的AI分析工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
将多智能体系统（LangGraph DAG）应用于癌症基因组学的跨网络调控因子识别，具有较好的新颖性。系统整合Bulk与单细胞调控网络，结合OncoKB过滤与MoA分配，逻辑严密、论证详实（含对照组实验及Z-score显著性验证）。但其定位为预计算网络的下游分析层，而非底层网络推断算法的突破，技术深度在交叉应用层面表现优异，原创理论深度略受限。

### 实用性 (评分: 8.5/10)
对生信与癌症研究从业者具有极高的参考价值。系统提供统一的Python API与MCP客户端，工程落地性极强；直接对接OncoKB等权威数据库，输出包含致癌潜力、成药性、临床相关性等维度的结构化结果，能直接指导从候选基因识别到生物学假设生成的端到端实践，适用范围明确（乳腺癌、结直肠癌等）。

### 社区活跃度 (评分: 7.5/10)
话题时效性极强，巧妙结合了当前AI前沿的Agent架构（LangGraph/MCP）与生物医学热点。但来源为arXiv预印本，且作者为单一作者，缺乏机构背书与同行评审，权威性与可信度尚需后续验证。发布时间标识为2026年，属于极早期或时间戳异常，影响力有待观察。

## 项目链接
https://arxiv.org/abs/2607.14097
