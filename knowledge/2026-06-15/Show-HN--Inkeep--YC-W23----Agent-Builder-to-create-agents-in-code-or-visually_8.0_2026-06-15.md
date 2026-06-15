# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agent, 低代码, 开发工具, 发布  
**更新日期：** 2026-06-15  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent 构建工具，核心亮点在于实现了代码与可视化编辑器之间的双向同步，解决了开发者与业务人员协作构建 AI Agent 的痛点。项目底层采用多智能体架构，并原生支持 MCP、A2A 等开放协议，兼容 Vercel AI SDK 和主流 IDE。该工具兼顾了代码开发的灵活性与低代码的易用性，为 AI Agent 的企业级落地与跨职能协作提供了高效的工程解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目实现了代码与可视化编辑器的双向同步，底层结合 LLM 与 TypeScript 语法糖处理 AST 转换；采用多智能体架构替代传统 if/else 流程，并深度集成 MCP、A2A 等前沿开放协议及 OTEL 可观测性，技术栈现代且工程实现难度较高。

### 实用性 (评分: 8.5/10)
极大提升了 AI 从业者的开发与协作效率。开发者可通过 SDK 编写逻辑并交由非技术人员在可视化界面调整，兼顾了代码的灵活性与低代码的便捷性；同时提供开箱即用的模板与主流工具链（Vercel/React/Cursor）兼容，对 Agent 快速落地与跨团队协作极具实用价值。

### 社区活跃度 (评分: 7.5/10)
获得 79 个 Points 和 49 条评论，在 Show HN 项目中表现良好，说明社区对“代码与低代码融合”及 Agent 构建工具的协作模式有较高关注度与讨论意愿，但尚未达到现象级爆款热度。

## 项目链接
https://github.com/inkeep/agents
