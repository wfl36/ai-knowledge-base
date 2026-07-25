# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据检索, 发布, 开源  
**更新日期：** 2026-07-25  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索中间件，旨在解决 Agent 难以跨应用获取和搜索内部上下文的问题。它通过整合数据爬取、规范化、实体提取与混合检索（语义+BM25+RRF），提供了比传统 MCP Server 更深度的搜索能力，为构建具备上下文感知的 Agent 提供了高价值的基础设施支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目技术栈扎实，涵盖了从数据源接入、内容规范化、分块、实体关系提取到混合检索（语义+BM25+RRF重排）的完整RAG链路。使用Temporal处理数据同步与编排，结合Postgres存储向量、关键词及轻量级图元数据，展现了较高的工程复杂度与技术深度。

### 实用性 (评分: 9.0/10)
直击当前AI Agent开发的核心痛点——缺乏获取跨应用内部上下文的有效途径。通过提供统一的API/MCP接口，解决了传统MCP Server仅做API包装而缺乏深度搜索能力的问题，对构建企业级Agent、RAG应用的开发者具有极高的实用参考与接入价值。

### 社区活跃度 (评分: 7.5/10)
获得164个点赞和30条评论，在Launch HN中表现出较好的社区关注度。讨论焦点集中在Agent数据检索层、MCP协议的实际效用以及RAG架构的优化，反映了社区对Agent基础设施建设与痛点解决的浓厚兴趣。

## 项目链接
https://github.com/airweave-ai/airweave
