# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.3  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据检索, 开源, 发布  
**更新日期：** 2026-07-24  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 上下文检索与数据编排平台，旨在解决 Agent 难以从分散的 SaaS 和数据库中获取准确内部上下文的痛点。相比简单的 MCP 包装器，它提供了更深度的数据处理能力：通过爬取、分块、实体提取构建向量+图+关键字的混合索引，利用 Temporal 实现实时数据同步，并在检索端采用语义与 BM25 混合搜索、RRF 融合与重排序技术。项目支持 REST、SDK 及 MCP 接入，为构建复杂企业级 Agent 提供了强大的基础设施支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目在技术实现上具有较高的含金量，不仅停留在简单的 API 包装层，而是深入到了数据处理与检索的管道构建。技术栈涵盖了实体关系提取、图元数据存储、混合搜索（语义+BM25）、RRF结果融合、重排序机制，以及使用 Temporal 进行复杂的数据同步编排（处理分页、限流、增量变更检测），体现了扎实的 RAG 与数据工程基础。

### 实用性 (评分: 9.0/10)
对 AI Agent 开发者具有极高的实际参考价值。项目直击当前 Agent 开发的核心痛点——跨应用内部上下文获取困难。通过提供统一的 LLM 友好 API 和 MCP 服务器，开箱即用地解决了数据孤岛、脏数据处理和实时检索问题，极大降低了构建企业级 Agent 的基础设施门槛。

### 社区活跃度 (评分: 7.5/10)
作为 YC 孵化项目的 Launch HN，获得了 164 个点赞和 30 条评论，显示出社区中等偏上的关注度。讨论聚焦于 Agent 上下文检索这一热点需求，MCP 协议的集成也契合了当前技术趋势，吸引了不少开发者的实际体验与反馈。

## 项目链接
https://github.com/airweave-ai/airweave
