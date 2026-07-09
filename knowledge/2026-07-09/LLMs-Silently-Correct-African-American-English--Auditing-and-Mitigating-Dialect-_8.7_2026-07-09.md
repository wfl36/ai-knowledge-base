# LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, AI伦理, 偏见与公平, 激活引导, NLP  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06845v1 Announce Type: new Abstract: African American English (AAE), a rule-governed dialect spoken by over 30 million people, is routinely misinterpreted and "corrected" by large language models (LLMs). Across six instruction-tuned LLMs (14B to 70B), we show that state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE. We present an end-to-end framework to audit and mitigate this bias. For auditing, we introduce conditional Dialect Group Invariance (cDGI), which isolates true model bias from translator-induced artifacts, and a feature-level localization analysis that identifies which AAE markers most strongly trigger bias; we find that syntactic constructions, especially negative concord (e.g., "ain't nobody"), are universal triggers across all models. For mitigation, we introduce, to our knowledge, the first application of activation steering to dialect bias: a training-free, test-time method that extracts dialect directions via causal tracing and injects them into bias-relevant layers. Activation steering reduces bias 5 to 20 times more than prompting while preserving SAE fluency. To enable this work, we release REAL-AAE , the largest real-AAE parallel corpus to date: 17,479 AAE/SAE/ AAE_back triplets from natural tweets (2 to 6 times larger than prior real-AAE resources), validated automatically (BERTScore F1 = 0.95) and by three native AAE speakers (83.0% semantic agreement).

## 综合总结
本文揭示了LLM系统性将非裔美国英语(AAE)重写为标准美国英语(SAE)的方言偏见，发现否定一致等句法结构是偏见触发点。研究提出了包含审计与缓解的端到端框架：审计端引入cDGI隔离翻译伪影，缓解端首次应用激活引导结合因果追踪，在无需重训模型的情况下，偏见缓解效果比提示词方法提升5-20倍。此外，发布了目前最大的真实AAE平行语料库REAL-AAE。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深入揭示了LLM系统性将非裔美国英语(AAE)“纠正”为标准美国英语(SAE)的方言偏见，创新性地提出了条件方言群不变性(cDGI)以隔离翻译伪影并提取模型真实偏见，通过特征级定位分析发现否定一致等句法结构是偏见的核心触发点。在缓解策略上，首次将激活引导应用于方言偏见，结合因果追踪提取方言方向并注入偏置相关层，该方法无需训练且效果比提示词方法提升5-20倍，技术深度与新颖性极高。

### 实用性 (评分: 8.5/10)
提出的偏见缓解方案基于激活引导，属于免训练的测试时干预方法，对LLM开发者及从业者具有极高的实操价值，可直接集成到现有模型的推理流程中以低成本消除方言偏见，且不损害模型原有的SAE流畅度。同时，论文开源了目前最大的真实AAE平行语料库REAL-AAE，为后续的偏见审计、评测及对齐研究提供了重要的数据基础。

### 社区活跃度 (评分: 8.5/10)
AI公平性与偏见是当前大模型伦理与安全领域的核心热点，方言偏见问题具有强烈的社会现实意义和学术关注度。该研究来自arXiv最新预印本，不仅指出了LLM中普遍存在却常被忽视的“静默纠正”现象，还提供了有效的干预手段，在AI伦理、对齐及NLP社区中具备产生广泛影响的潜力。

## 项目链接
https://arxiv.org/abs/2607.06845
