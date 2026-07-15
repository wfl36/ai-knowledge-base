# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 7.7  
**状态：** 正常  
**标签：** LLM监控, 幻觉检测, 可观测性, 发布  
**更新日期：** 2026-07-15  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一个 LLM 应用监控平台，通过开源的 OpenLLMetry（基于 OpenTelemetry）收集数据，并利用实时 NLP 指标检测 LLM 幻觉和异常，自动关联系统变更发现回归问题，为大规模 LLM 应用提供低成本的可观测性与质量保障方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
基于 OpenTelemetry 标准扩展构建 OpenLLMetry 实现 LLM 应用的数据采集；利用改进的实时 NLP 指标（如 faithfulness, relevancy, redundancy）评估生成质量，并与系统变更（如 prompt 或模型更新）关联进行回归检测，技术方案在工程实践层面具有较好的深度和合理性。

### 实用性 (评分: 8.5/10)
直击 LLM 应用规模化生产中的核心痛点——幻觉与异常监控。相比高成本、高延迟的 'LLM as a judge' 方案，提供了更轻量、实时的工程化替代方案，对 MLOps 工程师和 LLM 应用开发者具有极高的参考与落地使用价值。

### 社区活跃度 (评分: 7.5/10)
获得 101 个点赞和 72 条评论，互动表现良好。作为 YC W23 项目的发布，引发了社区关于 LLM 幻觉检测成本、准确性及可观测性标准的深入讨论，反映了业界对 LLM 生产环境监控问题的高度关注。

## 项目链接
https://news.ycombinator.com/item?id=40985609
