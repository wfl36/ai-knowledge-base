# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agent, 浏览器, 隐私计算, 发布, 开源  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一个开源、隐私优先的 AI 浏览器，核心差异化在于 Agent 循环完全在客户端本地运行，支持本地 LLM 或 BYOK。项目经历了从 Chrome 扩展到独立二进制文件的架构重构，从而顺畅实现了类似 Claude Cowork 的本地文件系统访问能力。此外，它还支持类 n8n 的工作流编排、作为 MCP Server 被其他工具调用，并创新性地提出了 Browser ACLs 以限制 Agent 的危险操作，为知识工作者提供了安全可靠的浏览器自动化方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目在工程架构上具有较高含金量，详细分享了从 Chrome 扩展（受限于 Service Worker 单线程和无 NodeJS 环境）向独立二进制文件+Chromium 底层架构迁移的演进过程。技术栈融合了 gemini-cli 与 Vercel AI SDK，实现了客户端 Agent Loop，并引入 MCP 协议支持及创新的 Browser ACLs（类 IAM 的 Agent 权限控制），展现了深度的系统级浏览器改造与 Agent 工程实践。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具参考价值。项目直击当前 AI 浏览器 Agent 的痛点：数据隐私与本地文件系统交互。其架构选型经验（扩展 vs 独立二进制）、MCP Server 的集成方式以及 Browser ACLs 的权限护栏设计，为开发企业级、高安全要求的 Agent 应用提供了成熟的落地思路和开源参考实现。

### 社区活跃度 (评分: 7.5/10)
作为 YC S24 项目的 Show HN 帖，获得了 88 个点赞和 35 条评论，在同类发布中表现中上。话题切中了本地化 Agent、隐私保护及 Claude Cowork 对标等热点，引发了社区对其架构选择和产品定位的探讨，关注度与讨论质量良好。

## 项目链接
https://github.com/browseros-ai/BrowserOS
