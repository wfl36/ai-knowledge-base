# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 7.8  
**状态：** 正常  
**标签：** LLM Observability, OpenTelemetry, Rust, Show HN, 开源, LLMOps, RAG, Agent, Pipeline Builder, 向量搜索  
**更新日期：** 2026-09-05  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向复杂 LLM 应用的开源可观测性与分析平台，主打基于 OpenTelemetry 的完整执行 trace 追踪、Rust 高性能 ingestor、图化 Pipeline Builder 以及基于向量 DB 的 trace 语义搜索。技术栈选型合理，架构有深度，部分设计（如自研图执行引擎、hybrid trace search）展现了较强的工程野心。项目尚处于早期阶段，对愿意尝试新工具的 LLM 开发者有吸引力，但生产级稳定性与生态成熟度仍待时间检验。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
技术栈较为扎实且有深度选择理由：Rust 编写 OpenTelemetry ingestor 保证了高吞吐低延迟，RabbitMQ+Postgres+Clickhouse+Qdrant 的组合覆盖消息队列、关系存储、OLAP 分析与向量检索四大场景。在 OpenTelemetry GenAI semantic conventions 之上做完整 execution trace 而非仅 LLM call，体现了对复杂 Agent/RAG 场景的深刻理解。Pipeline Builder 自研支持并行分支、循环的图执行引擎是真正的技术亮点，区别于简单 DAG。对每个 span 做向量索引实现 hybrid search 也是有前瞻性的工程决策。整体技术方案完整、有架构深度。

### 实用性 (评分: 7.5/10)
对 LLM 应用开发者有较高的实用价值：提供从 trace、analytics、eval 到 semantic search 的端到端 LLMOps 能力，定位为开源版 LLMOps Supabase 有吸引力。'本地运行 eval、结果上报 server' 的模式借鉴 Braintrust/W&B 已被验证。但当前产品仅发布几周，pipeline builder、hybrid search、evaluations 等核心功能仍处于早期/beta 阶段，稳定性、生产可用性尚未验证，社区文档和案例也尚不完善。从业者可关注其演进，但短期投入生产需谨慎。

### 社区活跃度 (评分: 7.5/10)
203 points 与 45 条评论在 Show HN 中属于中上等热度，体现了 HN 社区对 LLMOps 工具的持续关注。Show HN 类项目本身会吸引较多浏览和试用反馈，评论数不算极高但说明项目引发了实质性的技术讨论。社区关注度受 LLM observability 赛道热度加持，但项目差异化（vs LangSmith/Langfuse 等）的讨论深度还需观察。

## 项目链接
https://github.com/lmnr-ai/lmnr
