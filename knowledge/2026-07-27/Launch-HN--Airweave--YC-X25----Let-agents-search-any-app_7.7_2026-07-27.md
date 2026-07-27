# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 开源, 发布  
**更新日期：** 2026-07-27  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个YC X25孵化的开源项目，旨在解决AI Agent缺乏内部上下文的问题。它通过单一API或MCP服务器，让Agent能够搜索和检索跨应用及数据库的上下文。技术上，项目整合了数据爬取、实体关系提取、向量与BM25混合检索（RRF+重排），并利用Temporal实现可靠的数据同步。该方案对构建企业级Agent和RAG应用的开发者具有高实用价值，社区反响积极。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目展示了扎实的工程架构，结合了向量检索、BM25关键字搜索、RRF融合及重排技术，并利用Postgres存储图元数据，Temporal处理数据同步与变更检测，解决了Agent上下文获取中的数据稀疏、动态变化和复杂检索问题，技术深度和含金量较高。

### 实用性 (评分: 8.5/10)
直击AI Agent开发中“找不到正确内部上下文”的核心痛点，提供从数据接入、同步编排到混合检索的端到端解决方案。对于需要整合多SaaS和数据源构建Agent的从业者而言，具有极高的直接落地和参考价值。

### 社区活跃度 (评分: 7.0/10)
获得了164个点赞和30条评论，在HN上表现良好，说明社区对Agent上下文检索和MCP相关话题保持较高关注度。作为YC项目，其开源方案吸引了开发者的兴趣，但评论数相对点赞数偏少，讨论的激烈程度中等。

## 项目链接
https://github.com/airweave-ai/airweave
