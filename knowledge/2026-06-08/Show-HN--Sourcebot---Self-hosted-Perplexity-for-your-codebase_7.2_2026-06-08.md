# Show HN: Sourcebot – Self-hosted Perplexity for your codebase

**评分：** 7.2  
**状态：** 正常  
**标签：** 代码理解, AI编程, 开发者工具, 发布, 开源  
**更新日期：** 2026-06-08  
**来源：** hackernews  

## 项目描述
Hi HN,<p>We’re Brendan and Michael, the creators of Sourcebot (<a href="https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;</a>), a self-hosted code understanding tool for large codebases. We originally launched on HN 9 months ago with code search (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032</a>), and we’re excited to share our newest feature: Ask Sourcebot.<p>Ask Sourcebot is an agentic search tool that lets you ask complex questions about your entire codebase in natural language, and returns a structured response with inline citations back to your code. Some types of questions you might ask:<p>- “How does authentication work in this codebase? What library is being used?  What providers can a user log in with?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11</a>)<p>- “When should I use channels vs. mutexes in go? Find real usages of both and include them in your answer” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w</a>)<p>- “How are shards laid out in memory in the Zoekt code search engine?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb</a>)<p>- &quot;How do I call C from Rust?&quot; (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k</a>)<p>You can try it yourself here on our demo site (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~</a>) or checkout our demo video (<a href="https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q</a>).<p>How is this any different from existing tools like Cursor or Claude code?<p>- Sourcebot solely focuses on <i>code understanding</i>. We believe that, more than ever, the main bottleneck development teams face is not writing code, it’s acquiring the necessary context to make quality changes that are cohesive within the wider codebase. This is true regardless if the author is a human or an LLM.<p>- As opposed to being in your IDE or terminal, Sourcebot is a web app. This allows us to play to the strengths of the web: rich UX and ubiquitous access. We put a ton of work into taking the best parts of IDEs (code navigation, file explorer, syntax highlighting) and packaging them with a custom UX (rich Markdown rendering, inline citations, @ mentions) that is easily shareable between team members.<p>- Sourcebot can maintain an up-to date index of thousands of repos hosted on GitHub, GitLab, Bitbucket, Gerrit, and other hosts. This allows you to ask questions about repositories without checking them out locally. This is especially helpful when ramping up on unfamiliar parts of the codebase or working with systems that are typically spread across multiple repositories, e.g., micro services.<p>- You can BYOK (Bring Your Own API Key) to any supported reasoning model. We currently support 11 different model providers (like Amazon Bedrock and Google Vertex), and plan to add more.<p>- Sourcebot is self-hosted, fair source, and free to use.<p>Under the hood, we expose our existing regular expression search, code navigation, and file reading APIs to a LLM as tool calls. We instruct the LLM via a system prompt to gather the necessary context via these tools to sufficiently answer the users question, and then to provide a concise, structured response. This includes inline citations, which are just structured data that the LLM can embed into it’s response and can then be identified on the client and rendered appropriately. We built this on some amazing libraries like the Vercel AI SDK v5, CodeMirror, react-markdown, and Slate.js, among others.<p>This architecture is intentionally simple. We decided not to introduce any additional techniques like vector embeddings, multi-agent graphs, etc. since we wanted to push the limits of what we could do with what we had on hand. We plan on revisiting our approach as we get user feedback on what works (and what doesn’t).<p>We are really excited about pushing the envelope of code understanding. Give it a try: <a href="https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot">https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot</a>. Cheers!

## 综合总结
Sourcebot 推出名为 "Ask Sourcebot" 的新功能，这是一个针对大型代码库的自托管 Agentic 搜索工具。用户可通过自然语言提问，系统利用 LLM 调用代码搜索和文件读取等工具，返回带有内联代码引用的结构化答案。与 Cursor 等工具不同，它专注于代码理解而非代码生成，采用 Web 应用形式支持跨数千个远程仓库的索引与共享，且架构上摒弃了向量嵌入和多智能体，仅依靠传统搜索 API 结合 LLM Tool Calling 实现简单高效的代码上下文获取。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
采用 LLM Tool Calling 架构，将正则搜索、代码导航和文件读取 API 作为工具暴露给大模型，指导其收集上下文并生成带内联引用的响应。架构设计刻意保持简单，未引入向量嵌入或多智能体图，是对传统代码搜索与 LLM 结合的工程实践。

### 实用性 (评分: 8.0/10)
对 AI 应用开发者及企业工程团队具有较高参考价值。提供了不依赖向量数据库的代码 RAG 替代方案，支持 BYOK 和自托管，解决了大型跨仓库代码库理解与上下文获取的痛点，适合作为内部代码知识库工具的参考。

### 社区活跃度 (评分: 7.0/10)
获得 103 个点赞和 29 条评论，在 Show HN 项目中表现良好。社区关注点集中在与 Cursor/Copilot 等现有工具的差异化、代码理解的准确性、以及不使用向量数据库的架构选择上，反映了开发者对实用型代码助手的兴趣。

## 项目链接
https://github.com/sourcebot-dev/sourcebot/releases/tag/v4.6.0
