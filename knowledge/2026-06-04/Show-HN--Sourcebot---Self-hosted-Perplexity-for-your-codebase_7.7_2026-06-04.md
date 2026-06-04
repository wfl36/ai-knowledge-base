# Show HN: Sourcebot – Self-hosted Perplexity for your codebase

**评分：** 7.7  
**状态：** 正常  
**标签：** 代码理解, AI Agent, 开发工具, 发布  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hi HN,<p>We’re Brendan and Michael, the creators of Sourcebot (<a href="https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;</a>), a self-hosted code understanding tool for large codebases. We originally launched on HN 9 months ago with code search (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032</a>), and we’re excited to share our newest feature: Ask Sourcebot.<p>Ask Sourcebot is an agentic search tool that lets you ask complex questions about your entire codebase in natural language, and returns a structured response with inline citations back to your code. Some types of questions you might ask:<p>- “How does authentication work in this codebase? What library is being used?  What providers can a user log in with?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11</a>)<p>- “When should I use channels vs. mutexes in go? Find real usages of both and include them in your answer” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w</a>)<p>- “How are shards laid out in memory in the Zoekt code search engine?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb</a>)<p>- &quot;How do I call C from Rust?&quot; (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k</a>)<p>You can try it yourself here on our demo site (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~</a>) or checkout our demo video (<a href="https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q</a>).<p>How is this any different from existing tools like Cursor or Claude code?<p>- Sourcebot solely focuses on <i>code understanding</i>. We believe that, more than ever, the main bottleneck development teams face is not writing code, it’s acquiring the necessary context to make quality changes that are cohesive within the wider codebase. This is true regardless if the author is a human or an LLM.<p>- As opposed to being in your IDE or terminal, Sourcebot is a web app. This allows us to play to the strengths of the web: rich UX and ubiquitous access. We put a ton of work into taking the best parts of IDEs (code navigation, file explorer, syntax highlighting) and packaging them with a custom UX (rich Markdown rendering, inline citations, @ mentions) that is easily shareable between team members.<p>- Sourcebot can maintain an up-to date index of thousands of repos hosted on GitHub, GitLab, Bitbucket, Gerrit, and other hosts. This allows you to ask questions about repositories without checking them out locally. This is especially helpful when ramping up on unfamiliar parts of the codebase or working with systems that are typically spread across multiple repositories, e.g., micro services.<p>- You can BYOK (Bring Your Own API Key) to any supported reasoning model. We currently support 11 different model providers (like Amazon Bedrock and Google Vertex), and plan to add more.<p>- Sourcebot is self-hosted, fair source, and free to use.<p>Under the hood, we expose our existing regular expression search, code navigation, and file reading APIs to a LLM as tool calls. We instruct the LLM via a system prompt to gather the necessary context via these tools to sufficiently answer the users question, and then to provide a concise, structured response. This includes inline citations, which are just structured data that the LLM can embed into it’s response and can then be identified on the client and rendered appropriately. We built this on some amazing libraries like the Vercel AI SDK v5, CodeMirror, react-markdown, and Slate.js, among others.<p>This architecture is intentionally simple. We decided not to introduce any additional techniques like vector embeddings, multi-agent graphs, etc. since we wanted to push the limits of what we could do with what we had on hand. We plan on revisiting our approach as we get user feedback on what works (and what doesn’t).<p>We are really excited about pushing the envelope of code understanding. Give it a try: <a href="https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot">https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot</a>. Cheers!

## 综合总结
Sourcebot 推出了新功能 Ask Sourcebot，这是一个自托管的 Agentic 代码理解工具，允许用户用自然语言对大型/多仓库代码库提问并获取带引用的结构化回答。项目采用简洁的 Tool Call 架构，未使用向量检索，强调代码隐私与上下文获取，为开发团队提供了区别于 IDE 插件的 Web 端代码理解方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目采用 Agentic 架构，将正则搜索、代码导航和文件读取 API 暴露为 LLM 的 Tool calls，结合系统提示实现自然语言提问与带内联引用的结构化响应。架构设计务实且简洁，刻意未引入向量数据库或多智能体图，主要技术亮点在于工程整合与基于 Vercel AI SDK 等现代库的流畅实现。

### 实用性 (评分: 8.5/10)
对处理大型和多仓库（如微服务）代码库的开发团队极具实用价值。它聚焦于“代码理解”而非代码生成，解决了开发者获取上下文的痛点；支持自托管保障了代码隐私，BYOK 模式降低了使用成本；Web 端的形态也便于团队间分享上下文，是 Cursor 等 IDE 插件的良好补充。

### 社区活跃度 (评分: 7.5/10)
获得 103 个 Points 和 29 条评论，显示出 HN 社区对自托管、代码理解 AI 工具的浓厚兴趣。作为二次发布的项目，新功能的加入依然吸引了可观的关注，讨论焦点预计集中在与现有工具（如 Cursor、Perplexity）的对比及实际使用体验上。

## 项目链接
https://github.com/sourcebot-dev/sourcebot/releases/tag/v4.6.0
