# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.0  
**状态：** 正常  
**标签：** AI Agent, TypeScript, Durable Execution, 开源工具, Show HN, 基础设施, 工作流引擎, 工程化  
**更新日期：** 2026-09-03  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe 是 Hatchet 团队开源的 TypeScript 库，专注于解决 AI agent 在生产环境中的可靠性与可观测性问题，通过 durable execution 模式实现自动 checkpoint、suspend/resume 及 human-in-the-loop 支持。它不是 agent 框架，而是底层基础设施补充，与 LangChain 等上层工具互补。技术定位清晰，聚焦于 serverless 环境下长运行有状态 agent 的真实痛点，对需要构建生产级 agent 系统的工程师有实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
Pickaxe 聚焦于 AI agent 的 durable execution 基础设施，涉及 checkpoint 机制、基于事件驱动的 suspend/resume 模式、Postgres 线性事件日志等系统设计概念，技术实现有一定深度。但其定位明确为非框架库，不涉及 LLM 调用、记忆、prompt 等上层抽象，技术广度有限。核心创新在于将已有分布式工作流引擎（Hatchet）的 durable execution 能力封装为面向 AI agent 的轻量 TypeScript 库。

### 实用性 (评分: 7.0/10)
对需要构建生产级、长运行、有状态 AI agent 的从业者有较高参考价值，尤其是涉及 human-in-the-loop、外部事件等待、serverless 部署等真实工程痛点的场景。与 LangChain/AutoGen 等上层框架互补，定位基础设施层。70 points + 26 评论表明开发者社区关注度尚可，但目标用户群体较窄（主要是有大规模 agent 部署需求的后端工程师）。

### 社区活跃度 (评分: 6.5/10)
70 个赞和 26 条评论属于 HN 中等偏上热度，作为 Show HN 类项目表现合格，表明社区对 AI agent 工程化基础设施有兴趣但未达到爆款程度。评论数相对偏少，可能因技术话题较垂直，限制了广泛讨论；也可能因项目较新，反馈尚未充分积累。整体属于受关注的实用型发布。

## 项目链接
https://github.com/hatchet-dev/pickaxe
