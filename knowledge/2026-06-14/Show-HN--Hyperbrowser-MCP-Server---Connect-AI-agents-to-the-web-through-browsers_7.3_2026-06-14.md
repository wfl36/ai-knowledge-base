# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** AI Agent, Web Automation, MCP, Show HN, 开源  
**更新日期：** 2026-06-14  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser 发布了开源的 MCP Server，旨在通过其云浏览器基础设施将 AI Agent（如 Claude、Cursor 等）连接到互联网。该项目集成了7个核心工具，涵盖网页抓取、结构化数据提取、搜索及基于 OpenAI CUA 和 Claude Computer Use 的浏览器自动化操作，并自动处理验证码与代理。项目极大降低了 Agent 联网与网页交互的开发门槛，对从业者具有高实用价值，作者也坦诚当前 MCP 安装与认证体验仍存在痛点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目基于最新的 MCP (Model Context Protocol) 协议构建，并集成了当前前沿的 Browser Use、OpenAI CUA 和 Claude Computer Use 等浏览器自动化 Agent 模型。底层依托云浏览器基础设施处理反爬、代理和验证码，具备一定的工程门槛和架构设计，但核心属于应用层面的封装与集成创新，而非底层算法或理论突破。

### 实用性 (评分: 8.5/10)
对 AI Agent 开发者和自动化工程师具有极高的实用价值。直接解决了 Agent 联网获取数据与执行网页操作的核心痛点，通过一行命令即可无缝接入 Cursor、Windsurf、Claude Desktop 等主流客户端，大幅降低了开发门槛。提供的结构化提取、深度研究、代码审查等场景直击从业者日常需求。

### 社区活跃度 (评分: 6.5/10)
获得 63 个 Points 和 26 条评论，对于 Show HN 类项目属于中等偏上水平。26 条评论表明社区不仅有关注度，且产生了实质性的讨论互动（可能围绕 MCP 安装体验、认证痛点、Agent 执行效果等），但整体热度尚未达到引发广泛轰动的话题级别。

## 项目链接
https://github.com/hyperbrowserai/mcp
