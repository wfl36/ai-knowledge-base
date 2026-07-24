# Knowledge Injection Exists in MoE? Exploring Expert-Aware Contrast Decoding in MoE for Mitigating LLMs'Hallucinations

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, MoE, 幻觉缓解, 对比解码, 推理, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20426v1 Announce Type: new Abstract: Existing LLM hallucination mitigation methods, including prompt engineering and model optimization, either hardly alter models'internal knowledge or have poor cross-domain generalization. Contrastive decoding mitigates hallucinations by using layer-wise differences in LLMs. However, prior studies only explore transformer-based models (e.g., GPT), ignoring other effective frameworks like mixture-of-experts (MoE) models. Since MoE alters the traditional transformer architecture, we conduct empirical studies to investigate whether similar layer-wise differences exist in MoEs. Our results show that they do not exist in MoE with shared experts; nevertheless, across different MoEs, higher layers exhibit distinct expert activation patterns between factual and non-factual outputs. Building on these, we propose EAACD, an expert-aware adaptive contrast decoding that uses expert differences in MoE's higher layers to mitigate hallucinations on QA tasks. EAACD splits high-layer experts into a higher-reliability group and several lower-reliability groups based on their confidence and consistency. It contrasts the higher-reliability group's prediction with each lower-reliability group's prediction to calibrate the model's original predictions. To strengthen this contrast, EAACD amplifies hallucinations from lower-reliability experts via attention and masking to provide stronger negative references. EAACD outperforms all baselines on four datasets.

## 综合总结
本文针对大模型幻觉问题，探索了混合专家模型架构在对比解码中的特性。研究发现，传统Transformer的层间差异在带有共享专家的MoE中并不存在，但MoE高层在事实与非事实输出上表现出显著的专家激活模式差异。基于此发现，作者提出了一种专家感知自适应对比解码方法（EAACD），将高层专家按置信度和一致性划分为高/低可靠性组，通过对比两组预测来校准输出，并利用注意力掩码放大低可靠性专家的幻觉作为强负参考。实验表明，EAACD在四个数据集上超越了所有基线，为MoE架构的幻觉缓解提供了新思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文具有较高的研究深度与新颖性。作者敏锐地发现传统基于Transformer的对比解码方法在MoE架构中并不完全适用，特别是揭示了带有共享专家的MoE中不存在传统的层间差异，但高层的专家激活模式在事实与非事实输出间存在显著差异。基于此实证发现，创新性地提出了EAACD方法，将对比解码的粒度从'层间'细化至'专家间'，并通过置信度与一致性划分专家可靠性组，甚至反向利用注意力与掩码放大低可靠性专家的幻觉作为强负参考，论证逻辑严密，技术路径具有显著创新性。

### 实用性 (评分: 7.5/10)
对大模型从业者具有较好的实践指导价值。对比解码方法无需重新训练或微调模型，仅在推理阶段生效，落地成本较低。EAACD针对当前广泛采用的MoE架构（如Mixtral、DeepSeek等）提供了一种即插即用的幻觉缓解方案，特别适用于对事实性要求较高的QA任务。不过，该方法在推理时需要动态计算专家可靠性分组并进行对比解码，会带来一定的推理延迟和工程实现复杂度，需在实际部署中权衡效果与性能。

### 社区活跃度 (评分: 8.0/10)
话题时效性强且极具关注度。MoE架构是当前大模型领域的主流方向，而幻觉问题一直是限制大模型落地的核心痛点，两者的结合研究处于当前社区的风口。论文来源于arXiv，作者团队具备一定学术背景，且在四个数据集上超越了现有基线，具备较高的可信度和潜在影响力，有望引发对MoE架构内部机制及解码策略的进一步探讨。

## 项目链接
https://arxiv.org/abs/2607.20426
