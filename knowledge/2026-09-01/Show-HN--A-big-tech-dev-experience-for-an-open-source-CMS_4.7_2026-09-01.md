# Show HN: A big tech dev experience for an open source CMS

**评分：** 4.7  
**状态：** 待复核  
**标签：** Show HN, 开源 CMS, 内容创作工具, Constitutional AI, AI 开发体验, Replit, 开发者工具  
**更新日期：** 2026-09-01  
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
一个由前 Facebook/YC 创业者团队发起的开源 CMS 项目 Show HN，核心展示 AI 辅助内容生产管道的开发体验。当前阶段 AI 能力尚弱，重点在于提出可重复、可验证的身份卡片生成思路（借鉴 Constitutional AI）以及 AI-first 开发环境的设计理念（Replit + Sapling + Git 管理 agent 交互）。项目愿景宏大但当前实现过于早期，对 AI 从业者的实际技术参考价值有限，更多是一个社区和开发体验的早期展示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 4.5/10)
项目本身技术深度有限，核心展示的是一个简化版的 Twitter 用户名→身份卡片生成工具，AI 能力'frankly bad'。技术亮点主要在工程化层面：提出将 Constitutional AI 用于可重复、可测试、可验证的身份卡片生成，以及在开发流程上使用 Isograph+GraphQL、Replit AI 编码、Sapling 管理 agent 交互等组合。但缺乏具体技术细节、模型选型、评估方法等深入讨论，更像是一个开发体验 demo 而非技术突破。

### 实用性 (评分: 4.0/10)
对 AI 从业者的直接参考价值中等偏低。身份卡片生成工具过于简单，Constitutional AI 的应用场景描述模糊（微调样本 vs 推理时洞察），缺乏可复现的实现细节。开发流程理念（Git 管理 agent 交互、Sapling 管理有意义提交）有一定启发性，但属于工程实践层面的建议，对核心 AI 研究/工程从业者的帮助有限。

### 社区活跃度 (评分: 5.5/10)
58 points 和 28 条评论属于中等偏低的 HN 关注度。创始团队背景（YC W14、Facebook 创作者工具团队 5 年）有一定可信度加分，但内容偏向项目推介和团队故事而非技术讨论，社区参与质量预期一般。作为 Show HN 帖互动尚可，但缺乏引发深度技术辩论的爆点。

## 项目链接
https://contentfoundry.com/
