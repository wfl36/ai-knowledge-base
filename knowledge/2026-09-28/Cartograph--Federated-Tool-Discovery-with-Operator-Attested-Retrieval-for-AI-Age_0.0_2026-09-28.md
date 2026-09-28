# Cartograph: Federated Tool Discovery with Operator-Attested Retrieval for AI Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-28  
**来源：** rss  

## 项目描述
arXiv:2609.30293v1 Announce Type: new Abstract: The Model Context Protocol (MCP) enables AI agents to discover and call tools, but loading every definition becomes expensive as connected catalogs grow. We present Cartograph, a federated MCP proxy that changes agent-visible tool discovery from $O(n)$ catalog traversal to $O(k)$ progressive disclosure. Cartograph combines three mechanisms: (1) operator-attested capability cards, Ed25519-signed descriptions generated under the deploying operator's control rather than ranked publisher copy; (2) Rift, a three-layer confusable-cluster analysis comprising density clustering, query-margin analysis, and token diagnosis; and (3) two-stage retrieval, which ranks servers before tools. On a 22-server, 374-tool deployment, Cartograph exposes three proxy tools instead of 374 definitions. A 49-query author-constructed benchmark yields R@5 of 0.816, compared with 0.592 for a Jaccard keyword baseline, while a measured top-5 discovery exchange uses 475 tokens rather than 42,450 under the stated full-catalog accounting. Rift identifies 49 confusable clusters, including four HIGH-risk clusters in bootstrap-generated cards. An exploratory comparison of 119 LLM-generated descriptions removes the observed zero-distance cluster but shows that mixing card-generation regimes can reduce R@5. Gateway measurements over ten trials add 5ms mean latency (0.8%) relative to direct stdio MCP calls. Cartograph is complementary to code-execution approaches: it controls which tool descriptions are surfaced and records the provenance of the descriptions used for ranking for each query.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.30293
