# AlphaDiana: A Measurement System for Agents in Verifiable Reasoning Tasks

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20675v1 Announce Type: new Abstract: Agents pair reasoning models with harnesses that organize model calls, execute tools, load skill instructions, and retain history in memory. Understanding agent performance requires linking execution conditions to outcomes, behavior, and resource use. We introduce AlphaDiana, a measurement system with modular interfaces for datasets, agents, environments, and scorers. It preserves harness-native control loops while controlling file reuse and memory retention separately. AlphaDiana supports macro analyses of complete agents and micro interventions on agent components such as tools, skills, and memory under matched conditions. We study three open-source models and three open-source harnesses on five answer-based benchmarks, with two models also tested on two interactive benchmarks. We find that harnesses do not consistently improve the accuracy of reasoning: gains on questions unsolved by the model alone can be outweighed by losses on questions it answers correctly without tools. This inconsistency extends to component interventions: neither skill guidance nor retained history reliably improves accuracy. Behavior and output-token use must be assessed with correctness: low token entropy can accompany wrong answers, and less output per execution can mean more output tokens per correct answer when accuracy falls. AlphaDiana links answer correctness and execution status to traces and resource records for comparing agents and diagnosing failures under shared task and resource policies.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20675
