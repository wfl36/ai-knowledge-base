# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, Infrastructure, TypeScript, Durable Execution, Show HN, 开源  
**更新日期：** 2026-07-20  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是一个专注于构建可扩展与容错 AI Agent 的 TypeScript 库。它引入持久执行机制，通过自动状态检查点与事件监听，解决了 Agent 在生产环境中长运行、有状态及易中断的痛点。项目不干涉模型调用，仅专注基础设施层的可靠性，为 AI 从业者落地复杂 Agent 提供了高实用性的工程化方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
该项目将持久执行、状态检查点和事件监听等分布式系统概念引入 AI Agent 构建中，解决了 Agent 长时间运行、有状态及易中断的技术痛点。基于 Postgres 的线性事件日志实现执行历史的持久化与回放，技术方案扎实且针对性强，具有较高的工程含金量。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具参考价值。生产级 Agent 常面临部署中断、超时崩溃和人工介入等可靠性挑战，Pickaxe 专注于基础设施层的容错与可观察性，不干涉 LLM 调用与提示词管理，可无缝集成至现有技术栈，为 Agent 落地提供了关键的工程化支撑。

### 社区活跃度 (评分: 7.0/10)
获得 70 个 Points 和 26 条评论，对于偏向底层基础设施的 Show HN 项目而言表现中上，表明该痛点在开发者社区中引起了较好的共鸣与讨论，关注度良好。

## 项目链接
https://github.com/hatchet-dev/pickaxe
