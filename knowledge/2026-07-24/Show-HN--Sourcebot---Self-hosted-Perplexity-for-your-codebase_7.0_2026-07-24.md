# Show HN: Sourcebot – Self-hosted Perplexity for your codebase

**评分：** 7.0  
**状态：** 正常  
**标签：** 代码理解, AI Agent, 开源项目, 发布, 自托管  
**更新日期：** 2026-07-24  
**来源：** hackernews  

## 项目描述
Hi HN,<p>We’re Brendan and Michael, the creators of Sourcebot (<a href="https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;</a>), a self-hosted code understanding tool for large codebases. We originally launched on HN 9 months ago with code search (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032</a>), and we’re excited to share our newest feature: Ask Sourcebot.<p>Ask Sourcebot is an agentic search tool that lets you ask complex questions about your entire codebase in natural language, and returns a structured response with inline citations back to your code. Some types of questions you might ask:<p>- “How does authentication work in this codebase? What library is being used?  What providers can a user log in with?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11</a>)<p>- “When should I use channels vs. mutexes in go? Find real usages of both and include them in your answer” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w</a>)<p>- “How are shards laid out in memory in the Zoekt code search engine?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb</a>)<p>- &quot;How do I call C from Rust?&quot; (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k</a>)<p>You can try it yourself here on our demo site (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~</a>) or checkout our demo video (<a href="https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q</a>).<p>How is this any different from existing tools like Cursor or Claude code?<p>- Sourcebot solely focuses on <i>code understanding</i>. We believe that, more than ever, the main bottleneck development teams face is not writing code, it’s acquiring the necessary context to make quality changes that are cohesive within the wider codebase. This is true regardless if the author is a human or an LLM.<p>- As opposed to being in your IDE or terminal, Sourcebot is a web app. This allows us to play to the strengths of the web: rich UX and ubiquitous access. We put a ton of work into taking the best parts of IDEs (code navigation, file explorer, syntax highlighting) and packaging them with a custom UX (rich Markdown rendering, inline citations, @ mentions) that is easily shareable between team members.<p>- Sourcebot can maintain an up-to date index of thousands of repos hosted on GitHub, GitLab, Bitbucket, Gerrit, and other hosts. This allows you to ask questions about repositories without checking them out locally. This is especially helpful when ramping up on unfamiliar parts of the codebase or working with systems that are typically spread across multiple repositories, e.g., micro services.<p>- You can BYOK (Bring Your Own API Key) to any supported reasoning model. We currently support 11 different model providers (like Amazon Bedrock and Google Vertex), and plan to add more.<p>- Sourcebot is self-hosted, fair source, and free to use.<p>Under the hood, we expose our existing regular expression search, code navigation, and file reading APIs to a LLM as tool calls. We instruct the LLM via a system prompt to gather the necessary context via these tools to sufficiently answer the users question, and then to provide a concise, structured response. This includes inline citations, which are just structured data that the LLM can embed into it’s response and can then be identified on the client and rendered appropriately. We built this on some amazing libraries like the Vercel AI SDK v5, CodeMirror, react-markdown, and Slate.js, among others.<p>This architecture is intentionally simple. We decided not to introduce any additional techniques like vector embeddings, multi-agent graphs, etc. since we wanted to push the limits of what we could do with what we had on hand. We plan on revisiting our approach as we get user feedback on what works (and what doesn’t).<p>We are really excited about pushing the envelope of code understanding. Give it a try: <a href="https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot">https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot</a>. Cheers!

## 综合总结
Sourcebot 是一个自托管的代码理解工具，其新功能 Ask Sourcebot 通过将代码搜索与阅读API作为工具调用暴露给LLM，实现了自然语言提问并返回带内联引用的结构化回答。项目架构简单实用，未采用向量检索，专注于解决大型和多仓库代码库的上下文获取痛点，支持BYOK和自托管，为AI代码理解应用提供了优秀的工程实践参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.5/10)
项目采用经典的LLM Tool-use架构，将代码正则搜索、导航和文件读取API封装为工具供LLM调用，以生成带内联引用的结构化回答。架构刻意保持简单，未引入向量数据库或复杂多智能体系统，技术深度偏向工程应用而非算法创新。

### 实用性 (评分: 8.5/10)
对AI应用开发者具有较好的架构参考价值（如何构建带引用的Agent）；对软件团队而言，解决了大型和多仓库代码库的理解痛点，支持跨平台索引、BYOK和自托管，兼顾了企业数据隐私与成本，实用性极高。

### 社区活跃度 (评分: 7.0/10)
HN获得103个点赞和29条评论，在Show HN项目中表现中上，说明社区对“自托管代码理解Agent”及“与Cursor等工具的差异化竞争”有较高兴趣和一定讨论度。

## 项目链接
https://github.com/sourcebot-dev/sourcebot/releases/tag/v4.6.0
