# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 开源, 发布  
**更新日期：** 2026-07-22  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个 YC 孵化的开源项目，旨在解决 AI Agent 缺乏跨应用深度搜索与上下文检索能力的痛点。它通过统一接口连接各类 SaaS 与数据库，利用 Temporal 编排数据同步，对内容进行分块与实体关系提取，并结合向量检索、BM25 与图元数据提供高质量的混合检索与重排能力。该项目弥补了当前 MCP 生态在深度搜索上的不足，为 Agent 开发者提供了高价值的上下文编排与检索基础设施。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目技术栈扎实，涵盖了数据爬取、规范化、分块、实体关系提取、向量索引与图元数据结合（Postgres），并使用 Temporal 处理复杂的数据同步与编排。检索端采用语义与 BM25 双路召回加 RRF 融合与重排，是当前 RAG 领域的成熟工程实践，技术含金量较高，但属于工程架构整合而非底层算法突破。

### 实用性 (评分: 8.5/10)
对 AI Agent 和 RAG 应用开发者具有极高的参考与使用价值。项目直击当前 MCP 服务器多为 API 薄包装、缺乏深度搜索能力的痛点，提供了开箱即用的跨应用数据编排与检索层，支持 REST、SDK 及 MCP 接入，能显著降低企业级 Agent 构建中上下文获取的门槛。

### 社区活跃度 (评分: 7.0/10)
作为 YC 孵化项目的 Launch HN，获得了 164 个点赞和 30 条评论，显示出社区对 Agent 基础设施和 MCP 生态演进的中高关注度，引发了关于数据同步可靠性、MCP 局限性及 Agent 检索架构的实质性讨论。

## 项目链接
https://github.com/airweave-ai/airweave
