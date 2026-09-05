# Show HN: A big tech dev experience for an open source CMS

**评分：** 4.5  
**状态：** 待复核  
**标签：** Show HN, 开源CMS, 开发者工具, AI开发环境, Replit, 内容创作, 社区治理  
**更新日期：** 2026-09-05  
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
这是一个处于极早期阶段的开源CMS项目Show HN，作者团队来自YC W14和Facebook创作者工具背景，旨在构建面向内容创作者的全流程工具链。项目核心展示的是AI优先的开发体验理念（包括Replit集成、Git/Sapling双版本控制、Isograph等），并附带一个基于Twitter用户名生成身份卡片的简单AI工具demo。项目更侧重于社区治理创新和开发者体验优化，而非AI技术本身，AI部分坦诚表示效果尚不成熟。整体属于早期产品介绍，社区热度一般。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 4.5/10)
技术深度有限。主要讨论的是开源CMS的开发者体验和社区治理理念，技术栈涉及Isograph(GraphQL)、Replit、Sapling等成熟工具的组合使用。关于AI部分，仅展示了一个基于Twitter用户名生成'身份卡片'的简单工具，且自述AI效果较差(frankly bad)，借鉴了Constitutional AI的概念但未展示实质性技术实现。Git管理agent交互、Sapling管理'purposeful'提交的设计思路有一定新意，但整体技术含金量不高。

### 实用性 (评分: 4.0/10)
对AI从业者的参考价值一般。项目中关于'AI-first开发环境'的设计原则（为AI提供充分上下文、降低贡献门槛）有一定的启发性，特别是将AI视为'junior developer'的工作方式以及社区治理的创新想法。但作为内容生产管道的CMS，AI仅是辅助角色，且当前展示的功能过于简单，对从业者的实际参考价值有限。

### 社区活跃度 (评分: 5.0/10)
社区关注度中等偏低。58个points和28条评论表明HN社区有一定兴趣，但讨论热度不算高。项目处于早期阶段，创始团队背景（前YC W14创业者、Facebook创作者工具团队）有一定可信度，'Show HN'形式适合吸引早期贡献者，但缺乏实质性的技术展示来激发深度讨论。

## 项目链接
https://contentfoundry.com/
