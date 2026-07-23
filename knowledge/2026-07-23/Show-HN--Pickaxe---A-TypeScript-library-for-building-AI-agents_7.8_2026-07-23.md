# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.8  
**状态：** 正常  
**标签：** AI Agent, Infrastructure, TypeScript, 开源, 发布  
**更新日期：** 2026-07-23  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Hatchet团队开源了TypeScript库Pickaxe，专注于构建可扩展且容错的AI Agent。该库引入持久执行机制，通过自动状态检查点和事件监听解决Agent长运行、状态管理及外部依赖等工程痛点，为生产级AI Agent提供了高可靠的基础设施支持。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
Pickaxe将分布式系统中的“持久执行”概念引入AI Agent开发，通过自动状态检查点、事件监听(waitFor)和基于Postgres的线性事件日志，解决了Agent长运行易中断、状态易丢失及等待外部事件等工程痛点，技术深度与含金量较高。

### 实用性 (评分: 9.0/10)
对AI从业者极具实际参考价值。与市面上大而全的Agent框架不同，Pickaxe专注于Agent的可观测性与容错性，不干预LLM调用与Prompt设计，为生产环境下的Agent可靠性提供了即插即用的基础设施方案，直击Agent落地核心痛点。

### 社区活跃度 (评分: 6.5/10)
获得70个点赞和26条评论，在HN上表现出中等偏上的关注度，说明开发者对AI Agent的容错与基础设施话题有实际需求与探讨兴趣，但尚未形成现象级热度。

## 项目链接
https://github.com/hatchet-dev/pickaxe
