# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 6.7  
**状态：** 正常  
**标签：** AI Agent, 低代码/可视化开发, 多智能体系统, MCP协议, 开发者工具, Show HN, YC项目, TypeScript SDK  
**更新日期：** 2026-08-31  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 是一个面向开发者的 AI Agent 构建平台，核心卖点是代码与可视化编辑器之间的双向同步，使技术团队和非技术团队能在同一平台上协作。其技术亮点在于统一底层表征支持多协议互操作（MCP、A2A、Vercel AI SDK），并采用多 Agent 架构替代传统 if/else 工作流。作为 YC 孵化的 Show HN 项目，它瞄准了 Agent 工程化落地的实际痛点，但创新更偏向工程整合而非底层突破，生态成熟度有待市场检验。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目展示了多智能体架构设计，核心亮点在于代码与可视化编辑器之间的双向同步机制（2-way sync），通过统一底层表征和 CLI 桥接实现。技术栈涉及 TypeScript SDK、MCP 协议、Agent2Agent 协议、OTEL 可观测性等，涉及 LLM 与语法树转换等工程实现。但帖子未深入探讨具体的算法创新或性能优化，技术深度中等，更多是工程集成层面的工作。

### 实用性 (评分: 7.0/10)
对 AI 从业者具有较高参考价值：解决了一个真实的痛点——开发者和非开发者协作构建 Agent 的问题。支持 MCP、A2A、Vercel AI SDK 等开放协议，避免供应商锁定，降低了集成成本。提供 TypeScript SDK + 可视化编辑器的双模开发体验，对中小团队快速落地 AI Agent 较为实用。提供客户支持、深度研究、文档助手等模板也提升了上手效率。但作为 YC W23 项目，生态成熟度和生产案例仍待验证。

### 社区活跃度 (评分: 6.5/10)
79 points 和 49 条评论属于中等偏上的 HN 关注度。Show HN 帖通常会吸引对工具感兴趣的开发者讨论。评论数与点数比例适中，表明用户参与讨论而非仅点赞。话题触及 AI Agent 工程化这一当前热门方向，但并未引发激烈的技术辩论或突破性讨论，社区反响属于稳健型。

## 项目链接
https://github.com/inkeep/agents
