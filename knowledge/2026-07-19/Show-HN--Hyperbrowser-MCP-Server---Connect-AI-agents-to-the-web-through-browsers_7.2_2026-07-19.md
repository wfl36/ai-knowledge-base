# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.2  
**状态：** 正常  
**标签：** AI Agent, Web Automation, MCP, 发布, 开源  
**更新日期：** 2026-07-19  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了其开源的 MCP Server，旨在通过云端浏览器基础设施将 AI 代理连接到互联网。该项目提供了 7 个核心工具，涵盖网页抓取、爬取、结构化数据提取、搜索以及基于 Browser Use、OpenAI CUA 和 Claude Computer Use 的自动化代理，能够自动处理验证码和代理。项目可一键接入 Cursor 等主流 IDE 和客户端，为 AI 从业者构建 Web 交互 Agent 提供了高实用性的解决方案，并开放寻求关于 MCP 安装体验等问题的社区反馈。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
项目主要侧重于工程集成与封装，将现有的浏览器自动化框架（如 Browser Use、OpenAI CUA、Claude Computer Use）与 Anthropic 的 MCP 协议相结合，底层依赖云端浏览器基础设施处理反爬（验证码、代理等），技术深度属于应用层面的组合创新，而非底层算法或架构突破。

### 实用性 (评分: 8.5/10)
对 AI Agent 开发者具有极高的实用价值，开箱即用的工具集解决了 LLM 联网和 Web 自动化的核心痛点（如反爬、结构化数据提取），且能无缝接入 Cursor、Windsurf、Claude Desktop 等主流开发环境与客户端，大幅降低了构建 Web 交互 Agent 的门槛。

### 社区活跃度 (评分: 7.0/10)
获得 63 个点赞和 26 条评论，在 Show HN 项目中表现中等偏上，说明开发者社区对 MCP 生态扩展及 Web Agent 的实用性保持较高关注，讨论预计集中在反爬效果、与竞品对比及 MCP 当前安装与认证体验的痛点上。

## 项目链接
https://github.com/hyperbrowserai/mcp
