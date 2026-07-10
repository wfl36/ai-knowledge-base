# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** MCP, AI Agent, 浏览器自动化, Web Scraping, 发布, 开源  
**更新日期：** 2026-07-10  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了开源的 MCP Server，旨在通过云端浏览器基础设施将 AI 代理（如 Cursor、Windsurf、Claude Desktop）连接到互联网。该服务器集成了网页抓取、爬取、结构化数据提取、搜索以及基于 Browser Use、OpenAI CUA 和 Claude 的三种浏览器自动化代理工具，自动处理验证码和代理。项目对 AI Agent 开发者具有很高的实用价值，解决了 LLM 联网操作的痛点，但在技术上属于应用层整合而非底层突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
基于 MCP 协议构建，整合了云浏览器基础设施与多种前沿的 LLM 浏览器代理技术（如 OpenAI CUA、Claude computer use），自动处理验证码与隐身浏览，技术栈现代，但核心在于工程整合而非底层算法创新。

### 实用性 (评分: 8.5/10)
极大地提升了 AI 从业者开发联网 Agent 的效率，提供开箱即用的命令行工具，覆盖数据抓取、网页自动化等高频场景，对使用 Cursor/Windsurf 等工具的开发者具有直接参考和使用价值。

### 社区活跃度 (评分: 6.5/10)
获得 63 个点赞和 26 条评论，在 Show HN 项目中表现中规中矩，社区关注点集中在 MCP 的安装认证体验及各类浏览器代理的实际效果上，作者也积极回应了当前 MCP 生态的痛点。

## 项目链接
https://github.com/hyperbrowserai/mcp
