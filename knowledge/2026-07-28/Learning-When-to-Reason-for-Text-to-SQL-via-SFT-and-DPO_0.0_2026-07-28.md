# Learning When to Reason for Text-to-SQL via SFT and DPO

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-28  
**来源：** rss  

## 项目描述
arXiv:2607.22622v1 Announce Type: new Abstract: Recent Text-to-SQL methods rely heavily on reasoning-centric paradigms such as Chain-of-Thought (CoT), achieving substantial gains on complex benchmarks at the cost of high inference-time overhead. However, a large fraction of real-world queries are simple lookups or aggregations that can be resolved without multi-step deduction, making forced reasoning wasteful. Thus, we propose AutoThinkSQL, a framework that integrates an auto-thinking mechanism into both Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) on Text-to-SQL. Our approach enables the model to dynamically bypass reasoning for simple queries while invoking deep CoT for complex queries. On Qwen3-Coder-30B-A3B, our method achieves consistent gains compared to the best counterpart baseline on both Spider and BIRD benchmarks while simultaneously reducing average output tokens by 24.6% and 18.3%, and average latency by 17.1% and 11.5% compared to CoT-only generation. Further analysis indicates that the model learns to align its reasoning decisions with query difficulty.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.22622
