# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, RAG, 数据集成, 开源, 发布  
**更新日期：** 2026-07-14  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是一个开源的 AI Agent 数据检索层工具，旨在解决 Agent 难以从分散、杂乱的 SaaS 和数据库中获取上下文的问题。项目指出当前多数 MCP 服务器缺乏深度搜索能力，进而构建了一套集数据爬取、规范化、实体提取、混合检索（语义+BM25+图谱）及 Temporal 同步编排的完整架构，为开发者提供了高实用性的 Agent 上下文增强基础设施。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目深入探讨了 AI Agent 在企业数据检索中的技术痛点，批判了现有 MCP 仅作为 API 薄包装层的局限。技术实现上，采用 Temporal 编排数据同步（处理分页、限流、变更检测），结合向量检索、BM25 关键词搜索与 Postgres 图谱元数据，并使用 RRF 融合、时间衰减和重排序，构建了完整的混合 RAG 架构，技术栈成熟且具有相当的工程深度。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具参考价值。直击 Agent 开发中“找不到正确内部上下文”的核心痛点，提供了一套包含数据同步、清洗、检索的端到端开源解决方案，大幅降低了构建跨 SaaS 应用数据 Agent 的门槛，其架构设计对开发企业级 RAG 应用有直接的借鉴意义。

### 社区活跃度 (评分: 7.0/10)
获得 164 个点赞和 30 条评论，对于 YC 初创团队的 Launch HN 帖子表现良好，显示出 HN 社区对 Agent 底层基础设施及 MCP 增强/替代方案的关注，但整体讨论热度属于中等水平。

## 项目链接
https://github.com/airweave-ai/airweave
