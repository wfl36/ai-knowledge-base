# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 7.8  
**状态：** 正常  
**标签：** LLM, Observability, Evaluation, Hallucination, Launch  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目基于 OpenTelemetry 标准构建了 OpenLLMetry，将传统分布式追踪概念扩展至 GenAI 领域，并实现了实时版本的 NLP 评估指标（如忠实度、相关性等）来检测幻觉，通过关联系统变更（如提示词或模型更新）自动检测回归，技术实现上巧妙避开了大规模场景下 'LLM as a judge' 的高成本与高延迟问题。

### 实用性 (评分: 9.0/10)
对 AI 从业者极具实用价值。LLM 应用在生产环境下的幻觉监控与可观测性是当前行业核心痛点，该工具提供了开箱即用的解决方案；同时开源的 OpenLLMetry 已与 20 多家可观测性平台合作，标准化了数据采集，极大降低了开发者的接入成本和系统锁定风险。

### 社区活跃度 (评分: 7.5/10)
HN 获得 101 个 points 和 72 条评论，对于一个 YC Launch 帖子而言表现良好，表明社区对 LLM 可观测性与幻觉检测话题有较高关注度及实际讨论需求，评论互动质量较高。

## 项目链接
https://news.ycombinator.com/item?id=40985609
