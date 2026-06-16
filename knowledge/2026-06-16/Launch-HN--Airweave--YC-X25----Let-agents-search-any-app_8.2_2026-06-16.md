# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据检索, 发布, 开源  
**更新日期：** 2026-06-16  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索与编排层，旨在解决 Agent 访问分散在企业 SaaS 和数据库中上下文数据的难题。相比简单的 MCP 包装器，它通过深度抓取、分块、实体提取和混合检索（向量+BM25+图数据），为 Agent 提供了强大的自然语言搜索能力，对构建复杂 Agent 应用的开发者具有重要参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目技术栈扎实，涵盖了从数据抓取、规范化、分块到实体关系提取的完整数据处理链路。采用 Temporal 处理数据同步与编排，检索层结合了向量搜索、BM25 关键词搜索、RRF 融合排序及重排机制，并在 Postgres 中融合了向量、关键词和轻量级图元数据，展现了较深的 RAG 与 Agent 基础设施构建能力。

### 实用性 (评分: 9.0/10)
直击当前 AI Agent 开发中“缺乏内部上下文”的核心痛点，指出简单的 MCP 包装器无法提供深度搜索能力。该工具为开发者提供了一站式的数据编排与检索层，支持 REST、SDK 及 MCP 接入，对构建企业级智能客服、法律 AI 助手、代码辅助等应用的从业者具有极高的实用价值。

### 社区活跃度 (评分: 7.5/10)
作为 YC 孵化项目的发布，获得了 164 个点赞和 30 条评论，显示出社区对 Agent 检索层和 MCP 相关话题的较高关注度。讨论聚焦于 MCP 的局限性、RAG 实现细节及具体应用场景，互动质量较好。

## 项目链接
https://github.com/airweave-ai/airweave
