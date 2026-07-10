# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据集成, 发布, 开源  
**更新日期：** 2026-07-10  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个YC孵化的开源工具，旨在解决AI Agent跨应用检索内部上下文的难题。它通过深度整合RAG技术（混合搜索、重排序、实体提取）和Temporal数据同步编排，弥补了传统MCP服务器仅做API薄封装的不足，为Agent开发者提供高价值的统一检索API与MCP服务。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目整合了成熟的RAG架构（语义与BM25混合搜索、RRF结果融合、重排序），并引入实体关系提取与图元数据增强上下文；在数据同步层采用Temporal处理分页、限流和变更检测，工程实践扎实。针对当前MCP服务器多为API薄封装的痛点，提出了深度索引与检索的解决方案，具备较好的技术深度。

### 实用性 (评分: 8.5/10)
直击AI Agent开发中跨SaaS与数据库获取内部上下文的痛点，对Agent开发者构建企业级应用具有极高的参考与直接使用价值。提供开源方案、MCP服务器支持及多语言SDK，即插即用，能显著降低开发者实现数据编排与检索层的门槛。

### 社区活跃度 (评分: 7.0/10)
获得164个点赞和30条评论，作为YC孵化项目的Launch HN表现中规中矩，达到了不错的曝光度。评论数适中，反映了HN社区对Agent基础设施及MCP实际应用场景的关注与探讨，但尚未引发大规模的爆款讨论。

## 项目链接
https://github.com/airweave-ai/airweave
