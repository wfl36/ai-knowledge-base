# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** MCP, AI Agent, Web Scraping, Browser Automation, 发布  
**更新日期：** 2026-07-15  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了一款 MCP Server，旨在通过云端浏览器基础设施将 AI 代理与互联网连接。该项目集成了网页抓取、结构化数据提取、Bing 搜索以及基于 OpenAI CUA 和 Claude Computer Use 的浏览器自动化等七种工具，自动处理验证码与代理。开发者可通过简单命令将其接入 Cursor 和 Windsurf 等 IDE，为构建具备 Web 能力的 AI Agent 提供了便捷的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目基于 MCP 协议构建，核心在于将云端无头浏览器基础设施（处理验证码、代理等反爬机制）与多种前沿的浏览器自动化代理（如 OpenAI CUA、Claude Computer Use、Browser Use）及数据提取工具（Markdown 抓取、结构化 JSON 转换）进行深度整合。技术含金量主要体现在工程封装与最新 Agent 框架的对接上，底层依赖既有云浏览器服务，应用层集成特征明显。

### 实用性 (评分: 8.5/10)
对 AI 从业者尤其是 Agent 开发者和 IDE 用户具有极高的实用价值。它直接解决了大模型与 Agent 联网获取实时数据和处理复杂网页交互的痛点，通过简单的命令即可接入 Cursor、Windsurf 等主流开发环境，极大降低了构建具备 Web 能力的 AI 应用的门槛。

### 社区活跃度 (评分: 7.0/10)
获得 63 个点赞和 26 条评论，在特定开发者群体中引发了不错的关注与讨论。作者主动抛出 MCP 当前存在的痛点（如安装体验差、认证需硬编码）并寻求社区反馈，有效激发了关于 MCP 生态发展与改进方向的实质性交流。

## 项目链接
https://github.com/hyperbrowserai/mcp
