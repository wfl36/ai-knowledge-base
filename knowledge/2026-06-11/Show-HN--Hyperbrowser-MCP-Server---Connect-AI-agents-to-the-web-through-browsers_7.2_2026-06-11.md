# Show HN: Hyperbrowser MCP Server – Connect AI agents to the web through browsers

**评分：** 7.2  
**状态：** 正常  
**标签：** MCP, Browser-Automation, AI-Agent, Web-Scraping, 发布  
**更新日期：** 2026-06-11  
**来源：** hackernews  

## 项目描述
Hi HN! Excited to share our MCP Server at Hyperbrowser - something we’ve been working on for a few days. We think it’s a pretty neat way to connect LLMs and IDEs like Cursor &#x2F; Windsurf to the internet.<p>Our MCP server exposes seven tools for data collection and browsing:<p>1. `scrape_webpage` - Extract formatted (markdown, screenshot etc) content from any webpage<p>2. `crawl_webpages` - Navigate through multiple linked pages and extract LLM-friendly formatted content<p>3. `extract_structured_data` - Convert messy HTML into structured JSON<p>4. `search_with_bing` - Query the web and get results with Bing search<p>5. `browser_use_agent` - Fast, lightweight browser automation with the Browser Use agent<p>6. `openai_computer_use_agent` - General-purpose automation using OpenAI’s CUA model<p>7. `claude_computer_use_agent` - Complex browser tasks using Claude computer use<p>You can connect the server to Cursor, Windsurf, Claude desktop, and any other MCP clients with this command `npx -y hyperbrowser-mcp` and a Hyperbrowser API key. We&#x27;re running this on our cloud browser infrastructure that we&#x27;ve been developing for the past few months – it handles captchas, proxies, and stealth browsing automatically.<p>Some fun things you can do with it: (1) deep research with claude desktop, (2) summarizing the latest HN posts, (3) creating full applications from short gists in Cursor, (3) automating code review in cursor, (4) generating llms.txt for any website with windsurf, (5) ordering sushi from windsurf (admittedly, this is just for fun - probably not actually going to do this myself).<p>We&#x27;re building this server in the open and would love feedback from anyone building agents or working with web automation. If you find bugs or have feature requests, please let us know! One big issue with MCPs in general is that the installation UX sucks and auth credentials have to be hardcoded. We don’t have a solution to this right now but Anthropic seems to be working on something here so excited for that to come out. Love to hear any other complaints &#x2F; thoughts you have about the server itself, Hyperbrowser, or the installation experience.<p>You can check us out at <a href="https:&#x2F;&#x2F;hyperbrowser.ai">https:&#x2F;&#x2F;hyperbrowser.ai</a> or check out the source code at <a href="https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;hyperbrowserai&#x2F;mcp</a>

## 综合总结
Hyperbrowser发布了一款开源的MCP Server，旨在通过云端浏览器基础设施将AI Agent与IDE（如Cursor、Windsurf、Claude Desktop）无缝连接到互联网。该项目集成了7种工具，涵盖网页抓取、结构化数据提取、搜索引擎对接以及基于OpenAI CUA和Claude CUA的浏览器自动化操作，并自动处理验证码与代理。虽然技术上属于应用层封装，但极大降低了开发者构建具备Web访问与操作能力Agent的门槛，对AI从业者具有很高的实用参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目基于MCP（Model Context Protocol）协议构建，整合了Browser Use、OpenAI CUA和Claude CUA等现有的浏览器自动化与计算机使用模型，技术本质偏向于基础设施与API封装，而非底层AI算法的创新，但在工程实现上解决了云端浏览器代理、验证码处理和隐身浏览等复杂问题。

### 实用性 (评分: 8.5/10)
对AI应用开发者和Agent构建者具有极高的实用价值。通过一条命令即可将Cursor、Windsurf或Claude Desktop等客户端接入互联网，提供从网页抓取、结构化数据提取到复杂浏览器任务自动化的全套工具，极大降低了Agent获取外部网络信息与执行Web操作的门槛。

### 社区活跃度 (评分: 6.5/10)
获得了63个点赞和26条评论，对于一款开发者工具的Show HN而言属于中等偏上的关注度。讨论焦点预计集中在MCP的安装与鉴权体验痛点、云端浏览器的稳定性以及Agent实际执行Web任务的可靠性上，反映了社区对AI Agent基础设施的浓厚兴趣。

## 项目链接
https://github.com/hyperbrowserai/mcp
