# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agent, 开发者工具, 可视化编程, 发布, 协作平台  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款支持代码与可视化编辑器双向同步的 Agent 构建平台，旨在打破开发者与非技术人员在智能体构建上的协作壁垒。底层采用多智能体架构，支持 MCP、A2A 等开放协议，并提供丰富的集成与部署方案，对需要跨职能协作开发 AI 智能体的团队具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目实现了代码与可视化编辑器之间的真正双向同步，底层基于共享的通用表示层，并通过 LLM 与 TypeScript 语法糖进行桥接转换，技术实现具有一定难度与创新性。架构上全面拥抱多智能体设计，原生支持 MCP、A2A 等开放协议，并集成了 OTEL 可观测性，技术栈现代且完整。

### 实用性 (评分: 8.5/10)
极大提升了 AI 从业者的协作效率，精准解决了开发者与产品/运营等非技术人员在智能体构建与迭代上的协同痛点。同时兼容 Vercel AI SDK、提供 React UI 组件及 Docker/Vercel 极简部署方案，对快速落地企业级 AI 助手和工作流具有极高的实用价值。

### 社区活跃度 (评分: 7.5/10)
获得 79 个点赞和 49 条评论，在 Show HN 中表现良好。近 50 条评论表明社区对该工具的“代码与可视化双向同步”及多智能体协作模式有较强的探讨意愿，关注其与现有框架（如 LangGraph、Mastra）的差异化体验及实际落地效果。

## 项目链接
https://github.com/inkeep/agents
