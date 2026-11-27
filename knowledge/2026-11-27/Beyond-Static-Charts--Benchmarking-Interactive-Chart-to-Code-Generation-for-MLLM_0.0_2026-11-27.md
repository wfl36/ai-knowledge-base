# Beyond Static Charts: Benchmarking Interactive Chart-to-Code Generation for MLLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-27  
**来源：** rss  

## 项目描述
arXiv:2611.31345v1 Announce Type: new Abstract: In recent years, multimodal large language models (MLLMs) have achieved significant progress in chart-to-code generation. However, existing benchmarks mainly focus on static charts, overlooking interactive charts that enable richer and more expressive data exploration. Unlike static chart-to-code generation, which emphasizes visual consistency, interactive chart-to-code evaluation targets behavioral consistency, requiring chart states to evolve correctly under sequences of user interactions, thereby rendering traditional one-step evaluation paradigms ineffective. To address this gap, we introduce ChartInt, the first benchmark specifically designed for interactive chart-to-code generation. ChartInt consists of 2,779 carefully annotated examples covering common interaction patterns such as hover, highlight, and tooltips. Additionally, ChartInt incorporates editing tasks such as data updates, style adjustments, and cross-chart style transfer to expand real-world application scenarios. To enable reliable evaluation of interaction behavior, we propose a preset state snapshot protocol that predefines target interaction states and deterministically triggers interaction events, transforming dynamic behaviors into reproducible evaluation targets. Based on this protocol, we design a multi-dimensional evaluation framework measuring semantic and stylistic consistency. Experiments show that while current MLLMs perform well on static charts, their performance drops significantly on interactive tasks, highlighting the need for interaction-aware benchmarks.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.31345
