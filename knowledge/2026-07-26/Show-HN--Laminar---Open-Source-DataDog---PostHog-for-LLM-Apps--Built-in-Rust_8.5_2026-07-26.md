# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.5  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源, 发布  
**更新日期：** 2026-07-26  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个基于 Rust 构建的开源 LLM 应用可观测性与分析平台，旨在成为 LLMOps 领域的 Supabase。它通过 OpenTelemetry 实现全链路追踪，将语义指标与执行追踪深度绑定，并提供可视化的 Pipeline Builder 及向量数据库混合搜索功能，有效解决了复杂 Agent 和 RAG 架构下的调试与评估痛点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
技术栈硬核且现代，采用 Rust 构建高吞吐的 OpenTelemetry 数据摄入器，结合 ClickHouse 与 Qdrant 实现分析与向量混合搜索。核心创新在于将语义指标与全链路追踪深度绑定，并自研了支持并行与循环分支的图执行引擎用于 LLM Pipeline 构建，工程含金量高。

### 实用性 (评分: 9.0/10)
直击当前复杂 LLM 应用（特别是多步 Agent 和 RAG）的调试与可观测性痛点。全链路追踪、语义搜索 Trace、分离核心逻辑与事件处理等设计，对构建生产级 LLM 应用的开发者具有极高的实操参考价值和直接可用性。

### 社区活跃度 (评分: 8.0/10)
获得 203 个 Points 和 45 条评论，在 Show HN 项目中表现优异，表明社区对 Rust 驱动的 LLMOps 基础设施高度关注，讨论聚焦于架构选型、竞品差异及实际工程痛点，互动质量较高。

## 项目链接
https://github.com/lmnr-ai/lmnr
