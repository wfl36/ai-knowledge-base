# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.3  
**状态：** 正常  
**标签：** AI Agent, MCP, Web Automation, Show HN, 开源  
**更新日期：** 2026-06-10  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser开源了其MCP Server，允许AI Agent通过云端浏览器基础设施连接互联网。该服务器集成了网页抓取、搜索及多种浏览器自动化Agent（支持OpenAI和Claude的CUA），可无缝接入Cursor、Windsurf等客户端。项目对构建具备Web交互能力的AI应用极具参考价值，同时也引发了社区对MCP安装与认证体验的深入讨论。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目基于MCP协议构建了连接AI Agent与Web的桥梁，整合了网页抓取、结构化提取、搜索对接以及多种主流浏览器自动化Agent（Browser Use、OpenAI CUA、Claude CUA）。底层依托云端浏览器基础设施解决验证码、代理和隐身浏览等反爬问题，技术实现偏向工程整合与应用层封装，而非底层算法创新。

### 实用性 (评分: 8.5/10)
对AI从业者和开发者具有极高的实用价值。通过提供开箱即用的MCP Server，极大降低了在Cursor、Windsurf等IDE或Claude桌面端中集成Web浏览与数据获取能力的门槛。支持一键启动（npx），直接解决了Agent需要实时网络信息、自动化操作网页的痛点，非常适合需要构建具备上网能力Agent的开发者直接使用或参考。

### 社区活跃度 (评分: 7.0/10)
获得63个点赞和26条评论，显示出社区对MCP生态及Agent上网工具的持续关注。讨论不仅围绕项目本身的功能，还延伸至MCP当前普遍存在的安装体验差、认证凭据硬编码等痛点，反映了开发者在实际集成MCP工具时的真实反馈与需求。

## 项目链接
https://github.com/hyperbrowserai/mcp
