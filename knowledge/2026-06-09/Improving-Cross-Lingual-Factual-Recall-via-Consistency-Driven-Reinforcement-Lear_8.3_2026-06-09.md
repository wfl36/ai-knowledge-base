# Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 多语言, 强化学习, 事实一致性, 机制可解释性, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06586v1 Announce Type: new Abstract: Large language models (LLMs) trained predominantly on English data encode substantial world knowledge, yet often fail to express it reliably in other languages, a phenomenon known as cross-lingual factual inconsistency. To study and address this, we introduce PolyFact, a large-scale parallel multilingual factual QA dataset containing 100K Wikidata-grounded facts across 12 typologically diverse languages. Using PolyFact, we compare light continual pretraining (CPT), supervised fine-tuning (SFT), and reinforcement learning via Group Relative Policy Optimization (GRPO) for improving cross-lingual factual recall in Qwen-2.5-7B and OLMo-2-1124-7B. We find that GRPO consistently outperforms SFT, improving both cross-lingual consistency and generalization to unseen languages, while CPT on parallel data yields limited additional gains. Mechanistic analyses further show that GRPO reorganizes multilingual routing by reducing language specialization in MLP layers and attention heads, thereby promoting more shared cross-lingual representations. We release our code, models, and dataset.

## 综合总结
本文针对大模型跨语言事实不一致问题，构建了PolyFact多语言平行QA数据集，并系统比较了CPT、SFT和GRPO三种方法。实验表明GRPO效果显著优于SFT，且能泛化至未见语言；机制分析进一步揭示GRPO通过减少模型内部的语言特化来增强跨语言共享表征。该研究为多语言对齐提供了高效范式与开源资源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对LLM跨语言事实不一致问题，创新性地对比了CPT、SFT与GRPO（强化学习）。技术深度突出体现在机制可解释性分析上，揭示了GRPO通过减少MLP与注意力头的语言特化来促进跨语言共享表征的内在机理，论证严谨且具有启发意义。

### 实用性 (评分: 8.0/10)
对多语言模型从业者极具参考价值。证实了GRPO在跨语言事实召回和对未见语言泛化上优于传统SFT，提供了明确的技术路径。同时开源的10万级PolyFact数据集及代码，可直接用于指导多语言对齐与事实注入实践。

### 社区活跃度 (评分: 8.5/10)
紧扣当前大模型后训练与GRPO强化学习的热点，直击多语言模型跨语言知识表达不一致的痛点。来源为arXiv新文，作者包含知名NLP学者，且开源了高质量数据集与模型，在学术与工业界具备较高关注度和影响力。

## 项目链接
https://arxiv.org/abs/2606.06586
