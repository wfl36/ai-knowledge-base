# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.2  
**状态：** 正常  
**标签：** Agent Framework, Multi-Agent, MCP, A2A, No-Code, TypeScript, YC, Show HN, 发布, 开发工具  
**更新日期：** 2026-09-06  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 是一个面向 Agent 构建的混合开发平台，核心卖点是代码与可视化编辑器之间的双向同步，让技术团队与非技术团队能在同一平台上协作维护 AI Agent。技术栈涵盖 TypeScript SDK、多智能体架构、MCP/A2A 协议集成和 OTEL 可观测性，定位介于 LangGraph 等代码框架与 n8n/Zapier 等无代码工具之间。作为 YC 孵化的产品，其开源策略和开放协议支持降低了对从业者的尝试门槛，但能否在已有成熟方案的 Agent 框架市场中突围，仍需观察实际生产环境中的表现和社区生态发展。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目涉及多智能体架构设计、TypeScript SDK 开发、代码与可视化编辑器的双向同步机制、CLI 工具实现以及与 MCP/A2A/Vercel AI SDK 等开放协议的集成，技术覆盖面较广。底层采用了 LLM + 语法糖的桥接方案来处理代码与可视化表示之间的转换，架构设计上有一定深度。但整体仍属于应用层工具整合，未涉及底层模型创新或前沿算法研究。

### 实用性 (评分: 7.0/10)
对 AI 从业者有明确价值：解决了代码框架（LangGraph/Mastra）与无代码工具（n8n/Zapier）之间的协作断层，支持开发者与非技术团队的协同工作流。MCP/A2A/OTEL 等标准化集成降低了接入成本，提供的模板（客服、深度研究、文档助手）可直接复用。适合需要快速搭建生产级 Agent 系统的中小团队，但对大型企业或已有成熟框架的用户吸引力有限。

### 社区活跃度 (评分: 7.0/10)
79 points 和 49 条评论属于 HN 中等偏上热度，作为 Show HN 帖获得了实质性讨论。评论数与点数比例（约 0.62）较高，说明社区不仅点赞还积极参与讨论。YC W23 背书和创始人的详细技术说明有助于引发高质量交流，但缺乏突破性话题的爆发力，讨论深度有待观察。

## 项目链接
https://github.com/inkeep/agents
