# Show HN: Laminar – Open-Source DataDog + PostHog for LLM Apps, Built in Rust

**评分：** 7.6  
**状态：** 正常  
**标签：** LLMOps, 可观测性, OpenTelemetry, 开源, Show HN, Rust, RAG, Agents, 向量检索  
**更新日期：** 2026-09-01  
**来源：** hackernews  

## 项目描述
Hey HN, we’re Robert, Din and Temirlan from Laminar (<a href="https:&#x2F;&#x2F;www.lmnr.ai">https:&#x2F;&#x2F;www.lmnr.ai</a>), an open-source observability and analytics platform for complex LLM apps. It’s designed to be fast, reliable, and scalable. The stack is RabbitMQ for message queues, Postgres for storage, Clickhouse for analytics, Qdrant for semantic search - all powered by Rust.<p>How is Laminar different from the swarm of other “LLM observability” platforms?<p>On the observability part, we’re focused on handling full execution traces, not just LLM calls. We built a Rust ingestor for OpenTelemetry (Otel) spans with GenAI semantic conventions. As LLM apps get more complex (think Agents with hundreds of LLM and function calls, or complex RAG pipelines), full tracing is critical. With Otel spans, we can: 1. Cover the entire execution trace. 2. Keep the platform future-proof 3. Leverage an amazing OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), open-source package for span production.<p>The key difference is that we tie text analytics directly to execution traces. Rich text data makes LLM traces unique, so we let you track “semantic metrics” (like what your AI agent is actually saying) and connect those metrics to where they happen in the trace. If you want to know if your AI drive-through agent made an upsell, you can design an LLM extraction pipeline in our builder (more on it later), host it on Laminar, and handle everything from event requests to output logging. Processing requests simply come as events in the Otel span.<p>We think it’s a win to separate core app logic from LLM event processing. Most devs don’t want to manage background queues for LLM analytics processing but still want insights into how their Agents or RAGs are working.<p>Our Pipeline Builder uses graph UI where nodes are LLM and util functions, and edges showing data flow. We built a custom task execution engine with support of parallel branch executions, cycles and branches (it’s overkill for simple pipelines, but it’s extremely cool and we’ve spent a lot of time designing a robust engine). You can also call pipelines directly as API endpoints. We found them to be extremely useful for iterating on and separating LLM logic. Laminar also traces pipeline directly, which removes the overhead of sending large outputs over the network.<p>One thing missing from all LLM observability platforms right now is an adequate search over traces. We’re attacking this problem by indexing each span in a vector DB and performing hybrid search at query time. This feature is still in beta, but we think it’s gonna be crucial part of our platform going forward.<p>We also support evaluations. We loved the “run everything locally, send results to a server” approach from Braintrust and Weights &amp; Biases, so we did that too: a simple SDK and nice dashboards to track everything. Evals are still early, but we’re pushing hard on them.<p>Our goal is to make Laminar the Supabase for LLMOps - the go-to open-source comprehensive platform for all things LLMs &#x2F; GenAI. In it’s current shape, Laminar is just few weeks old and developing rapidly, we’d love any feedback or for you to give Laminar a try in your LLM projects!

## 综合总结
Laminar 是一个面向复杂 LLM 应用的端到端可观测性与分析开源平台，采用 Rust 构建核心 ingestor，整合 OTel traces、语义指标、pipeline builder、向量混合检索与 evaluations 等能力，旨在成为 'Supabase for LLMOps'。技术架构整合度高、差异化思路（语义指标绑定 trace、trace 上的混合检索）有说服力；对 LLM 工程师尤其是自建 Agent / RAG 流水线的团队具备较高参考价值；但项目尚处早期，稳定性与生态待验证。HN 热度中等偏上，社区反馈值得跟踪。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目涉及多项具有较高技术含量的工程决策：自建 Rust OTel ingestor 处理 GenAI semantic conventions、基于图结构的 pipeline 执行引擎（支持并行分支、环、并行执行）、使用 ClickHouse 做分析、Qdrant 做向量混合检索、用 RabbitMQ + Postgres 搭建消息与存储栈。将 traces、语义指标、向量检索与 evaluations 统一在一个开源平台中，工程整合度较高。但单项技术（如 OTel 处理、向量检索 hybrid search）属于业界已有方案的工程化整合，并未提出突破性新算法或新范式，技术亮点更偏系统架构层面。

### 实用性 (评分: 7.5/10)
对 LLM 应用开发者有明确参考价值：解决 Agent / RAG 等复杂 LLM 应用的端到端 trace 观测、语义指标与 trace 关联、低代码 pipeline builder 分离核心逻辑与 LLM 事件处理、evals 本地跑结果上报的轻量模式，都是 LLM 工程化中的痛点。开源 + 自托管形态对成本敏感或合规要求高的团队有吸引力。但项目仅 'few weeks old'，稳定性、文档、SDK 完善度尚待验证，从业者更多是早期试用与参考架构思路，而非立刻替换现有方案。

### 社区活跃度 (评分: 7.8/10)
203 points 与 45 条评论在 Show HN 类别中属于中上热度，表明 HN 社区对 LLM 基础设施层开源项目保持关注。评论数适中，预期会围绕'与 LangSmith/Langfuse/Helicone 等同类竞品差异化'、'Rust 实测性能'、'开源商业化路径'等议题展开讨论。社区关注点集中在技术栈合理性、差异化定位（'Supabase for LLMOps' 的愿景是否站得住）以及 pipeline builder 的实用性。整体讨论质量预估良好，但项目尚处于早期，社区尚在观望阶段。

## 项目链接
https://github.com/lmnr-ai/lmnr
