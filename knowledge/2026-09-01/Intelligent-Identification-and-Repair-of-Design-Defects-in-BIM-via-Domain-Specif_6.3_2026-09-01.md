# Intelligent Identification and Repair of Design Defects in BIM via Domain-Specific Large Language Models

**评分：** 6.3  
**状态：** 正常  
**标签：** 大模型, RAG, Prompt Engineering, 建筑信息模型(BIM), 领域应用, 工程实践, 论文  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28629v1 Announce Type: new Abstract: Existing methods lack a generalized approach to efficiently identify and resolve the diversity of design defects in BIM. Therefore, this study proposes an integrated framework to identify and repair various defects in BIM via domain-specific LLMs. Firstly, a BIM-to-Text method with component-balanced chunking is introduced to bridge BIM data with LLMs. Then, prompt learning with rule injection, few-shot prompting and RAG is proposed to identify defects and generate repair suggestions. Meanwhile, a hallucination control strategy combining key identifier validation and token-length thresholds is introduced to ensure reliability. Experiments show capability expansion yields 85% identification accuracy versus 70% for traditional rule checking, achieving a 94% rate of reasonable repair suggestions. Moreover, the proposed hallucination control further increased accuracy from 64% to 85%, eliminating 92.5% of hallucinations in a single intervention round. This study establishes an end-to-end prototype from raw BIM data input, through defect identification, to repair suggestion generation.

## 综合总结
本文提出了一个基于领域专属大语言模型的BIM设计缺陷智能识别与修复框架，通过BIM-to-Text转换、提示学习（含规则注入与RAG）以及幻觉控制策略，实现了从原始BIM数据到修复建议生成的端到端流程。实验结果显示该方法在识别准确率和修复合理性上均优于传统规则检查方法，具有较强的工程实践参考价值。技术贡献以已有方法的工程化整合为主，原创性突破有限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文提出了一套基于领域专属大语言模型的BIM设计缺陷识别与修复框架，技术层面包含BIM-to-Text的组件均衡分块方法、融合规则注入与少样本提示及RAG的提示学习策略、以及结合关键标识符验证和token长度阈值的幻觉控制机制。在BIM与LLM结合的工程应用上有一定的方法论创新，但核心技术点（chunking、prompt engineering、RAG、幻觉控制）多为已有技术的组合应用，原创性贡献有限，缺乏深入的模型架构或训练机制层面的创新。

### 实用性 (评分: 7.0/10)
对BIM从业者具有较强的实际参考价值，提供了从原始BIM数据到缺陷识别再到修复建议生成的端到端原型方案。实验中85%的识别准确率和94%的合理修复建议率表明方案具备工程落地潜力，幻觉控制策略将准确率从64%提升至85%的效果也较为显著。该框架适用于建筑设计、工程咨询等领域的实践应用，但通用性、可扩展性以及对复杂BIM场景的适配仍需进一步验证。

### 社区活跃度 (评分: 5.5/10)
arXiv预印本，发布于2026年9月，话题聚焦于BIM与LLM的交叉应用，属于建筑信息化领域的前沿探索，AI社区关注度相对有限。发布时间贴近知识截止日期，具备一定时效性，但来源为预印本未经同行评审，作者团队在BIM领域有一定积累。整体影响力有限，更偏向垂直领域的应用研究。

## 项目链接
https://arxiv.org/abs/2608.28629
