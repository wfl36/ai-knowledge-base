# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 6.2  
**状态：** 正常  
**标签：** AI浏览器, 本地LLM, Agent, 隐私优先, 开源, YC, Show HN, MCP, Claude替代, 客户端架构  
**更新日期：** 2026-09-04  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一个由 YC S24 团队开发的开源、本地优先的 AI 浏览器，主打客户端 agent 循环以保障数据隐私，并新发布文件系统访问能力以对标 Claude Cowork。技术上通过自编译 Chromium + 独立二进制运行 gemini-cli 改造的 agent 循环，配合 Vercel AI SDK 适配器实现 BYOK/本地 LLM 支持，并提供 MCP server 和 n8n 式工作流。社区反馈中等偏上热度，体现 HN 对隐私优先 AI 工具的关注，但项目本质是工程整合而非技术突破，长期价值取决于产品打磨和差异化（Browser ACLs）的兑现。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
该项目在客户端执行 agent 循环的技术决策有一定深度，从 Chrome 扩展 service worker 架构迁移到独立二进制+自编译 Chromium 是务实的工程取舍；基于 gemini-cli 改造并通过适配器接入 Vercel AI SDK 体现了一定的工程整合能力。但核心技术栈仍是已有组件的拼装（Chromium + gemini-cli + 适配器），缺乏自研模型或突破性算法，技术壁垒主要在系统集成层面。

### 实用性 (评分: 6.0/10)
对从业者有一定参考价值：(1) 客户端 AI agent 架构对隐私敏感场景（企业、本地数据）有实际意义；(2) 与 Claude Cowork、MCP、n8n 等趋势紧密对齐，可作为本地优先 AI 浏览器赛道的参考实现；(3) 8.5K stars 和 100K 下载量说明已有早期用户验证。但作为 YC 早期项目，稳定性、生产可用性、文档完善度存疑，参考价值更多在产品思路而非可直接借鉴的成熟方案。

### 社区活跃度 (评分: 6.0/10)
88 points 和 35 条评论属于 Show HN 中等偏上热度，反映社区对本地 AI 浏览器、隐私优先 agent 这类话题保持持续关注。作者主动参与评论区互动、迭代发布（引用上一次 Show HN 链接），有助于提高讨论质量。评论数不算特别高，说明话题有一定兴趣但尚未形成广泛争议或深度技术讨论。

## 项目链接
https://github.com/browseros-ai/BrowserOS
