# Agent-Controlled Forgetting for Tool-Using Agents: Reversible Context Curation in Practice

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10590v1 Announce Type: new Abstract: Tool-using agents repeatedly carry observations whose useful content can be much smaller than their original payload. We study agent-controlled forgetting: the acting model selects previously observed tool results, replaces each with a short note at its original position, and retains the exact original in a recoverable archive. A Python harness exposes batch archival and explicit recovery without task-specific model training, while protecting user instructions and assistant messages from these operations. In an exploratory OpenTelemetry debugging case followed by an unrelated implementation task, the method ended with 231,951 provider-reported prompt tokens versus 912,492 under retained history, used 50% fewer cumulative input tokens, and had an estimated API cost of USD 1.28-1.44 versus approximately USD 4.38. Both arms passed the two-case primary behavioral oracle; neither fully satisfied the follow-up evaluation. The method made more requests and took 17% longer. A contrasting application-development pair produced no context or cost saving, and an earlier continuation exhibited lower manually assessed quality despite reduced context. These observations demonstrate substantial resource savings in noisy tool-use trajectories and identify workload dependence as a central consideration for reversible context management.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10590
