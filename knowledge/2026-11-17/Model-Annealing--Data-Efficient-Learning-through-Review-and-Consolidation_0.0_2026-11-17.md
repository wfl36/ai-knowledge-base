# Model Annealing: Data-Efficient Learning through Review and Consolidation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-17  
**来源：** rss  

## 项目描述
arXiv:2611.17524v1 Announce Type: new Abstract: A small labelled dataset is memorized long before the training budget runs out, and the one-hot labels that remain to be fitted then mostly sharpen confidence. Model annealing spends the rest of the budget on review and consolidation, relearning from the network's own knowledge. Training is divided into episodes whose learning rate is raised again and cooled, every cooled state joins a memory of past selves, and each new episode learns from the labels, from the tempered predictions of this memory, and from adversarial dreams sought where student and memory disagree most. The memory averages predictions rather than weights, and the deployed network is the last student, so inference costs nothing extra. Across CIFAR-100, Tiny-ImageNet and Imagewoof, four architecture families and 5\% to 100\% of the labels, model annealing raises the top-1 accuracy of the AdamW-trained ConvNeXt, ViT and MLP-Mixer over cross-entropy training in 28 of 33 configurations, by 1.3 points on average, and is on par in accuracy with snapshot distillation, the closest competitor. On these families it is better than both in likelihood, calibration and robustness to corruptions and small adversarial perturbations. For an SGD-trained ResNet-18 it lowers accuracy but still improves robustness to small adversarial perturbations. Separating the reheated schedule from relearning shows that relearning helps every family and that the losses come from reheats, which undo most of this network's fit to its training set. How early the accuracy of a cross-entropy run saturates largely separates the AdamW families from ResNet-18 but does not predict the gain within them. With little data, relearning from the latest snapshot without dreams, as snapshot distillation does, compounds overconfidence in the AdamW families from episode to episode. The memory and the dreams each curb most of this drift, and together they remove it.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.17524
