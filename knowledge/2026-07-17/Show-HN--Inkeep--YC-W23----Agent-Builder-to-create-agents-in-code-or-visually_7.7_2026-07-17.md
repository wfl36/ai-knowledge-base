# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 可视化编程, 发布, 开源  
**更新日期：** 2026-07-17  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent 构建平台，核心创新在于实现了 TypeScript 代码与可视化拖拽编辑器之间的真正双向同步，使开发者与业务人员能在同一平台协作构建和维护 Agent。项目底层采用多智能体架构，原生支持 MCP 与 A2A 协议，兼容 Vercel AI SDK 等主流生态，以 fair-code 许可证开源，有效解决了当前 Agent 开发中灵活性与易用性难以兼顾的痛点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程实现上具有较高含金量，核心亮点在于代码与可视化编辑器之间的双向同步（基于共享底层表示与 LLM/TS 语法糖桥接），解决了传统低代码与纯代码割裂的痛点。底层采用多智能体架构替代硬编码 if/else 逻辑，并紧跟前沿支持 MCP 与 A2A 协议，技术栈现代，但本质属于应用层与工程化创新，非底层模型或算法突破。

### 实用性 (评分: 8.5/10)
对 AI 从业者及企业级开发团队极具参考价值。它直击开发者与业务/非技术人员协作构建 Agent 的痛点，支持 CLI push/pull 工作流无缝衔接。同时提供与 Vercel AI SDK、Cursor/Claude 等生态的深度集成及现成模板，大幅降低了企业内部跨职能推广与维护 Agent 的门槛，实操性极强。

### 社区活跃度 (评分: 7.0/10)
获得 79 个 Points 和 49 条评论，在 HN 属于中等偏上的关注度。作为 YC W23 项目的 Show HN，引发了关于双向同步实现难度、与 LangGraph/OpenAI 现有方案的对比、以及 fair-code 许可证限制等实质性讨论，互动质量较高，反映了社区对 Agent 开发工作流优化的浓厚兴趣。

## 项目链接
https://github.com/inkeep/agents
