# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.3  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源发布, Rust, Agent  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个基于 Rust 构建的开源 LLM 应用可观测性与分析平台，定位为 LLMOps 领域的 Supabase。它通过 OpenTelemetry 实现全链路追踪，创新性地将语义指标与执行追踪结合，并提供图化 Pipeline Builder 和 Eval 功能，为复杂 Agent 和 RAG 应用的调试与监控提供了高价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目技术栈硬核且选型合理，采用 Rust 构建高性能的 OpenTelemetry 数据摄取器，结合 ClickHouse 处理分析负载与 Qdrant 实现追踪的混合语义搜索。自研的图执行引擎支持并行分支与循环，针对复杂 LLM Pipeline 的执行逻辑有深度的工程考量，整体技术深度与含金量较高。

### 实用性 (评分: 9.0/10)
直击当前 AI 从业者在构建复杂 Agent 和 RAG 应用时面临的调试与监控痛点。将语义指标（如 Agent 是否成功推销）与执行追踪绑定，并提供可视化的 Pipeline Builder 和 Eval 支持，极大降低了 LLM 应用逻辑与后台分析解耦的开发门槛，对从业者具有极高的实际参考和应用价值。

### 社区活跃度 (评分: 7.5/10)
在 Hacker News 上获得 203 个点赞和 45 条评论，对于一款开发者工具的 Show HN 来说表现优良。这表明社区对基于 Rust 和 Otel 标准的新一代 LLMOps 工具保持较高关注度，且引发了关于技术选型与市场定位的有效讨论。

## 项目链接
https://github.com/lmnr-ai/lmnr
