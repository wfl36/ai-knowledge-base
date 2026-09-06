# Show HN: Pickaxe – A TypeScript library for building AI agents

**评分：** 7.0  
**状态：** 正常  
**标签：** AI Agent, TypeScript, 持久化执行, 分布式系统, 开源工具, Show HN, 基础设施  
**更新日期：** 2026-09-06  
**来源：** hackernews  

## 项目描述
Hey HN, Gabe and Alexander here from Hatchet. Today we&#x27;re releasing Pickaxe, a Typescript library to build AI agents which are scalable and fault-tolerant.<p>Here&#x27;s a demo: <a href="https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-4427-9574-e4c756b29dd4">https:&#x2F;&#x2F;github.com&#x2F;user-attachments&#x2F;assets&#x2F;b28fc406-f501-442...</a><p>Pickaxe provides a simple set of primitives for building agents which can automatically checkpoint their state and suspend or resume processing (also known as durable execution) while waiting for external events (like a human in the loop). The library is based on common patterns we&#x27;ve seen when helping Hatchet users run millions of agent executions per day.<p>Unlike other tools, Pickaxe is not a framework. It does not have any opinions or abstractions for implementing agent memory, prompting, context, or calling LLMs directly. Its only focus is making AI agents more observable and reliable.<p>As agents start to scale, there are generally three big problems that emerge:
1. Agents are long-running compared to other parts of your application. Extremely long-running processes are tricky because deploying new infra or hitting request timeouts on serverless runtimes will interrupt their execution. 
2. They are stateful: they generally store internal state which governs the next step in the execution path
3. They require access to lots of fresh data, which can either be queried during agent execution or needs to be continuously refreshed from a data source.<p>(These problems are more specific to agents which execute remotely -- locally running agents generally don&#x27;t have these problems)<p>Pickaxe is designed to solve these issues by providing a simple API which wraps durable execution infrastructure for agents. Durable execution is a way of automatically checkpointing the state of a process, so that if the process fails, it can automatically be replayed from the checkpoint, rather than starting over from the beginning. This model is also particularly useful when your agent needs to wait for an external event or human review in order to continue execution. To support this pattern, Pickaxe uses a Hatchet feature called `waitFor` which durably registers a listener for an event, which means that even if the agent isn&#x27;t actively listening for the event, it is guaranteed to be processed by Hatchet and stored in the execution history and resume processing. This infrastructure is powered by what is essentially a linear event log, which stores the entire execution history of an agent in a Postgres database managed by Hatchet.<p>Full docs are here: <a href="https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;">https:&#x2F;&#x2F;pickaxe.hatchet.run&#x2F;</a><p>We&#x27;d greatly appreciate any feedback you have and hope you get the chance to try out Pickaxe.

## 综合总结
Pickaxe是一个面向TypeScript生态的AI Agent持久化执行库，源自Hatchet团队处理数百万次agent执行的经验。它不与特定LLM或agent框架绑定，而是专注于解决agent规模化时的三个核心问题：长运行时间、有状态性、数据新鲜度。通过checkpoint机制、事件驱动的waitFor API和Postgres事件日志，提供可靠的状态恢复和人机协作能力。作为非框架的设计理念降低了集成成本，但依赖Hatchet平台的基础设施。整体是一个务实的工程方案，适合生产环境中需要高可靠性agent执行的项目。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该库聚焦于AI Agent的持久化执行（durable execution）基础设施，技术方向涉及checkpoint机制、事件监听器、Postgres线性事件日志等分布式系统概念。架构清晰，通过waitFor API实现可靠的外部事件等待与恢复，避免了serverless超时中断问题。但本身并不涉及LLM调用、prompt工程或agent推理等AI核心技术，更偏向工程基础设施层。

### 实用性 (评分: 7.0/10)
对正在构建生产级AI Agent的开发者有较高参考价值，特别是那些使用serverless架构或需要长时间运行、人机协作场景的团队。70 points和26条评论说明受到一定关注。作为一个非框架的轻量库，避免了与主流框架（如LangChain）的锁定，集成灵活。不过其依赖Hatchet底层基础设施，实用性受到平台绑定限制。

### 社区活跃度 (评分: 6.5/10)
70个points和26条评论属于中等偏上的HN关注度。作为Show HN帖子，展示了demo视频和完整文档，推广力度充分。讨论可能集中在durable execution模式与传统workflow引擎的比较、与Temporal等竞品的差异，以及serverless部署agent的实际痛点。社区参与度尚可但未达到热门话题水平。

## 项目链接
https://github.com/hatchet-dev/pickaxe
