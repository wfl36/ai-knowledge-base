# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 低代码, 发布, 开源  
**更新日期：** 2026-07-16  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 AI Agent 构建工具，核心亮点在于实现了代码与可视化编辑器的双向同步，支持开发与非开发人员协作。底层采用多 Agent 架构，并原生集成 MCP、A2A 等开放协议，兼顾了代码的灵活性与低代码的易用性，对需要跨职能协作的 AI 团队具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目实现了代码与可视化编辑器之间的真正双向同步，底层基于多 Agent 架构，通过 LLM 和 TypeScript 语法糖桥接 SDK 与 UI 的共同表示。同时原生支持 MCP、A2A 等现代开放协议，具备较高的工程复杂度与技术含量，但未涉及底层模型或算法的突破。

### 实用性 (评分: 8.5/10)
极大提升了 AI 从业者的开发与协作效率，解决了代码派与低代码派之间的割裂问题，允许开发者与非技术人员在同一平台协同。兼容 Vercel AI SDK、提供 OTEL 可观测性及现成模板，对构建企业级 Agent 平台和跨职能团队协作具有很高的实用价值。

### 社区活跃度 (评分: 7.5/10)
获得了 79 个点赞和 49 条评论，在 Show HN 项目中属于中等偏上热度。社区对其双向同步机制和协议兼容性表现出浓厚兴趣，讨论偏向工程实践与同类工具对比，互动质量较高。

## 项目链接
https://github.com/inkeep/agents
