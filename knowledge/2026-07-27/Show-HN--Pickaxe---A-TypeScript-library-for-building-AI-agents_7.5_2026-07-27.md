# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, TypeScript, Infrastructure, 发布, 开源  
**更新日期：** 2026-07-27  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Hatchet 团队发布了 Pickaxe，一个专注于构建可靠、可扩展 AI Agent 的 TypeScript 库。它引入持久执行和自动状态检查点机制，解决 Agent 长时运行易中断、状态易丢失的痛点，且不干预 LLM 调用和提示词管理，仅作为可靠的执行基础设施，为生产级 Agent 开发提供了实用的工程解法。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
Pickaxe 引入了持久执行和状态检查点机制来解决 AI Agent 的长时运行、状态管理和容错问题。它基于线性事件日志和 Postgres，通过 waitFor 原语实现外部事件监听与恢复，技术架构清晰，将分布式系统的可靠性模式应用到了 Agent 编排中。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具实用价值。当前 Agent 开发常受限于进程中断和状态丢失，Pickaxe 专注于解决这些生产环境痛点，且不绑定特定 LLM 框架，可作为现有 Agent 架构的可靠执行层补充，降低了构建高可用 Agent 的工程门槛。

### 社区活跃度 (评分: 6.5/10)
获得 70 个点赞和 26 条评论，显示出社区对 Agent 可靠性基础设施的关注。讨论聚焦于与传统工作流引擎（如 Temporal）的对比及在 Agent 场景下的优劣，互动质量较高。

## 项目链接
https://github.com/hatchet-dev/pickaxe
