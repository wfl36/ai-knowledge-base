# MER-R1: Multimodal Emotion Reasoning via Slow-Fast Thinking Synergy

**评分：** 8.0  
**状态：** 正常  
**标签：** 多模态, 情感识别, 强化学习, 推理, 慢快思考, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27652v1 Announce Type: new Abstract: We find that explicit reasoning does not necessarily translate into better multimodal emotion recognition (MER) accuracy, even though it makes predictions more interpretable. Specifically, for reasoning-based MLLMs, fast thinking by triggering direct answers often outperforms slow thinking after deliberative reasoning. Our empirical analyses show that fast thinking improves recall with broader and more confident predictions, whereas slow thinking favors precision through conservative filtering of incorrect categories. Building on these insights, we propose MER-R1, a reinforcement learning framework that turns slow-fast complementarity into explicit optimization. Dual-objective disentanglement separates recall and precision into two optimization signals, allowing them to be jointly optimized rather than traded off against each other. Slow-fast confidence calibration further aligns the final slow-thinking answer with fast-thinking intuition, strengthening correct emotions while suppressing incorrect ones. In this way, MER-R1 unifies the recall-oriented intuition of fast thinking with the precision-oriented selectivity of slow thinking. We further provide theoretical justification for this synergy, showing that it mitigates variance-induced interference during optimization. Extensive experiments on MER-UniBench and MME-Emotion show that MER-R1 achieves state-of-the-art performance and makes reasoning genuinely benefit emotion recognition.

## 综合总结
本文针对多模态情感识别(MER)中显式推理反而降低准确率的现象，揭示了快思考(高召回)与慢思考(高精确)的互补特性，并提出MER-R1强化学习框架。通过双目标解耦与慢快置信度校准机制，实现了召回与精确的联合优化，理论及实验均证明其有效性与SOTA表现，为推理模型在分类任务中的应用提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
文章揭示了多模态情感识别中'慢思考(显式推理)反而不如快思考(直接回答)'的反直觉现象，并深入剖析了快思考偏向高召回率、慢思考偏向高精确率的互补特性。基于此提出MER-R1强化学习框架，通过双目标解耦与慢快置信度校准实现联合优化，并提供了理论证明，技术深度与论证严谨性极高。

### 实用性 (评分: 7.5/10)
多模态情感识别在智能交互、内容分析等场景应用广泛。本文提出的慢快思考协同优化框架，为解决大模型推理过程中的'过度思考'或'推理失效'问题提供了切实可行的工程实践方案，对从业者优化MLLM在分类任务上的表现具有较高参考价值，但强化学习训练流程存在一定的工程门槛。

### 社区活跃度 (评分: 8.0/10)
多模态大模型与System 1/System 2(快/慢思考)机制的结合是当前AI领域的前沿热点，本文顺应了R1系列强化学习推理模型的研究趋势。在MER-UniBench和MME-Emotion等权威基准上达到SOTA，且对推理与识别效果的探讨具有较强启发性，话题时效性和学术可信度均表现优异。

## 项目链接
https://arxiv.org/abs/2606.27652
