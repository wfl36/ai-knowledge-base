# Show HN: A big tech dev experience for an open source CMS

**评分：** 4.7  
**状态：** 待复核  
**标签：** 开源CMS, AI-first开发, Constitutional AI, Show HN, Replit, 创作者工具, 项目启动, 开发者体验  
**更新日期：** 2026-09-06  
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
一支由 5 位前 Facebook/Vidpresso 创作者工具团队成员组成的小组，展示了一个面向创作者的开源 CMS 项目的初步进展。核心展示是基于 Twitter 用户名生成'身份卡片'的简单工具（采用 Constitutional AI 思路），但作者坦承 AI 效果不佳，重点实际上放在了'AI-first 开源开发体验'上：使用 Replit 作为协作平台、Git 管理 agent 交互、Sapling 管理人工提交、Isograph+GraphQL 简化组件，并提出社区治理创新（陪审团投票）。项目愿景宏大但当前实现非常早期，对 AI-first 工程实践有一定参考意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
讨论涉及多个技术维度的思考：将 Constitutional AI 方法应用于 Twitter 用户画像生成、使用 Git 管理 AI agent 交互、用 Sapling 管理人类'有目的'的提交、Isograph+GraphQL 简化组件、Replit 作为 AI-first 开发环境。技术深度中等，主要集中在工程实践和工作流设计层面，AI 模型本身（作者承认'frankly bad'）并非核心技术贡献，亮点在于'AI-first dev environment'的工程理念。

### 实用性 (评分: 4.0/10)
对从业者的参考价值有限。核心产品（CMS + identity card tool）仍处于非常早期阶段，且承认 AI 效果不佳。更像是一个项目启动公告和个人背景介绍，对想了解 Constitutional AI 应用或 AI-first 开发流程的从业者有一定启发性，但缺乏可复用的具体技术细节或可操作的实现方案。

### 社区活跃度 (评分: 5.0/10)
58 points 和 28 条评论属于中等关注度。讨论质量因 Show HN 性质以项目介绍和社区讨论为主，作者有 YC W14 背景和被 Facebook 收购的经历增加了可信度，'AI-first dev environment'和'AI 是人也需要聚焦上下文'的理念引发一定共鸣，但因产品尚处概念阶段，讨论深度有限。

## 项目链接
https://contentfoundry.com/
