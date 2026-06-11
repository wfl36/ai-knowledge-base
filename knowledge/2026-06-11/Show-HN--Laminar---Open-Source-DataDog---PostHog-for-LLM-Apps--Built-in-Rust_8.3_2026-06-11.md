# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.3  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源项目, 发布, Rust  
**更新日期：** 2026-06-11  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个基于 Rust 构建的开源 LLM 应用可观测性与分析平台，定位为“LLM 领域的 DataDog + PostHog”。项目核心优势在于支持基于 OpenTelemetry 的全链路执行追踪（覆盖 Agent 和 RAG 的复杂调用），将文本语义分析与执行追踪深度绑定，并提供可视化 Pipeline 构建器及向量数据库混合搜索功能，旨在成为 LLMOps 领域的 Supabase。该工具直击复杂 LLM 应用调试与监控痛点，对从业者具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目采用 Rust 构建高性能数据接入层，结合 RabbitMQ、Postgres、Clickhouse 和 Qdrant 等现代数据栈，技术选型扎实。核心亮点在于基于 OpenTelemetry 标准的全链路追踪（而非单一 LLM 调用），以及支持并行分支和循环的自定义图执行引擎，技术深度和工程复杂度较高。

### 实用性 (评分: 9.0/10)
对 AI 从业者极具参考价值。解决了当前 LLM 应用（尤其是复杂 Agent 和 RAG 架构）缺乏全链路可观测性的痛点。将文本分析与执行追踪绑定、支持语义搜索 Trace、以及本地运行评估同步结果的设计，直击开发者调试和监控 LLM 应用的核心需求，可作为 LLMOps 领域的重要基础设施。

### 社区活跃度 (评分: 7.5/10)
获得 203 个点赞和 45 条评论，在 HN 的 Show HN 项目中表现良好，说明社区对 Rust 驱动的开源 LLMOps 平台有较高关注度，讨论集中在技术架构、与竞品差异及实际应用场景上。

## 项目链接
https://github.com/lmnr-ai/lmnr
