# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.3  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据检索, 开源, 发布  
**更新日期：** 2026-06-14  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个面向 AI Agent 的开源上下文检索与数据编排平台，旨在解决 Agent 在多源 SaaS 和数据库中难以获取精准内部上下文的痛点。项目超越了简单的 MCP API 包装，通过接入源数据、爬取规范化、实体关系提取，并在 Postgres 中结合向量、BM25 关键词与图元数据进行混合索引；利用 Temporal 实现近实时数据同步；检索端支持语义与关键词并行搜索、RRF 融合、近期偏差与重排。该工具为 RAG 和 Agent 开发者提供了端到端的高价值基础设施。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目技术栈扎实且具有深度，超越了简单的 API 封装。核心涉及数据爬取与规范化、实体关系提取、Postgres 混合索引（向量+BM25+图元数据）、Temporal 工作流编排处理数据同步与变更检测，以及检索端的 RRF 融合、近期偏差与重排机制，展现了完整的 RAG 增强与数据工程实践。

### 实用性 (评分: 9.0/10)
对 AI 从业者（尤其是 Agent 和 RAG 应用开发者）具有极高的实用价值。直击当前 Agent 开发中“找不到正确内部上下文”的核心痛点，提供从数据接入、实时同步到复杂检索的端到端解决方案，且兼容 MCP 协议与主流 SDK，可直接作为基础设施集成到业务系统中。

### 社区活跃度 (评分: 7.5/10)
获得 164 个点赞和 30 条评论，在 YC Launch HN 项目中表现出中高水平的社区关注度。评论数表明社区不仅关注产品发布，更对其实际架构、MCP 实现细节及开源策略展开了实质性讨论，互动质量较高。

## 项目链接
https://github.com/airweave-ai/airweave
