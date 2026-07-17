# RegNetAgents: A Multi-Agent Framework for Cross-Network Regulatory Driver Identification in Cancer Genomics

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, AI4Science, 基因组学, 论文, 工程实践  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14097v1 Announce Type: new Abstract: We introduce RegNetAgents, an AI-oriented multi-agent framework for structured, query-driven regulatory candidate identification across heterogeneous gene regulatory networks. The system enables unified analysis of bulk tumor and single-cell-derived ARACNe networks by integrating TCGA-derived cancer networks with large-scale single-cell regulatory networks from the GREmLN project. For a given focal gene, the framework performs dual-network classification, cancer gene filtering using OncoKB annotations, and mode-of-action (MoA) assignment for tumor-derived regulatory relationships. Candidates are ranked by evidence consistency across networks (Both, TCGA-only, GREmLN-only). The system is implemented as a multi-agent LangGraph DAG workflow, accessible through a unified Python API and Model Context Protocol (MCP) client, operating as a downstream analytical layer over precomputed regulatory networks rather than a network inference method. Across eleven breast cancer (BRCA) and twelve colorectal cancer (COAD) focal genes, RegNetAgents identifies candidate regulators significantly enriched for OncoKB-annotated cancer genes. TCGA-derived candidates show strong enrichment (Stouffer Z = 6.69 for BRCA and 6.95 for COAD), while GREmLN-derived candidates also demonstrate significant enrichment (Z = 5.51 for BRCA and 7.06 for COAD; all p < 0.0001). No enrichment is observed in housekeeping or non-driver control gene sets, supporting signal specificity. An extended module enables structured evaluation of oncogenic potential, druggability, clinical relevance, and network vulnerability, supporting end-to-end interpretation from candidate identification to biological hypothesis generation. RegNetAgents establishes an interpretable AI framework for cross-network regulatory candidate identification in cancer genomics.

## 综合总结
RegNetAgents是一个基于多智能体（LangGraph DAG）的AI框架，用于癌症基因组学中跨异构基因调控网络的调控候选基因识别。该系统整合了TCGA和GREmLN单细胞网络，通过双网络分类、OncoKB癌症基因过滤和MoA分配，对候选基因进行跨网络证据一致性排名。实验在乳腺癌和结直肠癌数据上验证了其显著富集和信号特异性。框架提供Python API和MCP客户端，并包含致癌潜力与可成药性等扩展评估模块，为从候选识别到生物假设生成提供了高可解释性和可落地的端到端解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文将多智能体架构（LangGraph DAG）创新性地应用于癌症基因组学的跨网络调控基因识别，技术深度较好，整合了TCGA与单细胞网络，并通过OncoKB过滤与MoA分配增强了生物学解释性。实验设计严谨，引入了对照组验证信号特异性，统计显著性明确（p<0.0001）。

### 实用性 (评分: 8.5/10)
框架提供了统一的Python API和MCP客户端，工程化程度高，易于生物信息学从业者集成和使用。作为预计算网络的下游分析层，定位清晰，不仅输出候选基因，还提供致癌潜力、可成药性等扩展评估，对从候选识别到生物假设生成的端到端研究具有极高的实践指导价值。

### 社区活跃度 (评分: 7.5/10)
研究紧抓AI Agent（LangGraph、MCP）与单细胞/癌症基因组学交叉的前沿热点，时效性极强。基于TCGA、OncoKB等权威数据库构建，数据支撑扎实可信。虽为arXiv预印本且作者知名度有限，但在AI4Science交叉领域具有较好的潜在影响力。

## 项目链接
https://arxiv.org/abs/2607.14097
