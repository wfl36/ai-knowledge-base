# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 6.8  
**状态：** 正常  
**标签：** AI Agents, Durable Execution, TypeScript, 基础设施, 开源发布, Show HN, 工作流引擎, 可观测性  
**更新日期：** 2026-08-31  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是 Hatchet 团队开源的 TypeScript 库，专注于解决 AI agent 在生产环境中的可靠性与可观测性问题，通过持久执行模式实现状态自动 checkpoint、暂停恢复和外部事件等待。它定位为底层基础设施而非框架，不干预 prompt 或 LLM 调用细节。技术思路务实，适合需要构建可恢复、可扩展 agent 系统的团队参考和使用。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该库聚焦于 AI agent 的持久执行（durable execution）问题，技术思路清晰：通过 Postgres 线性事件日志实现状态 checkpoint、暂停/恢复、waitFor 事件监听等机制，解决长运行 agent 在 serverless 环境下的中断、状态管理和外部事件等待问题。不涉及 LLM 调用或 prompt 等上层抽象，而是作为基础设施层库，技术定位明确。但整体创新性中等——durable execution 概念在 Temporal/Inngest 等系统中已较成熟，Pickaxe 主要是将其与 AI agent 场景结合并基于 Hatchet 工作流引擎实现，技术含量中上。

### 实用性 (评分: 7.0/10)
对于正在构建生产级 AI agent 系统的工程师有一定参考价值，尤其是遇到长运行流程中断、human-in-the-loop、状态恢复等痛点的团队。提供了相对简洁的 TypeScript API 和文档入口。但作为新发布库，社区生态、成熟度和生产案例尚不充分，短期内更适合评估和小规模试用而非直接用于关键业务。其'不是框架'的定位降低了采用门槛，但也意味着用户需要自行组合其他工具。

### 社区活跃度 (评分: 6.0/10)
70 个 points 和 26 条评论属于 HN 中等偏上关注度，作为 Show HN 项目表现尚可，说明话题（AI agent 基础设施）本身具有吸引力。但评论数相对 points 不算特别高，深度讨论可能有限；社区对 agent 可靠性、可观测性话题持续关注，但热度未达到突破性级别。

## 项目链接
https://github.com/hatchet-dev/pickaxe
