# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.2  
**状态：** 正常  
**标签：** MCP, AI Agent, Web Automation, Browser, 发布, 开源  
**更新日期：** 2026-06-08  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了一个开源的 MCP Server，旨在让 AI Agent 通过云端浏览器基础设施连接互联网。它集成了7个核心工具，涵盖网页抓取、结构化数据提取、搜索以及基于 Browser Use、OpenAI CUA 和 Claude CUA 的浏览器自动化操作。该项目自动处理验证码和代理，对 AI Agent 开发者具有较高实用价值，同时也反映了当前 MCP 生态中安装与认证体验的普遍痛点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目基于当前热门的 MCP（Model Context Protocol）协议构建，集成了网页抓取、结构化提取、搜索以及多种前沿的浏览器自动化技术（如 Browser Use、OpenAI CUA、Claude Computer Use）。底层依托云浏览器基础设施处理验证码、代理和隐身浏览，技术栈紧跟 AI Agent 发展趋势，但本质属于应用层的 API 封装与基础设施集成，缺乏底层算法或架构的突破性创新。

### 实用性 (评分: 8.5/10)
对 AI 从业者（尤其是 Agent 开发者和自动化工程师）具有极高的实用价值。项目开箱即用，直接打通了主流 IDE/客户端（Cursor、Windsurf、Claude Desktop）与互联网的交互链路，解决了 Agent 获取实时信息和操作网页的核心痛点。开发者也坦诚指出了当前 MCP 生态在安装 UX 和认证硬编码方面的痛点，引发了有价值的行业探讨。

### 社区活跃度 (评分: 6.5/10)
获得 63 个点赞和 26 条评论，在 Show HN 项目中属于中等偏上热度。社区关注点集中在 MCP 的实际应用体验、安装认证的痛点以及 Agent 浏览器自动化的可行性，讨论具有针对性和实操参考价值。

## 项目链接
https://github.com/hyperbrowserai/mcp
