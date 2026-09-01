# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.5  
**状态：** 正常  
**标签：** Agent, Multi-Agent, Developer Tools, Show HN, MCP, Low-Code, TypeScript, YC  
**更新日期：** 2026-09-01  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 是一个面向 AI Agent 开发的可视化+代码双向同步构建平台，旨在弥合 LangGraph 等代码框架与 n8n 等无代码工具之间的鸿沟。支持 MCP、A2A、Vercel AI SDK 等开放协议，提供 TypeScript SDK 和 CLI 工具，实现开发者与非技术人员的协作工作流。技术整合度高、协议兼容性广，适合需要快速迭代 agent 且团队构成多元的中小公司，但在底层架构创新上属于渐进式改进而非突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目涉及多智能体架构设计、代码与可视化双向同步机制、TypeScript SDK 开发以及基于 MCP/A2A/Vercel AI SDK 的互操作性方案，技术覆盖面较广。CLI 通过 LLM + TypeScript 语法糖桥接可视化与代码表征的思路有一定创新性。但本质上是对现有 agent 框架（LangGraph、Mastra）和工作流工具（n8n、Zapier）的整合与差异化封装，底层技术并无重大突破，多智能体架构本身也已是行业常见模式。

### 实用性 (评分: 7.5/10)
对 AI 从业者有较高的实用价值：解决了代码型框架与无代码工具之间的协作痛点，2-way sync 让开发者和非技术团队能在同一平台协作；支持 MCP、A2A、Vercel AI SDK 等标准协议降低了集成成本；提供 traces UI 和 OTEL 日志便于生产部署。预设的 customer_support、deep_research 等模板降低了上手门槛。适合中小团队快速搭建 agent，但 LangGraph、Mastra 等成熟方案的深度用户未必会迁移。

### 社区活跃度 (评分: 7.5/10)
Show HN 帖子获得 79 分和 49 条评论，在 Show HN 中属于中上热度。评论区通常会对同类竞品（LangGraph、n8n、Dify、Vellum 等）进行比较，并质疑双向同步的可靠性、可视化表达力是否足够表达复杂 agent 逻辑。作为 YC W23 批次项目自带一定关注度，社区对其差异化定位（代码↔可视化双向同步）会展开实质讨论。

## 项目链接
https://github.com/inkeep/agents
