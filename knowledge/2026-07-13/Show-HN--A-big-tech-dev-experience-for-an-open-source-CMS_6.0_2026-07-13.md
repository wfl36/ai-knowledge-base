# Show HN: A big tech dev experience for an open source CMS

**评分：** 6.0  
**状态：** 正常  
**标签：** 开源CMS, AI应用开发, 开发者工具, 发布  
**更新日期：** 2026-07-13  
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
前Facebook团队发布的开源CMS项目Content Foundry，旨在为创作者提供大厂级别的开发体验。项目当前展示了基于Twitter生成身份卡的初步功能，并重点分享了其AI优先的开发环境设计，包括使用Replit进行AI辅助编码、结合Git与Sapling管理Agent交互等工程实践。项目还提出了创新的社区治理模式，试图解决传统开源项目重治理轻软件的问题。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.5/10)
项目在工程实践上有一定创新，采用了Isograph、Replit和Sapling等非传统技术栈，并探索了用Git管理AI Agent交互、用Sapling管理目的性提交的AI优先开发模式。但当前展示的AI功能（Twitter身份卡生成）较为简单，作者也承认AI表现不佳，底层算法与模型深度有限。

### 实用性 (评分: 6.0/10)
对AI应用开发者及全栈工程师具有较好的参考价值，尤其是其“AI优先”的开发环境设计理念，以及如何利用Replit等工具降低开源贡献门槛、将AI视为初级开发者进行协作的实践经验。但对底层AI算法或模型研发从业者的直接价值不高。

### 社区活跃度 (评分: 6.5/10)
获得了58个点赞和28条评论，在Show HN项目中表现中等偏上。项目强调开源社区治理（如陪审团投票机制）和极致的开发者体验，直击当前部分开源基金会脱离软件本身的痛点，引发了社区对开源协作与AI辅助开发的关注与讨论。

## 项目链接
https://contentfoundry.com/
