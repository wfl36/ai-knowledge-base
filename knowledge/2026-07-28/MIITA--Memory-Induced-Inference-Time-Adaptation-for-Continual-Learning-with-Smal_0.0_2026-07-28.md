# MIITA: Memory-Induced Inference-Time Adaptation for Continual Learning with Small Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-28  
**来源：** rss  

## 项目描述
arXiv:2607.22556v1 Announce Type: new Abstract: Continual learning (CL) is essential for small language models (SLMs) to adapt to evolving real-world needs in resource-constrained deployments. However, directly updating their limited parameter space causes catastrophic forgetting. While memory-based methods naturally address this by decoupling knowledge retention from parameters, existing approaches designed for large language models (LLMs) rely on abundant storage and strong in-context reasoning that SLMs lack. To address these challenges, we propose MIITA, a Memory-Induced Inference-Time Adaptation framework for supervised CL under constrained storage. MIITA stores supervised experiences as compact correction-direction prototypes with semantic anchors, and retrieves them at inference time using semantic and uncertainty-based cues. The retrieved directions are applied through gated temporary hidden-state adaptation, enabling non-destructive reuse of past supervision without backbone updates, prompt extensions, or test-time backpropagation. A local theoretical analysis links this design to first-order loss reduction, uncertainty-guided retrieval, and directional coverage for retaining old-stage knowledge. Extensive experiments across diverse supervised CL settings show that MIITA consistently improves final performance and mitigates forgetting under fixed memory budgets.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.22556
