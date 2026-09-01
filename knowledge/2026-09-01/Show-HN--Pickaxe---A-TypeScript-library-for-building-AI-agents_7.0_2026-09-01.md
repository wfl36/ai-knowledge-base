# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.0  
**状态：** 正常  
**标签：** AI Agent, Durable Execution, TypeScript, 开源工具, Show HN, 基础设施, Human-in-the-Loop  
**更新日期：** 2026-09-01  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是 Hatchet 团队开源的 TypeScript 库，专注于解决生产级 AI agent 的可靠性与可观测性问题，通过 durable execution 模式提供自动 checkpoint、状态恢复和事件等待能力。其不与框架绑定的库定位降低了对开发者技术栈的侵入成本。适合正在搭建 agent 生产化基础设施、对长时执行和 human-in-the-loop 有需求的团队评估使用。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目针对 AI agent 工程的三大核心痛点（长时运行、有状态、需要新鲜数据），提出基于 durable execution 的解决方案。技术上利用线性事件日志 + Postgres 实现自动 checkpoint、suspend/resume、waitFor 事件监听等机制，与 Temporal 等 durable execution 引擎思路类似但聚焦 agent 场景。架构思路清晰，有一定深度，但并未涉及模型层、推理层或新算法创新，属于工程基础设施层面的技术整合。

### 实用性 (评分: 7.0/10)
对正在构建生产级 AI agent 系统的工程师有明确参考价值，尤其是遇到长时 agent 执行中断、状态管理、human-in-the-loop 等问题的团队。定位为库而非框架的设计哲学（不强制 prompt/memory/LLM 抽象）降低了集成成本。但作为 Hatchet 的衍生产品，存在一定的 vendor lock-in 考量，需要权衡其与 Temporal 等成熟方案的关系。

### 社区活跃度 (评分: 6.5/10)
Show HN 帖子获得 70 分和 26 条评论，属于中等偏上关注度。作为 Hatchet 团队的项目发布，已有一定用户基础背书（'helping Hatchet users run millions of agent executions per day'）。评论数与点数的比例适中，说明有实质讨论而非纯刷量，社区参与质量尚可。

## 项目链接
https://github.com/hatchet-dev/pickaxe
