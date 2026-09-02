# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.3  
**状态：** 正常  
**标签：** AI Agents, RAG, MCP, Data Integration, Vector Search, Open Source, Launch HN, YC X25, Infrastructure  
**更新日期：** 2026-09-02  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个面向AI agent的统一数据检索编排层开源工具，通过连接各类SaaS与数据库、归一化分块并混合索引，为agent提供语义+关键词的融合检索能力，支持MCP/REST/SDK多接口。其核心论点——纯MCP集成不足以实现细粒度检索——对agent开发者有启发意义。技术上以成熟组件组合为主，工程完整性较好，但缺乏底层创新。作为YC新晋Launch HN项目，社区关注度尚可，适合关注agent基础设施的从业者参考评估。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目涉及多源数据连接、归一化、分块、实体关系提取、向量检索与BM25混合搜索（RRF融合）、重排序、Temporal编排增量同步等技术栈，技术栈组合成熟且覆盖面广。但各组件均为业界已有方案的拼接（向量库+Postgregres+BM25+RRF），缺乏底层算法或架构层面的原创性突破。

### 实用性 (评分: 7.0/10)
对正在构建agentic应用的开发者具有较高参考价值：明确指出MCP'thin wrapper'的局限性，并提供了统一的检索增强层抽象（REST/Python/TS SDK/MCP多端暴露）。开源自部署降低了试用门槛，但作为infra层产品，其对从业者的核心价值在于思路启发而非直接复用——多数大厂/团队可能自建类似管道。

### 社区活跃度 (评分: 7.5/10)
164 points与30条评论在Launch HN中属于中等偏上热度，YC X25背书带来一定关注度。讨论可能集中在与现有方案（Airbyte、Fivetran、专用MCP server等）的差异化、开源vs托管模式合理性、以及agent检索层是否值得作为独立产品等话题上。

## 项目链接
https://github.com/airweave-ai/airweave
