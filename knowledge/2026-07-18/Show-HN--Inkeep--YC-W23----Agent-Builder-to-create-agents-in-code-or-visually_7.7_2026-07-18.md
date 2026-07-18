# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, Multi-Agent, No-code, Release, Open Source  
**更新日期：** 2026-07-18  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep是一个支持代码与可视化编辑器双向同步的AI Agent构建平台。它允许开发者使用TypeScript SDK构建Agent，并通过CLI实现代码与可视化界面的无缝切换，从而解决技术人员与非技术人员在Agent开发中的协作难题。底层采用多智能体架构，支持MCP、A2A等开放协议，并兼容Vercel AI SDK等主流工具，兼顾了无代码的易用性与代码开发的灵活性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目实现了代码与可视化编辑器之间的双向同步，底层采用多智能体架构，并支持MCP、A2A等开放协议。通过LLM与TypeScript语法糖结合解决双向转换问题，具有一定的工程难度和技术亮点，但非底层算法层面的突破。

### 实用性 (评分: 8.5/10)
极大地提升了AI从业者的开发效率与团队协作体验。解决了开发者与非技术人员在构建Agent时的协同痛点，同时兼容Vercel AI SDK、React等主流生态，提供开箱即用的模板，对实际业务落地有很高的参考和使用价值。

### 社区活跃度 (评分: 7.0/10)
获得79个点赞和49条评论，在Show HN中表现良好。社区对“代码与可视化双向同步”这一核心特性表现出较高兴趣，讨论焦点可能集中在双向同步的实现机制、与现有框架（如LangGraph）的对比以及实际协作体验上。

## 项目链接
https://github.com/inkeep/agents
