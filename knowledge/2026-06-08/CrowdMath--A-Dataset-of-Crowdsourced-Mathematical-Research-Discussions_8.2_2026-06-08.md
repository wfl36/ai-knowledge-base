# CrowdMath: A Dataset of Crowdsourced Mathematical Research Discussions

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 数学推理, 多智能体协作, 数据集, 评估基准, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06526v1 Announce Type: new Abstract: Large language models have made substantial progress on mathematical reasoning, but existing benchmarks typically evaluate well-specified problems with final answers, step-by-step solutions, or complete proofs. They do not capture collaborative open-problem solving: a setting in which participants propose partial arguments, identify gaps or errors in prior steps, repair flawed reasoning, and gradually synthesize incremental contributions into a proof. We introduce CrowdMath, a dataset of 164 expert-annotated progress chains from the MIT PRIMES--Art of Problem Solving (AoPS) CrowdMath program (2016-2025), a collaborative research initiative whose discussions have led to peer-reviewed publications. Each chain traces a multi-participant forum discussion from an open-problem statement to a completed proof. Posts are labeled by their functional roles in the evolving solution process, including partial progress, proof completion, erroneous reasoning, and error identification. We define evaluation tasks and benchmark six frontier models. Models achieve 83-88% accuracy on next-post prediction, suggesting that they can follow the local flow of mathematical discussion. However, they struggle to identify the functional significance of individual contributions with the best model achieving only 0.42 macro-F1 on post-role classification. CrowdMath exposes a gap between solving well-specified mathematical problems and understanding collaborative mathematical progress as it unfolds.

## 综合总结
本文提出了CrowdMath数据集，包含164个来自MIT PRIMES-AoPS项目的专家标注协作数学研究讨论链，首次聚焦于多参与者从开放问题到完整证明的动态协作推理过程。数据集对帖子的功能角色（如部分进展、错误识别、证明完成等）进行了细粒度标注。对6个前沿模型的基准测试表明，尽管模型能较好预测讨论的局部走向（83-88%准确率），但在识别个体贡献的功能意义上表现挣扎（最佳macro-F1仅0.42）。该研究揭示了当前LLM在解决明确数学问题与理解协作数学进展之间存在显著差距，为多智能体协作推理评估提供了重要基准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究在评估范式上具有显著的新颖性和深度。传统数学推理基准仅关注具有明确答案或完整证明的静态问题，而本文首次系统性地构建了针对'协作式开放问题解决'的数据集与评估框架。数据集基于长达10年（2016-2025）的真实专家协作项目，标注了部分进展、错误识别、推理修复等细粒度功能角色，构建严谨。实验设计切中要害，揭示了前沿LLM虽然能捕捉讨论的局部上下文（预测准确率83-88%），但在理解个体贡献的功能意义时表现极差（最佳macro-F1仅0.42），论证极具启发性。

### 实用性 (评分: 7.0/10)
对从事大模型推理、多智能体交互和数学证明辅助的研究者与工程师具有很高的参考价值，为其提供了全新的评估视角和高质量的真实协作数据。然而，数据集规模相对较小（164条进展链），且高度聚焦于高难度数学证明领域，直接泛化应用于通用工业场景（如常规代码协作、客服多轮对话）仍需适配，整体落地适用范围偏向学术研究与特定垂直领域。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，切中当前大模型推理能力评估与多智能体协作两大热点。来源权威性高，依托MIT PRIMES与AoPS项目，且数据集已催生过同行评审出版物，作者团队包含知名学者。该研究指出了当前最强模型在协作推理上的严重缺陷，打破了'LLM数学推理已足够强大'的社区幻觉，预计将在AI推理评估社区产生重要影响力。

## 项目链接
https://arxiv.org/abs/2606.06526
