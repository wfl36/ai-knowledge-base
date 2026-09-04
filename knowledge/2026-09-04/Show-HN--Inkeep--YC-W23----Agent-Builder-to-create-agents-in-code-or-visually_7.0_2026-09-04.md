# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.0  
**状态：** 正常  
**标签：** agent-builder, multi-agent, MCP, A2A, low-code, developer-tools, YC, Show HN, TypeScript, 可视化编程  
**更新日期：** 2026-09-04  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 是 YC W23 孵化的 Agent Builder 平台，核心卖点是可视化编辑器与 TypeScript 代码之间的双向同步（push/pull），并通过 MCP、A2A、Vercel AI SDK 兼容等开放协议实现互操作性。其多智能体架构设计面向复杂工作流，试图统一 no-code（如 n8n、Zapier）和 code-based（如 LangGraph、Mastra）两类的体验。技术整合度较高，但对从业者的吸引力取决于其生态成熟度与社区后续反馈。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目涉及多智能体架构（multi-agent architecture）、MCP 协议、Agent2Agent（A2A）协议、双向同步（visual ↔ code）的实现细节，以及底层用 LLM + TypeScript 语法糖桥接代码与可视化编辑器的方案。技术栈涵盖了 TS SDK、可观测性（OTEL logs、traces UI）、Vercel AI SDK 兼容性等多个维度，技术深度尚可，但缺乏对核心算法或模型创新的深入披露，更多是工程整合层面的技术。

### 实用性 (评分: 7.0/10)
对 AI 从业者有一定参考价值：双向 push/pull 工作流、MCP 端点暴露、与 Vercel AI SDK useChat 兼容、A2A 协议支持等都是实用特性，可降低团队协作（开发与非开发）构建 agent 的门槛。提供 customer_support、deep_research、docs_assistant 等模板，quickstart 上手较快。但作为 YC 项目，处于早期阶段，生态成熟度和稳定性尚待验证。

### 社区活跃度 (评分: 6.5/10)
Show HN 贴，获 79 分、49 条评论，社区关注度中等偏上。讨论热度表明 HN 用户对其双向同步概念、MCP/A2A 互操作性、以及与 LangGraph/Mastra/OpenAI 的差异化定位有兴趣，但不算爆款话题。从评论数与点赞比的比值看，讨论质量较好，有一定深度互动。

## 项目链接
https://github.com/inkeep/agents
