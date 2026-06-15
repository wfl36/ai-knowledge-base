# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** MCP, AI Agent, 浏览器自动化, 开源, 发布  
**更新日期：** 2026-06-15  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了开源的 MCP Server，允许 AI Agent 通过云端浏览器基础设施连接互联网。该工具集成了网页抓取、搜索及 OpenAI/Claude 计算机使用代理等七大功能，支持一键接入 Cursor 等主流 IDE，为开发者构建联网 AI Agent 提供了极具实用价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目基于 MCP 协议，整合了 Browser Use、OpenAI CUA 和 Claude CUA 等前沿 Agent 浏览器交互技术，并依托云浏览器基础设施处理验证码与代理，技术栈紧跟当前 AI Agent 生态，属于优秀的工程封装与前沿技术整合。

### 实用性 (评分: 8.5/10)
对 AI 从业者和 Agent 开发者具有极高的实用价值。通过提供一键接入的 MCP Server，解决了 LLM 联网与网页交互的痛点，支持在 Cursor、Windsurf 等主流 IDE 中直接调用爬取、搜索及自动化操作，大幅降低 Agent 联网开发门槛。

### 社区活跃度 (评分: 6.5/10)
获得 63 个点赞和 26 条评论，在细分开发者社区中引起了一定关注。作者积极求反馈并坦诚讨论 MCP 安装体验的痛点，讨论质量较高，但整体热度属于中等水平。

## 项目链接
https://github.com/hyperbrowserai/mcp
