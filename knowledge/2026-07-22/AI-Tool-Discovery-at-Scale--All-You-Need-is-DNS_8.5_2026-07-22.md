# AI Tool Discovery at Scale: All You Need is DNS

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 工具发现, DNS, 网络协议, MCP, A2A, 论文, 架构设计  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18242v1 Announce Type: new Abstract: The coming era of autonomous AI agents demands a discovery mechanism capable of navigating millions of tools, yet existing solutions buckle under O(N) complexity and centralized governance. Instead of building another fragile overlay, we propose ToolDNS, a radical framework that retrofits semantic tool discovery onto the Internet's most resilient substrate: the Domain Name System (DNS). By embedding functional intent and organizational trust into a hierarchical namespace, ToolDNS transforms an expensive semantic search into a series of lightweight, O(log N) name resolutions. We introduce three protocol-compliant enhancements to enable decentralized governance and semantic pruning: partially unfolded names, EDNS0 intent payloads, and logical subdomains. To rigorously evaluate this approach across the fragmented tooling landscape, we construct and release a large-scale heterogeneous benchmark comprising 33,688 real-world tools spanning MCP, A2A, RESTful, and Skill protocols. On this dataset, ToolDNS slashes the per-query search space by 95.26% while matching state-of-the-art retrieval accuracy. Furthermore, its UDP-native design reduces discovery latency by orders of magnitude compared to HTTP-based registries. Our work demonstrates that scalable AI interoperability requires not more middleware, but a smarter utilization of the infrastructure already beneath our feet.

## 综合总结
该论文提出 ToolDNS，一种基于 DNS 的去中心化 AI 工具发现框架，旨在解决自主 Agent 时代海量工具发现的 O(N) 复杂度和中心化瓶颈。通过在 DNS 层级命名空间中嵌入功能意图与组织信任，并引入部分展开名称、EDNS0 意图负载和逻辑子域等协议增强，将昂贵的语义搜索转化为 O(log N) 的轻量级名称解析。在包含 33,688 个多协议工具的大规模基准测试中，ToolDNS 在保持 SOTA 检索精度的同时，将单次查询搜索空间缩减 95.26%，且 UDP 原生设计大幅降低了发现延迟。该工作为 AI 互操作性提供了一种无需额外中间件的底层基础设施重构方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
观点极具新颖性与颠覆性，跳出传统的中心化注册表或中间件范式，创造性地将互联网最底层的 DNS 基础设施重构用于 AI 工具发现。技术深度出色，不仅提出了 O(log N) 复杂度的理论优化，还设计了三个符合 DNS 协议规范的增强机制（部分展开名称、EDNS0 意图负载、逻辑子域）以实现语义剪枝与去中心化治理。论证严谨，构建了涵盖 33,688 个多协议工具的大规模基准测试，实验数据（95.26% 搜索空间缩减、SOTA 级精度、UDP 低延迟）充分支撑了其理论主张。

### 实用性 (评分: 7.5/10)
对 AI Agent 框架开发者和架构师具有极高的架构启发和参考价值，指明了避开中心化单点故障和 HTTP 高延迟的工程新路径。然而，由于涉及对 DNS 协议的扩展改造，在全局互联网范围内落地需跨越极高的标准化门槛与多方利益协调（如 ISP、ICANN），短期内在公网大规模部署难度极大。但在企业内网、私有 Agent 集群或特定生态（如 MCP/A2A）内，该方案具有极高的可落地性与实践指导意义。

### 社区活跃度 (评分: 8.8/10)
话题时效性极强，直击当前 AI Agent 爆发期面临的‘海量工具发现与互操作性’核心痛点，与近期火热的 MCP、A2A 等协议生态高度契合。作为 arXiv 上的最新研究，其‘All You Need is DNS’的口号极具传播性，若能引起网络与 AI 双边社区的关注，有望引发关于 Agent 底层基础设施走向的广泛讨论，具有潜在的高影响力。

## 项目链接
https://arxiv.org/abs/2607.18242
