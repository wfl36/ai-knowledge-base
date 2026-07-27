# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.5  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源项目, 发布  
**更新日期：** 2026-07-27  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar是一个开源的LLM应用可观测性与分析平台，定位为'LLMOps的Supabase'。项目基于Rust构建，核心亮点在于支持OpenTelemetry的全链路追踪、将语义分析与追踪深度结合、内置图化Pipeline构建器以及基于向量库的追踪混合检索。该工具直击复杂Agent和RAG应用的调试与监控痛点，对AI从业者具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目采用Rust构建核心数据摄取器，结合RabbitMQ、Postgres、Clickhouse和Qdrant，实现了高性能的OpenTelemetry spans处理。自研了支持并行分支和循环的图执行引擎用于Pipeline构建，并在追踪搜索上引入了向量数据库的混合检索，技术栈硬核且深度整合了现代云原生与向量检索技术。

### 实用性 (评分: 9.0/10)
对AI应用开发者极具参考价值。针对复杂Agent和RAG应用，提供了全链路追踪而非单一LLM调用监控，将语义指标与执行追踪绑定，并内置了Pipeline Builder和Evals功能，直击LLM应用调试难、评估难、逻辑与观测耦合等痛点，是构建生产级LLM应用的有力工具。

### 社区活跃度 (评分: 8.0/10)
获得了203个点赞和45条评论，在Show HN中表现良好，反映出开发者对LLM可观测性赛道及Rust底层实现的高度关注与讨论热情，社区互动质量较高。

## 项目链接
https://github.com/lmnr-ai/lmnr
