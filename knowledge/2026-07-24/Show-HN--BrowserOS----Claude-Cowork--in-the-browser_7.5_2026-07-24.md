# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, 浏览器, 开源项目, 隐私计算, 发布  
**更新日期：** 2026-07-24  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
YC S24 团队发布开源 AI 浏览器 BrowserOS，主打客户端运行 Agent 的隐私优先架构。项目经历了从 Chrome 扩展到伴生独立进程的彻底重构，解决了 Service Worker 限制，实现了类 Claude Cowork 的本地文件访问与 Shell 执行能力。项目还引入了 Browser ACLs 进行 Agent 权限管控，并支持作为 MCP Server 被其他工具调用，为浏览器级 AI Agent 的工程落地提供了极具参考价值的实践方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在架构上具有较高含金量，团队经历了从 Chrome 扩展（受限于 Service Worker 单线程和无 NodeJS 环境）到伴生独立二进制进程的架构重构，使用修改版的 gemini-cli 作为 Agent Loop 并编写了 Gemini 到 Vercel AI SDK 的适配器。本地运行 Agent 的架构使得其天然具备本地文件系统访问和 Shell 执行能力，同时创新性地提出了 Browser ACLs（类似 IAM 的浏览器级 Agent 权限控制），在工程实现和安全边界设计上展现了深度。

### 实用性 (评分: 8.0/10)
对 AI 从业者极具参考价值。其架构演进的踩坑经验（为何放弃扩展转向上层独立进程）为构建浏览器 Agent 的开发者提供了宝贵避坑指南；作为 MCP Server 集成到 Cursor/Claude Code 的思路，以及 n8n 式图形工作流和 Browser ACLs 权限管理设计，均为当前 Agent 应用落地提供了可直接借鉴的工程范式。

### 社区活跃度 (评分: 7.0/10)
获得 88 个 Points 和 35 条评论，在 Show HN 中属于中等偏上水平，表明该项目引起了社区的切实关注。本地隐私优先、客户端运行 Agent 以及与 Claude Cowork 的对比等话题，精准切中了当前 AI 社区对数据隐私和 Agent 控制权的痛点，引发了有质量的讨论。

## 项目链接
https://github.com/browseros-ai/BrowserOS
