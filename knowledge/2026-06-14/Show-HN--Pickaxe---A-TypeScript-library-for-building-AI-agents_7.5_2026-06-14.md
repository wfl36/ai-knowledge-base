# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, Infrastructure, TypeScript, 发布  
**更新日期：** 2026-06-14  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Hatchet 团队发布了 Pickaxe，一个专注于构建可靠、可扩展 AI Agent 的 TypeScript 库。该库不涉及 LLM 调用或提示词管理，而是通过持久执行机制解决 Agent 在生产环境中面临的长运行超时、状态丢失和外部事件等待（如人机协同）等工程痛点。它基于 Postgres 存储线性事件日志，实现状态自动检查点与故障重放，为 AI 从业者提供了极具实用价值的底层基础设施支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目将持久执行、状态检查点与事件溯源等分布式系统概念引入 AI Agent 领域，以解决长运行和有状态进程的容错问题，技术含金量较高，但核心机制并非全新突破。

### 实用性 (评分: 8.5/10)
直击生产级 AI Agent 面临的执行超时、状态丢失和人机交互等核心工程痛点，为需要构建高可靠性 Agent 的从业者提供了极具参考价值的底层基础设施方案。

### 社区活跃度 (评分: 6.5/10)
获得 70 个 Points 和 26 条评论，对于一个开发者工具库的 Show HN 帖子表现中规中矩，表明社区对 Agent 可靠性基础设施有一定关注与探讨。

## 项目链接
https://github.com/hatchet-dev/pickaxe
