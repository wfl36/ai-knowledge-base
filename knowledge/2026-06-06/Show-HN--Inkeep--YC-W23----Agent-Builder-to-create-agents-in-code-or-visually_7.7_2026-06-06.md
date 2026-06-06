# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 可视化编程, Show HN, 开源  
**更新日期：** 2026-06-06  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep (YC W23) 发布了一个AI Agent Builder，其核心创新在于实现了代码与可视化拖拽编辑器之间的真正双向同步（2-way sync），允许开发者与非技术人员在同一Agent上无缝协作。底层采用多Agent架构，全面支持MCP、A2A等开放协议，兼容Vercel AI SDK与React UI。该项目试图结合No-code的易用性与Code-based的灵活性，有效解决了企业内部跨职能团队构建与维护Agent的痛点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程实现上具有较高的技术含金量，核心亮点是代码与可视化编辑器之间的双向同步（底层共享统一表示，CLI通过LLM与TypeScript语法糖进行桥接转换）。底层架构全面拥抱多Agent设计及新兴开放协议（MCP、A2A），并集成了OTEL可观测性。虽非基础模型层面的算法突破，但在AI应用编排与AST/IR双向转换的工程挑战上展现了较深的技术深度。

### 实用性 (评分: 8.5/10)
对AI从业者及团队极具实际参考与应用价值。直击当前Agent开发中‘开发者需代码灵活性，非开发者需可视化易用性’的协作痛点，实现了跨职能（Dev与Marketing/Sales等）的无缝交接。同时，对Vercel AI SDK、React Chat UI及主流协议的兼容，极大降低了集成门槛，为企业级Agent的构建、部署与迭代提供了开箱即用的解决方案。

### 社区活跃度 (评分: 7.0/10)
79个Points与49条评论构成了中等偏上的社区热度，且互动率（评论/点赞比）较高。作为Show HN项目，引发了社区对双向同步可行性、Fair-code许可证、以及与LangGraph/Mastra等现有框架差异的实质性探讨，反映了当前AI开发者对Agent编排工具与协作模式的强烈关注。

## 项目链接
https://github.com/inkeep/agents
