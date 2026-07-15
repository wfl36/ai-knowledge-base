# Show HN: Sourcebot – Self-hosted Perplexity for your codebase

**评分：** 7.2  
**状态：** 正常  
**标签：** AI编程, 代码搜索, 开发工具, 发布, 开源  
**更新日期：** 2026-07-15  
**来源：** hackernews  

## 项目描述
Hi HN,<p>We’re Brendan and Michael, the creators of Sourcebot (<a href="https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.sourcebot.dev&#x2F;</a>), a self-hosted code understanding tool for large codebases. We originally launched on HN 9 months ago with code search (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=41711032</a>), and we’re excited to share our newest feature: Ask Sourcebot.<p>Ask Sourcebot is an agentic search tool that lets you ask complex questions about your entire codebase in natural language, and returns a structured response with inline citations back to your code. Some types of questions you might ask:<p>- “How does authentication work in this codebase? What library is being used?  What providers can a user log in with?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjkrbw000bnn7s8of2dm11</a>)<p>- “When should I use channels vs. mutexes in go? Find real usages of both and include them in your answer” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpiuqhu000bpg7s9hprio4w</a>)<p>- “How are shards laid out in memory in the Zoekt code search engine?” (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdm9nkck000bod7sqy7c1efb</a>)<p>- &quot;How do I call C from Rust?&quot; (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~&#x2F;chat&#x2F;cmdpjy06g000pnn7ssf4nk60k</a>)<p>You can try it yourself here on our demo site (<a href="https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~" rel="nofollow">https:&#x2F;&#x2F;demo.sourcebot.dev&#x2F;~</a>) or checkout our demo video (<a href="https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;olc2lyUeB-Q</a>).<p>How is this any different from existing tools like Cursor or Claude code?<p>- Sourcebot solely focuses on <i>code understanding</i>. We believe that, more than ever, the main bottleneck development teams face is not writing code, it’s acquiring the necessary context to make quality changes that are cohesive within the wider codebase. This is true regardless if the author is a human or an LLM.<p>- As opposed to being in your IDE or terminal, Sourcebot is a web app. This allows us to play to the strengths of the web: rich UX and ubiquitous access. We put a ton of work into taking the best parts of IDEs (code navigation, file explorer, syntax highlighting) and packaging them with a custom UX (rich Markdown rendering, inline citations, @ mentions) that is easily shareable between team members.<p>- Sourcebot can maintain an up-to date index of thousands of repos hosted on GitHub, GitLab, Bitbucket, Gerrit, and other hosts. This allows you to ask questions about repositories without checking them out locally. This is especially helpful when ramping up on unfamiliar parts of the codebase or working with systems that are typically spread across multiple repositories, e.g., micro services.<p>- You can BYOK (Bring Your Own API Key) to any supported reasoning model. We currently support 11 different model providers (like Amazon Bedrock and Google Vertex), and plan to add more.<p>- Sourcebot is self-hosted, fair source, and free to use.<p>Under the hood, we expose our existing regular expression search, code navigation, and file reading APIs to a LLM as tool calls. We instruct the LLM via a system prompt to gather the necessary context via these tools to sufficiently answer the users question, and then to provide a concise, structured response. This includes inline citations, which are just structured data that the LLM can embed into it’s response and can then be identified on the client and rendered appropriately. We built this on some amazing libraries like the Vercel AI SDK v5, CodeMirror, react-markdown, and Slate.js, among others.<p>This architecture is intentionally simple. We decided not to introduce any additional techniques like vector embeddings, multi-agent graphs, etc. since we wanted to push the limits of what we could do with what we had on hand. We plan on revisiting our approach as we get user feedback on what works (and what doesn’t).<p>We are really excited about pushing the envelope of code understanding. Give it a try: <a href="https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot">https:&#x2F;&#x2F;github.com&#x2F;sourcebot-dev&#x2F;sourcebot</a>. Cheers!

## 综合总结
Sourcebot 推出了 Ask Sourcebot 功能，打造自托管的“代码版Perplexity”。该工具专注于大型代码库的自然语言理解，通过Agent调用现有代码搜索与导航API，返回带内联引用的结构化答案。其架构简单实用，未采用向量数据库，但凭借支持多仓库索引、BYOK和Web端共享等特性，为开发者理解和梳理复杂代码库提供了高价值的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
项目在AI底层技术上并未追求前沿复杂度，明确表示未使用向量嵌入或多智能体图，而是采用相对简单直接的架构：将正则搜索、代码导航和文件读取API作为工具调用暴露给LLM，通过系统提示词引导LLM收集上下文并生成带内联引用的回答。技术含金量主要体现在工程实现与体验整合上，而非算法突破。

### 实用性 (评分: 8.5/10)
对AI开发者及软件工程师具有很高的实用价值。该工具精准切入了'大型代码库理解'这一痛点，区别于Cursor等侧重代码生成的工具，专注于提供跨仓库的上下文理解。支持自托管、BYOK（自带API密钥）、多代码托管平台索引及Web端共享，非常适合团队协作、微服务架构梳理和接手遗留代码的场景。

### 社区活跃度 (评分: 7.0/10)
在Hacker News上获得了103个点赞和29条评论，属于中等偏上的热度。作为Show HN项目，社区对'自托管的代码版Perplexity'概念表现出明确的兴趣，讨论主要围绕其与现有IDE内工具的差异、代码理解的准确性及实际应用场景展开，反馈质量较好。

## 项目链接
https://github.com/sourcebot-dev/sourcebot/releases/tag/v4.6.0
