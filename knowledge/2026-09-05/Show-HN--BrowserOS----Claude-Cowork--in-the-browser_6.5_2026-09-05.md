# Show HN: BrowserOS – "Claude Cowork" in the browser

**评分：** 6.5  
**状态：** 正常  
**标签：** AI浏览器, Agent, 开源, 隐私计算, Show HN, MCP, 客户端AI, YC项目  
**更新日期：** 2026-09-05  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Nithin and Nikhil, twin brothers building BrowserOS (YC S24). We&#x27;re an open-source, privacy-first alternative to the AI browsers from big labs.<p>The big differentiator: on BrowserOS you can use local LLMs or BYOK and run the agent entirely on the client side, so your company&#x2F;sensitive data stays on your machine!<p>Today we&#x27;re launching filesystem access... just like Claude Cowork, our browser agent can read files, write files, run shell commands! But honestly, we didn&#x27;t plan for this. It turns out the privacy decision we made 9 months ago accidentally positioned us for this moment.<p>The architectural bet we made 9 months ago: Unlike other AI browsers (ChatGPT Atlas, Perplexity Comet) where the agent loop runs server-side, we decided early on to run our agent entirely on your machine (client side).<p>But building everything on the client side wasn&#x27;t smooth. We initially built our agent loop inside a Chrome extension. But we kept hitting walls -- service worker being single thread JS; not having access to NodeJS libraries. So we made the hard decision 2 months ago to throw away everything and start from scratch.<p>In the new architecture, our agent loop sits in a standalone binary that we ship alongside our Chromium. And we use gemini-cli for the agent loop with some tweaks! We wrote a neat adapter to translate between Gemini format and Vercel AI SDK format. You can look at our entire codebase here: <a href="https:&#x2F;&#x2F;git.new&#x2F;browseros-agent" rel="nofollow">https:&#x2F;&#x2F;git.new&#x2F;browseros-agent</a><p>How we give browser access to filesystem: When Claude Cowork launched, we realized something: because Atlas and Comet run their agent loop server-side, there&#x27;s no good way for their agent to access your files without uploading them to the server first. But our agent was already local. Adding filesystem access meant just... opening the door (with your permissions ofc). Our agent can now read and write files just like Claude Code.<p>What you can actually do today:<p>a) Organize files in my desktop folder <a href="https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;NOZ7xjto6Uc</a><p>b) Open top 5 HN links, extract the details and write summary into a HTML file <a href="https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;uXvqs_TCmMQ</a><p>--- Where we are now
If you haven&#x27;t tried us since the last Show HN (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=44523409</a>), give us another shot. The new architecture unlocked a ton of new features, and we&#x27;ve grown to 8.5K GitHub stars and 100K+ downloads:<p>c) You can now build more reliable workflows using n8n-like graph <a href="https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;H_bFfWIevSY</a><p>d) You can also use BrowserOS as an MCP server in Cursor or Claude Code <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5nevh00lckM</a><p>We are very bullish on browser being the right platform for a Claude Cowork like agent. Browser is the most commonly used app by knowledge workers (emails, docs, spreadsheets, research, etc). And even Anthropic recognizes this -- for Claude Cowork, they have janky integration with browser via a chrome extension. But owning the entire stack allows us to build differentiated features that wouldn&#x27;t be possible otherwise. Ex:  Browser ACLs.<p>Agents can do dumb or destructive things, so we&#x27;re adding browser-level guardrails (think IAM for agents): &quot;role(agent): can never click buy&quot; or &quot;role(agent): read-only access on my bank&#x27;s homepage.&quot;<p>Curious to hear your take on this and the overall thesis.<p>We’ll be in the comments. Thanks for reading!<p>GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;browseros-ai&#x2F;BrowserOS</a><p>Download: <a href="https:&#x2F;&#x2F;browseros.com">https:&#x2F;&#x2F;browseros.com</a> (available for Mac, Windows, Linux!)

## 综合总结
BrowserOS是一个YC孵化的开源AI浏览器项目，主打隐私优先和客户端Agent架构（local LLM/BYOK），近期新增filesystem访问能力对标Anthropic的Claude Cowork。技术上通过将agent loop从Chrome扩展迁移到独立二进制+定制Chromium解决了服务worker单线程限制，并通过Gemini CLI+Vercel AI SDK适配层实现模型灵活性。作为AI Agent落地形态的参考案例有不错价值，但缺乏底层技术创新，且面对Atlas/Comet等大厂竞争时长期可持续性存疑。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目技术架构有一定深度：客户端Agent架构决策（绕过Chrome扩展的service worker单线程限制，转为基于独立二进制+Chromium的方案）、Gemini格式与Vercel AI SDK格式的适配层设计、以及Browser ACLs（agent级IAM）的安全沙箱思路，都体现了一定的工程取舍和技术判断力。但底层Agent loop直接基于gemini-cli改造，自研创新成分有限，更像是集成层面的差异化（隐私+本地化），而非底层模型或算法突破。

### 实用性 (评分: 6.0/10)
对从业者有中等参考价值：本地化Agent架构、客户端执行模式、MCP server支持、n8n-like graph工作流等设计点是AI Agent工程化落地的实际参考案例；隐私优先+B YOK的定位对企业用户有吸引力。但项目本身仍在早期阶段（8.5K stars），生产可用性和稳定性有待观察。作为开源参考实现对独立开发者和小团队价值较高。

### 社区活跃度 (评分: 7.0/10)
HN 88 points + 35 comments属于中等偏上的Show HN关注度，作为YC S24项目第二次Show HN能维持此热度说明产品迭代获得了社区认可。35条评论通常会围绕隐私声明的真实性、与其他AI浏览器（Atlas/Comet）的差异化、安全模型、以及YC项目常见的增长质疑展开讨论。讨论质量中等，更偏向产品反馈而非深度技术辩论。

## 项目链接
https://github.com/browseros-ai/BrowserOS
