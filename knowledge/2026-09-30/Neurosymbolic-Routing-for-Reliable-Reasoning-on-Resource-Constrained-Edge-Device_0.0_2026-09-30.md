# Neurosymbolic Routing for Reliable Reasoning on Resource-Constrained Edge Devices

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35833v1 Announce Type: new Abstract: Running a language model on edge hardware provides private and low-latency reasoning without a network connection, and yet the small models that fit on such devices are unreliable on the tasks computers are expected to handle well, such as arithmetic, algebra, and formal logic problems. We argue that much of this unreliability is avoidable. Many queries appearing to demand reasoning are in fact structurally deterministic and permit fast and exact symbolic solutions. Therefore, forcing a probabilistic model to approximate them sacrifices accuracy and energy for little benefit. We present a neurosymbolic router that classifies each incoming query and dispatches it to the cheapest correct solver, sending structured tasks to deterministic engines and reserving the small language model (SLM) for open-ended word problems. Instead of hand-coding the routing logic, we learn a deterministic finite automaton (DFA) with the L* grammatical inference algorithm, using the SLM as a membership oracle and labeled data as an equivalence oracle. On a Raspberry Pi 4B (8 GB RAM, no GPU), evaluated on 100 untested prompts from DeepMind Mathematics, GSM8K, and RuleTaker, learned routing attains 100% routing accuracy and 98.3% overall accuracy with a 512-token reasoning budget (93.3% on word problems), compared with 72.0% for the strongest agent baseline, Program-of-Thought, and 58.7% for a tool-calling agent given the same solvers. Since formatted queries never reach the model, the router answers them in 1-11 ms and, in its 30-token configuration, runs 8.8x faster and 2.8x more energy-efficient than Program-of-Thought.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35833
