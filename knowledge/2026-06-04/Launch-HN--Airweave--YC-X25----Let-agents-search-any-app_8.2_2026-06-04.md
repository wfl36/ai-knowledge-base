# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, 数据检索, MCP, 发布, 开源  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 上下文检索中间件，旨在解决 Agent 难以从分散的 SaaS 和数据库中获取准确内部上下文的问题。它通过自动化的数据同步编排（Temporal）、混合检索（语义+BM25+RRF）和实体关系提取，为 Agent 提供了超越简单 API 包装的深度搜索能力，对构建企业级 Agent 极具实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
深入探讨了 AI Agent 的数据编排与检索层架构，涉及数据爬取规范化、实体关系提取、图元数据存储、混合检索（语义+BM25+RRF融合）、重排序及基于 Temporal 的实时数据同步机制，技术栈成熟且具备一定深度。

### 实用性 (评分: 9.0/10)
直击 Agent 开发中“找对上下文”的核心痛点，提供从多源数据接入、自动化同步到高级检索的一站式开源解决方案，并兼容 MCP 协议，对构建企业级 RAG 和 Agent 应用的从业者具有极高的实用与落地参考价值。

### 社区活跃度 (评分: 7.5/10)
作为 YC 孵化项目的 Launch HN，获得了 164 个点赞和 30 条评论，显示出社区对 Agent 上下文检索基础设施的较高关注，但讨论深度和争议性相对适中。

## 项目链接
https://github.com/airweave-ai/airweave
