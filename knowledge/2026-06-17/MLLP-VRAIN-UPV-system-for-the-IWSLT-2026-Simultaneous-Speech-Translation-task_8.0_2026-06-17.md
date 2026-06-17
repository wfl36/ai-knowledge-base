# MLLP-VRAIN UPV system for the IWSLT 2026 Simultaneous Speech Translation task

**评分：** 8.0  
**状态：** 正常  
**标签：** 同声传译, 语音翻译, 大模型, RAG, 工程实践, 比赛系统  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17255v1 Announce Type: new Abstract: This work describes the participation of the MLLP-VRAIN research group in the shared task of the IWSLT 2026 Simultaneous Speech Translation track. Our submission utilizes the recently released Parakeet and Qwen 3.5 models to create a robust, cascaded solution for long-form SimulST through the use of adaptive "black-box" policies. We explore relaxations of these policies to achieve better quality-latency trade-offs. Compared to last year, we participate on all language directions. In addition to this, for the En$\rightarrow${De, It, Zh} directions we also participate in this year's new context track employing a combination of ASR word-boosting and a RAG mechanism of offline pre-translated exemplars to guide generation and enrich our system with domain-specific context. Finally, we provide a detailed latency analysis of our system. Compared to last year, results on the MCIF En$\rightarrow$De test set shows a substantial quality improvement of +5.82 XCOMET-XL. Our context track processing further improves performance by +1.03.

## 综合总结
本文介绍了MLLP-VRAIN团队参加IWSLT 2026同声传译任务的级联系统。该系统利用最新的Parakeet和Qwen 3.5模型，通过自适应黑盒策略及松弛优化实现长语音同传的质量-延迟平衡。同时，针对新上下文赛道，结合ASR词增强与RAG机制有效引入领域上下文。系统在En->De方向较去年提升5.82 XCOMET-XL，上下文机制进一步带来1.03提升，为同传系统的工程落地与优化提供了极具时效性和实用性的参考方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
系统基于最新的Parakeet和Qwen 3.5模型构建级联同传方案，探索了自适应“黑盒”策略的松弛机制以优化质量与延迟的权衡。在上下文赛道中，创新性地结合了ASR词增强与离线预翻译样本的RAG机制，为级联系统引入领域上下文提供了有效解法，技术组合与工程优化具有较高深度。

### 实用性 (评分: 8.5/10)
针对同声传译这一高价值场景，提供了从前沿模型选型、延迟策略优化到上下文引入（RAG+词增强）的完整级联系统构建方案。附带详细的延迟分析，且在长语音同传和特定领域上下文适应上给出了可复现的实践路径，对工业界构建和优化同传系统具有极高的参考价值。

### 社区活跃度 (评分: 8.0/10)
本文为IWSLT 2026同声传译赛道的参赛系统报告，来源权威且时效性极强（采用最新Qwen 3.5模型）。相比去年系统在En->De方向取得+5.82 XCOMET-XL的显著质量提升，上下文机制进一步带来+1.03增益，对语音翻译和同传社区具有积极的示范和参考影响力。

## 项目链接
https://arxiv.org/abs/2606.17255
