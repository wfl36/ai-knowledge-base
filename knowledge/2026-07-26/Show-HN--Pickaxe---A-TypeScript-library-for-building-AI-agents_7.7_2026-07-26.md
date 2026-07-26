# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, TypeScript, Durable Execution, 发布, 工程化  
**更新日期：** 2026-07-26  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Hatchet 团队发布 TypeScript 库 Pickaxe，专注于解决 AI Agent 在生产环境中的可扩展性与容错问题。它引入持久执行机制，通过自动状态检查点和事件日志确保长运行、有状态 Agent 的可靠性，特别支持 Human-in-the-loop 场景，为 AI Agent 的工程化落地提供了实用的基础设施。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
聚焦于 AI Agent 的工程化痛点，引入了持久执行和事件溯源机制。通过自动状态检查点和线性事件日志（基于 Postgres），解决了 Agent 长时间运行、状态管理及外部事件等待（如 Human-in-the-loop）下的容错与恢复问题，技术深度和含金量较高。

### 实用性 (评分: 8.5/10)
对从事 AI Agent 生产化部署的开发者具有极高的参考价值。当前 Agent 从 Demo 走向生产最大的阻碍就是可靠性和状态管理，Pickaxe 提供的 Durable Execution 模式和 `waitFor` API 直接切中痛点，且不侵入现有 LLM 调用和 Prompt 框架，易于集成。

### 社区活跃度 (评分: 6.5/10)
获得 70 个 Points 和 26 条评论，在 Show HN 类项目中表现中等偏上，说明社区对 AI Agent 基础设施及容错机制有切实的关注和讨论需求。

## 项目链接
https://github.com/hatchet-dev/pickaxe
