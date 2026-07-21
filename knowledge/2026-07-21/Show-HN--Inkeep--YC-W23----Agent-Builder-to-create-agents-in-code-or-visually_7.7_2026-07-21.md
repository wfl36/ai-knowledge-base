# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, DevTools, No-code, 发布, 开源  
**更新日期：** 2026-07-21  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 推出了一款 Agent Builder，核心亮点在于实现了代码（TypeScript）与可视化拖拽编辑器之间的真正双向同步（push/pull），使开发者与非技术人员能无缝协作。项目采用多智能体架构，原生支持 MCP、A2A 协议及 Vercel AI SDK，兼顾了无代码的易用性与代码开发的灵活性，为 AI Agent 的工程化落地与跨职能团队协作提供了高价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目实现了代码（TypeScript SDK）与可视化编辑器之间的真正双向同步，底层依赖共享表示层与 LLM+TS 语法糖进行桥接转换。架构上全面拥抱多智能体模式，并原生支持 MCP、A2A 等开放协议及 OTEL 可观测性，工程集成度高，但非底层算法层面的突破。

### 实用性 (评分: 8.5/10)
极大解决了开发者与非技术人员（如营销、销售）在 Agent 构建与维护上的协作痛点，兼顾了无代码的易用性与代码开发的灵活性。对 Vercel AI SDK、React UI 组件及主流 Agent 生态的兼容性良好，且提供开箱即用的业务模板，对 AI 工程师和产品团队的实操落地具有很高的参考价值。

### 社区活跃度 (评分: 7.5/10)
获得 79 个 points 和 49 条评论，在 Show HN 类项目中表现中上，说明社区对该方向有实质性兴趣。预计讨论焦点集中在双向同步的实际可行性、与 LangGraph/OpenAI 等竞品的差异对比以及 fair-code 许可证模式，互动质量较高。

## 项目链接
https://github.com/inkeep/agents
