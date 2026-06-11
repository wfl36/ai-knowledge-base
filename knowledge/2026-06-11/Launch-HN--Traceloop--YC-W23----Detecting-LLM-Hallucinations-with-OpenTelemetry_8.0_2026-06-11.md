# Launch HN: Traceloop (YC W23) – Detecting LLM Hallucinations with OpenTelemetry

**评分：** 8.0  
**状态：** 正常  
**标签：** LLM可观测性, 幻觉检测, OpenTelemetry, 发布, YC  
**更新日期：** 2026-06-11  
**来源：** hackernews  

## 项目描述
Hey everyone, we are Nir and Gal from Traceloop (<a href="https:&#x2F;&#x2F;www.traceloop.com">https:&#x2F;&#x2F;www.traceloop.com</a>). We help teams understand when their LLM apps are failing or hallucinating at scale. See a demo: <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;video">https:&#x2F;&#x2F;www.traceloop.com&#x2F;video</a> or try it yourself at <a href="https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo">https:&#x2F;&#x2F;www.traceloop.com&#x2F;docs&#x2F;demo</a>.<p>When moving your LLM app to production, significant scale makes it harder for engineers and data scientists alike to understand when their LLM is hallucinating or returning malformed responses. When you get to millions of calls to OpenAI a month, methods like “LLM as a judge” can’t work at a reasonable cost or latency. So, what most people we talked to usually do is sample some generations by hand, maybe for some specific important customers, and manually look for errors or hallucinations.<p>Traceloop is a monitoring platform that detects when your LLM app fails. Under the hood, we built real-time versions of known metrics like faithfulness, relevancy, redundancy, and many others. These are loosely based on some well-known NLP metrics that work well for LLM-generated texts. We correlate them with changes we detect in your system - like updates to prompts or to the model you’re using - to detect regressions automatically.<p>Here are some cool examples we’ve seen with our customers -<p>1. Applying our QA relevancy metric to an entity extraction task, we managed to discover issues where the model was not extracting the right entities (like an address instead of a person’s name); or returning random answers like “I’m here! What can I help you with today?”.<p>2. Our soft-faithfulness metric was able to detect cases in summarization tasks where a model was completely making up stuff that never appeared in the original text.<p>One of the challenges we faced was figuring out how to collect the data that we need from our customers&#x27; LLM apps. That’s where OpenTelemetry came in handy. We built OpenLLMetry (<a href="https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry">https:&#x2F;&#x2F;github.com&#x2F;traceloop&#x2F;openllmetry</a>), and announced it here almost a year ago. It standardized the use of OpenTelemetry to observe LLM apps. We realized that the concepts of traces, spans, metrics, and logs that were standardized with OpenTelemetry can easily extend to gen AI. We partnered with 20+ observability platforms to make sure that OpenLLMetry becomes the standard for GenAI observability and that the data that we collect can be sent to other platforms as well.<p>We plan to extend the metrics we provide to support agents that use tools, vision models, and other amazing developments in our fast-paced industry.<p>We invite you to give Traceloop a spin and are eager for your feedback! How do you track and debug hallucinations? How much has that been an issue for you? What types of hallucinations have you encountered?

## 综合总结
Traceloop 是一家 YC W23 孵化的初创公司，致力于通过 OpenTelemetry 标准解决 LLM 应用在生产环境中的幻觉与故障检测问题。面对大规模调用下传统“LLM as a judge”方案的高成本与高延迟，Traceloop 推出了开源项目 OpenLLMetry 采集数据，并基于实时 NLP 指标（如 faithfulness、relevancy）监控 LLM 输出质量，关联系统变更自动发现回归。该项目为 AI 工程化落地提供了高价值的可观测性解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目将 OpenTelemetry 标准引入 LLM 可观测性领域，构建了 OpenLLMetry；通过实时计算 faithfulness、relevancy 等传统 NLP 指标来替代高成本的 LLM-as-a-judge 方案，工程实现巧妙，但底层算法并非颠覆性创新。

### 实用性 (评分: 9.0/10)
直击 LLM 应用规模化生产中的核心痛点——幻觉检测与成本/延迟的平衡。其基于 OpenTelemetry 的数据采集方案和实时指标监控体系，为 AI 工程师和架构师提供了极具实操性的可观测性建设参考。

### 社区活跃度 (评分: 8.0/10)
101 个点赞和 72 条评论表明该项目引起了 HN 社区的显著关注。作为 YC 项目的 Launch 帖，其切入的 LLM 幻觉与可观测性话题引发了开发者关于工程实践、技术选型及产品可行性的深度交流。

## 项目链接
https://news.ycombinator.com/item?id=40985609
