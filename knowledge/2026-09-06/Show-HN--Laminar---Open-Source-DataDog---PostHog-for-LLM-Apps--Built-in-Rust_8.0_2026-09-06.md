# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 8.0  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源工具, Show HN, Rust, OpenTelemetry, Agent, RAG, 向量数据库, 发布  
**更新日期：** 2026-09-06  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向复杂 LLM 应用的开源可观测性平台，以 Rust 为核心构建，集成了 OpenTelemetry 全链路追踪、Pipeline Builder 图化执行引擎、混合检索等差异化功能。其定位是成为 LLMOps 领域的 Supabase，主打全链路 trace 关联语义分析的开源解决方案。项目技术架构完整且有亮点，对 Agent/RAG 开发者有实用价值，但作为数周龄项目，成熟度和生产稳定性尚待验证。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
技术含量较高，项目采用了 Rust 构建的高性能 OpenTelemetry 摄入器，并集成了 RabbitMQ、Postgres、ClickHouse、Qdrant 等多样化基础设施栈。核心技术亮点包括：1) 基于 GenAI 语义约定的 Otel span 全链路追踪；2) 支持并行分支、循环的自研图执行引擎；3) 向量数据库索引 span 实现混合检索；4) 将语义指标与执行 trace 关联的分析范式。在 LLMOps 可观测性领域展现出系统级的架构设计能力，但本质上仍是已有组件的整合而非底层创新。

### 实用性 (评分: 7.5/10)
对 AI 从业者具有较高参考价值，尤其是构建复杂 Agent 和 RAG 系统的开发者。核心价值在于：1) 全链路 trace 而非单一 LLM 调用观测，对调试多步骤 AI 流程至关重要；2) Pipeline Builder 的图化 UI + API 部署方式可有效分离业务逻辑与 LLM 处理；3) 开源特性降低使用门槛。但项目仅数周龄，评估功能和向量搜索仍在 beta 阶段，生产可用性需谨慎评估。

### 社区活跃度 (评分: 8.0/10)
203 points 和 45 条评论属于 HN 上较高的关注度，表明社区对 LLM 可观测性这一赛道有强烈兴趣。Show HN 形式配合明确的技术差异化定位（全链路 trace + 语义分析 + 开源 + Rust 性能）激发了讨论。评论数适中说明讨论质量可能较为深入，但相对于同类 Show HN 项目，互动深度不算最高，社区热度整体偏上。

## 项目链接
https://github.com/lmnr-ai/lmnr
