# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 6.3  
**状态：** 正常  
**标签：** AI浏览器, 本地LLM, Agent, 隐私优先, 开源, MCP, Show HN, YC项目, Claude Cowork  
**更新日期：** 2026-09-01  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一个开源、隐私优先的 AI 浏览器，主打本地 agent 执行（不依赖服务端），支持 BYOK/本地 LLM、文件系统访问、MCP server 集成等。其核心差异化在于 9 个月前押注客户端架构，恰逢 Claude Cowork 等产品兴起而凸显价值。本次新增文件系统访问能力，并展示了 n8n 式可视化工作流和浏览器级 ACL 等扩展。技术上有务实的工程决策（独立二进制 + 适配器层），但核心 AI 能力依赖第三方。在 AI 浏览器红海（Atlas、Comet）中定位差异化，但产品成熟度仍需时间验证。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
技术亮点在于客户端优先的架构决策：将 agent loop 从 Chrome extension 的 service worker 迁出到独立二进制进程，从而获得 NodeJS 生态和文件系统访问能力。使用 gemini-cli 作为 agent runtime 并通过适配器对接 Vercel AI SDK 是务实的工程选择。但核心 LLM 推理并非自研，技术深度受限于集成层。Browser ACLs/IAM 概念有一定新意，但缺乏具体实现细节。

### 实用性 (评分: 6.5/10)
对从业者而言，作为本地化 AI 浏览器方案的参考实现有一定价值，特别是隐私敏感场景（企业数据不外传）。MCP server 集成、本地 LLM 支持、文件系统访问等特性对构建类似产品的工程师有借鉴意义。但作为产品本身，与 Atlas/Comet 相比功能成熟度仍待验证，工作流可靠性（agent 在浏览器中的稳定性）需要实际使用才能评估。

### 社区活跃度 (评分: 6.0/10)
88 points 和 35 条评论属于中等热度水平。YC S24 背书 + Show HN 模式带来一定关注，但讨论量未达到爆款级别。8.5K GitHub stars 和 100K 下载量说明已有一定用户基础。作为浏览器 agent 赛道的开源选项，社区对其隐私优先定位和开放性会给予正面反馈，但也会就 agent 可靠性、安全边界等展开讨论。

## 项目链接
https://github.com/browseros-ai/BrowserOS
