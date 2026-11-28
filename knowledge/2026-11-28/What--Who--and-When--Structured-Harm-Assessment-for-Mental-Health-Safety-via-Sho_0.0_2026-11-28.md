# What, Who, and When: Structured Harm Assessment for Mental Health Safety via Short Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-28  
**来源：** rss  

## 项目描述
arXiv:2611.33263v1 Announce Type: new Abstract: The growing use of large language models (LLMs) for mental health support raises important safety concerns. Existing guard models primarily identify categories of harmful content, often overlooking the context needed to determine an appropriate response. We introduce a clinically grounded taxonomy that characterizes harm along three dimensions: what the harm is, who is involved, and when it occurs. It further separates harm characterization from intervention decisions, thus enabling safety policies to be specified outside the model weights through explicit, clinician-curated instructions that can be updated and audited. We validate the taxonomy with expert clinicians and validate a panel of LLM judges to scale annotation. Relabeling public benchmarks in this taxonomy shows that they rarely contain harm directed at the user, which accounts for nearly half of the harm in real conversations. We then train MindGuard2, a 35B-A3B reasoning-based guard model using supervised fine-tuning on short reasoning traces followed by reinforcement learning with a reasoning-length penalty, to minimize inference overhead while preserving the benefits of reasoning. On two public benchmarks and real-world conversations, MindGuard2 achieves balanced accuracy comparable to the substantially larger GLM-5.3 at approximately 10x lower median latency, advancing the accuracy-latency Pareto frontier. Furthermore, it achieves low false-positive rates at high recall, helping balance the need to detect unsafe situations against the risk of unnecessary interventions that may disrupt support and undermine user trust. We release a safety guardrail model with SOTA performance trained on synthetic data, together with synthetic conversations and annotations of public benchmarks in our taxonomy.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.33263
