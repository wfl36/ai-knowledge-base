# Loss-Aware Feature-Map Pruning in Convolutional Neural Networks Using Multi-Armed Bandits

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-28  
**来源：** rss  

## 项目描述
arXiv:2607.22564v1 Announce Type: new Abstract: Convolutional neural networks often contain redundant feature maps that increase storage and inference cost. This paper presents a loss-aware feature-map pruning framework using multi-armed bandits. Feature-map pruning is structured because it removes complete convolutional output channels and their producing filters rather than isolated scalar weights. Each candidate feature map is treated as an arm. At each play time, one map is temporarily masked and evaluated on a sampled mini-batch; the map is then restored and the observed loss change is converted into a safe-removal reward. After a fixed play budget, candidate maps are ranked by learned scores and the top-k maps are permanently removed with their filters, biases and corresponding next-layer input-channel kernels. The study evaluates UCB1 and Thompson Sampling, compares them with direct/oracle-style evaluation on LeNet/MNIST, and extends the evaluation to MNIST, CIFAR-10, CIFAR-100, SVHN, CUB-200-2011 and Oxford Flowers 102. Results show that UCB1 and Thompson Sampling preserve accuracy close to unpruned models while removing feature maps and reducing convolutional computation. Friedman and Nemenyi tests show that UCB1 obtains the highest mean rank, followed by Thompson Sampling; both significantly outperform greedy and magnitude-based pruning while remaining statistically comparable to the original unpruned model.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.22564
