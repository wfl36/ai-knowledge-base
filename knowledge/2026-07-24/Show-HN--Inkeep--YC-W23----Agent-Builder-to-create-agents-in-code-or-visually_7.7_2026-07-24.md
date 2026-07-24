# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 可视化, 发布, 开源  
**更新日期：** 2026-07-24  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent 构建平台，核心亮点在于实现了 TypeScript 代码与可视化拖拽编辑器之间的真正双向同步，打破了开发者与非开发者之间的协作壁垒。底层基于多智能体架构，并原生支持 MCP、A2A 等开放协议，方便与现有 AI 生态集成。该项目采用公平代码许可开源，为 Agent 的工程化落地提供了兼顾代码灵活性与无代码易用性的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目核心工程难点在于实现代码与可视化编辑器之间的真正双向同步（2-way sync），底层通过 LLM 配合 TypeScript 语法糖将 SDK 与可视化构建器的共享表示进行桥接。架构上采用多智能体设计（LLMs, MCPs, agent-to-agent），并原生支持 MCP、A2A 等新兴开放协议，技术栈现代且具备一定深度，但本质属于工程与架构层面的创新，而非底层算法突破。

### 实用性 (评分: 8.5/10)
对 AI 从业者和开发团队具有极高的实用价值。它精准解决了当前 Agent 开发中技术人员与非技术人员（如产品、营销）协作困难的痛点，兼顾了代码的灵活性与无代码的易用性。同时，对 Vercel AI SDK、MCP、React UI 库及主流部署方案的良好支持，使其能无缝融入现有开发工作流，大幅降低 Agent 的构建与交付门槛。

### 社区活跃度 (评分: 7.5/10)
作为 Show HN 项目，获得 79 个 Points 和 49 条评论，表现中规中矩且具备一定的讨论热度。评论数与点赞比例较好，说明项目切中了开发者的实际痛点，引发了关于双向同步实现机制、与 LangGraph/OpenAI 竞品差异以及开源协议等方面的实质性探讨。

## 项目链接
https://github.com/inkeep/agents
