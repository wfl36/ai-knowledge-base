# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** AI Agent, Web Automation, MCP, Release, Open Source  
**更新日期：** 2026-07-18  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser发布了开源的MCP Server，旨在通过云浏览器基础设施将AI Agent与互联网连接。该工具提供7种核心功能（如网页抓取、结构化提取、基于OpenAI/Claude的浏览器自动化等），支持一键接入Cursor、Windsurf等客户端，并自动处理验证码与代理。项目虽非底层技术突破，但极大提升了Agent开发者的实操效率，是MCP生态中极具实用价值的工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目基于MCP（模型上下文协议）构建，集成了云浏览器基础设施与主流大模型（OpenAI CUA、Claude Computer Use、Browser Use），实现了网页抓取、结构化数据提取及自动化操作。技术层面更多是工程化集成与应用，解决了验证码、代理和反爬等实际问题，但在底层AI算法或架构上并无原创性突破。

### 实用性 (评分: 8.5/10)
对AI从业者尤其是Agent开发者具有极高的实用价值。通过一条命令即可让Cursor、Windsurf或Claude Desktop等客户端具备联网和操控浏览器的能力，极大降低了Agent获取实时网络信息及执行复杂网页任务的门槛，直击当前AI Agent落地中“连接真实网络”的痛点。

### 社区活跃度 (评分: 7.0/10)
获得63个点赞和26条评论，在Show HN类项目中表现中上，显示出社区对MCP生态及Agent联网工具的浓厚兴趣。评论中可能涉及对MCP安装体验、认证机制及实际自动化效果的探讨，反馈质量较高。

## 项目链接
https://github.com/hyperbrowserai/mcp
