# Show HN: A big tech dev experience for an open source CMS

**评分：** 6.2  
**状态：** 正常  
**标签：** 开源CMS, AI工程化, 开发者体验, Agent工作流, Show HN  
**更新日期：** 2026-07-24  
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
前Facebook团队推出的AI优先开源CMS项目，旨在提供大厂级开发者体验与新型社区治理模式。项目展示了基于Twitter生成'身份卡'的初步工具，并探讨了Constitutional AI在结构化内容验证中的应用。技术栈融合Isograph、Replit和Sapling，创新性地使用Git管理Agent交互，强调为AI提供聚焦上下文以优化开发流程。项目还提出陪审团投票等开源治理新思路，目前处于极早期，核心AI能力与工程实现仍有待完善。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
项目在工程架构和AI Agent工作流设计上有一定亮点，如采用Isograph、Replit和Sapling组合栈，创新性地使用Git管理Agent交互、Sapling管理目的性提交，并探讨了Constitutional AI在结构化内容验证中的应用。但作者坦诚当前展示的AI能力极弱，核心仍停留在概念和开发体验展示阶段，缺乏底层AI技术的深度突破与细节呈现。

### 实用性 (评分: 6.5/10)
对AI应用开发者和工程化从业者具有参考价值，其'AI-first'的开发环境设计理念（如为AI提供聚焦上下文、减少跨文件搜索干扰）和Agent版本控制实践值得借鉴。此外，利用Constitutional AI思路生成可验证的微调数据或推理时洞察，为AI数据工程提供了新思路。但由于项目处于极早期，直接可用的工具和代码参考有限。

### 社区活跃度 (评分: 6.0/10)
HN上获得58个点赞和28条评论，对于一个极早期的Show HN项目表现中规中矩。项目切中了当前开源社区对传统基金会（如WordPress）的不满情绪，其提出的'陪审团投票'开源治理模式和极低门槛的贡献体验引发了一定关注与讨论，但整体热度尚未爆发。

## 项目链接
https://contentfoundry.com/
