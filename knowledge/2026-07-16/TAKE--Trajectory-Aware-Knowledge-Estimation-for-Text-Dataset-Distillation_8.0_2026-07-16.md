# TAKE: Trajectory-Aware Knowledge Estimation for Text Dataset Distillation

**评分：** 8.0  
**状态：** 正常  
**标签：** 数据集蒸馏, 数据为中心AI, 影响函数, 最优传输, NLP, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.11898v1 Announce Type: new Abstract: Large-scale text corpora have become a quiet bottleneck in modern NLP, not just in storage, but in the accumulated cost of training, fine-tuning, and continual learning. We propose a text dataset distillation framework that reduces corpora to as little as 0.1% of their original size while preserving downstream task fidelity. We approach distillation through the lens of influence functions, which quantify each sample's contribution to the downstream objective, a natural and principled basis for selection. We introduce Trajectory-Aware Knowledge Estimation (TAKE), which convolves the knowledge-based influence along the training trajectory into a single per-sample knowledge score, capturing informative samples. These scores serve as sample weights within a discrete Optimal Transport objective, guiding prototype selection from a synthetically generated candidate pool. We evaluate TAKE on downstream accuracy across text classification and natural language inference tasks at extreme compression (0.1% or 20 samples/class), showing that data efficiency is achievable without sacrificing task fidelity. The approach is theoretically grounded, with broader implications for coreset construction and data-centric AI. We release our source code at https://github.com/votrinhan88/take.

## 综合总结
本文提出TAKE文本数据集蒸馏框架，通过轨迹感知知识估计量化样本在训练过程中的知识贡献，并结合离散最优传输进行原型选择。该方法在0.1%的极端压缩率下，于文本分类和NLI任务中保持了良好的下游保真度，有效缓解了大规模语料库带来的存储与训练成本问题，为数据高效AI提供了坚实的理论支撑与实用工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出轨迹感知知识估计（TAKE），创新性地将影响函数与模型训练轨迹相结合，量化样本在整个训练过程中的动态知识贡献，并引入离散最优传输理论指导原型选择，方法新颖、理论严谨且论证深入。

### 实用性 (评分: 8.0/10)
在0.1%的极端压缩率下仍能保持下游任务保真度，对降低NLP模型训练与微调成本具有极高的参考价值；已开源代码便于从业者复现与落地，但目前验证主要集中在分类和NLI任务，在复杂生成任务上的适用性有待进一步探索。

### 社区活跃度 (评分: 7.5/10)
聚焦数据集蒸馏与数据为中心的AI，切中当前大模型时代训练成本高昂的痛点，话题时效性强；arXiv首发并附带开源代码，具备较好的学术可信度与社区传播潜力。

## 项目链接
https://arxiv.org/abs/2607.11898
