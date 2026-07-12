# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.2  
**状态：** 正常  
**标签：** LLMOps, Observability, Open-Source, Release  
**更新日期：** 2026-07-12  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个基于 Rust 构建的开源 LLM 应用可观测性与分析平台，定位为“LLMOps 领域的 Supabase”。它基于 OpenTelemetry 实现覆盖全执行链路的追踪，支持将文本语义指标与具体执行节点绑定，并提供可视化的 DAG Pipeline 构建器及基于向量数据库的 Trace 混合检索功能，旨在解决复杂 Agent 和 RAG 架构下的深度监控、调试与评测难题。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目采用 Rust 构建高吞吐的数据摄入器，整合 RabbitMQ、Postgres、Clickhouse 和 Qdrant 等组件。技术上核心亮点在于基于 OpenTelemetry 语义规范实现全链路执行追踪（覆盖非 LLM 调用），自研支持并行分支与循环的 DAG 图任务执行引擎，以及利用向量数据库对 trace 进行混合检索，展现了较高的后端架构与 MLOps 工程深度。

### 实用性 (评分: 9.0/10)
对 AI 工程师和应用开发者具有极高的实用价值。随着 Agent 和 RAG 架构日益复杂，仅停留在 LLM 调用层的监控已无法满足需求，全链路追踪与语义指标分析直击生产环境调试痛点。其内置的 Pipeline Builder 和评测功能提供了开箱即用的开发辅助，将核心逻辑与 LLM 事件处理分离的设计思路对从业者构建复杂 LLM 应用具有极大参考意义。

### 社区活跃度 (评分: 7.5/10)
获得 203 个点赞和 45 条评论，在 Show HN 中表现优良。社区对 Rust 构建 LLM 可观测性平台展现了较浓厚的兴趣，讨论多聚焦于底层架构选型、同类竞品（如 Langfuse）对比及 OpenTelemetry 的应用场景，具备扎实的话题热度与工程探讨深度。

## 项目链接
https://github.com/lmnr-ai/lmnr
