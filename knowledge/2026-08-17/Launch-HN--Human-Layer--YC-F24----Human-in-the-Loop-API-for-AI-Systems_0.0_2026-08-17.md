# Launch HN: Human Layer (YC F24) – Human-in-the-Loop API for AI Systems

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** hackernews  

## 项目描述
Hey HN! I&#x27;m Dex, building HumanLayer (<a href="https:&#x2F;&#x2F;humanlayer.dev">https:&#x2F;&#x2F;humanlayer.dev</a>), an API that lets AI agents contact humans for feedback, input, and approvals. We enable safe deployment of autonomous&#x2F;headless AI systems in production. You can try it with our Python or TypeScript SDKs and start using it immediately with a free trial. We have a free tier and transparent usage-based pricing. Here’s a demo: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;5sbN8rh_S5Q?t=51" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;5sbN8rh_S5Q?t=51</a><p>What&#x27;s really exciting is that we&#x27;re enabling teams to deploy AI systems that would otherwise be too risky. We let you focus on building powerful agents while knowing that critical steps will <i>always</i> get a human-in-the-loop. It&#x27;s been dope seeing people start to think bigger when they consider dynamic human oversight as a key ingredient in production AI systems.<p>This started when we were building AI agents for data teams. We wanted to automate tedious tasks like dropping unused tables, but customers were (rightfully!) opposed to giving AI agents direct access to production systems.<p>Getting AI to &quot;production grade&quot; reliability is a function of &quot;how risky is this task the AI is performing&quot;. We didn&#x27;t have the 3+ months it would have taken to sink into evals, fine tuning, and prompt engineering to get to a point where the agent had 99.9+% reliability—and even then, getting decision makers comfortable with flipping the switch on was a challenge. So instead we built some basic approval flows, like &quot;ask in Slack before dropping tables&quot;.<p>But this communication itself needed guardrails—what if the agent contacted the wrong person? How would the head of data look if a tool he bought sent a nagging Slack message to the CEO? Our buyers wanted the agent to ask stakeholders for approval, but first <i>they</i> wanted to approve the &quot;ask for approval&quot; action itself. And then I started thinking about it... as a product builder + owner, <i>I</i> wanted to approve the &quot;ask for approval to ask for approval&quot; action!<p>I hacked together a human-AI interaction that would handle each of these cases across both my and my customers&#x27; Slack instances. By this time, I was convinced that any team building AI agents would need this kind of infrastructure and decided to build it as a standalone product. I presented the MVP at an AI meetup in SF and had a ton of incredible conversations, and went all in on building HumanLayer.<p>When you integrate the HumanLayer SDK, your AI agent can request human approval at any point in its execution. We handle all the complexity of routing these requests to the right people through their preferred channels (Slack or email, SMS and Teams coming soon), managing state while waiting for responses, and providing a complete audit trail. In addition to &quot;ask for approval&quot;, we also support a more generic &quot;human as tool&quot; function that can be exposed to an LLM or agent framework, and will handle collecting a human response to a generic question like &quot;I&#x27;m stuck on $PROBLEM, I&#x27;ve tried $THINGS, please advise&quot; (I get messages like this sometimes from in-house agents we rolled out for back-office automations).<p>Because it&#x27;s at the tool-calling layer, HumanLayer&#x27;s SDK works with any AI framework like CrewAI, LangChain, etc, and any language model that supports tool calling. If you&#x27;re rolling your own agentic&#x2F;tools loop, you can use lower level SDK primitives to manage approvals however you want. We&#x27;re even exploring use cases where HumanLayer is used for human-to-human approval, not just AI-to-human.<p>We&#x27;re already seeing HumanLayer used in some cool ways. One customer built an AI SDR that drafts personalized sales emails but asks for human approval in Slack before sending anything to prospects. Another uses it to power an AI newsletter where subscribers can have email conversations with the content. HumanLayer handles receiving inbound emails and routing them to agents that can respond, and giving those agents tools to do so. One team uses HumanLayer to build a customer-facing DevOps agent—their AI agent reviews PRs, plans and executes db migrations, all while getting human sign-off at critical steps and reaching out to the team for steering if it encounters any issues.<p>We have a free tier and flexible credits-based pricing. For teams building customer-facing agents, you get whitelabeling and additional features and priority support.<p>If you want to integrate HumanLayer into your systems, check out our docs at <a href="https:&#x2F;&#x2F;humanlayer.dev&#x2F;docs">https:&#x2F;&#x2F;humanlayer.dev&#x2F;docs</a> or book a demo at <a href="https:&#x2F;&#x2F;humanlayer.dev">https:&#x2F;&#x2F;humanlayer.dev</a>.<p>Thank you for reading! We’re admittedly early and I welcome your ideas and experiences as it relates to agents, reliability, and balancing human+AI workloads.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://news.ycombinator.com/item?id=42247368
