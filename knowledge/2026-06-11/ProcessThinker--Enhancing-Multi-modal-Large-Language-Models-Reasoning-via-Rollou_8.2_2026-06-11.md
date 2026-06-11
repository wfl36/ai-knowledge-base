# ProcessThinker: Enhancing Multi-modal Large Language Models Reasoning via Rollout-based Process Reward

**评分：** 8.2  
**状态：** 正常  
**标签：** 多模态, 推理, 强化学习, 过程奖励模型, RLVR, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11209v1 Announce Type: new Abstract: Visual question answering increasingly requires multi-step reasoning. Recent post-training with reinforcement learning under verifiable rewards (RLVR) and Group Relative Policy Optimization (GRPO) can improve multimodal reasoning, but most approaches rely on sparse outcome-only rewards. As a result, they struggle to tell whether an incorrect answer comes from a small mistake late in the reasoning or from an unhelpful trajectory from the start. A common solution is to train a process reward model (PRM) for step-level supervision, but this typically requires large-scale high-quality chain-of-thought annotations and additional training cost. We propose ProcessThinker, a practical post-training pipeline that provides step-level process rewards without training an explicit PRM. ProcessThinker first rewrites reasoning traces into a step-tagged format for cold-start supervised fine-tuning, then applies GRPO with a standard format reward and our rollout-based process reward. Concretely, for each intermediate step, we sample multiple continuations from that step and use the empirical success rate (final-answer verification) as the step reward. This gives dense credit assignment and encourages reasoning steps that more reliably support a correct conclusion, helping reduce inconsistent or self-contradictory progress across steps -- a key issue in logical reasoning. Across four challenging video benchmarks (Video-MMMU, MMVU, VideoMathQA, and LongVideoBench), ProcessThinker consistently improves over the baseline model Qwen3-VL-8B-Instruct

## 综合总结
ProcessThinker提出了一种无需显式训练过程奖励模型（PRM）的多模态推理后训练管线。针对稀疏结果奖励无法精确定位推理错误及PRM标注成本高的问题，该方法通过在中间步骤进行多次rollout采样，并以最终答案验证的经验成功率作为步骤级过程奖励，实现了密集的信用分配。实验表明，该方法在多个视频推理基准上显著提升了Qwen3-VL模型的性能，为多模态复杂推理提供了一种高效且低成本的监督范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文针对多模态推理中稀疏结果奖励无法定位推理错误，以及传统过程奖励模型（PRM）标注与训练成本高的问题，提出了一种巧妙的替代方案：基于rollout的过程奖励。通过在中间步骤采样多次续写，并以最终答案验证的经验成功率作为该步骤的奖励，实现了无需显式PRM的密集信用分配。该方法在算法设计上具有较高新颖性，有效缓解了多步推理中的步骤不一致和自相矛盾问题，论证严谨且切中痛点。

### 实用性 (评分: 7.5/10)
对从业者具有较高参考价值，无需构建昂贵的步骤级标注数据和训练独立的PRM，降低了过程监督的门槛。然而，在训练或推理阶段对每个中间步骤进行多次采样验证，会带来显著的算力和时间开销。该方案适用于对推理质量要求极高且算力资源充足的应用场景，在实际大规模落地部署时需权衡计算成本与收益。

### 社区活跃度 (评分: 8.5/10)
多模态大模型推理与强化学习微调（RLVR/GRPO）是当前AI社区的核心热点，该论文发布于2026年，时效性极强。作者团队包含知名学者Volker Tresp，且在Video-MMMU等四个极具挑战性的视频推理基准上进行了充分验证，基于Qwen3-VL的基线也极具代表性，预计将在多模态推理和对齐领域引起广泛关注。

## 项目链接
https://arxiv.org/abs/2606.11209
