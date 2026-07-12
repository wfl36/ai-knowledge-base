# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 低代码, 发布, 开源  
**更新日期：** 2026-07-12  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent 构建平台，实现了 TypeScript 代码与可视化编辑器的双向同步，使开发者与非技术人员能无缝协作。底层采用多智能体架构并支持 MCP/A2A 等开放协议，兼顾了代码的灵活性与低代码的易用性，为 AI Agent 的工程化与团队协作落地提供了高价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目核心在于实现了代码与可视化编辑器之间的双向同步，底层依赖统一的中间表示，并通过 CLI 结合 LLM 与 TypeScript 语法糖进行转换；架构上采用多智能体模式替代传统硬编码工作流，并原生支持 MCP、A2A 等开放协议，具备较高的工程复杂度与技术深度。

### 实用性 (评分: 8.5/10)
极大提升了 AI 从业者的开发与跨团队协作效率。开发者可使用 TS SDK 灵活编码，非技术人员可通过可视化界面调整，解决了 Agent 开发中代码派与低代码派割裂的痛点。同时兼容 Vercel AI SDK、提供 Docker 部署及 OTEL 可观测性，开箱即用性强，对落地实际业务场景极具参考价值。

### 社区活跃度 (评分: 7.0/10)
HN 获得 79 个点赞和 49 条评论，显示出社区对“代码与低代码融合”这一痛点的关注。作为 Show HN 项目，引发了关于双向同步实现机制、fair-code 开源协议限制以及 Agent 架构实用性的实质性讨论，互动质量较高。

## 项目链接
https://github.com/inkeep/agents
