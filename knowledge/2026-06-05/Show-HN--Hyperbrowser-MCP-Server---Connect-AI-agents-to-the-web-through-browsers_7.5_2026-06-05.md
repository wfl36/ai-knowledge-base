# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.5  
**状态：** 正常  
**标签：** AI Agent, MCP, 浏览器自动化, 网页抓取, 发布, 开源  
**更新日期：** 2026-06-05  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 推出了一款开源的 MCP Server，旨在通过云端浏览器基础设施将 AI Agent（如 Cursor、Windsurf、Claude Desktop）连接到互联网。该服务器集成了网页抓取、爬取、结构化数据提取以及基于 Browser Use、OpenAI CUA 和 Claude CUA 的浏览器自动化工具，自动处理验证码和代理。项目为开发者提供了开箱即用的 Agent 联网方案，引发了社区对 MCP 体验和 Agent 网络交互的积极讨论。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目基于最新的 MCP 协议，整合了 Browser Use、OpenAI CUA 和 Claude CUA 等前沿的浏览器自动化技术，并提供了从网页抓取、爬取到结构化数据提取的完整工具链。底层云浏览器基础设施解决了验证码、代理和隐身浏览等反爬技术难题，技术栈新颖且具有较高含金量。

### 实用性 (评分: 8.5/10)
对 AI Agent 开发者和 IDE 用户具有极高的实用价值。通过简单的 npx 命令即可将联网能力赋予 Cursor、Windsurf 或 Claude Desktop，直接解决了 Agent 缺乏实时网络信息和操作网页能力的痛点，开箱即用，大幅降低了构建联网 Agent 的门槛。

### 社区活跃度 (评分: 6.5/10)
获得 63 个点赞和 26 条评论，在 Show HN 类项目中表现中等偏上。社区讨论集中在 MCP 的安装与认证体验痛点、Agent 联网的实际效果以及不同浏览器自动化方案的对比上，反馈质量较高，反映了开发者对 Agent 联网基础设施的强烈需求。

## 项目链接
https://github.com/hyperbrowserai/mcp
