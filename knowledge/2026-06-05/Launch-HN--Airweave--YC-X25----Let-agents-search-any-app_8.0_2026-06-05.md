# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agents, RAG, MCP, Data Orchestration, Launch, Open-source  
**更新日期：** 2026-06-05  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个开源的AI Agent上下文检索与数据编排工具，旨在解决Agent在跨应用获取内部数据时的痛点。与仅做API封装的MCP服务器不同，它通过爬取、标准化、分块、提取实体关系并索引到向量库与Postgres中，结合Temporal实现近实时数据同步；在检索端采用语义与BM25混合搜索、RRF融合及重排序，为Agent提供精准的上下文支撑。该项目对Agent开发者具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目在技术实现上具有较高的含金量，不仅停留在简单的 API 封装，而是深入到了数据编排、实体关系提取、向量+关键词+图元数据的混合存储，以及语义与BM25并行检索、RRF融合与重排序等高级RAG技术栈，并使用Temporal处理复杂的数据同步与状态管理，技术栈成熟且复杂。

### 实用性 (评分: 9.0/10)
对AI从业者极具参考和应用价值。项目直击当前AI Agent开发中的核心痛点——跨应用内部上下文的精准获取。提供开箱即用的MCP服务器和SDK，极大降低了为Agent接入外部SaaS和数据库上下文的开发门槛，是构建实用Agent基础设施的关键一环。

### 社区活跃度 (评分: 7.0/10)
获得164个点赞和30条评论，在HN社区引起了不错的关注度与讨论。作为YC项目的Launch，该数据表现良好，说明社区对Agent上下文检索这一痛点有共鸣，但讨论热度未达到现象级爆发，属于中等偏上的社区反馈水平。

## 项目链接
https://github.com/airweave-ai/airweave
