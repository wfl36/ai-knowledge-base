# BaFCo: A Document Understanding Benchmark for Complex Bangla Form Comprehension

**评分：** 7.5  
**状态：** 正常  
**标签：** 多模态, 文档理解, 低资源语言, 基准评测, 关键信息提取, 论文, 数据集  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05614v1 Announce Type: new Abstract: Document comprehension is a challenging yet impactful task for Multimodal Large Language Models, especially as these systems see growing adoption in real-world, human-centric applications. However, this adoption is limited for low-resource languages such as Bangla due to the scarcity of high-quality annotated data. To address this gap, we introduce BaFCo, a benchmark dataset for Bangla form comprehension with a focus on Document Layout Analysis (DLA) and Key Information Extraction (KIE). BaFCo curates 200 multi-page complex Bangladeshi government forms, sourced from across diverse sectors including agriculture, education, banking, and land management. To accurately capture the structural and contextual complexity of these forms, we define a fine-grained annotation schema comprising 26 types of form entities, along with a separate coarse form entity set consisting of 5 types. We evaluate the latest MLLMs from the ChatGPT, Gemini, Claude, Qwen, and Kimi series using zero-shot and chain-of-thought prompts under both low and high reasoning setups. Our results reveal limitations in current MLLMs' ability in comprehending Bangla forms, particularly in accurately localizing highly granular form entities. Our dataset and code is available at: https://huggingface.co/datasets/Mausul/bafco

## 综合总结
本文提出了BaFCo，首个针对复杂孟加拉语表单理解的基准数据集，包含200份多领域政府表单及细/粗粒度双层标注。通过对主流多模态大模型（如GPT、Gemini、Claude等）的全面评估，揭示了现有模型在低资源语言文档细粒度实体定位上的不足，为多语言文档理解的研究与落地提供了重要的评测工具和基线。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
针对低资源语言孟加拉语在多模态文档理解上的数据空白，构建了BaFCo基准数据集。该研究设计了包含26种细粒度和5种粗粒度实体的双层标注模式，精准刻画了复杂政府表单的结构与语境。通过对主流MLLMs在多种提示和推理设置下的全面评估，严谨地揭示了当前模型在低资源语言细粒度实体定位上的显著缺陷，填补了该领域的方法学与实验空白。

### 实用性 (评分: 7.0/10)
对从事多语言大模型和文档理解系统的开发者具有直接参考价值。数据集和代码的开源使得从业者可直接用于模型微调或能力评测，特别是在政务、金融、农业等表单密集型场景的落地应用中，能有效指导多语言系统的优化方向与缺陷排查。

### 社区活跃度 (评分: 8.0/10)
文档理解与多模态大模型是当前AI社区的热点方向，该工作聚焦低资源语言，具有高度的时效性和社会价值。评估涵盖了GPT、Gemini、Claude等最新前沿模型，且数据集已在HuggingFace开源，来源权威可信，对推动多语言AI的公平性和普惠性具有积极影响。

## 项目链接
https://arxiv.org/abs/2607.05614
