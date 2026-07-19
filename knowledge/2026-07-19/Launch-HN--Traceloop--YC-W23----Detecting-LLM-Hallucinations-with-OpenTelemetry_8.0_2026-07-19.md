# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 8.0  
**状态：** 正常  
**标签：** LLM可观测性, 幻觉检测, OpenTelemetry, 发布, 创业公司  
**更新日期：** 2026-07-19  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop (YC W23) 发布了其 LLM 应用监控平台，旨在解决大规模生产环境中 LLM 幻觉和错误难以监控的问题。该平台通过实时 NLP 指标替代高成本的 LLM-as-a-judge，并基于 OpenTelemetry 开源了 OpenLLMetry 以标准化 GenAI 可观测性数据采集，为 AI 从业者提供了极具实用价值的工程化解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
讨论了如何利用 OpenTelemetry 标准对 LLM 应用进行可观测性数据采集，并基于传统 NLP 指标（如 faithfulness, relevancy）构建实时评估机制，以低成本、低延迟替代 LLM-as-a-judge 方案，技术实现具有较好的工程深度和标准化思维。

### 实用性 (评分: 9.0/10)
对 AI 工程师和 MLOps 从业者具有极高价值，直击 LLM 规模化上线的痛点（幻觉与错误监控），且其开源的 OpenLLMetry 项目为行业提供了通用的数据采集标准，实用性极强。

### 社区活跃度 (评分: 7.5/10)
获得 101 个点赞和 72 条评论，在 Launch HN 类帖子中表现出色，表明社区对 LLM 生产环境监控、幻觉解决方案及 OpenTelemetry 扩展有浓厚兴趣和实际需求。

## 项目链接
https://news.ycombinator.com/item?id=40985609
