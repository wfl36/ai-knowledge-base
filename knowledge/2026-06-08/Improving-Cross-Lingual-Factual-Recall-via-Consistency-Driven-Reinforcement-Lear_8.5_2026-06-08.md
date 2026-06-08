# Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 多语言, 强化学习, GRPO, 机制分析, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06586v1 Announce Type: new Abstract: Large language models (LLMs) trained predominantly on English data encode substantial world knowledge, yet often fail to express it reliably in other languages, a phenomenon known as cross-lingual factual inconsistency. To study and address this, we introduce PolyFact, a large-scale parallel multilingual factual QA dataset containing 100K Wikidata-grounded facts across 12 typologically diverse languages. Using PolyFact, we compare light continual pretraining (CPT), supervised fine-tuning (SFT), and reinforcement learning via Group Relative Policy Optimization (GRPO) for improving cross-lingual factual recall in Qwen-2.5-7B and OLMo-2-1124-7B. We find that GRPO consistently outperforms SFT, improving both cross-lingual consistency and generalization to unseen languages, while CPT on parallel data yields limited additional gains. Mechanistic analyses further show that GRPO reorganizes multilingual routing by reducing language specialization in MLP layers and attention heads, thereby promoting more shared cross-lingual representations. We release our code, models, and dataset.

## 综合总结
本文针对大模型跨语言事实不一致问题，提出了PolyFact多语言平行事实QA数据集，并对比了CPT、SFT和GRPO三种方法。实验表明，基于强化学习的GRPO方法在Qwen和OLMo模型上均显著优于SFT，不仅提升了跨语言一致性，还增强了对未见语言的泛化能力。机制分析进一步揭示，GRPO通过减少模型内部的语言特化路由，促进了跨语言共享表示。该研究为多语言模型的知识对齐提供了新范式，并开源了数据与代码。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该研究在跨语言事实一致性问题上具有显著的新颖性和深度。创新性地将强化学习（GRPO）引入跨语言知识对齐，并证明其优于传统的CPT和SFT方法。尤为突出的是其机制分析，揭示了GRPO通过降低MLP层和注意力头中的语言特化，促进了跨语言共享表示的形成，从机理层面解释了RL方法的有效性，论证严谨且洞见深刻。

### 实用性 (评分: 8.5/10)
对多语言大模型研发者具有极高的实践指导价值。研究明确指出在跨语言事实对齐任务中，GRPO比SFT泛化性更强，且CPT收益有限，这直接为训练策略选择提供了数据支撑。同时，开源的PolyFact数据集（10万条、12种语言）及代码模型，使得从业者能够立即复现并应用于出海/国际化多语言模型的优化中。

### 社区活跃度 (评分: 8.0/10)
跨语言事实不一致是当前LLM全球化部署的核心痛点，该研究切中时弊，时效性极强。作者来自知名机构且论文发布于arXiv，开源了高质量数据集与模型，具备较高的权威性与社区影响力，有望成为多语言对齐领域的重要参考。

## 项目链接
https://arxiv.org/abs/2606.06586
