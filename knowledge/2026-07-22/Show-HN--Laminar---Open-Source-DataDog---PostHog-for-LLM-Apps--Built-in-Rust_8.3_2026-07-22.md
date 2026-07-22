# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.3  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源项目, 发布  
**更新日期：** 2026-07-22  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个开源的 LLM 应用可观测性与分析平台，定位为 LLMOps 领域的 Supabase。项目基于 Rust 和 OpenTelemetry 构建，主打全链路追踪与语义指标的结合，提供可视化 Pipeline Builder、基于向量库的 Trace 搜索及 Eval 评估功能，旨在解决复杂 Agent 和 RAG 应用的监控与调试难题。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
项目采用 Rust 构建核心数据摄取器，结合 RabbitMQ、Clickhouse、Qdrant 等现代数据栈，基于 OpenTelemetry 标准实现 LLM 应用的全链路追踪。自研图执行引擎支持复杂流水线的并行与循环，并创新性地引入向量数据库进行 Trace 的混合搜索，技术深度与工程含金量极高。

### 实用性 (评分: 9.0/10)
直击复杂 LLM 应用（如多 Agent、RAG）的调试与监控痛点，将语义指标与执行追踪深度绑定，提供可视化的 Pipeline Builder 和本地优先的 Eval 功能，帮助开发者剥离 LLM 旁路逻辑，对 AI 工程化落地具有极高的实操参考价值。

### 社区活跃度 (评分: 7.5/10)
获得 203 个点赞和 45 条评论，在 HN 社区引起了中高热度的关注与讨论，开发者对 Rust 技术栈及 LLM 可观测性解决方案表现出浓厚兴趣。

## 项目链接
https://github.com/lmnr-ai/lmnr
