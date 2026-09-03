# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 7.8  
**状态：** 正常  
**标签：** LLMOps, 可观测性, OpenTelemetry, Rust, Show HN, 开源, RAG, Agent, 向量数据库  
**更新日期：** 2026-09-03  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向复杂 LLM 应用的 Rust 开源可观测性与分析平台，定位为 LLM 版的 DataDog + PostHog。核心差异点在于：基于 OpenTelemetry 全链路 span 追踪、Rust 自研 ingestor 与图执行引擎、将语义指标直接挂载到 trace 上、支持 trace 的向量混合搜索、并提供 Pipeline Builder 与本地运行的 Evals。其目标是成为 LLMOps 领域的 Supabase 式综合开源平台。项目尚处早期但技术选型扎实，社区反响积极，对构建复杂 Agent / RAG 应用的从业者有较高参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
技术栈组合具有较高含金量：Rust 构建的 OpenTelemetry ingestor、自研支持并行/分支/循环的图执行引擎、Rust 全栈后端、ClickHouse + Qdrant 向量检索的混合搜索方案。技术架构覆盖消息队列、存储、分析、语义检索等完整链路，且自研 Pipeline Engine 说明底层有较深投入。但部分描述偏产品愿景层面，缺少具体的性能基准、架构图或对比数据，技术深度展示略有保留。

### 实用性 (评分: 7.5/10)
对 LLM 应用开发者具有较高的实际参考价值：解决全链路 trace 而非单次 LLM 调用追踪的痛点、语义指标与 trace 绑定的思路、Pipeline Builder 分离核心逻辑与 LLM 事件处理、以及混合搜索定位 trace 等功能均为实际工程问题提供方案。对正在构建 Agent / RAG 应用的从业者尤其有用，可作为 LLMOps 基础设施选型参考。但项目仅几周龄，稳定性、生产案例、文档成熟度有待验证。

### 社区活跃度 (评分: 7.8/10)
203 points 与 45 条评论属于 Show HN 中较高热度的表现，话题命中 LLM 工程化这一当前热门赛道，标题中 DataDog + PostHog for LLM Apps 的类比清晰且引发共鸣，社区关注度良好。讨论质量有望围绕定位差异化、技术选型、竞品对比等展开，但项目尚处早期，社区尚需时间沉淀出深度技术讨论。

## 项目链接
https://github.com/lmnr-ai/lmnr
