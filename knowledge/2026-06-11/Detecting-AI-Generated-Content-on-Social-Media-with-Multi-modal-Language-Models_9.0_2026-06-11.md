# Detecting AI-Generated Content on Social Media with Multi-modal Language Models

**评分：** 9.0  
**状态：** 正常  
**标签：** AIGC检测, 多模态, 视觉语言模型, 内容安全, 深度伪造, 论文, 工程实践  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11200v1 Announce Type: new Abstract: Generative AI has enabled the creation of photorealistic images and videos that are increasingly disseminated on social media, often used for spam, misinformation, manipulation, and fraud. Existing AI-generated content (AIGC) detection methods face challenges including poor generalization to new generation models, reliance on single modalities, and lack of interpretable explanations. We present our pipeline that mitigates these issues by continuously curating diverse multi-modal social media data and training a compact vision-language model for detection and explanation. Our model achieves state-of-the-art detection performance on public benchmarks and demonstrates robust detection and explanation capabilities on internal social media datasets across multiple platforms. We deployed our model for post recommendation on social media platforms and observed positive downstream impacts on user engagement, demonstrating that it is feasible to perform effective AIGC detection in dynamic, real-world social media environments.

## 综合总结
本文提出了一种基于紧凑型视觉语言模型(VLM)的多模态AIGC检测流水线，通过持续收集多样化的社交媒体数据训练模型，有效解决了现有方法泛化性差、单模态局限和缺乏可解释性的问题。该模型在公开及内部跨平台数据集上均取得SOTA表现，并已成功部署于社交媒体推荐系统，验证了在动态真实环境中进行高效AIGC检测的可行性与业务价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文针对现有AIGC检测方法泛化性差、依赖单一模态及缺乏可解释性三大痛点，创新性地提出通过持续收集多模态数据并训练紧凑型视觉语言模型(VLM)的流水线。该方法不仅在公开基准上达到SOTA，还赋予了检测过程可解释性，技术路线新颖且论证严谨，具备较高的研究深度。

### 实用性 (评分: 9.5/10)
极高的可落地性。该研究不仅停留在学术基准测试，更已实际部署于社交媒体平台的推荐系统中，并验证了对用户参与度的正向业务影响。对于各大内容平台、社交网络及媒体审核机构防范AIGC滥用（如虚假信息、欺诈等），提供了直接可借鉴的工程实践方案和闭环思路。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，AIGC泛滥与深度伪造检测是当前及未来社会与科技界的核心痛点。作者团队阵容庞大且具备明显的工业界背景，结合内部跨平台数据集与真实部署验证，来源权威性与可信度极高，对内容安全领域具有显著的影响力与示范效应。

## 项目链接
https://arxiv.org/abs/2606.11200
