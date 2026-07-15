# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 8.0  
**状态：** 正常  
**标签：** AI Agent, 浏览器, 开源, 隐私, 发布  
**更新日期：** 2026-07-15  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一款开源且隐私优先的 AI 浏览器（YC S24），核心差异在于 Agent Loop 完全在客户端本地运行，支持本地 LLM 和 BYOK，避免数据上传。项目经历了从 Chrome 扩展到独立 Chromium+本地二进制的底层架构重构，最新推出了文件系统与 Shell 访问功能，并引入 Browser ACLs 以限制 Agent 的危险操作。同时支持作为 MCP Server 接入 Cursor 等工具，为构建安全、可控的本地化浏览器 Agent 提供了完整的开源工程方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目展现了较高的系统重构与工程深度。团队放弃了受限于单线程 Service Worker 的 Chrome 扩展架构，转而采用独立 Chromium 搭配本地二进制程序的方案运行 Agent Loop。底层基于 gemini-cli 并开发了向 Vercel AI SDK 格式转换的适配器，实现了客户端本地闭环执行（含文件系统与 Shell 访问）。此外，创新性地提出了 Browser ACLs（浏览器访问控制列表），为 Agent 的破坏性操作设计了类似 IAM 的权限隔离机制。

### 实用性 (评分: 8.5/10)
对 AI 从业者极具实际参考价值。其客户端运行架构与 BYOK（自带密钥）模式直击企业数据隐私痛点；开源的 Agent Loop 实现及 MCP Server 支持为开发者构建本地化工作流和 IDE 集成提供了可直接复用的方案；Browser ACLs 的安全思路也为业内解决 Agent 可靠性问题提供了优秀实践范本。

### 社区活跃度 (评分: 7.5/10)
HN 获得 88 个点赞与 35 条评论，对于 Show HN 类项目表现良好，反映了社区对本地隐私优先架构及底层重构话题的探讨热情。GitHub 8.5K Star 和 10万+下载量也印证了项目在开发者群体中已具备较高的认可度和早期用户基础。

## 项目链接
https://github.com/browseros-ai/BrowserOS
