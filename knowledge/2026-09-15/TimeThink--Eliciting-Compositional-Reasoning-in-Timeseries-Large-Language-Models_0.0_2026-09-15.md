# TimeThink: Eliciting Compositional Reasoning in Timeseries Large Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13457v1 Announce Type: new Abstract: Timeseries multimodal large language models (TS-MLLMs) have recently begun leveraging the reasoning capabilities of large language models (LLMs) for question-answering tasks. However, these models often fail to capture dynamic temporal patterns, providing only implicit reasoning that lacks the underlying explanations critical for high-stakes applications like healthcare. While reinforcement learning (RL)-based timeseries language models aim to address this, they often fall short because they are trained on narrow, in-distribution data and struggle with out-of-distribution compositional questions. To address these challenges, we present TimeThink, a synthetic framework for eliciting compositional timeseries reasoning. Core timeseries primitives (e.g., trend, seasonality) are domain-independent and can be deterministically generated. Guided by this premise, TimeThink first designs a synthetic data generator that produces atomic and composite question-answer pairs, providing objective ground truth with reasoning traces. Building on this framework, TimeThink employs a reinforcement learning with verifiable rewards (RLVR) training strategy that encourages explicit reasoning. Unlike template-reliant methods, this approach enables the model to learn the underlying logic of composition rather than simply imitating traces. Extensive experiments show that TimeThink, trained only on synthetic data, significantly outperforms strong baselines on both synthetic and real-world benchmarks.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13457
