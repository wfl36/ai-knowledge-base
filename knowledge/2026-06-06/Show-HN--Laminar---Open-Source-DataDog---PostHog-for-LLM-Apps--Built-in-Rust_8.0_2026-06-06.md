# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.0  
**状态：** 正常  
**标签：** LLMOps, Observability, Open-Source, Release, Rust  
**更新日期：** 2026-06-06  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个专为复杂 LLM 应用设计的开源可观测性与分析平台，定位为“LLMOps 领域的 Supabase”。项目基于 Rust 和现代数据栈构建，核心优势在于采用 OpenTelemetry 标准实现全链路追踪，将语义指标与执行轨迹深度绑定，并提供支持复杂逻辑的 Pipeline Builder 和 Trace 向量混合搜索功能。该项目直击 Agent/RAG 开发中的可观测性与评估痛点，对 AI 工程师具有极高的实用价值，并在 HN 社区引发了积极反响。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在系统工程架构上具有较高技术含量，采用 Rust 构建高性能数据摄取器，结合 RabbitMQ、Postgres、Clickhouse 和 Qdrant 等现代数据栈。技术亮点在于引入 OpenTelemetry 标准实现全链路追踪（而非仅限 LLM 调用），开发了支持并行分支与循环的自定义任务执行引擎，并创新性地基于向量数据库实现了 Trace 的混合搜索，体现了扎实的底层工程与系统集成能力。

### 实用性 (评分: 9.0/10)
对 AI 从业者极具实用价值。随着 Agent 和 RAG 架构日益复杂，LLM 应用的可观测性与评估成为核心痛点。该项目不仅提供全链路追踪，还将文本分析与执行轨迹绑定（语义指标），并内置可视化 Pipeline Builder 和 Evals 功能，极大降低了开发者处理 LLM 后台分析逻辑和评估的门槛，直击当前 LLMOps 的落地痛点。

### 社区活跃度 (评分: 7.5/10)
在 Hacker News 上获得 203 个点赞和 45 条评论，对于 Show HN 类项目而言表现优异，表明开发者社区对基于 Rust 和 Otel 标准的开源 LLMOps 解决方案有强烈兴趣与需求，讨论关注度较高。

## 项目链接
https://github.com/lmnr-ai/lmnr
