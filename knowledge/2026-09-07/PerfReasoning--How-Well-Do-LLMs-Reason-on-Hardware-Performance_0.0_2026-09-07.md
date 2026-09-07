# PerfReasoning: How Well Do LLMs Reason on Hardware Performance?

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-07  
**来源：** rss  

## 项目描述
arXiv:2609.04476v1 Announce Type: new Abstract: Performance modeling is central to hardware design and software optimization, yet constructing these models requires structured reasoning about computation, data reuse, storage, and movement. We introduce PerfReasoning, a benchmark that evaluates LLMs both as direct performance reasoners and as generators of analytical performance-model code. Given workload, architecture, and mapping specifications, models compare mappings and predict off-chip traffic and buffer requirements. The strongest closed-source models exceed 90% on reasoning-based Q&A, and the best open-weight model reaches 82.4%. However, model construction is substantially harder: while GPT-5.6 Sol exceeds 80% pass rate, all other model configurations average below 15% and vary markedly across runs. Task-specific RL raises a 4B model's mapping-reasoning accuracy by 15.7 points, whereas feedback-free multi-round self-revision prompting is not reliably effective. PerfReasoning exposes the gap between plausible architectural reasoning and reliable performance-model construction. We will publicly release the benchmark to support reproducible evaluation and track future progress.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.04476
