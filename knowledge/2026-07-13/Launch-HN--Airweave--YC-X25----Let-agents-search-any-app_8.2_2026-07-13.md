# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, 开源, 发布, MCP, 数据检索  
**更新日期：** 2026-07-13  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 上下文检索层工具，旨在解决 Agent 难以从分散的 SaaS 和数据库中获取正确内部数据的问题。它通过爬取、规范化、分块和提取实体关系，结合 Postgres 向量存储与 Temporal 数据同步，提供语义与关键词混合搜索及重排功能，并以 API 和 MCP 服务器形式暴露给 Agent，对构建企业级 AI 应用具有高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
讨论了构建 AI Agent 上下文检索层的技术架构，包括数据爬取与规范化、实体关系提取、基于 Postgres 的向量+关键词+图元数据混合存储，以及使用 Temporal 进行数据同步编排。检索端采用语义与 BM25 并行搜索、RRF 融合、新近度偏差与重排机制，技术栈完整且深度较高。

### 实用性 (评分: 9.0/10)
对 AI 从业者极具参考价值，直击 Agent 开发中“缺乏内部上下文”的核心痛点。提供了从数据接入、同步到检索的端到端开源方案，并适配 MCP 协议，可直接应用于企业级 AI 助手、编程代理等场景的开发。

### 社区活跃度 (评分: 7.5/10)
获得 164 个点赞和 30 条评论，在 HN 社区达到中等偏上的关注度。作为 YC 项目的 Launch 帖，引发了关于 MCP 服务器局限性及 Agent 数据检索方案的实质性讨论。

## 项目链接
https://github.com/airweave-ai/airweave
