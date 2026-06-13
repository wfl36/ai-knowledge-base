# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 低代码, 开发工具, 发布  
**更新日期：** 2026-06-13  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 AI Agent 构建平台，实现了代码与可视化编辑器的真正双向同步，使开发者与非技术人员能无缝协作。该工具基于多 Agent 架构，支持 MCP/A2A 协议，提供完整的 TS SDK、CLI 及 UI 组件，兼顾了代码的灵活性与低代码的易用性，对当前 AI Agent 的工程化落地具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目核心难点在于代码与可视化编辑器的双向同步，通过底层共享表示结合 LLM 与 TypeScript 语法糖实现 AST 级别的转换；架构上采用多 Agent 模式替代传统 if/else，并原生支持 MCP 和 A2A 等开放协议，技术整合度高，工程深度可观。

### 实用性 (评分: 8.5/10)
极大提升了 AI 从业者的开发与协作效率，解决了开发者需要代码灵活性、业务人员需要可视化易用性的痛点；提供完整的 TS SDK、CLI 工具链、React UI 组件及 Vercel/Docker 部署方案，开箱即用，对构建企业级 AI 应用具有很高的参考和直接使用价值。

### 社区活跃度 (评分: 7.0/10)
获得 79 个点赞和 49 条评论，在 Show HN 项目中表现出中上水平的热度，双向同步机制及 fair-code 许可证引发了社区对 Agent 开发范式与协作模式的积极讨论。

## 项目链接
https://github.com/inkeep/agents
