# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 7.0  
**状态：** 正常  
**标签：** AI浏览器, Agent, 本地化LLM, 隐私安全, MCP, 开源, Show HN, 发布, Claude Cowork竞品  
**更新日期：** 2026-09-03  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一个开源、隐私优先的 AI 浏览器，主打客户端 agent loop + 本地 LLM/BYOK 架构，区别于 ChatGPT Atlas/Perplexity Comet 的服务端方案。此次更新加入了 filesystem access（对标 Claude Cowork）、MCP server 集成、n8n-like 工作流编排和 Browser ACL 权限控制等功能。项目技术架构演进清晰，隐私定位契合当下市场需求，但核心依赖 gemini-cli，原创性技术突破有限。作为 YC S24 项目，社区热度中等，对关注 AI agent 隐私和本地化部署的从业者有参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目展示了清晰的技术架构演进：从 Chrome 扩展的 service worker 单线程限制，转向独立的 Chromium 配套二进制进程，将 agent loop 放在客户端运行。基于 gemini-cli 进行定制，编写了 Gemini 与 Vercel AI SDK 格式之间的 adapter 层，技术实现有实际深度。引入 MCP server 集成、n8n-like graph 工作流编排、Browser ACL 权限控制（IAM for agents）等概念，体现了对 agent 安全与可组合性的思考。但核心 agent 能力仍依赖第三方 (gemini-cli)，原创性技术突破有限。

### 实用性 (评分: 7.0/10)
对 AI 从业者有较高参考价值：本地化 LLM/BYOK + 客户端 agent loop 的隐私架构是当下 AI 浏览器赛道的差异化方案，对关心数据安全的团队有实际意义；filesystem access + browser agent 的组合打开了新的自动化场景；MCP server 能力使其可直接接入 Cursor/Claude Code 工作流；Browser ACL 的设计思路对构建企业级 agent 产品有借鉴价值。但项目仍处于早期 (8.5K stars, 100K downloads)，生产可用性有待验证。

### 社区活跃度 (评分: 6.5/10)
HN 88 points + 35 条评论属于中等偏上热度，作为 Show HN 帖表现尚可。创始团队亲自下场答疑（双胞胎兄弟），讨论质量应该不错。话题切中 AI 浏览器 + 隐私本地化 + Claude Cowork 类竞品对比等热点，天然吸引关注。但与同类高热度 Show HN (200+ points) 相比还有差距，社区讨论深度需结合评论内容判断。

## 项目链接
https://github.com/browseros-ai/BrowserOS
