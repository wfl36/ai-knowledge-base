# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, Infrastructure, TypeScript, Show HN, Release  
**更新日期：** 2026-06-10  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是一个用于构建可扩展、容错 AI Agent 的 TypeScript 库，核心通过持久执行机制解决 Agent 长运行进程的中断恢复、状态保存及外部事件等待（如人机协同）问题，专注于提升 Agent 的可靠性与可观测性，而不干预具体的 LLM 交互逻辑。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
Pickaxe 引入了持久执行（Durable Execution）模式来解决 AI Agent 的长运行、有状态和数据刷新问题。它利用基于 Postgres 的线性事件日志进行状态检查点记录，并通过 waitFor 机制实现外部事件监听与人机协同，为 Agent 的可靠性与可观测性提供了扎实的工程级解决方案，且没有对 LLM 调用或记忆管理强加主观抽象。

### 实用性 (评分: 8.5/10)
对 AI 从业者具有极高的实用价值，直击生产环境中 Agent 部署的痛点：进程中断、状态丢失和长时间等待。通过将基础设施层面的容错与状态管理与 Agent 业务逻辑解耦，为开发者构建可扩展、可观测的生产级 Agent 提供了直接可用的 TypeScript 工具。

### 社区活跃度 (评分: 6.5/10)
获得了 70 个点赞和 26 条评论，表现出中等偏上的社区关注度。讨论聚焦于持久执行在 Agent 架构中的实际价值及其与现有框架的对比，反映了工程社区对生产级 Agent 可靠性基础设施的强烈需求与探讨。

## 项目链接
https://github.com/hatchet-dev/pickaxe
