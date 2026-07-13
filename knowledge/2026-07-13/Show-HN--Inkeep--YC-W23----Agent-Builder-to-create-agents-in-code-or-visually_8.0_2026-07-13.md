# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, AI Tooling, Release, Low-code  
**更新日期：** 2026-07-13  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep推出了一款Agent构建工具，实现了TypeScript SDK与可视化拖拽编辑器之间的真正双向同步，使开发者与非技术人员能在同一平台上无缝协作。该工具基于多智能体架构，支持MCP和A2A等开放协议，兼具代码框架的灵活性与无代码工具的易用性，为AI聊天助手和工作流的构建、部署及维护提供了高效实用的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程实现上具有较高技术含量，通过LLM与TypeScript语法糖实现了代码与可视化编辑器间的双向同步，解决了表示层转换的难题。底层采用多智能体架构，并原生支持MCP、A2A等现代AI开放协议，摆脱了传统的if/else硬编码工作流，展现了良好的架构灵活性与前沿协议跟进能力。

### 实用性 (评分: 9.0/10)
对AI从业者及开发团队具有极高的实用价值。它精准解决了开发者偏好代码控制与非技术人员偏好可视化操作之间的协作痛点。CLI的push/pull工作流、对Vercel AI SDK的兼容、开箱即用的模板以及可观测性支持，大幅降低了AI Agent的构建、交付与维护门槛。

### 社区活跃度 (评分: 7.5/10)
79个点赞和49条评论在Show HN类别中表现良好，反映出社区对AI开发工具链的持续关注。讨论焦点预计集中在代码与无代码双向同步的实际体验、多智能体架构的落地效果，以及与传统工作流引擎的对比，社区互动质量较高。

## 项目链接
https://github.com/inkeep/agents
