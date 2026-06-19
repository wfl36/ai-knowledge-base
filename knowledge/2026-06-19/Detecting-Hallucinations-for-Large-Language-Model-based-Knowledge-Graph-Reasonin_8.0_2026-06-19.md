# Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 幻觉检测, 知识图谱, 图神经网络, 推理, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19351v1 Announce Type: new Abstract: Knowledge graph (KG) reasoning infers new knowledge from existing facts and is widely applied in question answering, recommendation, and decision support. With the rapid development of large language models (LLMs), LLM-based KG reasoning frameworks have become increasingly popular by leveraging retrieved KG information. However, hallucinations in LLMs remain a critical issue. Even when relevant KG knowledge is incorporated, models may still generate incorrect outputs, leading to misinformation and unreliable decisions. Existing hallucination detection methods either focus on LLM internal states or verify consistency with retrieved contexts, but both overlook the structural information in KGs, resulting in suboptimal performance. To address this gap, we propose LUCID, the first halLUcination deteCtIon method for LLM-based knowleDge graph reasoning frameworks. LUCID jointly leverages LLM attention scores, KG semantics, and structural information. Specifically, it extracts node and edge features from attention scores and semantic similarities, and integrates them with KG structure using a graph neural network. We also construct manually annotated benchmark datasets for evaluation. Experiments on nine datasets show that LUCID achieves state of the art performance compared to 15 baselines.

## 综合总结
本文提出了LUCID，首个针对基于LLM的知识图谱推理框架的幻觉检测方法。该方法创新性地结合LLM注意力分数、语义相似度与KG结构信息，利用图神经网络进行幻觉识别，并构建了人工标注基准数据集。实验表明LUCID在9个数据集上达到SOTA，为解决LLM在KG推理中的幻觉问题提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对现有LLM幻觉检测方法在KG推理场景中忽略图结构信息的不足，提出了LUCID方法。该方法创新性地融合了LLM注意力分数、语义相似度与KG结构信息，通过图神经网络进行特征聚合与检测，并构建了人工标注的基准数据集，在9个数据集上击败15个基线，展现了较高的技术深度与严谨性。

### 实用性 (评分: 7.5/10)
该研究直击LLM在KG推理中的可靠性痛点，对提升问答、推荐等系统的可信度具有重要参考价值。但方法依赖提取LLM内部注意力分数（需白盒访问权限）及训练GNN模型，工程落地存在一定门槛，更适合具备模型微调和图计算能力的团队参考。

### 社区活跃度 (评分: 8.0/10)
幻觉检测是当前大模型社区的核心关注点，该论文结合知识图谱推理场景切入，话题时效性极强。作者团队构建了新的基准数据集并进行了充分的对比实验，增强了成果的可信度与影响力，对推动LLM在知识密集型任务中的可靠应用具有积极意义。

## 项目链接
https://arxiv.org/abs/2606.19351
