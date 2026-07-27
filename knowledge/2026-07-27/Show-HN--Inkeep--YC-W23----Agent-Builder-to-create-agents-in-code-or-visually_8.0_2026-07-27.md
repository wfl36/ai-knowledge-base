# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agent, DevTools, 发布, 开源  
**更新日期：** 2026-07-27  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一个支持代码与可视化编辑器双向同步的 AI Agent 构建平台，解决了开发者与非技术人员协作开发 Agent 的核心痛点。底层基于多智能体架构，支持 MCP/A2A 等开放协议，兼顾了代码的灵活性与低代码的易用性，对 AI 工程化落地与团队协作具有极高参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目采用 TypeScript SDK 与可视化编辑器共享底层表示的架构，通过 CLI 和 LLM+TS 语法糖实现代码与可视化的真正双向同步（2-way sync）。底层采用多智能体架构，并原生支持 MCP、A2A 等开放协议，具备较强的工程深度和架构设计含金量，但并非底层模型或算法层面的突破。

### 实用性 (评分: 9.0/10)
极大解决了 AI 从业者在 Agent 开发中的核心痛点：既保留了代码开发的灵活性与 DevEx（如 LangGraph），又兼顾了非技术人员协作的便利性（如 n8n/Zapier）。支持一键交接给业务团队、原生集成 Vercel AI SDK、React Chat UI 及可观测性（OTEL），对 Agent 的工程化落地与跨职能协作具有极高的实用价值。

### 社区活跃度 (评分: 7.5/10)
获得 79 个点赞和 49 条评论，在 Show HN 项目中属于中上水平。评论数与点赞数比例接近 1:1.6，表明该话题引发了开发者对双向同步实现细节、Agent 开发范式及公平代码许可的深入探讨，社区互动质量与关注度良好。

## 项目链接
https://github.com/inkeep/agents
