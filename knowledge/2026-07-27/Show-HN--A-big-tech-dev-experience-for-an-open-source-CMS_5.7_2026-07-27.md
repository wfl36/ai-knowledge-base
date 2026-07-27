# Show HN: A big tech dev experience for an open source CMS

**评分：** 5.7  
**状态：** 待复核  
**标签：** 开源CMS, AI辅助开发, 开发者体验, Show HN  
**更新日期：** 2026-07-27  
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
这是一个由前Facebook员工团队打造的开源CMS项目，旨在为创作者提供大厂级别的开发者体验。项目目前展示了基于Twitter用户名生成'身份卡'的极简工具，并计划引入Constitutional AI方法以保证输出的可重复性和可测试性。项目强调AI优先的开发环境设计，采用Isograph、Replit和Sapling等非传统技术栈来优化AI Agent的交互与代码管理，同时探索新的开源社区治理模式。虽然目前AI功能尚不成熟，但其对AI辅助开发流程和开源治理的思考值得关注。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
项目目前处于极早期，展示的AI功能较为简陋（作者自承AI表现不佳）。技术亮点在于提出了'AI优先'的开发环境设计原则，并采用非传统技术栈（Isograph、Replit、Sapling）来优化AI Agent的代码交互与版本控制（用Git管理Agent交互，Sapling管理目的性提交），以及设想应用Constitutional AI来保证身份卡生成的可重复性与可测试性，但整体仍停留在概念和架构探索阶段，缺乏深度的AI技术实现。

### 实用性 (评分: 5.5/10)
对AI从业者的直接技术借鉴价值有限，但在工程实践层面有一定启发性。其关于'AI优先'的开发者体验（DX）设计原则（如无需查文档即可发现命令、上下文贴近代码、AI需聚焦上下文等），以及利用Sapling与Git协同管理AI Agent代码生成的思路，对构建AI辅助开发工具或Agent工作流的从业者具有参考价值。

### 社区活跃度 (评分: 6.5/10)
HN上获得58个点赞和28条评论，对于一个极早期的Show HN项目表现中规中矩。团队前Facebook和YC的背景、对现有开源基金会（如WordPress、Apache）的批评，以及提出的开源社区治理新思路（如陪审团投票），有效引发了社区关于开源治理和开发者体验的讨论，互动质量较好。

## 项目链接
https://contentfoundry.com/
