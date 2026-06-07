# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agent, 低代码, 开发工具, 发布, 开源  
**更新日期：** 2026-06-07  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一个 AI Agent 构建器，核心亮点在于实现了 TypeScript 代码与可视化拖拽编辑器之间的双向同步，打破了开发者与非开发者之间的协作壁垒。该工具结合了无代码的易用性与代码框架的灵活性，原生支持 MCP、A2A 等开放协议及 Vercel AI SDK，底层采用多智能体架构，为企业级 Agent 的开发、维护与跨团队协作提供了极具实用价值的工程化解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程实现上具有较高含金量，核心难点在于实现代码与可视化编辑器之间的真正双向同步（2-way sync），这依赖于底层的统一表示以及 LLM 结合 TypeScript 语法糖的桥接技术。同时，底层采用多智能体架构替代传统的 if/else 逻辑，并原生支持 MCP、A2A 等前沿开放协议，展现了良好的技术前瞻性和架构设计能力，但本质上属于应用架构与工程化整合，非底层算法突破。

### 实用性 (评分: 9.0/10)
对 AI 从业者及开发团队极具实际参考价值。它精准击中了当前 Agent 开发中‘代码灵活性’与‘低代码易用性’难以兼得的痛点，实现了技术人员与非技术人员（如营销、销售）在同一平台上的无缝协作。对 Vercel AI SDK、React Chat UI、Docker 部署及 OTEL 可观测性的开箱即用支持，极大降低了企业内部落地 Agent 的工程门槛。

### 社区活跃度 (评分: 7.5/10)
获得 79 个点赞和 49 条评论，在 Hacker News 上属于中等偏上的热度。这表明社区对‘代码与低代码融合’及‘Agent 协作构建’的话题具有切实的兴趣和讨论需求，评论数反映出该工具触及了开发者在实际工作流中的痛点，引发了较好的互动与探讨。

## 项目链接
https://github.com/inkeep/agents
