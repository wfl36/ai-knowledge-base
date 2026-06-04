# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, MCP, 浏览器自动化, 开源, 发布  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 推出了一款开源的 MCP Server，将网页抓取、结构化提取及基于 Browser Use/OpenAI CUA/Claude Computer Use 的浏览器自动化能力整合，使 Cursor、Windsurf 等 AI 客户端能轻松联网执行复杂任务，为 AI Agent 开发者提供了高实用性的网络交互解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目基于 Anthropic 的 MCP 协议，整合了 Browser Use、OpenAI CUA 和 Claude Computer Use 等当前前沿的浏览器自动化 Agent 框架，并依托云端基础设施解决了验证码、代理和隐身浏览等技术痛点，具有较高的工程集成度和技术时效性。

### 实用性 (评分: 8.5/10)
对 AI 从业者和开发者极具实用价值，通过简单的命令即可让 Cursor、Windsurf 或 Claude Desktop 等客户端具备联网、网页抓取、结构化数据提取和复杂浏览器任务自动化能力，直接解决了 Agent 缺乏网络交互手段的痛点。

### 社区活跃度 (评分: 6.5/10)
获得了 63 个点赞和 26 条评论，在 Show HN 类项目中表现中等偏上。作者主动提及了 MCP 当前存在的安装体验和认证痛点，容易引发社区关于 MCP 生态现状及改进方向的讨论。

## 项目链接
https://github.com/hyperbrowserai/mcp
