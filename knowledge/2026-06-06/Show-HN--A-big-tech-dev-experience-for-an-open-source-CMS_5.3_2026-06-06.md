# Show HN: A big tech dev experience for an open source CMS

**评分：** 5.3  
**状态：** 待复核  
**标签：** 开源CMS, AI辅助开发, 开发者体验, 发布  
**更新日期：** 2026-06-06  
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
这是一个由前Facebook/YC团队打造的面向创作者的开源CMS项目。项目目前展示了基于Twitter用户名生成“身份卡”的初步AI工具，并提出了利用Constitutional AI确保结果可复现与可测试的构想。其核心亮点不在于AI算法深度，而在于构建“AI优先”的开发者体验：强调为AI提供聚焦上下文，并创新性地使用Git管理Agent交互、Sapling管理代码提交。项目尚处极早期，但在AI辅助开发工作流和开源社区治理方面提供了有趣的探索方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 4.5/10)
项目目前处于极早期阶段，作者坦言当前展示的AI功能较为简陋。技术亮点主要在于工程实践层面，如采用Constitutional AI思路生成可验证的结构化“身份卡”，以及使用Git管理AI Agent交互、Sapling管理代码提交的版本控制策略。整体AI算法深度有限，更侧重于开发体验与工作流设计。

### 实用性 (评分: 6.0/10)
对AI从业者而言，其核心参考价值在于“AI优先”的开发环境设计理念，特别是如何为AI提供聚焦上下文以减少检索干扰，以及利用Git追踪Agent行为的实践思路。此外，基于Constitutional AI生成可复现、可测试的结构化数据用于微调或推理的构想具有一定启发性，但当前工具尚不具备直接的生产级应用价值。

### 社区活跃度 (评分: 5.5/10)
该项目在HN上获得58个点赞和28条评论，属于中等偏下的关注度。社区讨论可能更多围绕其前Facebook/YC团队的背景、开源社区治理理念以及Replit/Sapling等非传统技术栈的选择展开，而非AI技术本身，反映出社区对新型开源CMS及AI辅助开发模式的初步探索兴趣。

## 项目链接
https://contentfoundry.com/
