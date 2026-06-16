# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** AI Agent, MCP, Web Automation, Browser, Show HN, 开源, 发布  
**更新日期：** 2026-06-16  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了一款开源的 MCP Server，旨在通过云端浏览器基础设施将 AI 代理和 IDE 连接到互联网。该服务器集成了网页抓取、结构化数据提取、搜索及多种浏览器自动化工具（支持 Browser Use、OpenAI CUA 和 Claude CUA），并自动处理验证码与代理。项目为开发者提供了开箱即用的 Web Agent 解决方案，显著降低了 Agent 联网操作的实现门槛。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目基于最新的 MCP (Model Context Protocol) 协议，整合了当前主流的浏览器自动化技术（Browser Use、OpenAI CUA、Claude CUA），并依托云端基础设施解决了验证码、代理和隐身浏览等工程痛点。技术栈前沿且具有较高的工程复杂度，但本质上是现有底层模型能力与协议的封装整合，底层算法级创新有限。

### 实用性 (评分: 8.5/10)
对 AI Agent 开发者和 IDE 插件开发者具有极高的实用价值。它直接解决了 Agent 联网获取数据和执行操作的痛点，提供开箱即用的7个核心工具，支持 Cursor、Windsurf、Claude Desktop 等主流客户端，极大降低了构建 Web Agent 的开发门槛，是连接 LLM 与互联网的高效基础设施。

### 社区活跃度 (评分: 6.5/10)
获得 63 个 Points 和 26 条评论，在 HN 上属于中等偏上的讨论热度。作为 Show HN 项目，成功吸引了开发者对 MCP 生态和 Web Agent 落地场景的关注，评论中可能涉及对 MCP 安装体验、认证痛点及实际应用效果的探讨，反映了社区对 Agent 联网工具的切实需求。

## 项目链接
https://github.com/hyperbrowserai/mcp
