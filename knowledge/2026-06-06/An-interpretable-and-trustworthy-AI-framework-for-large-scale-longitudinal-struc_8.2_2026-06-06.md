# An interpretable and trustworthy AI framework for large-scale longitudinal structure-pain association studies using data from the Osteoarthritis Initiative (OAI)

**评分：** 8.2  
**状态：** 正常  
**标签：** 医学影像, 可解释AI, 不确定性量化, 骨关节炎, 论文  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05357v1 Announce Type: new Abstract: Purpose: To develop an interpretable and trustworthy AI framework that combines deep learning based MRI Osteoarthritis Knee Score (MOAKS) prediction with interpretable statistical modeling to study structure-pain relationships at scale using data from the Osteoarthritis Initiative (OAI). Materials and Methods: We first developed a deep learning framework to predict MOAKS features directly from knee MRIs and incorporated conformal prediction to provide prediction uncertainty quantification. This uncertainty-aware strategy enables explicit filtering of model outputs, retaining only high-confidence MOAKS predictions at the knee level. Second, we applied a longitudinal latent class mixed model (LCMM) to examine associations between key structural abnormalities and four complementary knee pain measurements. Results: Among the three MRI-defined abnormalities (i.e., bone marrow lesions (BML), cartilage loss (CART), and meniscal extrusion (ME)), our framework substantially improved the Matthews correlation coefficient (MCC) and some other metrics. For example, MCC increased from 0.69 to 0.91 for BML, from 0.45 to 0.80 for CART, and from 0.59 to 0.89 for ME. Using these high-confidence predictions, we expanded the sample size to 2,175 knees for the LCMM analysis. Two distinct pain trajectories were identified (rapid and stable pain progression). The estimated odds ratios (95% CI) for the rapid progression group were 1.62 (1.12-2.35) for BML, 1.83 (1.24-2.70) for CART loss, and 2.50 (1.75-3.57) for ME. Conclusion: These results highlight the importance of these structural abnormalities as risk factors for pain and functional progression in osteoarthritis.

## 综合总结
本文提出一种结合深度学习与可解释统计建模的可信AI框架，用于大规模骨关节炎纵向结构-疼痛关联研究。框架通过深度学习预测MRI上的MOAKS特征，并引入共形预测进行不确定性量化与高置信度过滤，使MCC指标大幅提升；随后利用高置信度数据扩大样本量，通过LCMM模型分析证实了骨髓病变、软骨损失和半月板挤出是疼痛快速进展的重要风险因素。该研究为医学影像到临床统计分析提供了高可靠性的自动化Pipeline。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
该研究将深度学习、共形预测与纵向潜在类别混合模型(LCMM)有效结合，构建了可解释且可信赖的AI框架。技术创新主要体现在引入共形预测对深度学习输出的MOAKS特征进行不确定性量化与高置信度过滤，显著提升了预测的Matthews相关系数(MCC)，为医学影像分析提供了一种严谨的置信度筛选机制，论证逻辑严密。

### 实用性 (评分: 8.5/10)
对医学影像分析和临床流行病学研究具有很高的落地指导价值。该框架提供了一条从影像自动化评估到临床纵向统计分析的完整Pipeline，其不确定性过滤机制能有效解决临床AI应用中误判风险高的问题，可直接复用于其他大规模队列研究中的结构-表型关联分析。

### 社区活跃度 (评分: 8.0/10)
医学影像AI与可解释性/可信AI均是当前学术界关注的热点。共形预测作为不确定性量化的新兴方法，提升了研究的时效性。研究基于权威的OAI数据集，且作者团队包含骨关节炎领域知名专家，来源可信度高，对相关临床与交叉学科社区具有较强的影响力。

## 项目链接
https://arxiv.org/abs/2606.05357
