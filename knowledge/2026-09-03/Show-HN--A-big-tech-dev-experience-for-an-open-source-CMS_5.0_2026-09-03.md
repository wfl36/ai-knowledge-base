# Show HN: A big tech dev experience for an open source CMS

**评分：** 5.0  
**状态：** 待复核  
**标签：** Show HN, 开源CMS, AI开发工具, 开发者体验, 创作者工具, Replit, 社区治理  
**更新日期：** 2026-09-03  
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
一个由前Facebook创作者工具团队（前YC W14 Vidpresso创始人）发起的开源CMS项目Show HN。核心展示点并非CMS本身，而是一个AI-first的开发环境理念：整合Replit、Isograph、Sapling等技术栈，强调让任何开发者都能轻松参与开源贡献。技术上将Git用于管理AI agent交互、Sapling管理人工提交的工作流，以及借鉴Constitutional AI做可验证的identity card是亮点。但项目处于极早期，AI工具效果尚不成熟，主要价值在于工程理念和社区治理模式（陪审团投票）的探索。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.5/10)
讨论涉及多个技术栈整合：Isograph（GraphQL组件简化）、Replit（AI编码环境）、Sapling（版本控制）以及用Git管理agent交互的创新思路。提到了Constitutional AI的概念用于身份卡片生成，强调可重复性、可测试性和可验证性。但实际展示的AI工具非常基础，技术深度有限，更多是开发体验和工程理念的分享，而非核心AI技术的突破。

### 实用性 (评分: 4.5/10)
对AI从业者的实际参考价值中等。其AI-first开发环境的理念（'AI是人也需要聚焦上下文'）和将Git用于管理agent交互、Sapling管理人工提交的工作流设计有一定借鉴意义。但项目本身处于极早期阶段，所展示的工具效果'frankly bad'，缺乏可复用的具体技术方案或代码实践，更多是方向性的思路展示。

### 社区活跃度 (评分: 5.0/10)
58个points和28条评论属于中等偏低的HN关注度。Show HN帖通常会吸引一定讨论，但评论数不多说明社区参与度一般。项目背景（YC W14、Facebook收购创业经历）有一定背书效应，团队5人全职投入也有可信度。讨论质量可能集中在对其开发理念和社区治理（陪审团投票）的探讨上。

## 项目链接
https://contentfoundry.com/
