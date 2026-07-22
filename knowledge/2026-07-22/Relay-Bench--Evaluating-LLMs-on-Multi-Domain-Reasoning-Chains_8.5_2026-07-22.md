# Relay-Bench: Evaluating LLMs on Multi-Domain Reasoning Chains

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, Agent, 基准测试, 评估, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18438v1 Announce Type: new Abstract: Introducing Relay-Bench, an unsaturated, holistic, text-only benchmark that measures LLMs' ability to complete an assortment of tasks from distinct domains in a single prompt. The leading model, GPT-5.5 (xHigh), scores 43.3%. The test set entirely consists of composite problems: groups of single-domain subproblems that are strung together into challenges that require reasoning across multiple domains in combination. Many of these problems then have layers of complexity added through prompt encoding and deliberate context bloat. Domains tested include visual reasoning, coding, math, information extraction (with a focus on web search), problem-solving, general knowledge, and data analysis. No restrictions are imposed outside of the model harness, and models are explicitly encouraged to leverage code-execution, web searches, and all available tools. All problems are composed of two to thirteen subproblems and do not require multi-modal input or output.

## 综合总结
Relay-Bench 是一个针对大语言模型多领域组合推理能力的新型未饱和基准测试。它通过将不同领域的子问题串联成复合问题，并引入上下文膨胀和提示编码增加难度，同时允许模型调用外部工具。测试结果显示，即使是当时的最强模型 GPT-5.5 也仅获得 43.3% 的得分，揭示了当前 LLM 在处理复杂长程跨域推理任务时的显著不足，为未来 Agent 和推理模型的发展指明了优化方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了‘跨领域组合推理链’的评估新范式，打破了传统单任务基准测试的局限。通过将不同领域的子问题串联，并引入‘上下文膨胀’和‘提示编码’增加干扰，有效测试了模型在复杂长程任务中的抗干扰与推理能力。允许模型调用代码执行和网络搜索等工具，高度契合 Agent 发展趋势。最强模型 GPT-5.5 仅得 43.3%，证明该基准具有极高的区分度和未饱和性。

### 实用性 (评分: 8.0/10)
对大模型研发者和 Agent 应用开发者具有极高的参考价值。直接暴露了当前最强模型在多域组合推理和复杂上下文处理中的短板，为下一代模型的训练优化（尤其是长程规划、工具调用编排和抗干扰能力）提供了明确的指导方向和测试标准。

### 社区活跃度 (评分: 9.0/10)
发布时间标为 2026 年且涉及 GPT-5.5 模型，具有极强的前瞻性和话题热度。当前社区对现有基准测试饱和的担忧日益加深，该论文切中痛点，提出的评估方式更贴近真实复杂场景，极易引发学术界和工业界的广泛关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.18438
