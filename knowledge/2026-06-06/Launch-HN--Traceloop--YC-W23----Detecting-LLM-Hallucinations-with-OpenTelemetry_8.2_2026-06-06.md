# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 8.2  
**状态：** 正常  
**标签：** LLM可观测性, 幻觉检测, OpenTelemetry, 发布, 创业  
**更新日期：** 2026-06-06  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop (YC W23) 发布了基于 OpenTelemetry 的 LLM 幻觉检测与监控平台。该平台通过开源的 OpenLLMetry 标准化收集 LLM 应用数据，并实时计算忠实度、相关性等指标，结合系统变更自动检测回归，旨在解决大规模生产环境下 LLM 调用的幻觉监控与成本延迟问题，为 AI 从业者提供了高价值的工程实践参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
探讨了利用 OpenTelemetry 标准化 LLM 可观测性的工程实践，以及实时计算忠实度、相关性等 NLP 指标来检测幻觉的技术方案。在系统架构和评估指标设计上有一定深度，但并非底层模型算法层面的突破。

### 实用性 (评分: 9.0/10)
直击 LLM 应用落地生产环境的核心痛点——幻觉检测与可观测性。对于需要处理大规模调用、控制成本和延迟的 AI 工程师而言，其基于 OpenTelemetry 的标准化监控方案和自动化回归检测思路具有极高的实战参考价值。

### 社区活跃度 (评分: 8.0/10)
获得 101 个点赞和 72 条评论，在 HN 上表现出较高的关注度。作为 YC 创业公司的 Launch 帖，引发了社区对 LLM 可观测性标准、幻觉检测成本及现有方案对比的活跃讨论，互动质量较高。

## 项目链接
https://news.ycombinator.com/item?id=40985609
