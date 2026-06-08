# Show HN: Inkeep (YC W23) – Agent Builder to create agents in code or visually

**评分：** 7.7  
**状态：** 正常  
**标签：** AI Agent, 开发工具, 发布, 低代码  
**更新日期：** 2026-06-08  
**来源：** hackernews  

## 项目描述
Hi HN! I&#x27;m Nick from Inkeep. We built an agent builder with true 2-way sync between code and a drag-and-drop visual editor, so devs and non-devs can collaborate on the same agents. Here’s a demo video: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;video">https:&#x2F;&#x2F;go.inkeep.com&#x2F;video</a>.<p>As a developer, the flow is:
1) Build AI Chat Assistants or AI Workflows with the TypeScript SDK 2) Run `inkeep push` from your CLI to publish 3)Edit agents in the visual builder (or hand off to non-technical teams) 4) Run `inkeep pull to edit in code again.<p>We built this because we wanted the accessibility of no-code workflow builders (n8n, Zapier), but the flexibility and devex of code-based agent frameworks (LangGraph, Mastra). We also wanted first-class support for chat assistants with interactive UIs, not just workflows. OpenAI got close, but you can only do a one-time export from visual builder to code and there’s vendor lock-in.<p>How I&#x27;ve used it: I bootstrapped a few agents for our marketing and sales teams, then was able to hand off so they can maintain and create their own agents. This has enabled us to adopt agents across technical and non-technical roles in our company on a single platform.<p>To try it, here’s the quickstart: <a href="https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart">https:&#x2F;&#x2F;go.inkeep.com&#x2F;quickstart</a>.<p>We leaned on open protocols to make it easy to use agents anywhere:
An MCP endpoint, so agents can be used from Cursor&#x2F;Claude&#x2F;ChatGPT
A Chat UI library with interactive elements you can customize in React
An API endpoint compatible with the Vercel AI SDK `useChat` hook
Support for Agent2Agent (A2A) so they work with other agent ecosystems<p>We made some practical templates like a customer_support, deep_research, and docs_assistant. Deployment is easy with Vercel&#x2F;Docker with a fair-code license and there&#x27;s a traces UI and OTEL logs for observability.<p>Under the hood, we went all-in on a multi-agent architecture. Agents are made up of LLMs, MCPs, and agent-to-agent relationships. We’ve found this approach to be easier to maintain and more flexible than traditional “if&#x2F;else” approaches for complex workflows.<p>The interoperability works because the SDK and visual builder share a common underlying representation, and the Inkeep CLI bridges it with a mix of LLMs and TypeScript syntactic sugar. Details in our docs: <a href="https:&#x2F;&#x2F;docs.inkeep.com">https:&#x2F;&#x2F;docs.inkeep.com</a>.<p>We’re open to ideas and contributions! And would love to hear about your experience building agents - what works, hasn’t worked, what’s promising?

## 综合总结
Inkeep推出现代化Agent构建平台，核心创新在于实现了TypeScript代码与可视化拖拽编辑器之间的双向同步，打破了传统低代码平台与纯代码框架的壁垒，使技术与非技术团队能无缝协作。项目深度整合MCP、A2A等开放协议，采用多智能体架构，为AI Agent的企业级开发与跨团队协作提供了高实用性的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目在工程实现上具有较高含金量，核心亮点在于实现了代码与可视化编辑器之间的真正双向同步（2-way sync），这需要解决抽象语法树（AST）与可视化节点之间的复杂映射问题。底层采用多智能体架构，并紧跟当前主流开放协议（如MCP、A2A），支持Vercel AI SDK及OTEL可观测性，技术栈现代且实用，但并非底层算法层面的突破。

### 实用性 (评分: 8.5/10)
对AI从业者（尤其是AI应用开发者和工程师）极具参考价值。它有效解决了业界痛点：技术人员与非技术人员在Agent构建上的协作难题。开发者可以用TypeScript SDK保持灵活性，非技术人员可以通过可视化界面进行修改，且互不冲突。对希望引入低代码/无代码协作流程的团队有直接的落地指导意义。

### 社区活跃度 (评分: 7.5/10)
获得79个Points和49条评论，在Show HN类项目中表现中上，说明社区对该方向有较高关注度。讨论焦点预计集中在双向同步的技术实现细节、与LangGraph等主流框架的对比、以及MCP/A2A等新协议的实际体验上，反馈质量较高。

## 项目链接
https://github.com/inkeep/agents
