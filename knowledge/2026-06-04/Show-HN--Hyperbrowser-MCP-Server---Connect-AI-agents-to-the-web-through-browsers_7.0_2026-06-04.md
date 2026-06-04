# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.0  
**状态：** 正常  
**标签：** AI Agent, MCP, Web Automation, Browser Use, Release, Open Source  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
项目基于MCP（模型上下文协议）构建，整合了Browser Use、OpenAI CUA和Claude Computer Use等现有浏览器自动化技术。技术核心在于云端浏览器基础设施的封装（自动处理验证码、代理和隐身浏览），属于工程集成与应用创新，而非底层算法或模型突破，整体技术深度中等。

### 实用性 (评分: 8.5/10)
对AI从业者（尤其是Agent开发者和Cursor/Windsurf/Claude Desktop用户）具有极高的实用价值。通过一条npx命令即可为LLM赋予联网、爬取和结构化提取能力，有效解决了Agent与Web交互的工程痛点，大幅降低了开发门槛并拓展了IDE的自动化场景。

### 社区活跃度 (评分: 6.5/10)
获得63个点赞和26条评论，在Show HN中属于中等偏上的关注度。社区讨论聚焦于MCP的实际应用场景、安装与认证UX的痛点，以及云端浏览器服务的稳定性，反馈质量较高且具有建设性，表明社区对Agent联网工具存在真实需求。

## 项目链接
https://github.com/hyperbrowserai/mcp
