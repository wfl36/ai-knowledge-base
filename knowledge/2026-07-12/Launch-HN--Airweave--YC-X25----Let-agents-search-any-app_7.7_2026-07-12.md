# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, RAG, 数据集成, MCP, 发布, 开源  
**更新日期：** 2026-07-12  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个开源的AI Agent上下文检索与数据编排层，旨在解决Agent跨SaaS和数据库搜索内部数据困难的问题。项目批判了现有MCP服务器仅做浅层包装的局限，通过整合API爬取、数据规范化、实体关系提取、混合搜索（向量+BM25+RRF）及Temporal工作流编排，为Agent提供深度的数据理解与实时检索能力，对构建复杂企业级Agent具有高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在传统RAG基础上进行了深度工程化，结合了向量搜索、BM25关键词检索与RRF结果融合，并利用Postgres存储轻量级图元数据与实体关系以增强上下文关联。采用Temporal进行复杂的数据同步、分页限流与变更检测编排，技术栈成熟且在数据处理与检索链路上具备较高含金量。

### 实用性 (评分: 8.5/10)
直击当前AI Agent开发中'上下文检索难'的核心痛点，明确指出现有MCP服务器仅做浅层API包装的局限性。提供了一站式的数据规范化、索引与检索方案，支持REST/SDK/MCP多接口，对构建企业级Agent（如法律、客服、研发助手）的从业者具有极高的直接使用与架构参考价值。

### 社区活跃度 (评分: 7.0/10)
作为YC孵化项目的Launch HN，获得了164个点赞和30条评论，在HN社区属于中高热度。讨论聚焦于MCP的局限性、Agent数据检索的工程实践以及RAG架构的细节，表明该议题精准切中了开发者当前的现实痛点。

## 项目链接
https://github.com/airweave-ai/airweave
