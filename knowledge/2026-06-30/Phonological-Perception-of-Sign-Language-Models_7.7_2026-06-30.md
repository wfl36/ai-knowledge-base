# Phonological Perception of Sign Language Models

**评分：** 7.7  
**状态：** 正常  
**标签：** 手语识别, 机制可解释性, 多模态, 音韵学, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28667v1 Announce Type: new Abstract: Sign languages are compositional systems where meaning arises by combining sublexical phonological parameters, such as handshape, location, and movement. While deep learning models for Sign Language Recognition (SLR) have achieved increased performance on translation benchmarks, it remains unclear whether these models distinguish abstract phonological features or merely rely on low-level statistical correlations. This work evaluates the phonological perception of SLR models trained on American Sign Language (ASL) by probing phonological sensitivity using minimal pairs and evaluating representational alignment with human behavioral data. Our results reveal that SLR models exhibit emergent phonological sensitivity, but with clear architectural trade-offs: pose-based models are sensitive to handshape contrasts, while pixel-based models better capture location changes. Furthermore, pose-based models learn latent representations that correlate with human perceptual similarity judgments (r~0.49). These findings suggest that while SLR models exhibit emergent phonology, current training paradigms are insufficient to scale them beyond their architectural inductive biases.

## 综合总结
本研究探讨了手语识别(SLR)模型是否真正理解手语的音韵特征。通过最小对立对探测和人类行为对齐实验，发现SLR模型虽涌现出音韵敏感性，但受限于架构归纳偏置：基于姿态的模型擅长手形识别且与人类感知更对齐，基于像素的模型则更擅长捕捉位置变化。这表明当前训练范式难以突破架构限制，为未来多模态融合的手语模型设计提供了重要理论依据。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文从语言学音韵学视角切入，使用最小对立对和人类行为对齐实验，严谨地评估了SLR模型的内部表征。揭示了模型涌现音韵感知能力的同时，存在显著的架构归纳偏置差异（pose-based擅长手形，pixel-based擅长位置），技术深度和理论洞见极高。

### 实用性 (评分: 6.5/10)
研究结论指出了当前单一架构的局限性，为未来手语模型设计（如融合姿态与像素的多模态架构）提供了理论指导，但作为基础机制可解释性研究，对工程实践的短期直接落地价值相对有限。

### 社区活跃度 (评分: 8.0/10)
手语识别是AI向善和具身智能的重要分支，探讨模型是否具备类似人类的音韵感知契合当前大模型机制可解释性的热点趋势，arXiv首发，具备较高的学术关注度和权威性。

## 项目链接
https://arxiv.org/abs/2606.28667
