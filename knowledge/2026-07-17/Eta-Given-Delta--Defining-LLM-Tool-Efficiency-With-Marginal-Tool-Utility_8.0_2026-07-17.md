# Eta Given Delta: Defining LLM Tool Efficiency With Marginal Tool Utility

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, LLM评估, 工具调用, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14108v1 Announce Type: new Abstract: This paper introduces tool efficiency, a new quantitative metric to evaluate the rate of useful tool calls in an LLM agent trajectory. To ensure that tool efficiency is well-defined, we also introduce marginal tool utility, a new quantitative metric defined per tool call indicating whether a tool is useful or whether it can be safely removed from the tool suite without affecting accuracy while increasing tool efficiency; in this paper, we determine the sign of marginal tool utility for each tool call in a trajectory using LLM-as-a-Judge. While much prior work has been done to develop techniques that improve tool use by LLMs and design evaluation methods measuring efficiency indirectly using accuracy as a proxy, our work is centered on measuring efficiency directly via the quantitative metric proposed in this paper in post hoc trajectory analyses. It is our intention that this work contributes to the frontier of LLM evaluation research as a springboard for future benchmark designs and agent harness engineering (specifically with regards to creating lean tool suites) that optimize for metrics that complement but are distinct from accuracy.

## 综合总结
本文针对LLM Agent工具调用中的冗余问题，创新性地提出了“工具效率”与“边际工具效用”两个定量评估指标，利用LLM-as-a-Judge判定单次工具调用的必要性。该研究打破了传统仅以准确率间接衡量效率的局限，为直接评估和优化Agent工具集精简度提供了新范式，对降低Agent运行成本和延迟具有重要工程指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文创新性地提出了“工具效率”和“边际工具效用”两个定量指标，借鉴经济学边际概念评估LLM Agent轨迹中工具调用的必要性。突破了以往仅以准确率间接代理效率的局限，采用LLM-as-a-Judge进行事后轨迹分析以判定单次调用的效用符号，论证逻辑清晰，视角新颖，填补了Agent行为评估的方法论空白。

### 实用性 (评分: 8.5/10)
对Agent工程实践具有高度参考价值。通过量化工具调用的冗余度，该指标可直接指导开发者精简工具集、优化Agent轨迹，从而有效降低API调用成本和系统延迟，适用范围涵盖所有涉及外部工具调用的LLM应用场景。

### 社区活跃度 (评分: 7.5/10)
话题紧扣当前Agent研究热点，时效性强。作为arXiv预印本，虽未经正式同行评审且作者知名度有限，但提出的评估指标直击社区痛点（Agent冗余调用与成本），有望成为未来基准测试和Agent框架设计的重要参考。

## 项目链接
https://arxiv.org/abs/2607.14108
