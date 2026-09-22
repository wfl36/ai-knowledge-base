# LoRA Enhanced Contrastive Learning with SAS Vision Transformers

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.21061v1 Announce Type: new Abstract: Automatic target recognition (ATR) with synthetic aperture sonar (SAS) supports advanced naval capabilities, but deep learning is constrained by scarce target imagery, background clutter, and human-in-the-loop assessment. We adapt DINOv3 Vision Transformer (ViT) models to underwater SAS ATR using a three-stage parameter-efficient framework. Stage 1 uses Low-Rank Adaptation (LoRA) while freezing the ViT backbone, bridging the gap between natural-image pretraining and underwater acoustic propagation. Stage 2 uses hard-negative mining to strengthen the decision boundary against acoustic mimics, including rocks and sediment formations resembling man-made targets. Stage 3 uses Supervised Contrastive Learning (SupCon) to separate target and clutter representations. We evaluate at-sea SAS data using a mission-level geographic split, compare all arms at 85 percent test recall, and repeat each comparison over three random seeds. LoRA accounts for the primary effect, increasing area under the precision-recall curve (AUPRC) from 0.300 to 0.679 +/- 0.027 using the same frozen backbone. Rank 4 achieves this result while training only 0.26 percent of weights. Neither refinement stage exceeds its matched control: hard-negative mining changes AUPRC by -0.0045 +/- 0.0119 versus an equal-size random curriculum, and SupCon changes AUPRC by +0.0002 +/- 0.0096 versus the preceding stage. These null results indicate that mining occurred on data the encoder had already fit and that supervised stages had already imposed most target-clutter geometry. One efficient adaptation stage is sufficient; stacked refinement is not.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.21061
