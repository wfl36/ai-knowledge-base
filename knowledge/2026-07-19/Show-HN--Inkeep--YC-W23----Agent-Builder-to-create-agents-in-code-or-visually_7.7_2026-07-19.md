# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 多智能体, 发布, 开源  
**更新日期：** 2026-07-19  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 AI Agent 构建平台，其核心亮点在于实现了代码（TypeScript SDK）与可视化拖拽编辑器之间的真正双向同步，打破了开发者与业务人员的协作壁垒。底层采用多智能体架构，并原生支持 MCP、A2A 等开放协议及 Vercel AI SDK，兼顾了无代码的易用性与代码开发的灵活性。该项目在 HN 上获得了较高的关注度与讨论，为当前 AI Agent 的工程化落地与团队协作提供了一种极具参考价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目实现了代码与可视化编辑器之间的双向同步，底层依赖统一的表示形式，并通过 CLI 结合 LLM 与 TypeScript 语法糖进行转换。架构上全面拥抱多智能体，并原生支持 MCP、A2A 等新兴开放协议，技术栈现代且具备良好的互操作性，但核心更偏向工程架构与协议整合，而非底层算法创新。

### 实用性 (评分: 8.5/10)
极大缓解了 AI Agent 开发中技术人员与业务人员协作的痛点。开发者可使用 TypeScript SDK 进行开发，非技术人员可通过可视化界面调整，两者通过 CLI 实现无缝衔接。同时提供丰富的集成接口（MCP、Vercel AI SDK、React UI 组件）和开箱即用的模板，对 AI 应用团队具有极高的实操参考价值。

### 社区活跃度 (评分: 7.5/10)
获得 79 个点赞和 49 条评论，在 Show HN 类项目中表现出较好的关注度。讨论焦点集中在双向同步的实现机制、与 LangGraph/OpenAI 等现有方案的对比、以及 MCP/A2A 协议的实用性，社区互动质量较高，反映了当前开发者对 Agent 开发工具链的强烈需求。

## 项目链接
https://github.com/inkeep/agents
