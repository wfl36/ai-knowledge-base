# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 7.3  
**状态：** 正常  
**标签：** Show HN, AI Browser, Agent, 本地LLM, 隐私优先, MCP, 开源, YC项目  
**更新日期：** 2026-09-02  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS 是一个开源、隐私优先的 AI 浏览器项目，由 YC S24 团队打造。其核心差异化在于将 agent loop 完全运行在客户端（本地机器），支持本地 LLM 或 BYOK，避免数据上传到服务器。当前发布新增了文件系统访问能力，使其功能对标 Claude Code/Cowork。技术上经历了从 Chrome 扩展到独立二进制 + 自定义 Chromium 的重大架构重构。商业化思路包括 n8n 式的工作流图编辑、作为 MCP server 集成到 Cursor/Claude Code、以及浏览器级别的 agent 权限控制（agent IAM）。虽然不属于基础模型层面的突破，但在 AI agent 隐私架构和客户端部署方向上是有意义的工程实践。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在架构设计上具有较高技术含量：从最初的 Chrome 扩展方案因 service worker 单线程和缺乏 NodeJS 库访问而受限，到推倒重来采用独立二进制 + 自定义 Chromium 嵌入式方案，技术决策有清晰的演进逻辑。客户端运行 agent loop 的架构选择涉及浏览器内核定制、本地 LLM 推理集成、跨进程通信等复杂工程问题。使用 gemini-cli 作为 agent loop 核心并通过适配器层（Gemini format ↔ Vercel AI SDK format）解耦的设计也体现了不错的工程抽象能力。但整体技术深度属于工程整合层面，未涉及底层算法或模型创新。

### 实用性 (评分: 7.5/10)
对 AI 从业者具有较高参考价值：1）本地化 agent 架构解决了数据隐私这一核心痛点，对企业用户尤其敏感数据场景有实际意义；2）支持 BYOK 和本地 LLM 降低了使用门槛；3）MCP server 集成使其可作为 Cursor、Claude Code 等工具的能力扩展；4）浏览器级别的 ACL/guardrails（agent IAM）思路对 agent 安全落地有借鉴价值；5）文件系统访问能力使其能完成真实的工作流自动化任务。对正在构建 AI agent 产品的团队在隐私架构和客户端 agent 设计方面有启发意义。

### 社区活跃度 (评分: 7.0/10)
Show HN 帖子获得 88 points 和 35 条评论，社区关注度处于中等偏上水平。作为 YC S24 项目的第二次 Show HN（前次链接也有提及），社区已有一定认知基础（8.5K GitHub stars, 100K+ 下载量）。讨论质量预期较高，因为作者明确表示会在评论区互动，且项目涉及多个热点话题（AI browser、local agent、privacy、Claude Cowork 对标），容易激发 HN 用户的技术辩论。

## 项目链接
https://github.com/browseros-ai/BrowserOS
