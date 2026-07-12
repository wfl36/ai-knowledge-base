# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** MCP, Agent, Web-Automation, Browser, Show-HN, 开源, 发布  
**更新日期：** 2026-07-12  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser推出了开源的MCP Server，通过集成多种浏览器自动化工具（包括爬取、结构化提取及最新的Computer Use代理），使AI Agent和IDE能够便捷地接入互联网。该项目工程实用性强，为开发者提供了一键式的Agent联网解决方案，引发了社区对MCP生态及Agent交互模式的关注与讨论。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目基于新兴的MCP协议，整合了Browser Use、OpenAI CUA及Claude Computer Use等前沿浏览器自动化技术，并依托云端基础设施解决验证码与代理问题，技术栈新颖，但核心更偏向工程集成而非底层算法突破。

### 实用性 (评分: 8.5/10)
对AI开发者及从业者具有极高的实用价值，一键配置即可让Cursor、Windsurf或Claude Desktop等主流客户端具备联网、抓取与自动化操作网页的能力，直击Agent开发中信息获取与交互的痛点。

### 社区活跃度 (评分: 6.5/10)
获得63个点赞和26条评论，对于Show HN项目表现出中等偏上的关注度，评论互动率较高，社区对MCP生态的安装体验及Agent联网方案展开了实质性讨论。

## 项目链接
https://github.com/hyperbrowserai/mcp
