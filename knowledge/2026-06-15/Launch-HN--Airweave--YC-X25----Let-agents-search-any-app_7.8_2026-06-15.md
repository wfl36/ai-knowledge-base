# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 开源, 发布  
**更新日期：** 2026-06-15  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个开源的Agent数据检索中间件（YC X25项目），旨在通过单一API或MCP服务器让Agent搜索并检索各类应用和数据库的上下文。项目解决了Agent开发中上下文获取的痛点，通过Temporal编排数据同步，结合语义搜索、BM25及图元数据进行混合检索与重排，超越了传统MCP的浅层API封装，为AI从业者提供了高价值的Agent数据集成与RAG解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目聚焦于AI Agent的上下文检索层，技术栈成熟且完整。采用Temporal进行数据同步与编排，结合向量检索、BM25关键词搜索与图元数据（Postgres），通过RRF融合与重排提升召回质量。超越了简单的MCP API封装，实现了深度的数据解析与实体关系提取，技术工程含金量较高。

### 实用性 (评分: 9.0/10)
对AI从业者具有极高的实用价值。解决了Agent开发中“找不到正确内部上下文”的核心痛点，提供开箱即用的多数据源同步、清洗、检索及MCP接入方案，大幅降低了构建企业级Agent的数据集成与RAG开发门槛。

### 社区活跃度 (评分: 7.0/10)
获得了164个点赞和30条评论，作为YC项目的Launch HN表现中规中矩，显示出社区对Agent基础设施及MCP协议的持续关注，但讨论热度未达现象级。

## 项目链接
https://github.com/airweave-ai/airweave
