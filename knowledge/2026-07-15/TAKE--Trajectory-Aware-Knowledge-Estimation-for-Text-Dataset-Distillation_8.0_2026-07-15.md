# TAKE: Trajectory-Aware Knowledge Estimation for Text Dataset Distillation

**评分：** 8.0  
**状态：** 正常  
**标签：** 数据集蒸馏, NLP, 影响函数, 最优传输, 以数据为中心的AI, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11898v1 Announce Type: new Abstract: Large-scale text corpora have become a quiet bottleneck in modern NLP, not just in storage, but in the accumulated cost of training, fine-tuning, and continual learning. We propose a text dataset distillation framework that reduces corpora to as little as 0.1% of their original size while preserving downstream task fidelity. We approach distillation through the lens of influence functions, which quantify each sample's contribution to the downstream objective, a natural and principled basis for selection. We introduce Trajectory-Aware Knowledge Estimation (TAKE), which convolves the knowledge-based influence along the training trajectory into a single per-sample knowledge score, capturing informative samples. These scores serve as sample weights within a discrete Optimal Transport objective, guiding prototype selection from a synthetically generated candidate pool. We evaluate TAKE on downstream accuracy across text classification and natural language inference tasks at extreme compression (0.1% or 20 samples/class), showing that data efficiency is achievable without sacrificing task fidelity. The approach is theoretically grounded, with broader implications for coreset construction and data-centric AI. We release our source code at https://github.com/votrinhan88/take.

## 综合总结
本文提出文本数据集蒸馏框架TAKE，通过轨迹感知知识估计将训练轨迹上的知识影响卷积为样本分数，并结合离散最优传输进行原型选择。在0.1%的极端压缩率下，该方法在文本分类和自然语言推断任务中实现了高效的数据压缩且不牺牲任务保真度。研究理论扎实且已开源，为解决大模型训练数据瓶颈和以数据为中心的AI提供了极具价值的新思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文从影响函数的视角出发，创新性地提出了轨迹感知知识估计（TAKE），将训练轨迹上的知识影响卷积为单一样本知识分数，并结合离散最优传输目标从合成候选池中指导原型选择。该方法理论推导扎实，技术栈涵盖了影响函数、轨迹卷积与最优传输，兼具深度与新颖性，有效解决了文本数据集蒸馏中的样本贡献度量难题。

### 实用性 (评分: 8.0/10)
针对NLP领域日益严峻的存储与训练成本瓶颈，该框架提供了可操作的数据集蒸馏方案。在0.1%的极端压缩率（每类仅20个样本）下仍能保持较高的下游任务保真度，对微调数据集精简、核心集构建及持续学习具有极高的实际参考价值。作者已开源代码，进一步提升了工业界与学术界的可复现性与落地可能。

### 社区活跃度 (评分: 7.5/10)
数据集蒸馏与以数据为中心的AI是当前大模型时代降低数据与算力成本的重要研究方向，话题时效性强。论文来自arXiv预印本，虽作者并非顶级业界领袖，但其解决了NLP中数据压缩的痛点问题，理论结合实验的论证方式扎实，具备在数据集蒸馏与核心集构建社区产生广泛影响力的潜力。

## 项目链接
https://arxiv.org/abs/2607.11898
