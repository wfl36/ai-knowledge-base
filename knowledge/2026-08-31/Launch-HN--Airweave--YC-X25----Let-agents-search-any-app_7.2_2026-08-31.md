# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.2  
**状态：** 正常  
**标签：** AI Agents, RAG, MCP, 开源工具, Launch HN, YC, 数据编排, 混合搜索  
**更新日期：** 2026-08-31  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个面向AI agent的统一数据检索编排层，通过连接各类SaaS和数据库、归一化内容、向量化索引，为agent提供自然语言查询接口。技术上是混合检索+RAG的成熟工程化封装，核心卖点是填补MCP薄包装在深度搜索上的能力空白。作为YC X25项目具有一定参考价值，适合正在搭建agent上下文层的团队关注。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.2/10)
讨论围绕AI agent检索层展开，涉及向量检索+BM25混合搜索（RRF融合）、重排序、实体关系抽取、Temporal编排同步、PostgreSQL图元数据等组合方案，技术栈成熟完整。但本质上是已有组件的工程化整合而非原创算法突破，深度尚可但缺乏新颖性。

### 实用性 (评分: 7.5/10)
对正在构建agent应用的从业者具有较高参考价值：直接回应了MCP服务器薄包装的痛点，提供了开箱即用的多源数据编排方案。对构建企业级RAG、法律/客服/研究类agent的团队有实用价值，开源+托管服务降低了试用门槛。

### 社区活跃度 (评分: 7.0/10)
164分/30评论表明HN社区对此类agent基础设施工具有一定关注度，但讨论深度有限。Launch HN+YC背书带来初始流量，作为二发热度属中等偏上。评论数偏少说明话题争议性不强，更多是产品展示而非激烈讨论。

## 项目链接
https://github.com/airweave-ai/airweave
