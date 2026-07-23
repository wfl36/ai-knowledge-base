# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 8.2  
**状态：** 正常  
**标签：** LLM, 可观测性, 发布, YC, 幻觉检测, OpenTelemetry  
**更新日期：** 2026-07-23  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一个专注于 LLM 应用监控与幻觉检测的平台，通过扩展 OpenTelemetry 构建 OpenLLMetry 标准化数据收集，并基于实时 NLP 指标与系统变更关联来发现回归问题。该方案有效解决了大规模生产环境中传统评估方法成本高、延迟大的痛点，对 AI 应用工程化落地极具参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目将 OpenTelemetry 标准扩展至 LLM 领域，构建了 OpenLLMetry 以标准化可观测性数据收集；在检测层面，实现了 faithfulness、relevancy 等 NLP 评估指标的实时版本，并关联系统变更（如 prompt 或模型更新）进行自动回归检测，具备一定的工程深度与系统设计挑战，但底层未脱离现有 NLP 评估框架。

### 实用性 (评分: 9.0/10)
直击 LLM 应用生产环境中的核心痛点：大规模调用下的幻觉检测与监控。相比成本高、延迟大的 'LLM as a judge' 方案，该平台提供了更实用的工程化解法，且开源的 OpenLLMetry 已与 20+ 平台合作，对 AI 工程师和 MLOps 从业者具有极高的落地参考价值。

### 社区活跃度 (评分: 8.0/10)
作为 Launch HN 帖子，101 个点赞与 72 条评论表现出中等偏上的社区热度。LLM 幻觉与可观测性是当前开发者高度关注的实操难题，引发了关于技术实现细节、成本考量及行业方案的实质性讨论。

## 项目链接
https://news.ycombinator.com/item?id=40985609
