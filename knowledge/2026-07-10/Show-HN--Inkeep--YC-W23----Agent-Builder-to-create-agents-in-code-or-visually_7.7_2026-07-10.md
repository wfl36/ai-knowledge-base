# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, DevTools, 发布, 开源  
**更新日期：** 2026-07-10  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep推出了一款支持代码与可视化编辑器双向同步的Agent构建工具，旨在打破开发者与业务人员之间的协作壁垒。项目基于多智能体架构，原生支持MCP和A2A等开放协议，兼具代码级灵活性与无代码易用性，为企业级AI Agent的跨团队开发与落地提供了高价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程实现上具有较高含金量，特别是实现了代码与可视化编辑器之间的双向同步（基于LLM和TypeScript语法糖的底层统一表示）。底层采用多智能体架构，并原生支持MCP、A2A等开放协议，技术栈紧跟当前AI智能体生态前沿，但未涉及底层模型算法的突破。

### 实用性 (评分: 8.5/10)
对AI从业者和企业团队极具参考价值。它精准解决了当前Agent开发中“代码灵活性与无代码易用性不可兼得”的痛点，允许开发者与非技术人员在同一平台上协作。支持Vercel/Docker部署及主流AI SDK集成，提供了开箱即用的模板，能显著降低企业内部落地AI Agent的门槛。

### 社区活跃度 (评分: 7.0/10)
获得79个点赞和49条评论，在开发者工具类Show HN中表现良好。社区对“代码与可视化双向同步”及“多角色协作”的痛点共鸣强烈，讨论集中在与LangGraph/Zapier等现有方案的对比、双向同步的技术实现细节以及开源协议上，互动质量较高。

## 项目链接
https://github.com/inkeep/agents
