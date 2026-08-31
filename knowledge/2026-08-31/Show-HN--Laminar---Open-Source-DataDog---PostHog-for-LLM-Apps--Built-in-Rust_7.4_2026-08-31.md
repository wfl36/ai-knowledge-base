# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 7.4  
**状态：** 正常  
**标签：** LLMOps, 可观测性, 开源, Show HN, Rust, OpenTelemetry, RAG, Agent, 向量数据库  
**更新日期：** 2026-08-31  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向复杂 LLM 应用的开源可观测性平台，核心卖点是用 Rust 构建高性能 OpenTelemetry ingestor 处理完整执行 trace，并将语义化分析与 trace 深度绑定。其 Pipeline Builder 图编排引擎和混合搜索 trace 检索是有特色的差异化功能。项目瞄准 'Supabase for LLMOps' 定位，赛道竞争激烈但需求真实，作为早期项目值得关注其后续发展。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
技术栈具有相当深度：基于 Rust 构建的 OpenTelemetry ingestor 处理 GenAI 语义约定，展示了高性能基础设施能力；自定义图执行引擎支持并行分支、循环等复杂控制流，技术实现有亮点；混合搜索（向量DB + 全文检索）用于 trace 检索也是较前沿的技术方向。整体架构（RabbitMQ + Postgres + ClickHouse + Qdrant + Rust）体现了对 LLM observability 场景的系统性思考。但相对于 LangSmith、Helicone 等竞品，核心创新点集中在工程实现层面而非底层算法突破。

### 实用性 (评分: 7.0/10)
对 LLM 应用开发者有较高参考价值：完整 execution tracing 对构建复杂 Agent/RAG 应用的团队是真实痛点；Pipeline Builder 提供的可视化编排 + API endpoint 能力可显著降低 LLM 逻辑迭代成本；语义指标与 trace 关联的思路对生产环境调试很有帮助。开源 + 自托管模式对数据敏感场景友好。但作为'几周龄'项目，成熟度、文档完整性、稳定性尚待验证，距离生产可用还需时间。

### 社区活跃度 (评分: 7.8/10)
203 points 和 45 条评论属于 HN 上 AI infra 类 Show HN 中较高热度的表现，说明社区对 LLM observability 赛道的关注度较高。Show HN 形式本身容易获得较多关注，标题中 'DataDog + PostHog for LLM' 的类比定位清晰，有助于吸引目标受众。45 条评论通常意味着有实质性技术讨论而非纯赞叹。

## 项目链接
https://github.com/lmnr-ai/lmnr
