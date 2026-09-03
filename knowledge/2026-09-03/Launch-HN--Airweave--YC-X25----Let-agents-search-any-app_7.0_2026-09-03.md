# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.0  
**状态：** 正常  
**标签：** AI Agents, RAG, MCP, 数据集成, 检索增强, 开源, Launch HN, Y Combinator, 工具链  
**更新日期：** 2026-09-03  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave是一个面向AI Agent的开放源代码应用集成与检索层，试图解决Agent在多个SaaS/数据库中获取上下文的核心痛点。它将MCP仅做API暴露的局限提升为真正的语义+关键词混合检索能力，并提供完整SDK和托管服务。技术上属于扎实的工程整合而非范式创新，对实际构建Agent的团队具有较高参考价值，社区反响中规中矩。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目涉及多源数据接入、向量化索引（向量库+BM25+Postgres图元数据）、RRF融合排序、重排序与时间衰减、Temporal工作流编排等多项技术栈，技术广度较高。但整体属于成熟的RAG/检索增强架构组合，技术方案没有突破性创新，更偏向工程整合而非底层突破。

### 实用性 (评分: 7.5/10)
对于构建Agent应用的从业者有明确参考价值：解决MCP server仅做API包装而缺乏深度检索的痛点，提供统一的数据编排层。涵盖真实场景（电商、客服、法律、编码Agent），并给出REST/Python/TS SDK/MCP多种接入方式，开源降低了试用门槛。对正在设计Agent上下文检索层的团队有借鉴意义。

### 社区活跃度 (评分: 6.5/10)
Launch HN贴164分、30条评论属于中等偏上的关注度。Y Combinator背景加上明确的演示视频和使用案例引发了一定讨论。但相比热门AI话题（如新模型发布），讨论体量不算爆款；从评论数与点数的比例看，社区参与度尚可，未出现极端争议或深度技术辩论。

## 项目链接
https://github.com/airweave-ai/airweave
