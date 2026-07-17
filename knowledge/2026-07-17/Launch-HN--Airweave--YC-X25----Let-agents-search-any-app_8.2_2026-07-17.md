# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据集成, 开源, 发布  
**更新日期：** 2026-07-17  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个获 YC 支持的开源工具，旨在解决 AI Agent 难以跨应用检索内部上下文的问题。它超越了简单的 MCP API 包装，通过抓取、规范化、分块和实体关系提取，将 SaaS 和数据库内容索引至 Postgres（结合向量、关键字和图元数据），并使用 Temporal 实现实时数据同步。检索端支持语义与 BM25 混合搜索、RRF 融合及重排序，为 Agent 提供精准的上下文和引用。该项目对构建企业级 Agent 的开发者具有极高的工程参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目技术栈成熟且具有深度，涵盖了数据处理与检索的核心环节：通过 Temporal 编排实现含分页/限流/变更检测的实时数据同步；在存储端将向量检索、BM25 关键词与轻量级图元数据结合于 Postgres；在检索端采用语义与关键词并行搜索、RRF 融合、新近度偏置及重排序机制。相比仅作 API 映射的薄包装 MCP 服务器，该方案在数据深度解析与混合检索上具有显著技术优势。

### 实用性 (评分: 9.0/10)
对 AI Agent 开发者极具实用价值。项目直击当前 Agent 开发中的核心痛点——跨应用内部数据的获取与理解。提供了从 REST、SDK 到 MCP 的多种接入方式，开箱即用；其开源特性与架构设计（如 Temporal 编排、混合 RAG）为企业级 Agent 构建提供了高参考性的工程范式，特别适用于法律、客服、研发等需要深度上下文增强的场景。

### 社区活跃度 (评分: 7.5/10)
作为 YC X25 的 Launch HN 项目，获得了 164 个 Points 和 30 条评论，显示出社区对 Agent 检索增强与 MCP 深度化发展方向的较高关注度。讨论量适中，表明开发者对该类基础设施的实际需求与实现细节有探讨兴趣，属于中等偏上的优质技术讨论热度。

## 项目链接
https://github.com/airweave-ai/airweave
