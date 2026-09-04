# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 7.8  
**状态：** 正常  
**标签：** Show HN, 开源, LLM可观测性, OpenTelemetry, Rust, LLMOps, RAG, Agent, 可观测平台  
**更新日期：** 2026-09-04  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向 LLM 应用的开源全栈可观测性平台，基于 Rust 构建，集成了全链路 OpenTelemetry tracing、语义化文本分析、Pipeline Builder（可视化 LLM 流程编排引擎）、span 向量化混合搜索及评估功能。其差异化主张在于将完整执行追踪与文本语义分析结合，并提供自托管的 LLMOps 一站式方案。技术架构扎实，思路清晰，但作为刚发布数周的新项目，在稳定性、生产案例和与 LangSmith、Phoenix、Helicone 等竞品的功能对比上尚需时间验证。整体是一个值得关注和尝试的开源 LLMOps 基础设施项目。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.2/10)
技术栈丰富且深度较高：基于 Rust 自研 OpenTelemetry 摄入器，采用 RabbitMQ + Postgres + ClickHouse + Qdrant 多组件架构，针对 LLM 应用的可观测性场景做了系统性设计。核心技术亮点包括：GenAI 语义约定的 Otel span 摄入、全链路执行追踪（非仅 LLM 调用）、向量数据库索引 span 实现混合搜索、自研支持并行分支/循环的图执行引擎用于 Pipeline Builder，以及将文本语义指标与执行追踪绑定的思路。在 LLM Observability 这一细分赛道展现了较扎实的技术深度。

### 实用性 (评分: 7.8/10)
对 AI 从业者有明确参考价值：1) 解决了 Agent 和复杂 RAG 流水线的全链路追踪痛点；2) Pipeline Builder 提供了可视化编排 LLM 工作流的能力，可作为 API 端点直接调用；3) 评估（Evals）功能借鉴 Braintrust/W&B 的本地运行模式，降低使用门槛；4) 开源 + 自托管定位对成本敏感和数据隐私敏感的团队有吸引力。不足之处是项目仅发布数周，稳定性、生产案例和文档成熟度有待验证；与 LangSmith/Phoenix/Helicone 等竞品的功能重叠需要持续差异化。

### 社区活跃度 (评分: 7.5/10)
203 points 与 45 条评论属于 HN 上较高的关注度，说明 Show HN 类产品发布中获得了显著的社区曝光。评论数与点数的比例（约 4.5:1）反映出讨论质量较好——既有兴趣也有实质性反馈。从发布主体看，多位创始人在 HN 评论区积极回复互动，符合高质量 Show HN 的社区参与模式。作为发布仅数周的开源项目，社区热度属于积极正面。

## 项目链接
https://github.com/lmnr-ai/lmnr
