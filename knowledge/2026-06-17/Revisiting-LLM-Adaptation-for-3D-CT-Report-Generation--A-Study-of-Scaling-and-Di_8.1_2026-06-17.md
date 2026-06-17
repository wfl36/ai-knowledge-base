# Revisiting LLM Adaptation for 3D CT Report Generation: A Study of Scaling and Diagnostic Priors

**评分：** 8.1  
**状态：** 正常  
**标签：** 大模型, 多模态, 医疗影像, 报告生成, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17213v1 Announce Type: new Abstract: Recent advances in multimodal learning, including large language models (LLMs) and vision-language models (VLMs), have demonstrated strong adaptability to natural images. However, extending their use to the medical domain, particularly for volumetric (3D) images, is challenging due to high computational complexity, volumetric dependencies and the semantic gap between visual features and clinical terminology. Naively fine-tuning LLMs on limited medical data often leads to overfitting and clinical hallucination, where linguistic fluency is prioritized over clinical factuality. In this study, we investigate parameter-efficient adaptation strategies for volumetric CT report generation and introduce RAD3D-Prefix, a lightweight diagnostic-prior conditioning framework that minimizes the need for extensive parameter training. This module integrates image embeddings with multi-label diagnostic classification logits, preserving critical clinical details while bridging the semantic gap. By keeping the LLM frozen, our method requires minimal trainable parameters and mitigates the risk of overfitting on small, domain-specific datasets. Through a systematic study spanning LLMs from 96.1M to 1.6B parameters, we find that fine-tuning is most beneficial for smaller LLMs, whereas freezing larger (~1B+ LLMs and training only lightweight projection layers provides a superior trade-off between performance, generalization, and computational efficiency. Across multiple automatic metrics and a clinical reader study, RAD3D-Prefix outperforms comparable parameter-efficient baselines and demonstrates strong out-of-domain generalization while using substantially fewer trainable parameters than fully fine-tuned alternatives.

## 综合总结
本文研究了LLM在3D CT报告生成中的适配问题，提出RAD3D-Prefix框架，通过引入多标签诊断先验并冻结LLM参数，有效缓解了临床幻觉与过拟合。跨参数规模的系统实验表明，对于1B+参数的大模型，仅训练轻量投影层优于全量微调。该方法在大幅减少训练参数的同时提升了性能与域外泛化能力，为医疗多模态大模型的高效落地提供了重要范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.8/10)
针对LLM在3D医学影像中易过拟合和产生临床幻觉的问题，提出了RAD3D-Prefix轻量级诊断先验框架。该框架将多标签分类logits与图像嵌入结合，保持LLM冻结，有效弥合了视觉特征与临床术语间的语义鸿沟。研究系统评估了96.1M至1.6B参数的LLM，发现冻结大模型（~1B+）仅训练轻量投影层能在性能、泛化和效率间取得最佳平衡，论证严谨且具有扎实的实证深度。

### 实用性 (评分: 8.5/10)
对医疗AI从业者具有极高的落地指导价值。RAD3D-Prefix模块实现简单，且证明了在有限医疗数据下“冻结大模型+轻量级投影”优于全量微调，大幅降低了计算成本和过拟合风险。其优秀的域外泛化能力和更少的可训练参数需求，为实际临床场景中的资源受限部署提供了极具参考性的实践范式。

### 社区活跃度 (评分: 8.0/10)
研究聚焦于多模态大模型在3D医疗影像领域的适配，属于当前AI+医疗的热点前沿。论文不仅包含常规自动评估指标，还进行了临床读片研究，显著增强了结果的医学可信度。作为arXiv新发论文，时效性强，对医学影像分析及多模态大模型社区具有较好的启发和参考意义。

## 项目链接
https://arxiv.org/abs/2606.17213
