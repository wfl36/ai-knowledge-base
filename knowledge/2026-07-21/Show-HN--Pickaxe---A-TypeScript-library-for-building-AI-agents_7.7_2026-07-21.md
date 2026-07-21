# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agents, Infrastructure, TypeScript, Open Source, Release  
**更新日期：** 2026-07-21  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是一个基于 TypeScript 的 AI Agent 构建库，由 Hatchet 团队发布。它引入了持久化执行机制，通过自动状态检查点和 waitFor 事件监听，解决了 Agent 在生产环境中面临的长时运行中断、状态丢失和外部事件（如人工审核）等待等可靠性问题。该库不干预 LLM 调用或提示词管理，专注提升 Agent 的容错性与可观测性，为构建生产级 AI Agent 提供了坚实的基础设施支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目将持久化执行（Durable Execution）引入 AI Agent 领域，通过自动状态检查点和 waitFor 事件监听机制，解决了 Agent 长时运行易中断、有状态及数据刷新等工程难题。底层基于 Postgres 的线性事件日志实现，虽非 AI 底层算法突破，但在分布式系统与 AI 工程结合上具有较高深度。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具参考价值。当前 Agent 走向生产环境最大的痛点就是稳定性和状态管理。该库不绑定特定 LLM 或框架，专注解决容错与可观测性，能直接作为基础设施层集成到现有 Agent 架构中，大幅降低生产级 Agent 的开发与维护门槛。

### 社区活跃度 (评分: 7.0/10)
获得 70 个点赞和 26 条评论，对于一个垂直领域的开发者工具而言表现良好。讨论聚焦于持久化执行机制、与 Temporal 等现有方案的对比，以及 Agent 基础设施的实际痛点，受众精准，社区互动质量较高。

## 项目链接
https://github.com/hatchet-dev/pickaxe
