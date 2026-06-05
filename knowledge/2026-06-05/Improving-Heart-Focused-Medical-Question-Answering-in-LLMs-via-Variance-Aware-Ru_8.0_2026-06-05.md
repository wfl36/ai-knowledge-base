# Improving Heart-Focused Medical Question Answering in LLMs via Variance-Aware Rubric Rewards with GRPO

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 强化学习, 医疗AI, GRPO, 奖励模型, 论文  
**更新日期：** 2026-06-05  
**来源：** rss  

## 项目描述
arXiv:2606.05174v1 Announce Type: new Abstract: Large Language Models (LLMs) have shown strong promise in healthcare applications. Yet deploying general-purpose models in real-world settings remains difficult due to data privacy constraints, inference costs, and limited suitability for edge or on-device use. These challenges motivate the development of smaller, more efficient models that require robust post-training strategies to ensure reliable medical reasoning. In this work, we investigate Group Relative Policy Optimization (GRPO) for post-training LLMs on heart-focused medical question answering with rubric-based supervision derived from RaR-Medicine. We propose a Variance-Aware Reward Framework that extends the Explicit Aggregation and Implicit Aggregation strategies of Rubrics as Rewards by replacing weighted binary criterion aggregation and single overall Likert-style scoring with continuous analytical reward functions derived from criterion-level rubric outcomes. This formulation provides richer optimization signals for feedback that is sparse, multi-criteria, and difficult to verify automatically, and enables more stable on-policy reinforcement learning. On a held-out heart-related subset of HealthBench, our best GRPO variant improves accuracy from 0.362 to 0.502 and F1 from 0.532 to 0.668 relative to the Qwen3-14B base model, while remaining competitive with GPT-OSS-120B (0.508 accuracy, 0.674 F1). Our findings show that carefully designed rubric-based rewards provide a practical strategy for improving heart-focused medical question answering in LLMs, with potential to extend to other rubric-based tasks.

## 综合总结
本文提出一种基于方差感知量规奖励的GRPO框架，用于提升小模型在心脏医学问答任务中的表现。该框架通过连续解析奖励函数替代传统的离散评分，有效解决了医疗强化学习中反馈稀疏和多准则难以验证的问题。实验表明，该方法使Qwen3-14B模型的准确率和F1分数大幅提升，性能媲美GPT-OSS-120B，为医疗等垂直领域小模型的高效落地提供了极具参考价值的实践方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文针对强化学习中反馈稀疏、多准则且难以自动验证的痛点，提出了方差感知奖励框架。通过引入基于准则级别量规结果的连续解析奖励函数，替代了传统的加权二值聚合和单一Likert式评分，为策略优化提供了更丰富、更稳定的梯度信号。该方法在GRPO算法中的应用展现了较好的技术深度和新颖性，实验论证严谨，14B模型媲美120B模型的结果有力支撑了方法的有效性。

### 实用性 (评分: 8.5/10)
研究直击医疗AI落地痛点（隐私、成本、边缘部署），通过后训练策略显著提升小模型（14B）在垂直医疗场景（心脏科QA）的性能，使其达到大模型（120B）水平，极具工程落地价值。此外，基于量规的奖励设计方法具备良好的通用性，可扩展至其他需要多准则评估的垂直领域，对从业者具有极高的实操指导意义。

### 社区活跃度 (评分: 7.5/10)
GRPO与医疗大模型均为当前AI社区高度关注的热点方向，话题时效性强。文章来源于arXiv，具备一定的学术可信度，且小模型战胜大模型的实验结果具有较好的传播潜力。但作者团队在顶会权威性方面相对常规，且发布时间标注存在异常（2026年），整体影响力和权威性处于中等偏上水平。

## 项目链接
https://arxiv.org/abs/2606.05174
