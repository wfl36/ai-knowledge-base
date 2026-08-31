# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 7.2  
**状态：** 正常  
**标签：** AI Browser, Agent, Privacy, Local LLM, Show HN, Open Source, MCP, YC  
**更新日期：** 2026-08-31  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一个 YC S24 出品的开源、隐私优先的 AI 浏览器，其核心差异化在于将 agent loop 完整运行在客户端（独立二进制 + 自定义 Chromium），从而原生支持本地文件系统访问而无需上传数据。项目借 Claude Cowork 发布的时机展示其架构优势，并扩展了 n8n 风格工作流、MCP server、浏览器级 ACL 等能力。技术上属于成熟工程集成而非原始创新，但对 AI Agent 架构选型（server vs client）具有清晰的参考意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目在架构决策上有清晰的技术深度：将 agent loop 从 Chrome extension service worker 迁移到独立二进制（基于自定义 Chromium 打包），并通过 adapter 实现 Gemini CLI 与 Vercel AI SDK 格式互译，属于工程上较为成熟的取舍。同时提出了浏览器级别的 ACL/Guardrail 概念（IAM for agents），具有系统性思考。但整体技术栈组合（Chromium fork + 本地 LLM + MCP server）并无本质性创新，更多是已有组件的集成与重新组合。

### 实用性 (评分: 7.5/10)
对从业者具有较高参考价值：客户端 agent 架构绕开了 server-side agent（如 Atlas、Comet）的隐私瓶颈，使本地文件/Shell 访问成为可能，这一架构对比对正在设计 AI Agent 产品的团队很有借鉴意义。MCP server 集成、n8n-like 工作流图等扩展方向也贴合当下 AI 工程化趋势。YC S24 背景加上 8.5K stars、100K+ downloads 的数据点，对评估 AI 浏览器赛道有数据参考价值。

### 社区活跃度 (评分: 7.0/10)
Show HN 获得 88 分与 35 条评论，属于中等偏上关注度。讨论热度反映出社区对 AI 浏览器+本地 Agent 方向的兴趣，以及对隐私优先架构的认同；但相比头部 AI 产品发布（动辄 500+ 分）仍有差距，讨论更多集中在产品反馈与使用体验层面，深度技术辩论有限。

## 项目链接
https://github.com/browseros-ai/BrowserOS
