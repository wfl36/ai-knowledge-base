# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 6.3  
**状态：** 正常  
**标签：** Agent Builder, Multi-Agent, TypeScript SDK, MCP, A2A, Show HN, YC W23, No-Code, 可视化编程  
**更新日期：** 2026-09-05  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 是一个 YC W23 孵化的智能体构建平台，核心卖点是 TypeScript 代码与可视化编辑器之间的双向同步，定位介于代码优先框架（LangGraph）和无代码工作流工具（n8n）之间。支持多智能体架构、MCP/A2A 协议、OpenTelemetry 可观测性，并提供开箱即用的客服、研究、文档助手模板。技术亮点在于统一底层表征实现双向同步，但在核心技术深度上属于工程整合而非范式创新。对中小团队的非技术协作场景有一定实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
讨论涉及多智能体架构设计、TypeScript SDK、MCP/A2A 协议集成、代码与可视化编辑器的双向同步机制等中等深度的技术内容。多智能体架构作为核心设计理念有一定讨论价值，但整体属于工程实现层面，缺乏算法或模型层面的创新性技术深度。

### 实用性 (评分: 7.0/10)
对 AI 从业者具有较高参考价值：双向代码/可视化同步解决了实际开发协作痛点；支持 MCP、A2A、Vercel AI SDK 等主流协议提升了互操作性；提供客服、深度研究、文档助手等实用模板降低了上手门槛；但作为开发者工具，定位偏向 no-code/low-code，与 LangGraph 等专业框架存在功能重叠。

### 社区活跃度 (评分: 5.5/10)
Show HN 帖子获得 79 points 和 49 条评论，互动活跃度中等偏上。作为 YC W23 项目展示，社区对其差异化定位（代码与可视化双向同步）表现出一定兴趣，但讨论热度未达到爆款级别，评论数量和质量处于常规 Show HN 水平。

## 项目链接
https://github.com/inkeep/agents
