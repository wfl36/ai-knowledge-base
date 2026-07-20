# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 8.2  
**状态：** 正常  
**标签：** AI Agent, RAG, MCP, 数据检索, 开源, 发布  
**更新日期：** 2026-07-20  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个获YC支持的开源项目，旨在解决AI Agent难以获取和搜索跨应用/数据库内部上下文的痛点。不同于仅做API转换的薄MCP封装，Airweave构建了完整的数据编排与检索层：通过Temporal实现近实时数据同步，结合向量、BM25与图元数据进行混合索引，并采用RRF融合与重排机制提供精准检索。项目支持REST、SDK及MCP接口，对Agent开发者具有极高的工程实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目深入探讨了AI Agent的数据编排与检索层问题，超越了简单的API/MCP封装。技术实现上涵盖了数据抓取、规范化、实体关系提取、混合索引（向量+BM25+图元数据）、基于Temporal的数据同步及RRF结果融合与重排，技术栈完整且具有深度。

### 实用性 (评分: 9.0/10)
直击AI Agent开发中“缺乏正确内部上下文”的核心痛点。提供的开源方案整合了数据同步、混合检索与MCP接口，对构建企业级Agent、RAG应用及编码助手的开发者具有极高的直接参考和实用价值，开箱即用。

### 社区活跃度 (评分: 7.5/10)
作为YC项目的Launch HN，获得了164个点赞和30条评论，显示出社区对Agent数据检索层及MCP相关话题的较高关注度，讨论活跃度中等偏上，但未达到现象级爆款热度。

## 项目链接
https://github.com/airweave-ai/airweave
