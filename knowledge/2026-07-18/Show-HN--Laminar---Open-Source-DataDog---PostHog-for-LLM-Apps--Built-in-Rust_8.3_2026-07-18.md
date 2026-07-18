# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.3  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 大模型应用, 开源, 发布  
**更新日期：** 2026-07-18  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个基于 Rust 构建的开源 LLM 应用可观测与分析平台，定位为 LLMOps 领域的 Supabase。它通过 OpenTelemetry 实现全链路追踪，创新性地将语义分析与执行 trace 绑定，并提供了支持复杂 DAG 的可视化 Pipeline Builder 及基于向量库的 trace 混合检索。该项目技术深度高，精准解决 AI 工程化中的调试与评估痛点，对从业者极具参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目技术栈现代且硬核，采用 Rust 构建高性能 OpenTelemetry span 接入层，结合 Clickhouse 处理海量分析数据，并引入 Qdrant 向量数据库实现 trace 的混合检索。自研的 Pipeline 执行引擎支持复杂 DAG（含并行分支与循环），在分布式追踪与语义数据结合方面展现了较高的工程深度与技术壁垒。

### 实用性 (评分: 9.0/10)
直击当前复杂 LLM 应用（尤其是 Agent 与多步 RAG）在可观测性和评估方面的工程痛点。通过将语义指标提取与执行链路追踪绑定，以及提供可视化、可 API 化的 Pipeline Builder，极大降低了开发者调试、监控和迭代 LLM 逻辑的门槛，对 AI 工程师和从业者具有极高的实用与落地参考价值。

### 社区活跃度 (评分: 7.5/10)
在 Hacker News 上获得 203 个点赞和 45 条评论，属于中上等热度。这表明社区对基于 Rust 的高性能 LLMOps 开源项目以及全链路追踪方案有着强烈的兴趣与需求，讨论参与度良好。

## 项目链接
https://github.com/lmnr-ai/lmnr
