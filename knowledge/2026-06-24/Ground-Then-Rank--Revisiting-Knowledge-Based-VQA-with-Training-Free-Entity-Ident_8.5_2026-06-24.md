# Ground Then Rank: Revisiting Knowledge-Based VQA with Training-Free Entity Identification

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 多模态, RAG, VQA, 论文  
**更新日期：** 2026-06-24  
**来源：** rss  

## 项目描述
arXiv:2606.23881v1 Announce Type: new Abstract: Knowledge-Based Visual Question Answering (KB-VQA) requires grounding visual queries to external knowledge beyond directly observable content in images. While recent multi modal large language models (MLLMs) show strong perceptual abilities, they struggle on KB-VQA tasks requiring groundings from both fine-grained entity and evidence levels. Most existing multi-modal retrieval augmented generation (MM-RAG) methods tightly couple entity discrimination and section-level evidence ranking into a single re-ranking stage, leading to high cost and limited generalization. In this work, we revisit existing MM-RAG solutions from a workflow perspective and argue both entity-level and fact-level groundings are key bottlenecks. We observe that although MLLMs often fail under open-ended entity naming, they can better identify the correct entity when selecting from a small set of candidate names. Based on this insight, we propose a simple and training-free identify-before-answer IBA framework that decouples entity identification from section-level re-ranking. Our approach prompts an MLLM to select high-confidence entities using only candidate names, followed by an off-the-shelf textual re-ranker for evidence selection. Experiments on Encyclopedic-VQA and InfoSeek show that our method consistently outperforms fine-tuned multi-modal re-ranking baselines while reducing training and inference complexity. Additional analyses reveal that the improvements arise not only from better entity identification, but also from selecting more informative evidence once correct entity is fixed. Our implementation is made public to ease reproducibility.

## 综合总结
本文针对基于知识的视觉问答(KB-VQA)中多模态RAG方法耦合实体判别与证据排序导致成本高、泛化差的问题，提出了无需训练的IBA(identify-before-answer)框架。该框架利用MLLM在候选集中选择实体的优势，将实体识别与证据重排解耦，先识别高置信度实体再进行文本重排。实验表明，该方法在降低复杂度的同时超越了微调基线，且代码已开源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
深入分析了KB-VQA中现有MM-RAG方法将实体判别与证据排序耦合的局限性，基于MLLM在候选集选择上优于开放式命名的洞察，创新性地提出了解耦的IBA框架，论证严谨且揭示了性能提升的双重来源（实体识别与证据选择）。

### 实用性 (评分: 9.0/10)
提出的IBA框架无需训练，采用即插即用的设计，利用现成文本重排器，显著降低了训练和推理复杂度。在标准数据集上优于微调基线，对多模态RAG和VQA系统的工程落地具有极高的参考和直接应用价值。

### 社区活跃度 (评分: 8.5/10)
针对当前热门的多模态大模型和RAG技术痛点，提出了高效简洁的解决方案。论文开源了实现代码，增强了可复现性，在KB-VQA社区具有较好的时效性和可信度，有望引发对RAG工作流解耦的进一步探讨。

## 项目链接
https://arxiv.org/abs/2606.23881
