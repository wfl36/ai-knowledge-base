# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 8.0  
**状态：** 正常  
**标签：** LLM, Observability, Hallucination, OpenTelemetry, Launch, Startup  
**更新日期：** 2026-07-10  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一个专注于 LLM 应用可观测性与幻觉检测的监控平台。它通过开源的 OpenLLMetry 基于 OpenTelemetry 标准化数据采集，并利用改进的实时 NLP 指标（如 faithfulness、relevancy）结合系统变更关联，实现自动化的故障与幻觉回归检测，为大规模 LLM 应用提供了一种低成本、低延迟的工程化监控方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目将 OpenTelemetry 标准扩展至 LLM 领域，推出 OpenLLMetry 以标准化 GenAI 可观测性数据采集；在幻觉检测方面，基于传统 NLP 指标构建了实时的 faithfulness、relevancy 等评估体系，并与系统变更（如 prompt 或模型更新）关联实现自动回归检测。工程实践扎实且具备开源生态整合能力，但核心检测算法未见底层理论的根本性突破。

### 实用性 (评分: 9.0/10)
直击 LLM 应用生产化过程中的核心痛点——大规模调用下的幻觉监控与可观测性。相比高成本、高延迟的 'LLM as a judge' 方案，该实时指标监控方案更具工程落地性；且开源的 OpenLLMetry 已与 20+ 平台合作，对 AI 工程师和 DevOps 构建生产级监控体系具有极高的直接参考与使用价值。

### 社区活跃度 (评分: 8.0/10)
获得 101 个点赞和 72 条评论，在 HN 社区引发了较高关注。作为 YC 创业项目的 Launch，其切中时弊的痛点引发了开发者对 LLM 监控实践、OpenTelemetry 标准化及幻觉检测有效性的深入讨论，互动质量较高。

## 项目链接
https://news.ycombinator.com/item?id=40985609
