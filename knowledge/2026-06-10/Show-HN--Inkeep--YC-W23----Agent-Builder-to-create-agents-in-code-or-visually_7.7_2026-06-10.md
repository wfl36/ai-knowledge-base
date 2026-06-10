# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, Developer Tools, 发布, 开源  
**更新日期：** 2026-06-10  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 AI Agent 构建器，核心亮点在于实现了代码与可视化编辑器之间的双向同步，使开发者与非技术人员能在同一平台上协作构建 Agent。该项目基于多智能体架构，支持 MCP 和 A2A 协议，兼顾了代码的灵活性与无代码的易用性，并提供丰富的集成与部署方案，为当前 Agent 开发中的跨团队协作痛点提供了实用的工程化解决思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目解决了代码与可视化编辑器双向同步的工程难题，底层采用共享表示并通过 LLM 与 TypeScript 结合进行状态桥接，具备一定技术深度。支持 MCP 和 A2A 协议，符合当前多智能体架构的前沿趋势，但整体仍属应用层封装与工程优化，缺乏底层算法突破。

### 实用性 (评分: 8.5/10)
对 AI 从业者及团队极具实用价值。有效解决了开发者追求代码控制力与非技术人员追求可视化易用性之间的协作痛点。提供丰富的集成（Vercel AI SDK、MCP、A2A）、现成模板及可观测性方案，开箱即用，能显著降低企业内部落地 Agent 的门槛。

### 社区活跃度 (评分: 7.5/10)
79 点和 49 条评论显示出社区对该工具的较高关注度。双向同步和跨团队协作的痛点切中当下 Agent 开发实际需求，引发了关于实现机制、与现有框架（如 LangGraph、OpenAI）对比及 MCP/A2A 生态的实质性讨论，互动质量较高。

## 项目链接
https://github.com/inkeep/agents
