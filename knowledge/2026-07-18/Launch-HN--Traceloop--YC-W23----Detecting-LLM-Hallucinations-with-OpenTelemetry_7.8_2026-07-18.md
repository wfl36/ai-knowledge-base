# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 7.8  
**状态：** 正常  
**标签：** LLM, 幻觉检测, 可观测性, 发布  
**更新日期：** 2026-07-18  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop (YC W23) 发布了一款基于 OpenTelemetry 的 LLM 应用监控平台，旨在解决大规模生产环境下的 LLM 幻觉检测和故障排查问题。该项目通过开源 OpenLLMetry 标准化数据收集，并提供实时的 NLP 评估指标与系统变更关联分析，为 AI 从业者提供了高价值的工程化解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
讨论了利用 OpenTelemetry 扩展构建的 OpenLLMetry 标准，以及基于此实现的 LLM 实时监控指标（如 faithfulness, relevancy 等）和系统变更关联回归检测，具备一定的工程架构深度与系统可观测性技术含金量。

### 实用性 (评分: 8.5/10)
直击 LLM 应用生产环境中的幻觉检测和监控痛点，解决了大规模调用下传统评估方法成本高、延迟大的问题，其开源的 OpenLLMetry 标准对 AI 工程师和应用开发者具有极高的实践参考与接入价值。

### 社区活跃度 (评分: 7.5/10)
获得 101 个点赞和 72 条评论，作为 YC 创业公司的发布帖，引发了社区对 LLM 幻觉检测方案及 OpenTelemetry 应用的积极讨论，互动质量较高，热度中上。

## 项目链接
https://news.ycombinator.com/item?id=40985609
