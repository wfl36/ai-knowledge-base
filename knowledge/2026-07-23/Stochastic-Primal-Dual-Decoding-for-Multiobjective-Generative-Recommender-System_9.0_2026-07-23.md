# Stochastic Primal-Dual Decoding for Multiobjective Generative Recommender Systems

**评分：** 9.0  
**状态：** 正常  
**标签：** 推荐系统, 生成式模型, 多目标优化, 解码策略, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19357v1 Announce Type: new Abstract: Recent advances in recommender systems (RS) have shown substantial performance gains through generative modelling. In practice, recommendation often involves constructing slates -- ordered lists of items -- that must satisfy multiple objectives beyond relevance, such as constraints defined over item attributes or fairness constraints. Existing multiobjective approaches either rely on post-processing techniques designed for non-generative settings, or incorporate auxiliary objectives directly into model training. The former does not explicitly account for the sequential nature of generative RS, while the latter is often impractical in large-scale systems. We propose a lightweight, inference-time decoding layer that augments autoregressive generative RS to support multiobjective slate generation without modifying or retraining the underlying model. We formulate decoding as an online constrained optimisation problem, where items are selected sequentially, and trade-offs between relevance and auxiliary objectives are adjusted dynamically based on the remaining constraint slack, i.e., how much of each objective remains to be satisfied. This is implemented via a stochastic primal-dual approximation scheme that balances relevance and auxiliary objectives during generation. We provide theoretical guarantees on constraint violation and regret, and evaluate the proposed approach through extensive offline experiments and a large-scale online A/B experiment in a real-world recommender system. Our results show consistent improvements in multiobjective trade-offs, including a +1.8\% gain in the auxiliary objectives achieved at zero cost to user satisfaction.

## 综合总结
本文针对生成式推荐系统中的多目标优化问题，提出了一种轻量级的推理时解码层。该方法将解码过程建模为在线约束优化问题，利用随机原始-对偶近似方案动态平衡相关性与辅助目标，无需修改或重训底层模型。理论分析提供了约束违规和遗憾的保证，且大规模在线A/B实验表明，该方法在用户满意度零损失的情况下实现了辅助目标+1.8%的提升，具有极高的工业落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
将多目标推荐解码重新构建为在线约束优化问题，并引入随机原始-对偶近似算法，无需重训底层模型即可在自回归生成过程中动态平衡相关性与辅助目标。论文提供了约束违规与遗憾的理论保证，技术路径新颖且论证严谨。

### 实用性 (评分: 9.5/10)
具有极高的工程落地价值。提出的推理时解码层无需修改或重训底层生成模型，极大降低了工业界应用多目标优化的改造成本。大规模在线A/B实验验证了其在真实系统中的有效性（辅助目标+1.8%且用户满意度无损），对推荐系统从业者具有直接的指导意义。

### 社区活跃度 (评分: 9.0/10)
生成式推荐系统是当前学术界与工业界的热点，多目标优化是实际落地中的核心痛点。论文结合了理论推导与真实大规模A/B测试，来源可信度极高。其“免重训”的轻量级方案切中工业界痛点，预计将在推荐系统社区产生较大影响力。

## 项目链接
https://arxiv.org/abs/2607.19357
