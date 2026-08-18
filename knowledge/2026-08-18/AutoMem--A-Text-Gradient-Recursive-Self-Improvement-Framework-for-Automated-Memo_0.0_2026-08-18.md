# AutoMem: A Text-Gradient Recursive Self-Improvement Framework for Automated Memory Architectures Search

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-18  
**来源：** rss  

## 项目描述
arXiv:2608.14621v1 Announce Type: new Abstract: Long-term memory is increasingly central to LLM agents, yet memory design remains a highly coupled architecture problem: what to encode, how to store it, how to retrieve it, and how to manage it can vary substantially across tasks and backbone models. We construct a discrete search space with 5 encoders, 5 stores, 6 retrievers, and 4 managers, and show that no single memory architecture consistently dominates: different tasks favor different module combinations, leading to substantial performance gaps. Motivated by this, we propose \textsc{AutoMem}, a text-gradient recursive self-improvement framework for task-adaptive memory architecture search. \textsc{AutoMem} optimizes over the factored space through two components: Experience-Guided Architecture Search, which proposes candidate architectures from historical search trajectories and accumulated reflections, and Failure-Guided Module Diagnosis, which localizes memory-related failures to specific modules and converts them into targeted textual feedback. Experiments on GAIA, WebWalkerQA, and xBench-DeepSearch across two LLM backbones show that \textsc{AutoMem} consistently discovers task-adaptive memory architectures that outperform the strongest human-designed memory baselines, improving accuracy by $2.8$ points on average across six benchmark-backbone settings. Further analysis shows that \textsc{AutoMem} achieves a favorable accuracy-efficiency trade-off, reducing token cost by $14.3\%$ over the strongest accuracy baselines under Qwen3.5-122B-A10B, while also finding stronger architectures than substantially larger random searches within only a few guided iterations.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.14621
