# Show HN: A big tech dev experience for an open source CMS

**评分：** 6.7  
**状态：** 正常  
**标签：** 开源CMS, AI应用, 开发者体验, 发布  
**更新日期：** 2026-07-25  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re building an open-source CMS designed to help creators with every
part of the content production pipeline.<p>We&#x27;re showing our tiny first step: A tool designed to take in a Twitter username
and produce an &quot;identity card&quot; based on it. We expect to use an approach similar
to [Constitutional AI] with an explicit focus on repeatability, testability, and
verification of an &quot;identity card.&quot; We think this approach could be used to
create finetuning examples for training changes, or serve as inference time
insight for LLMs, or most likely a combination of the two.<p>The tooling we&#x27;re showing today is extremely simplistic (and the AI is frankly
bad) but this is intentional. We&#x27;re more focused on showing the dev experience
and community aspects. We&#x27;d like to make it easier to contribute to this project
than edit Wikipedia. Communities are frustrated with things like Wordpress,
Apache, and other open source foundations focusing on things other than
software. We have a lot of community ideas (governance via vote by jury is
perhaps the most interesting).<p>We&#x27;re a team of 5, and we&#x27;ve bounced around a few companies with each other.
We&#x27;re all professional creators (video + music) and we&#x27;re creating tooling for
ourselves first.<p>Previously, we did a startup called Vidpresso (YC W14) that was acquired by
Facebook in 2018. We all worked at Facebook for 5 years on creator tooling, and
have since left to start this thing.<p>After leaving FB, it was painful for us to leave the warm embrace of the
Facebook infra team where we had amazing tooling. Since then, we&#x27;ve pivoted a
bunch of times trying to figure out our &quot;real&quot; product. While we think we&#x27;ve
finally nailed it, the developer experience we built is one we think others
could benefit from.<p>Our tooling is designed so any developer can easily jump in and start
contributing. It&#x27;s an AI-first dev environment designed with a few key
principles in mind:<p>1. You should be able to discover any command you need to run without looking at
   docs.
2. To make a change, as much context as possible should be provided as close to
   the code as possible.
3. AIs are &quot;people too&quot;, in the sense that they benefit from focused context,
   and not being distracted by having to search deeply through multiple files or
   documentation to make changes.<p>We have a few non-traditional elements to our stack which we think are worth
exploring. [Isograph] helps us simplify our component usage with GraphQL.
[Replit] lets people use AI coding without needing to set up any additional
tooling. We&#x27;ve learned how to treat it like a junior developer, and think it
will be the best platform for AI-first open source projects going forward.
[Sapling] (and Git together) for version control. It might sound counter
intuitive, but we use Git to manage agent interactionsand we use Sapling to
manage &quot;purposeful&quot; commits.<p>My last [Show HN post in 2013] ended up helping me find my Vidpresso cofounder
so I have high hopes for this one. I&#x27;m excited to meet anyone, developers,
creators, or nice people in general, and start to work with them to make this
project work. I have good references of being a nice guy, and aim to keep that
going with this project.<p>The best way to work with us is [remix our Replit app] and [join our Discord].<p>Thanks for reading and checking us out! It&#x27;s super early, but we&#x27;re excited to
work with you!<p>[Constitutional AI]: <a href="https:&#x2F;&#x2F;www.anthropic.com&#x2F;research&#x2F;constitutional-ai-harmlessness-from-ai-feedback" rel="nofollow">https:&#x2F;&#x2F;www.anthropic.com&#x2F;research&#x2F;constitutional-ai-harmles...</a><p>[Isograph]: <a href="https:&#x2F;&#x2F;isograph.dev" rel="nofollow">https:&#x2F;&#x2F;isograph.dev</a><p>[Replit]: <a href="https:&#x2F;&#x2F;replit.com" rel="nofollow">https:&#x2F;&#x2F;replit.com</a><p>[Sapling]: <a href="https:&#x2F;&#x2F;sapling-scm.com" rel="nofollow">https:&#x2F;&#x2F;sapling-scm.com</a><p>[Show HN post in 2013]: <a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=6993981">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=6993981</a><p>[remix our Replit app]: <a href="https:&#x2F;&#x2F;replit.com&#x2F;t&#x2F;bolt-foundry&#x2F;repls&#x2F;Content-Foundry&#x2F;view#README.md" rel="nofollow">https:&#x2F;&#x2F;replit.com&#x2F;t&#x2F;bolt-foundry&#x2F;repls&#x2F;Content-Foundry&#x2F;view...</a><p>[join our Discord]: <a href="https:&#x2F;&#x2F;discord.gg&#x2F;TjQZfWjSQ7" rel="nofollow">https:&#x2F;&#x2F;discord.gg&#x2F;TjQZfWjSQ7</a>

## 综合总结
前 Facebook 团队开源的 AI 优先 CMS 项目，当前展示了基于 Twitter 生成身份卡的简易工具。项目核心亮点在于创新的技术栈组合与开发者体验设计：使用 Isograph、Replit 和 Sapling+Git 构建，强调为 AI 和人类提供聚焦上下文，利用 Replit 降低开源贡献门槛，并尝试用 Git 管理 Agent 交互。AI 能力尚处早期，重点在于探索全新的开源社区协作与 AI 辅助开发范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
项目采用非传统技术栈组合（Isograph、Replit、Sapling+Git），创新性地提出利用 Git 管理 AI Agent 交互、Sapling 管理目的性提交的工程实践。当前 AI 功能较为初级，但规划引入 Constitutional AI 提升生成的可测试性与可重复性，技术亮点集中在 AI 协同架构设计而非底层算法。

### 实用性 (评分: 7.0/10)
对 AI 应用开发者及开源项目维护者具有较高参考价值。项目提出的“AI优先开发环境”三大原则（免查文档发现命令、高内聚上下文、为AI提供聚焦上下文）以及利用 Replit 降低开源贡献门槛的思路，为构建 AI 辅助开发与协作流程提供了有益借鉴。

### 社区活跃度 (评分: 6.5/10)
作为早期 Show HN 项目获得 58 个点赞和 28 条评论，热度中等偏上。前 Facebook/YC 创业者的背景为项目带来了一定初始关注，社区对“开源社区治理（如陪审团投票机制）”和“大厂级开发者体验”等话题表现出探讨兴趣。

## 项目链接
https://contentfoundry.com/
