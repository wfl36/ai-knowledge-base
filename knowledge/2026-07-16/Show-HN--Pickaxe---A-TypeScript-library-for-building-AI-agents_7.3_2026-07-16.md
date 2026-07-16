# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.3  
**状态：** 正常  
**标签：** AI Agent, Infrastructure, TypeScript, 发布  
**更新日期：** 2026-07-16  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是一个 TypeScript 库，旨在解决 AI Agent 在生产环境中面临的长时间运行、状态管理和容错等工程挑战。它不干预 LLM 调用或提示词管理，而是专注于通过持久执行、状态检查点和事件监听来提升 Agent 的可靠性与可观察性，为构建可扩展的 AI Agent 提供了实用的基础设施支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
专注于 AI Agent 的持久执行与容错机制，通过自动状态检查点和线性事件日志（基于 Postgres）解决长运行、有状态 Agent 的中断与恢复问题，并支持 waitFor 等待外部事件，技术架构设计扎实。

### 实用性 (评分: 8.5/10)
对 AI 工程师极具参考价值，直击生产环境中 Agent 部署的痛点（如超时、状态丢失、人机协同），提供非侵入式的基础设施层方案，TypeScript 实现也契合前端与全栈开发者生态。

### 社区活跃度 (评分: 6.5/10)
获得 70 个点赞和 26 条评论，作为工具库发布获得了中等偏上的社区关注度，表明开发者对 Agent 可靠性基础设施有实际需求与讨论兴趣。

## 项目链接
https://github.com/hatchet-dev/pickaxe
