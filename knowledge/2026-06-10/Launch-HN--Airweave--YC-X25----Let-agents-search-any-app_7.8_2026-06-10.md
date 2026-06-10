# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, RAG, 数据检索, 开源项目, 发布  
**更新日期：** 2026-06-10  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索与编排层，通过单一 API 或 MCP 服务器连接各类 SaaS 和数据库。它整合了数据爬取、分块、实体提取、混合检索（向量+BM25+RRF）及重排序等功能，解决了传统 MCP 封装过薄无法深度搜索与理解资源的问题，为 Agent 提供了精准的内部上下文获取能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目技术栈现代且完整，涉及数据编排、向量搜索与BM25混合检索、RRF结果融合、实体关系提取，并使用Temporal处理数据同步与变更检测，具备较高的工程含金量与技术深度。

### 实用性 (评分: 8.5/10)
直击AI Agent开发中内部上下文获取难的痛点，提供从数据同步、处理到混合检索的端到端解决方案，对构建企业级Agent和RAG应用的开发者具有极高的实用参考价值。

### 社区活跃度 (评分: 7.0/10)
获得164个点赞和30条评论，作为YC创业项目发布，引发了中等偏上的社区关注与讨论，反映了开发者对Agent数据检索层与MCP实际落地的兴趣。

## 项目链接
https://github.com/airweave-ai/airweave
