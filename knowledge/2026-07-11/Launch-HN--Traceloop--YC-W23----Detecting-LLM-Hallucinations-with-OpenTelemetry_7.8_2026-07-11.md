# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 7.8  
**状态：** 正常  
**标签：** LLM可观测性, 幻觉检测, 发布  
**更新日期：** 2026-07-11  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一家 YC W23 孵化的初创公司，专注于通过 OpenTelemetry 标准检测 LLM 应用的幻觉与故障。其开源了 OpenLLMetry 以标准化 GenAI 可观测性数据采集，并在商业平台中提供实时的 NLP 指标监控与回归检测，解决了大规模 LLM 调用下的监控难题。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
讨论围绕 LLM 幻觉检测与可观测性展开，涉及将传统 NLP 评估指标（如 faithfulness, relevancy）实时化，并创新性地利用 OpenTelemetry 扩展出 OpenLLMetry 标准进行数据采集与系统变更关联分析。技术实现结合了工程架构与算法指标，具有一定深度，但非底层模型算法的突破。

### 实用性 (评分: 9.0/10)
对 AI 从业者（尤其是 LLM 应用开发与运维人员）具有极高的参考价值。直击生产环境中大规模 LLM 调用的幻觉监控与回归检测痛点，提供了比“LLM as a judge”更低成本、低延迟的替代方案，且开源了 OpenLLMetry 可直接集成使用，实操性极强。

### 社区活跃度 (评分: 7.5/10)
帖子获得了 101 个点赞和 72 条评论，在 Launch HN 中表现出中上的社区热度。说明 LLM 幻觉检测与可观测性切中了当前开发者的普遍痛点，引发了关于实现细节、OpenTelemetry 标准化及幻觉判定边界的实质性讨论。

## 项目链接
https://news.ycombinator.com/item?id=40985609
