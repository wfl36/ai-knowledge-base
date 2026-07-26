# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, Open-source, Launch  
**更新日期：** 2026-07-26  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索与编排层，旨在解决 Agent 难以从分散、杂乱的 SaaS 和数据库中获取准确上下文的痛点。它超越了简单的 MCP API 包装，通过爬取、分块、实体提取，并在 Postgres 中结合向量、关键词与图元数据进行索引；检索端采用语义与 BM25 混合搜索、RRF 融合及重排机制，为 Agent 提供精准的上下文召回。该项目为 Agent 开发者提供了极具价值的端到端解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目技术栈完整且具有深度，不仅停留在简单的 API 封装，而是深入到数据编排层面。采用 Temporal 处理数据同步与变更检测，结合语义搜索与 BM25 关键词搜索的 RRF 融合、重排序机制，并在 Postgres 中整合了向量存储、关键词与轻量级图元数据，实现了结构化与非结构化数据的深度检索与实体关系提取。

### 实用性 (评分: 9.0/10)
对 AI Agent 开发者具有极高的实用价值。直击当前 Agent 开发中'获取正确内部上下文'的核心痛点，提供了一套开箱即用的开源解决方案。支持 MCP 协议、REST API 及多语言 SDK，能直接集成到现有 Agent 架构（如 Cursor）中，大幅降低构建具备企业级数据检索能力 Agent 的门槛。

### 社区活跃度 (评分: 7.5/10)
作为 YC 孵化项目的 Launch HN，获得了 164 个点赞和 30 条评论，表现出中等偏上的社区关注度。讨论围绕 Agent 上下文获取难题、MCP 协议的局限性与潜力展开，表明该话题切中了当前 AI 开发者的实际需求与痛点，互动质量较高。

## 项目链接
https://github.com/airweave-ai/airweave
