# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.3  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 开源, 发布  
**更新日期：** 2026-07-18  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个获 YC 支持的开源项目，旨在解决 AI Agent 难以跨应用检索和理解内部数据的痛点。它超越了简单的 MCP API 包装，通过爬取、规范化、实体提取，构建结合向量、关键词和图元数据的混合索引，并利用 Temporal 实现实时数据同步。检索端支持语义与 BM25 并行搜索、RRF 融合及重排，为 Agent 提供高质量的上下文与引用，对 AI 应用开发者具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目技术栈成熟且深入，涵盖了数据同步编排、多模态检索（向量+BM25+图元数据）、RRF融合与重排等高级 RAG 技术。通过 Temporal 解决了分页、限流和变更检测等复杂的数据编排问题，并指出了当前 MCP 服务器多为薄包装的痛点，提供了深度的实体关系提取与索引方案，技术含金量较高。

### 实用性 (评分: 9.0/10)
精准切中当前 AI Agent 开发中“跨应用获取与理解内部数据”的核心痛点。提供了从数据同步、处理到检索增强的完整开源解决方案，且同时提供 REST API、SDK 及 MCP 接口，对构建企业级 AI 助手、RAG 应用和 Agent 的开发者具有极高的直接使用与架构参考价值。

### 社区活跃度 (评分: 7.5/10)
获得 164 个点赞和 30 条评论，对于 YC 初创项目的 Launch HN 而言属于中上水平，表明项目在 HN 社区获得了良好的关注度，并引发了关于 MCP 局限性、数据同步及 RAG 架构的实质性讨论。

## 项目链接
https://github.com/airweave-ai/airweave
