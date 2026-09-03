# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.2  
**状态：** 正常  
**标签：** Agent, Multi-Agent, MCP, A2A, Show HN, YC, 开源, 低代码, TypeScript, 工作流编排  
**更新日期：** 2026-09-03  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep是一个面向AI Agent开发的低代码/全代码混合平台，核心卖点是可视化编辑器与TypeScript代码之间的双向同步，并支持MCP/A2A等开放协议实现互操作性。项目解决了devs与non-devs协作构建Agent的痛点，定位介于n8n/Zapier与LangGraph/Mastra之间，技术整合能力较强但原创突破有限。适合需要快速搭建并迭代Agent的中小团队，但面临已有成熟方案的竞争。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目涉及多智能体架构（multi-agent）、MCP协议集成、A2A互操作性、代码与可视化双向同步等多项技术亮点。技术栈包括TypeScript SDK、React Chat UI、OpenTelemetry可观测性，以及与Vercel AI SDK的兼容性。在智能体编排层面提出了一套统一表征层的设计思路，有一定架构深度，但底层更多是对现有范式（LangGraph/LLM-based workflow）的整合而非原创性突破。

### 实用性 (评分: 7.0/10)
对AI从业者有一定实用价值：提供了TypeScript SDK降低开发门槛，MCP/A2A等开放协议支持有助于避免供应商锁定，模板化方案（客服、深度研究、文档助手）可直接复用。可视化与代码双向同步的工作流对中小团队协作有吸引力。但作为YC W23项目，生态成熟度和生产验证尚待观察，且市面上同类工具（n8n、LangGraph、Dify等）竞争激烈，差异化优势需要时间验证。

### 社区活跃度 (评分: 7.0/10)
79个points和49条评论在Show HN中属于中等偏上热度，评论区互动较为活跃。作为YC背书的Show HN项目，社区给予了适度关注但未形成刷屏级讨论。话题触及Agent框架选型这一HN持续关注的方向，从评论数看存在实质性技术讨论而非纯营销反馈，讨论质量中等偏上。

## 项目链接
https://github.com/inkeep/agents
