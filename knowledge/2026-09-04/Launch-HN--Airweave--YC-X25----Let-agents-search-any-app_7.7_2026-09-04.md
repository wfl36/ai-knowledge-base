# Launch HN: Airweave (YC X25) – Let agents search any app

**评分：** 7.7  
**状态：** 正常  
**标签：** RAG, AI Agent, MCP, 开源工具, YC X25, Launch HN, 向量检索, 数据同步  
**更新日期：** 2026-09-04  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Lennert and Rauf. We’re building Airweave (<a href="https:&#x2F;&#x2F;airweave.ai&#x2F;">https:&#x2F;&#x2F;airweave.ai&#x2F;</a>), an open-source tool that lets AI agents search and retrieve context from your existing apps and databases through a single LLM-friendly API (or an MCP server, if that’s your thing). Our Github is at <a href="https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;airweave-ai&#x2F;airweave</a>. We previously did a Show HN <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43964201</a> and since then we’ve recently launched the managed service and new search functionality.<p>Here’s an example of Cursor using Airweave <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=IvxidK9Ciy4</a>. And here’s a general example of our new search functionality: <a href="https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8" rel="nofollow">https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=iqEqc_iGUO8</a><p>We came to this problem while building agentic applications for webshop owners and customer service, and noticing most failure modes weren’t about tool execution, but finding the right internal context to enable the right actions.<p>We started solving, what seemed at the time, a problem for our own use case, and quickly fell into a rabbithole of issues. Company and user data lives across SaaS and databases; it’s sparse, messy, and constantly changing. Agents need a data orchestration and retrieval layer that accepts free-form natural language queries and returns actionable results quickly.<p>Simply pointing an agent at an MCP server does not equate to fine-grained search functionality or deep understanding of the underlying resource. Most MCP servers are thin wrappers that expose an existing API in a more LLM-friendly way, but this doesn’t actually give the agent any new capabilities beyond what the resource or app already offered. Specifically, it doesn’t give the agent a way to thoroughly search and understand the contents of the resource.<p>Airweave connects to sources via their APIs, crawls and normalizes content, chunks it, extracts entity relationships, and indexes the chunks in a vector store alongside keyword fields and lightweight graph metadata in Postgres. Data sync is orchestrated with Temporal (handles pagination&#x2F;rate limits, schedules, and change detection via timestamps and content hashes) so collections stay close to real-time with their sources.<p>On retrieval, Airweave can run semantic and BM25 keyword search in parallel, fuse results (RRF), apply recency bias, and re-rank. Agents can fetch ranked chunks with citations or ask for a synthesized answer. The same interface is exposed via REST, Python&#x2F;TS SDKs, and MCP so agents can discover it like any other tool.<p>It’s been fun to see what users have built with Airweave; from legal AI assistants to research discovery agents and context augmentation for coding agents. We’re currently experimenting with agentic search patterns, layering different types of enrichment and indexing, RBAC on indexed data, and streaming architectures.<p>If this is interesting to you, feel free to take it for a spin. Curious to hear your thoughts and feedback on the problem and our solution!

## 综合总结
Airweave 是 YC X25 的开源项目，为 AI agent 提供跨应用和数据库的统一语义检索层。通过 Temporal 编排多源数据同步，结合向量检索、BM25 关键词搜索和 RRF 融合排序，暴露为 MCP/REST/SDK 多接口。技术上是对 RAG 与 agent 工具调用之间空白地带的有力工程化方案，对正在构建 agent 应用的开发者具有实际参考价值，但本质是整合性创新而非底层突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该项目在 RAG 检索增强架构上展示了扎实的技术深度：结合语义搜索与 BM25 关键词检索的并行融合（RRF 倒数排名融合）、recency bias 时间衰减重排序、PostgreSQL 中的轻量级图元数据存储、以及基于 Temporal 的数据同步编排（含分页/速率限制/变更检测）。对 MCP 薄包装局限性的批判也有一定洞察力。技术栈完整但未涉及特别前沿的创新，属于工程整合层面的优秀实践。

### 实用性 (评分: 8.0/10)
对 AI Agent 开发者具有较高实用价值：解决了 agent 落地中最常见的痛点——跨 SaaS 和数据库的统一语义检索层。支持 REST/Python/TS SDK/MCP 多接口暴露，开发者集成门槛低。开源自托管选项加上托管服务，覆盖不同阶段需求。从法律 AI、客服到 coding agent 增强，应用场景明确，工程师可直接试用评估。

### 社区活跃度 (评分: 7.5/10)
HN 获得 164 points 和 30 条评论，作为 Launch HN 属于中等偏上的关注度。YC X25 背书 + 二次 Launch（之前 Show HN）带来一定的回访关注者。评论数量适中表明有实质性讨论但非现象级热门。社区对 agent 检索基础设施类项目持续保持兴趣。

## 项目链接
https://github.com/airweave-ai/airweave
