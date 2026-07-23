# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据检索, 开源, 发布  
**更新日期：** 2026-07-23  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索与编排层，旨在解决 Agent 难以跨 SaaS 应用和数据库获取准确内部上下文的痛点。它通过 API 连接数据源，利用 Temporal 进行实时数据同步，结合向量搜索、BM25 及图元数据进行混合索引，并通过 RRF 融合与重排序提供高质量检索结果。项目支持 REST、SDK 及 MCP 接口，对构建企业级 Agent 和 RAG 应用的开发者具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在数据编排与检索上展现了较高的工程深度，采用 Temporal 处理复杂的 API 同步与变更检测，结合向量搜索、BM25 关键字与图元数据的混合索引，并使用 RRF (Reciprocal Rank Fusion) 进行结果融合与重排序。技术栈成熟且切中 Agent 数据接入痛点，但本质上是现有技术的优秀组合与工程化落地，缺乏底层算法级别的突破。

### 实用性 (评分: 9.0/10)
直击当前 AI Agent 开发中的核心痛点——缺乏跨应用的高质量内部上下文获取能力。通过提供统一的 API/MCP 接口和开箱即用的数据同步与检索方案，极大降低了开发者构建企业级 RAG 和 Agent 应用的门槛，对从业者具有极高的直接使用与架构参考价值。

### 社区活跃度 (评分: 7.0/10)
获得 164 个点赞和 30 条评论，在 YC 创业项目的 Launch 帖中表现良好，说明该痛点引起了 HN 社区开发者的共鸣。围绕 MCP 的局限性、Agent 数据获取挑战以及 RAG 架构的讨论具备一定的活跃度与质量。

## 项目链接
https://github.com/airweave-ai/airweave
