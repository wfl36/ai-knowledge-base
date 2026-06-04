# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 7.8  
**状态：** 正常  
**标签：** LLM可观测性, 幻觉检测, 发布, YC  
**更新日期：** 2026-06-04  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一个专注于 LLM 应用可观测性与幻觉检测的监控平台。它通过开源的 OpenLLMetry（基于 OpenTelemetry）标准化数据采集，并利用实时 NLP 指标替代高成本的 LLM 评估方案，实现大规模生产环境下的 LLM 失败检测与回归分析。该项目直击 LLM 落地痛点，为 AI 从业者提供了高价值的工程解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在工程架构上具有较高含金量，将传统可观测性标准 OpenTelemetry 扩展至 GenAI 领域并推出 OpenLLMetry，解决了 LLM 应用链路追踪的标准化问题。在幻觉检测方面，摒弃了大规模应用下成本和延迟过高的 'LLM as a judge' 方案，转而实现基于传统 NLP 指标（如 faithfulness, relevancy）的实时版本，并与系统变更（如 prompt 或模型更新）关联进行回归检测，展现了扎实的工程与算法结合能力。

### 实用性 (评分: 8.5/10)
对 AI 应用开发者和 MLOps 从业者具有极高的实际参考价值。LLM 生产环境下的幻觉和输出不稳定是当前行业核心痛点，该项目提供了一种可落地的规模化监控方案。其开源的 OpenLLMetry 标准及与 20 多家可观测性平台的兼容，极大降低了 LLM 应用接入监控的门槛，为构建可靠的 LLM 应用提供了关键基础设施。

### 社区活跃度 (评分: 7.5/10)
作为 Launch HN 帖子，获得 101 个点赞和 72 条评论，表现中等偏上。幻觉检测和 LLM 可观测性直击当前开发者痛点，引发了关于监控成本、指标有效性以及 OpenTelemetry 在 AI 领域适用性的实质性讨论，社区关注度与讨论质量均较好。

## 项目链接
https://news.ycombinator.com/item?id=40985609
