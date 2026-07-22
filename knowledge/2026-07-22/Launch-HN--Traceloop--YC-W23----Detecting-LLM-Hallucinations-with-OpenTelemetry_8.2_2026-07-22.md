# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 8.2  
**状态：** 正常  
**标签：** LLM可观测性, 幻觉检测, OpenTelemetry, 发布, YC  
**更新日期：** 2026-07-22  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一个专注于 LLM 应用幻觉检测与监控的平台，通过实时计算 NLP 评估指标并与系统变更关联来发现回归问题。同时，其开源的 OpenLLMetry 基于 OpenTelemetry 为 GenAI 可观测性建立了数据收集标准，为解决 LLM 大规模生产环境下的监控痛点提供了高价值的工程实践。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
结合传统 NLP 评估指标（如 faithfulness, relevancy）进行实时计算，并利用 OpenTelemetry 扩展出 OpenLLMetry 标准来收集 LLM 应用数据，在工程架构和可观测性标准化方面具有较高的技术含量，但底层评估算法并非全新突破。

### 实用性 (评分: 9.0/10)
直击 LLM 应用规模化上线的痛点（幻觉检测与回归监控），提供了比 LLM-as-a-judge 成本更低、延迟更低的替代方案，对 AI 工程师构建生产级 LLM 应用具有极高的实操参考价值。

### 社区活跃度 (评分: 8.0/10)
获得 101 个点赞和 72 条评论，对于 YC 发布帖而言互动热烈，反映了社区对 LLM 幻觉监控和可观测性标准化的强烈关注与需求。

## 项目链接
https://news.ycombinator.com/item?id=40985609
