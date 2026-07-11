# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, DevTools, No-code, Open Protocol, Show HN, 发布  
**更新日期：** 2026-07-11  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent Builder，核心亮点是实现了代码与可视化编辑器之间的双向同步，解决了开发人员与非技术人员在构建 AI Agent 时的协作痛点。项目底层采用多智能体架构，并深度集成了 MCP、A2A 等开放协议，支持 Vercel AI SDK 和 OTEL 可观测性，为当前 AI 工程化提供了兼具灵活性与易用性的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程架构上具有较高含金量，特别是代码与可视化编辑器的双向同步机制，结合了 LLM 与 TypeScript AST 处理。同时，底层采用多智能体架构替代传统 if/else 逻辑，并原生支持 MCP、A2A 等前沿开放协议及 OTEL 可观测性，展现了良好的系统设计与技术前瞻性。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具实际参考价值，直击开发与业务团队协作的痛点。支持 Vercel AI SDK、Docker 部署及丰富的实用模板（如客服、深度研究），大幅降低了 Agent 的开发、交接与维护门槛，非常适合需要跨职能协作的 AI 产品团队落地应用。

### 社区活跃度 (评分: 7.0/10)
获得 79 个点赞和 49 条评论，在 Show HN 项目中表现出中等偏上的热度，反映出 HN 社区对“代码与无代码双向协同”以及 MCP/A2A 等开放协议的浓厚兴趣与实际探讨。

## 项目链接
https://github.com/inkeep/agents
