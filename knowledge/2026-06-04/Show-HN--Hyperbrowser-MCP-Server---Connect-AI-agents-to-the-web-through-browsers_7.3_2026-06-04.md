# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** MCP, AI Agent, Web自动化, 开源, 发布  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 开源了其 MCP Server，通过云端浏览器基础设施将 AI 代理和 IDE 连接到互联网。项目集成了网页抓取、搜索及多种主流浏览器自动化工具（Browser Use, OpenAI/Clude CUA），自动处理验证码与代理，为 AI 从业者提供了高实用性的 Web 交互解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目基于 MCP 协议，整合了 Browser Use、OpenAI CUA 和 Claude Computer Use 等当前主流的浏览器自动化技术，并依托云端基础设施解决验证码和代理问题。技术整合度较高，但底层核心创新性相对有限，属于应用层面的优秀封装。

### 实用性 (评分: 8.5/10)
对 AI Agent 开发者和 IDE 用户具有极高的实用价值。通过提供开箱即用的网页抓取、结构化提取和自动化操作工具，直接解决了 Agent 连接互联网的核心痛点，显著降低了 Web 自动化的开发门槛。

### 社区活跃度 (评分: 6.5/10)
获得 63 个点赞和 26 条评论，在 Show HN 项目中表现出中等偏上的社区关注度。评论数表明开发者对 MCP 生态及 Web 交互方案有实际讨论需求，尤其是针对安装体验和认证痛点有较多互动。

## 项目链接
https://github.com/hyperbrowserai/mcp
