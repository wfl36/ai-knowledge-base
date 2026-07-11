# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, TypeScript, Durable Execution, 发布  
**更新日期：** 2026-07-11  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是一个基于 TypeScript 的 AI Agent 构建库，专注于解决 Agent 在生产环境中面临的长时间运行、状态持久化和容错等工程痛点。它引入了持久执行机制，通过自动检查点和 waitFor 事件监听，确保 Agent 在中断或等待外部事件时能够可靠恢复，底层依赖 Postgres 存储事件日志。该库不干预 LLM 调用或记忆管理等，仅提升 Agent 的可观察性与可靠性，对 AI 工程化落地具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该项目将分布式系统中的持久执行、状态检查点和事件监听等概念引入 AI Agent 构建，解决了 Agent 长时间运行、状态维护及容错等工程难题。技术实现上基于 Postgres 的线性事件日志，虽非底层算法创新，但在 Agent 工程架构层面具有相当的深度和含金量。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具实际参考价值。当前多数 Agent 框架偏重于提示词和记忆管理，缺乏对生产环境下容错、中断恢复和可观察性的支持。Pickaxe 专注解决这些工程痛点，且不干涉 LLM 调用等核心逻辑，易于集成到现有系统中，对 Agent 落地落地有直接帮助。

### 社区活跃度 (评分: 6.5/10)
获得 70 个 Points 和 26 条评论，在 HN 上属于中等偏上热度。这表明社区对 AI Agent 工程化及容错问题有切实关注，但讨论规模尚未达到现象级，属于垂直领域的深度交流。

## 项目链接
https://github.com/hatchet-dev/pickaxe
