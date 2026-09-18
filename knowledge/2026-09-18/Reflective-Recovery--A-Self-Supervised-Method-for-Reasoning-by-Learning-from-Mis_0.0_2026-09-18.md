# Reflective Recovery: A Self-Supervised Method for Reasoning by Learning from Mistakes

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-18  
**来源：** rss  

## 项目描述
arXiv:2609.19156v1 Announce Type: new Abstract: Data-driven fine-tuning is widely adopted to enhance reasoning in Large Language Models (LLMs) due to its simplicity and efficiency. However, mainstream imitation learning methods that rely exclusively on perfect reasoning trajectories suffer from a Scaling Collapse: when the problem set is limited, increasing positive examples fails to yield continuous improvement. However, during inference, an LLM can not guarantee that every intermediate step is correct and is therefore prone to errors. Once such errors arise, the LLM often struggles to recover and may be further misled by the accumulation of previous mistakes. To address this, we propose Reflective Recovery, a simple yet effective self-supervised approach that transforms failed reasoning attempts into recovery training data. Specifically, we extract initial segments of failed trajectories, concatenate them with prompts, and use them to guide the LLM toward valid solutions. Because these segments from failed trajectories are likely to contain errors, this process teaches models to recognize and correct mistakes during reasoning, enabling recovery from erroneous states without relying on external critics or reward models. Evaluated on extensive benchmarks, Reflective Recovery significantly improves performance. On DeepSeek-R1-Distill-Qwen-7B, it boosts accuracy from 30.0% to 37.5% on AIME 2025 and from 37.6% to 47.8% on Minerva. More importantly, analyses demonstrate that it breaks the scaling collapse barrier and enables models to develop emergent self-correction behaviors, representing a paradigm shift from outcome-oriented memorization to process-oriented reflective reasoning.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.19156
