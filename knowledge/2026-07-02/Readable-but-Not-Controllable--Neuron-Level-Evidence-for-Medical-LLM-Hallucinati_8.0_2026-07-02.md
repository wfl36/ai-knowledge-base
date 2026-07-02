# Readable but Not Controllable: Neuron-Level Evidence for Medical LLM Hallucination

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 幻觉, 医疗AI, 机械可解释性, 神经元控制, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00158v1 Announce Type: new Abstract: Hallucination remains one of the central obstacles to deploying medical LLMs. Yet, even when hallucination can be detected, it is still unclear whether the internal representations associated with it can be used for control rather than detection alone. Using four open-source models across a suite of medical question-answering datasets, we show that a simple, carefully conditioned probe can reliably detect hallucination, with AUROC scores between 0.77 and 0.86 in our case. We further show that this signal is distributed and redundant rather than narrowly localized. Systematically selected neurons outperform random neurons only at very small subset sizes, whereas random subsets of a few hundred neurons recover nearly the full signal, and low-dimensional random projections preserve most of the detection performance. Beyond detection, we test whether this representation is causally actionable. Across 16 model--dataset combinations, our results reveal a sharp gap between decodability and controllability. The same internal structure that makes hallucination easy to detect does not translate into reliable neuron-level control. These findings show that medical hallucination seems to be readily visible in internal activations, but not easily corrected by steering the neurons most associated with it. More broadly, our results suggest that hallucination mitigation is not simply a matter of identifying the right neurons, and point to a deeper separation between what representations reveal and what they allow us to change.

## 综合总结
本文研究了医疗大模型幻觉的内部表征，发现幻觉信号在神经元中是分布式且冗余的，可通过简单探针高精度检测。然而，研究揭示了一个关键鸿沟：幻觉的‘可解码性’并不等同于‘可控性’，基于神经元的干预无法可靠地纠正幻觉。这表明幻觉缓解并非简单的神经元定位问题，揭示了模型内部表征中‘可见’与‘可变’之间的深层分离。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
研究深度极高，通过严谨的实验设计（4个开源模型、16种模型-数据集组合）揭示了医疗LLM幻觉内部表征的分布式与冗余特性。最核心的洞见在于打破了机械可解释性中‘识别即控制’的乐观假设，明确论证了‘可解码性与可控性之间的鸿沟’，指出内部结构易于检测但难以通过神经元干预纠正，为理解大模型内部运作机制提供了深刻且反直觉的见解。

### 实用性 (评分: 6.5/10)
对工程实践的直接影响偏负向（证明了当前神经元级控制方法在缓解幻觉上失效），但具有极高的‘避坑’参考价值。其提供的幻觉检测探针方法（AUROC达0.77-0.86）可应用于医疗场景的幻觉监控预警；同时，结论提醒从业者不要盲目投入资源于神经元级干预，需转向更高维度的结构或训练策略来缓解幻觉。

### 社区活跃度 (评分: 8.5/10)
医疗AI与幻觉问题是当前大模型安全落地的核心痛点，话题时效性极强。该研究结论对当前机械可解释性社区中‘定位即修复’的倾向构成了有力挑战，具有较高的学术权威性和社区影响力，预计将引发关于模型可控性边界与幻觉本质的广泛讨论。

## 项目链接
https://arxiv.org/abs/2607.00158
