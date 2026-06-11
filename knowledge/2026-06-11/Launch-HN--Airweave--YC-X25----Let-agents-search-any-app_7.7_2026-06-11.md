# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, RAG, 数据检索, MCP, 发布, 开源  
**更新日期：** 2026-06-11  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索与编排平台，旨在解决 Agent 跨应用获取上下文的难题。相比仅做 API 映射的薄层 MCP 服务器，它通过深度爬取、规范化、实体提取和多路召回（向量+BM25+RRF）提供更精细的搜索能力，并利用 Temporal 实现实时数据同步。该项目对构建复杂企业级 Agent 的从业者具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目聚焦于 AI Agent 的数据检索与编排层，技术栈成熟且全面。采用 Temporal 处理数据同步与状态管理，结合语义向量搜索与 BM25 关键词搜索并进行 RRF 融合，同时引入实体关系提取和图元数据增强上下文。对 MCP 协议的局限性（仅作为 API 薄封装）有深刻认知，并提出了更深度的索引与检索方案。

### 实用性 (评分: 8.5/10)
直击 AI Agent 开发中“找不到正确内部上下文”的核心痛点。为从业者提供了一套开箱即用的跨应用数据集成与检索方案，涵盖数据抓取、分块、同步、多路召回与重排，支持 REST/SDK/MCP 多种接入方式，极大降低了构建企业级 RAG 和 Agent 应用的工程门槛。

### 社区活跃度 (评分: 7.0/10)
获得 164 个点赞和 30 条评论，在 HN 社区表现出中等偏上的关注度。作为 YC 项目的发布，引发了开发者对 MCP 服务器本质、RAG 架构选型及数据同步机制的实质性探讨，反映了社区对 Agent 基础设施建设的浓厚兴趣。

## 项目链接
https://github.com/airweave-ai/airweave
