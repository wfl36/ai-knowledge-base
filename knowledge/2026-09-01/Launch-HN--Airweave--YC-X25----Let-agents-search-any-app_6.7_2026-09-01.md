# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 6.7  
**状态：** 正常  
**标签：** AI Agent, MCP, RAG, 开源工具, Launch HN, YC X25, 数据检索, 企业搜索  
**更新日期：** 2026-09-01  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是YC X25孵化的开源项目,旨在为AI Agent提供统一的跨应用数据检索层,解决当前MCP server普遍缺乏深度搜索能力的问题。通过连接各类SaaS和数据库,实现内容归一化、分块、索引,并提供语义+BM25混合检索、RRF融合、重排序等能力,支持REST/MCP/SDK多种接入方式。技术方案成熟但缺乏突破性创新,核心价值在于产品定位准确击中Agent开发痛点,适合需要整合多源数据的Agent项目参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
技术方案涉及数据接入、归一化、分块、实体关系抽取、向量索引、BM25与语义搜索混合召回、RRF融合、重排序等典型RAG/检索增强技术栈,并使用Temporal做数据同步编排,选型合理但未涉及深度技术创新。整体是一个集成度较高的工程实现,技术深度中等。

### 实用性 (评分: 6.5/10)
对AI Agent开发者具有较高参考价值,直击当前MCP生态的核心痛点——多数MCP server只是API的薄包装,缺乏细粒度搜索与上下文理解能力。Airweave提供了统一的检索层,支持REST/MCP/SDK多种接入方式,降低Agent构建者的集成成本。但作为开源工具,实际生产可用性还需社区验证。

### 社区活跃度 (评分: 7.0/10)
Launch HN帖子获得164 points和30条评论,属于YC项目发布中的中等偏上热度。评论数相对偏少但points较高,说明浏览者认可度高但主动讨论意愿一般,可能因为技术方向(MCP/RAG检索增强)虽热门但讨论切入点有限。

## 项目链接
https://github.com/airweave-ai/airweave
