# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.2  
**状态：** 正常  
**标签：** Agent Builder, 多智能体, MCP, TypeScript SDK, 可视化编程, Show HN, YC, 无代码/低代码, Agent2Agent, 可观测性  
**更新日期：** 2026-09-02  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep 是 YC W23 孵化的 agent builder 平台，核心卖点是可视化编辑器与 TypeScript 代码之间的双向同步，让开发者和非技术团队在同一平台上协作构建 AI agents 和工作流。产品采用多智能体架构，原生支持 MCP、A2A、Vercel AI SDK 等开放协议，定位介于 LangGraph/Mastra（代码框架）与 n8n/Zapier（无代码工具）之间。技术整合有亮点但缺乏深度披露，对正在选型 agent 框架或需要跨职能协作的团队有实用价值，社区关注度中等偏上。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目在技术架构上有一定深度：采用多智能体架构（multi-agent），智能体由 LLM、MCP 和 agent-to-agent 关系组成；实现了可视化编辑器与代码之间的双向同步（two-way sync），底层通过共享表示 + CLI 桥接（结合 LLM 与 TypeScript 语法糖）实现同步机制。集成方面支持 MCP 端点、Agent2Agent (A2A) 协议、Vercel AI SDK 兼容 API，并提供 OTEL 可观测性。但技术细节披露有限，未深入说明多智能体协作、状态管理、context 传递等核心机制，技术新颖性属于工程整合层面而非底层突破。

### 实用性 (评分: 7.5/10)
对 AI 从业者具有较高参考价值：解决了实际痛点——代码框架（LangGraph、Mastra）与无代码工作流工具（n8n、Zapier）之间的鸿沟，让开发者与非技术团队可在同一平台协作。TypeScript SDK + CLI push/pull 流程清晰，附带 customer_support、deep_research、docs_assistant 等实用模板，部署支持 Vercel/Docker，且采用 fair-code 许可证。对正在评估 agent 框架、构建内部 agent 平台、或需要技术与业务团队协作的团队有直接借鉴意义。

### 社区活跃度 (评分: 7.0/10)
79 个 points 和 49 条评论属于中等偏上的 HN 关注度。作为 YC W23 的 Show HN，发布内容结构完整（痛点、方案、使用流程、协议支持、贡献邀请），容易引发讨论。评论数与点数的比例（约 0.62）表明讨论参与度较高，社区对 agent builder 赛道和无代码/代码协作模式有兴趣，但未达到现象级热度（如破百评论或高票 trending），属于稳步获得关注的 Show HN 类型。

## 项目链接
https://github.com/inkeep/agents
