# Low Resource Multimodal Translation of Nepali Spoken Words into Emotion-Conditioned Sign Language Avatars

**评分：** 5.7  
**状态：** 待复核  
**标签：** 多模态, 手语翻译, 低资源语言, 语音识别, 情感计算, 虚拟人, 论文, 概念验证  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26107v1 Announce Type: new Abstract: Sign language communication systems, that integrate emotional expression remain underexplored, particularly for low-resource languages. This pilot study presents NEST-V1 (Nepali Emotion and Speech Transformer - Version 1), a proof-of-concept multimodal framework that demonstrates the feasibility of generating emotion-conditioned Nepali Sign Language avatars from spoken input. As a preliminary investigation, we focus on four common Nepali words ("thank you", "hello", "house", "me") across three emotional states (happy, neutral, sad) to validate our core technical approach. Our lightweight architecture employs a shared acoustic encoder for simultaneous Automatic Speech Recognition and emotion classification, achieving 81.1% ASR accuracy and 79.21% emotion recognition accuracy on a dataset of 600 labeled audio samples from 50 speakers. The system demonstrates 37% parameter efficiency compared to separate model architectures while maintaining a lightweight footprint with only 22.1M parameters suitable for edge deployment. This pilot work establishes the technical foundation for emotion-aware sign language translation in low-resource settings and provides a scalable framework for future expansion to larger vocabularies and more diverse emotional expressions. Our preliminary results indicate the viability of real-time, emotionally expressive sign language communication systems for the hearing-impaired community, with clear pathways for enhancement in subsequent development phases.

## 综合总结
本文提出了NEST-V1，一个针对低资源语言（尼泊尔语）的情感条件手语虚拟人翻译框架。该研究采用共享声学编码器实现ASR与情感识别的多任务学习，在仅22.1M参数的轻量级架构下实现了37%的参数效率提升，适合边缘部署。尽管在600个样本上取得了不错的识别准确率，但目前仅为验证4个词汇和3种情感的概念验证阶段，为低资源环境下的实时情感手语翻译系统奠定了初步基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
提出了一种轻量级的多任务学习架构，通过共享声学编码器同时处理语音识别（ASR）和情感分类，实现了37%的参数效率提升。但该研究目前仅为概念验证阶段，仅覆盖4个词汇和3种情感状态，技术验证规模极小，深度有限。

### 实用性 (评分: 5.0/10)
模型仅22.1M参数，具备边缘部署的潜力，为低资源语言的情感手语翻译提供了可扩展的工程框架。然而，当前系统仅能处理4个特定词汇，完全无法满足实际交流需求，距离真正的产品落地还有很长的路要走。

### 社区活跃度 (评分: 6.0/10)
关注低资源语言（尼泊尔语）和听障群体的情感表达需求，具有较好的社会意义和话题时效性。但作为arXiv上的初步预印本，作者影响力较弱，且验证规模过小，目前的社区影响力和可信度一般。

## 项目链接
https://arxiv.org/abs/2606.26107
