# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.2  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开发工具, 开源, 发布  
**更新日期：** 2026-07-14  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个用 Rust 构建的开源 LLM 应用可观测性与分析平台，定位为 LLMOps 领域的 Supabase。它区别于仅监控 LLM 调用的传统工具，通过支持 OpenTelemetry 实现全执行链路追踪，并将文本语义分析与 Trace 深度绑定。项目提供图形化 Pipeline Builder 以解耦 LLM 逻辑，并创新性地使用向量数据库进行 Trace 混合搜索，为构建复杂 Agent 和 RAG 的开发者提供了强大的调试与监控方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目采用 Rust 构建核心数据摄取器，技术栈现代且硬核（RabbitMQ+Postgres+ClickHouse+Qdrant），深入结合 OpenTelemetry 标准实现全链路追踪，并自研支持并行分支与循环的图状 Pipeline 执行引擎，技术深度与工程含金量较高。

### 实用性 (评分: 8.5/10)
直击复杂 LLM 应用（Agent/RAG）的可观测性痛点，支持全链路追踪与语义指标绑定，帮助开发者解耦 LLM 逻辑与核心业务，并创新性地提供基于向量数据库的 Trace 混合检索及 Eval 评估体系，对 AI 工程与运维人员极具实操价值。

### 社区活跃度 (评分: 7.5/10)
获得 203 个点赞和 45 条评论，对于刚发布数周的新项目而言，在 HN 社区取得了良好的初始关注度，反映出开发者对 Rust 构建 LLMOps 工具及可观测性方案的浓厚兴趣与探讨热情。

## 项目链接
https://github.com/lmnr-ai/lmnr
