# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, Data Orchestration, 发布, 开源  
**更新日期：** 2026-06-08  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 上下文检索与数据编排平台，旨在解决 Agent 访问分散企业数据时的搜索与理解难题。它通过爬取、规范化、分块及提取实体关系，将多源数据统一索引至 Postgres 向量库，并利用 Temporal 实现实时数据同步。在检索端，结合语义搜索、BM25 及 RRF 融合与重排，为 Agent 提供精准的上下文引用。该项目对构建企业级 Agent 和 RAG 系统的从业者具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在应用架构层具有较高技术深度，结合了向量搜索、BM25、RRF 融合排序、实体关系提取与轻量级图元数据。采用 Temporal 进行数据同步与状态编排，有效解决了 RAG 系统中的数据新鲜度与多源异构问题，并原生支持 MCP 协议与多种 SDK。

### 实用性 (评分: 8.5/10)
对 AI 从业者（特别是 Agent 和 RAG 开发者）极具参考与实用价值。直击 Agent 获取企业内部上下文的核心痛点，提供从数据接入、同步编排到混合检索与重排的端到端开源方案，可作为 Agent 基础设施直接集成使用。

### 社区活跃度 (评分: 6.5/10)
获得 164 个点赞和 30 条评论，在 YC 创业项目发布中表现中等偏上，引发了社区关于 MCP 局限性及 Agent 数据检索架构的实质性讨论，关注度与讨论质量良好。

## 项目链接
https://github.com/airweave-ai/airweave
