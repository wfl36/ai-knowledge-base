# Beyond Raw Transcripts: Structured Persona Extraction for LLM-Based Digital Twins

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-24  
**来源：** rss  

## 项目描述
arXiv:2608.20344v1 Announce Type: new Abstract: LLM-based "digital twins" aim to simulate how an individual would behavein new environments or respond to novel questions, given some representation of that individual's prior responses. A common approach constructs this representation from survey transcripts or summaries responses. Prior work shows that compressing long transcripts into shorter LLM-generated summaries does not significantly reduce predictive accuracy, suggesting that information volume is not the primary bottleneck. In this work, we argue that the key limitation is instead structural:how persona information is organized before being provided to thesimulator model. We study this by comparing unstructured summaries with structured persona representations. First, we introduce a hand-craftedschema (BDE: Background, Decision procedure, Evaluation), grounded in consumer-behavior theory, and show that it improves predictive accuracy over raw transcripts by +1.91 percentage points on a homogeneous benchmark (Twin-2K-500), with similar gains on gpt-5.4-mini and Qwen3-8B as robustness checks. However, this fixed structure does not generalizeacross more heterogeneous tasks, where performance is statistically indistinguishable from the raw transcript baseline. To address this limitation, we propose an automatic structure-discovery pipeline in which an LLM iteratively proposes and refines task-specific persona structures and extraction prompts. On a benchmark of 13 diverse sub-studies, this approach restores performance, improving mean accuracy by +1.91 percentage points over the raw transcript baseline and eliminating significant losses observed with the fixed schema. Overall, our results suggest that the main constraint in LLM-based digital twins is not how much information is provided, but how it is structured -- and that the optimal structure depends on the task.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.20344
