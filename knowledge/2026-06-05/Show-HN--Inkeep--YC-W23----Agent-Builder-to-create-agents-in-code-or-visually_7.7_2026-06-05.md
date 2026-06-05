# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 发布, 开源  
**更新日期：** 2026-06-05  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 AI Agent 构建平台，实现了 TypeScript SDK 与可视化拖拽编辑器之间的双向同步，使开发者与非技术人员能无缝协作构建和维护 Agent。项目底层采用多 Agent 架构，原生支持 MCP、A2A 等开放协议，并兼容 Vercel AI SDK，兼顾了代码的灵活性与无代码的易用性，有效解决了当前 Agent 开发中协作困难与厂商锁定的痛点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目核心技术在于代码与可视化编辑器的双向同步（2-way sync），底层通过共享表示层，结合 LLM 与 TypeScript 语法糖实现 CLI 桥接；架构上采用多 Agent 模式替代传统 if/else 工作流，并原生支持 MCP、A2A 等开放协议，技术整合度高且契合当前 AI Agent 前沿范式，但本质属于工程架构创新而非底层算法突破。

### 实用性 (评分: 8.5/10)
对 AI 从业者和开发团队极具实用价值，精准解决了开发者（追求代码灵活性与版本控制）与非技术人员（追求可视化易用性）在构建 Agent 时的协作痛点；同时兼容 Vercel AI SDK、提供 React UI 库及 OTEL 可观测性，开箱即用且避免了厂商锁定，能显著降低企业内部落地 Agent 的门槛。

### 社区活跃度 (评分: 7.0/10)
HN 获得 79 个点赞与 49 条评论，互动比例良好，说明项目切中了社区关于 Agent 开发体验与低代码/代码协作的讨论热点；作为 YC W23 团队的 Show HN 帖，吸引了开发者对双向同步实现细节和开源协议的关注与交流，社区热度中等偏上。

## 项目链接
https://github.com/inkeep/agents
