# Agentic Security: A Systematization of Tools, Failure Modes, and Design Laws for LLM-Driven Penetration Testing

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-26  
**来源：** rss  

## 项目描述
arXiv:2608.21423v1 Announce Type: new Abstract: Agentic security uses large-language-model (LLM) agents to plan, dispatch, and interpret security tools. As these systems move from demonstrations to deployed products, practitioners repeatedly encounter the same operational failures. We systematize these failures through a hands-on evaluation of ten widely used static, dynamic, cloud, orchestration, and AI red-teaming tools for unattended pipelines. We introduce a four-dimensional Integration Friction Index that separates one-time engineering cost from recurring organisational, legal, and maintenance cost. We then derive quantitative regularities that explain recurring failure modes. Modelling an agentic security system as stochastic LLM policies wrapped by a deterministic mediator, we show that long-lived sessions lose resident evidence with phase count, while short-lived sub-agents extend the usable horizon according to the compression ratio between raw evidence and its summary. We show that a two-stage verdict cascade multiplies scorer likelihood ratios, but provides little benefit when scorer errors correlate. We show that treating unevaluable outcomes as attack failures biases downstream measurements toward evasive and severe responses. We formulate planner-versus-worker model routing as a knapsack problem and derive a closed-form execution cap for heavy-tailed tools, eta* = alpha v/c. Finally, we show why scope and budget enforcement cannot be delegated to system prompts: prompts do not constrain what actually executes. Inspectra, our implemented platform, serves as a worked instantiation, with mechanisms labelled shipped, partial, or planned, including those that did not work.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.21423
