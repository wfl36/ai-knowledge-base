# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 7.3  
**状态：** 正常  
**标签：** Show HN, LLMOps, 可观测性, OpenTelemetry, Rust, 开源, RAG, Agent, 向量搜索, Pipeline Builder  
**更新日期：** 2026-09-02  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向复杂 LLM 应用的开源可观测性 + 分析平台，核心差异化在于：基于 OpenTelemetry 覆盖完整执行 trace（而非仅 LLM call）、将文本语义指标与 trace 节点联动、Pipeline Builder 支持图结构 LLM 流程编排、以及对 trace 进行向量混合搜索。技术栈选型合理（Rust + ClickHouse + Qdrant），目标明确对标 Supabase-for-LLMOps。但项目刚发布数周，功能成熟度、评估能力与竞品差异化仍有待验证。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
技术方案有明确深度：基于 OpenTelemetry GenAI 语义约定构建 Rust ingestor 处理完整执行 trace，而非仅 LLM 调用；混合使用 Postgres/ClickHouse/Qdrant 等异构存储分别应对事务、olap 分析与向量检索；自定义图执行引擎支持并行分支、循环与分支执行，体现工程能力。但架构选择偏组合创新而非底层突破，OpenLLMetry 等关键依赖仍为外部项目，整体技术深度中高。

### 实用性 (评分: 7.0/10)
对 LLM 应用开发者具备直接参考价值：trace + 文本语义分析联动解决 agent/RAG 调试痛点；Pipeline Builder 将 LLM 逻辑与核心业务解耦的设计思路实用；混合搜索 trace 的方向有差异化潜力。但项目尚处早期（几周大），功能稳定性与文档完备性存疑，且 LLMOps 赛道已有 LangSmith、Phoenix、Langfuse 等成熟竞品，从业者更多是增加一个备选方案。

### 社区活跃度 (评分: 7.5/10)
203 points + 45 comments 属于 HN 上 AI 基础设施类 Show HN 中较高热度，反映 LLM observability 是当前社区持续关注赛道；Show HN 形式天然带来试用与反馈型讨论。评论数相对 points 偏低，说明更多是认同式 upvote 而非深度辩论，社区讨论质量中等。

## 项目链接
https://github.com/lmnr-ai/lmnr
