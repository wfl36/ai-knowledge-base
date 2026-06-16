# Fusion is not one-size-fits-all: Cross-Modal Representation Alignment for Time-to-Event Modeling

**评分：** 8.2  
**状态：** 正常  
**标签：** 多模态, 医疗AI, 生存分析, 基础模型, 表示对齐, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15038v1 Announce Type: new Abstract: Accurate time-to-event (TTE) prediction from multimodal clinical data remains challenging due to modality imbalance and distribution shift. We introduce a foundation model-driven framework for cross-modal representation alignment between CT imaging and longitudinal EHR data, designed to generalize across tasks and institutions. CT and EHR modalities are encoded independently using domain-specific foundation models and aligned in a shared latent space through four principled fusion strategies: late fusion, contrastive alignment, cross-attention, and co-attention. We evaluate two clinically distinct TTE tasks: pulmonary embolism (PE) mortality and cardiovascular disease (CVD) outcomes, on large-scale multi-institutional cohorts (PE: N=3,099 train; 1,098 internal; 435 external; CVD: N=2,951 train; 837 internal; 682 external). Fusion consistently improves concordance index by 1.5-5.4% over unimodal baselines when modalities contribute comparably. Overall, contrastive multimodal fusion, particularly with CLMBR representations, provided the most consistent and statistically robust improvements, especially for PE mortality prediction. For MACE, cross-attention (one-hot) achieved the highest internal performance and image-guided co-attention achieved the best external performance. We therefore introduce a generalizable foundation model-based cross-modal alignment framework and provide the first systematic analysis of fusion behavior under modality imbalance in TTE prediction. Our results establish task-aware multimodal alignment as a necessary design principle for robust generalization and scalable clinical deployment.

## 综合总结
本文提出了一种基于基础模型的跨模态表示对齐框架，用于多模态临床数据的生存时间（TTE）预测。针对模态不平衡和分布偏移问题，研究系统比较了晚期融合、对比对齐、交叉注意力和共注意力四种策略在PE死亡率和CVD结果两个任务上的表现。结果表明，不同任务需要不同的融合策略（如对比融合在PE中表现最佳，而交叉/共注意力在MACE中各有优势），证明了'融合非一刀切'的观点。该研究首次系统分析了TTE预测中模态不平衡下的融合行为，确立了任务感知的多模态对齐是实现鲁棒泛化和临床部署的必要设计原则。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究具有显著的方法论新颖性与技术深度。文章打破了多模态融合'一刀切'的惯性思维，首次系统性地在生存分析（TTE）任务中剖析了模态不平衡对融合策略的影响。技术上，依托领域基础模型独立编码CT与EHR数据，并在共享潜空间中严谨对比了晚期融合、对比对齐、交叉注意力和共注意力四种策略。论证过程扎实，通过大规模多机构内外部验证集证实了不同任务对融合策略的偏好差异，确立了任务感知对齐的必要性。

### 实用性 (评分: 8.0/10)
对医疗AI从业者具有极高的实践指导价值。研究不仅提供了一个可泛化、可扩展的基础模型驱动跨模态对齐框架，更重要的是给出了明确的实践启示：在模态贡献不均衡时如何选择融合策略（如PE预测优选对比融合，MACE预测视场景选交叉/共注意力）。这直接指导了临床多模态模型的架构设计，避免了无效的模态堆砌，为鲁棒泛化和临床部署提供了可操作的路径。

### 社区活跃度 (评分: 8.0/10)
话题时效性强，契合当前医疗AI多模态基础模型的发展趋势。作者团队兼具AI与医学背景，实验基于大规模多中心真实临床队列（超8000例样本），数据可信度极高。虽然目前为arXiv预印本，但其'融合非一刀切'及'任务感知对齐'的观点对医疗多模态社区具有纠偏和引领作用，预计将引发对该领域融合范式更精细化的探讨，具备较高的潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.15038
