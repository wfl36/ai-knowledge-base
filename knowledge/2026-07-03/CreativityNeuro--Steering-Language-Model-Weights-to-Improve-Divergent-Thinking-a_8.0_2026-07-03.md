# CreativityNeuro: Steering Language Model Weights to Improve Divergent Thinking and Reduce Mode Collapse

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 创造力, 权重引导, 模式崩溃, 论文  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01433v1 Announce Type: new Abstract: Divergent thinking is a crucial aspect of creativity, yet large language models (LLMs) tend to consistently generate similar responses to open-ended questions, in what has been termed the artificial hivemind effect. Here, we introduce CreativityNeuro, a data-free method for enhancing divergent thinking in LLMs via contrastive weight steering. We evaluate our method across multiple creativity assessments and report several main findings. On the Divergent Association Task (DAT), a vocabulary-space creativity test, CreativityNeuro improves performance by up to 14 human percentile points. Next, in a large-scale human evaluation (N=720) on the Alternative Uses Test (AUT) and the Task Task, CreativityNeuro achieves significant improvements in originality, surprise, and creativity, transferring to longer-form and more open-ended tasks. Importantly, we find that across all three tasks, CreativityNeuro demonstrably reduces measures of mode collapse. Moreover, activation steering achieves comparable performance to CreativityNeuro on the DAT, but it does not transfer to the AUT and Task Task, demonstrating the effectiveness of weight-space steering in generalizing to unseen tasks. In conclusion, CreativityNeuro improves divergent thinking and reduces mode collapse without requiring behavioral data, re-training, or gradient-based fine-tuning, providing a straightforward way to enhance LLM performance in creative domains.

## 综合总结
本文提出了CreativityNeuro，一种无需数据、无需重训的对比权重引导方法，旨在提升大语言模型的发散思维并缓解模式崩溃（人工蜂群效应）。实验表明，该方法在词汇创造力测试（DAT）中提升了14个百分位点，并在大规模人类评估（N=720）的开放性任务（AUT, Task Task）中显著提高了原创性和惊喜度。此外，研究证明权重空间引导比激活空间引导具有更好的跨任务泛化能力，为轻量级增强LLM创造力提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了一种新颖的无数据对比权重引导方法，从权重空间干预LLM的创造力输出。技术深度体现在对权重空间与激活空间引导泛化差异的深入对比分析，论证严谨，结合了认知科学经典测试（DAT, AUT）与大规模人类评估，有效验证了方法在缓解模式崩溃和提升发散思维上的机制与效果。

### 实用性 (评分: 7.5/10)
对解决LLM在开放域生成中普遍存在的同质化输出（人工蜂群效应）具有较高实用价值。该方法无需行为数据、重训或梯度微调，落地成本低，可直接应用于创意写作、头脑风暴等需要高发散性的业务场景，但在事实性要求严格的场景需谨慎权衡。

### 社区活跃度 (评分: 8.0/10)
切中当前LLM同质化输出的行业痛点，话题时效性强。作者团队背景扎实，评估体系结合了标准化测试与大规模人类评测（N=720），来源可信度高。该研究为模型干预和创造力对齐提供了新思路，有望在AI创意生成和模型调控社区引起广泛关注。

## 项目链接
https://arxiv.org/abs/2607.01433
