# A Consensus-Based Framework for Relative Preference Evaluation of Large Language Models

**评分：** 7.2  
**状态：** 正常  
**标签：** 大模型, 评估, LLM-as-a-Judge, 相对偏好, 论文  
**更新日期：** 2026-07-27  
**来源：** rss  

## 项目描述
arXiv:2607.21632v1 Announce Type: new Abstract: Traditional benchmarks for LLMs primarily rely on static datasets and objective scoring metrics, which often fail to capture differences in response quality when multiple answers are acceptable. In such settings, correctness alone is insufficient to distinguish between responses that vary in clarity, completeness, and usefulness. This paper introduces a consensus-based evaluation framework that measures relative preference among model-generated responses rather than absolute correctness. Instead of evaluating outputs against a fixed ground truth, we assess how a panel of diverse LLMs ranks anonymized candidate responses to the same prompt. This approach treats aggregate inter-model agreement as a proxy for perceived response quality under blind conditions. We conduct a controlled study using five state-of-the-art LLMs across multiple domains, including programming, general knowledge, safety, logical reasoning, and mathematics. Each model generates responses and independently ranks peer outputs through a structured voting process. Scores are aggregated into a Relative Intelligence Index (RII), representing how frequently a model's responses are preferred by other models. Our findings reveal consistent preference patterns across domains, with certain models more frequently ranked highly by their peers. However, we emphasize that these results reflect inter-model preference alignment rather than objective correctness or human judgment. This framework provides a scalable, model-driven method for comparative evaluation, offering an alternative perspective on response quality in scenarios where multiple valid answers exist. While not directly aligned with human evaluation, prior work suggests that aggregated model preferences can partially correlate with human judgments, motivating this as a proxy signal.

## 综合总结
本文针对传统LLM基准在多答案场景下的评估局限，提出了一种基于共识的相对偏好评估框架。该框架利用多个先进LLM作为评委对匿名响应进行结构化投票，并汇总生成相对智能指数（RII），以模型间共识作为响应质量的代理。研究在编程、逻辑等多个领域进行了验证，发现了一致的模型间偏好模式。该框架为开放性场景下的模型评估提供了高可落地性的自动化替代方案，但作者也明确指出其反映的是模型间偏好对齐而非客观正确性或人类判断。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
论文提出了一种基于共识的相对偏好评估框架，以解决传统静态基准在多答案可接受场景下的评估局限。通过引入相对智能指数（RII），利用多个先进LLM作为评委进行盲评和结构化投票，将模型间的共识作为响应质量的代理指标。该方法在概念上区分了绝对正确性与相对偏好，论证严谨且承认了与人类判断对齐的局限性，但在“LLM-as-a-judge”领域属于增量式创新，技术突破性有限。

### 实用性 (评分: 8.0/10)
该框架对AI从业者的实际参考价值较高。在开放性问答、代码生成、创意写作等没有唯一标准答案的场景中，RII提供了一种可扩展、自动化的模型对比方案，能够有效指导模型选型和评估实践，适用范围广泛且易于落地实施，降低了人工评估的成本。

### 社区活跃度 (评分: 6.5/10)
大模型评估是当前AI社区的核心痛点之一，话题时效性强。但本文作为单作者的arXiv预印本，缺乏顶级会议或知名研究机构的背书，权威性和初始社区影响力相对有限。尽管如此，其提出的“模型共识替代绝对标准”的评估视角仍能引发评估社区的讨论与关注。

## 项目链接
https://arxiv.org/abs/2607.21632
