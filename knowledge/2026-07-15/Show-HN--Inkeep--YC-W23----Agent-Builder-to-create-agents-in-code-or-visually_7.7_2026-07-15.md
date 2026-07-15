# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, DevTool, Low-code, Multi-agent, 发布  
**更新日期：** 2026-07-15  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent 构建器，实现了代码（TypeScript SDK）与可视化拖拽编辑器之间的真正双向同步，旨在解决开发者与非技术人员在构建 AI Agent 时的协作痛点。该项目结合了无代码工具的易用性与代码框架的灵活性，底层采用多智能体架构，并原生支持 MCP、A2A 等开放协议及 Vercel AI SDK，提供了良好的可观测性与部署方案，对 AI 工程化落地有很高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程架构上具有较高含金量，核心亮点在于实现了代码与可视化编辑器之间的真正双向同步（2-way sync），这需要底层共享统一表示并通过 LLM 与 TypeScript 进行桥接；底层采用多智能体架构，并原生支持 MCP、A2A 等前沿开放协议及 OTEL 可观测性，但整体属于工程与架构层面的整合创新，非底层算法突破。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具参考与实用价值，精准击中了当前 Agent 开发中技术人员与非技术人员协作割裂的痛点，兼顾了无代码工具的易用性与代码框架（如 LangGraph）的灵活性；对 Vercel AI SDK、MCP、A2A 的支持及开箱即用的模板，极大降低了 Agent 集成到现有业务流的门槛。

### 社区活跃度 (评分: 7.0/10)
获得了 79 个点赞和 49 条评论，对于 Show HN 项目而言表现中上，表明社区对该工具解决协作痛点的方案有较高兴趣，讨论可能围绕双向同步的实现机制、fair-code 许可证的限制以及与现有框架的对比展开，互动质量较好。

## 项目链接
https://github.com/inkeep/agents
