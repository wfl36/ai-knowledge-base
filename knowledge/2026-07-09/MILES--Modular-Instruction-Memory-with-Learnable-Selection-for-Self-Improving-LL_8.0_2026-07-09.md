# MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, 测试时计算, 记忆机制, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06974v1 Announce Type: new Abstract: Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection policies requires large-scale training data and fixed action spaces, making such approaches unsuitable for test-time settings where memory expands incrementally and only limited supervision is available. We propose MILES (Modular Instruction Memory with LEarnable Selection for self-improving LLM reasoning), a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. MILES maintains modular memory units consisting of asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. This memory structure enables a coarse-to-fine retrieval mechanism: The coarse level enables memory expansion and collects supervision for training selection heads from confident samples, while the fine stage applies learned selection heads to rerank coarse-level candidates and guide reasoning for uncertain samples. MILES consistently matches or outperforms prior methods while achieving superior accuracy-efficiency tradeoffs. Extensive experiments demonstrate its effectiveness, robustness, and transferability.

## 综合总结
本文提出MILES框架，用于自我改进的LLM推理。针对测试时推理孤立处理问题及现有记忆方法泛化差、未优化最终正确性的局限，MILES设计了子目标与子指令的非对称模块化记忆单元，并采用粗到细检索机制：粗阶段实现记忆动态扩展与监督收集，细阶段通过可学习选择头重排候选指导推理。该方法在有限监督的测试时约束下实现了正确性优化的记忆组合，实验证明其有效、鲁棒且具可迁移性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对现有LLM测试时推理孤立处理问题、记忆泛化差及启发式选择未优化最终正确性的痛点，提出MILES框架。其创新点在于设计了由子目标嵌入和子指令构成的非对称模块化记忆单元，并引入粗到细的检索机制：粗粒度阶段支持记忆增量扩展并收集高置信样本监督，细粒度阶段利用可学习选择头重排候选以指导低置信样本推理，有效解决了测试时有限监督下的策略学习难题，技术深度与新颖性较高。

### 实用性 (评分: 7.5/10)
该框架为构建具备持续学习和经验积累能力的LLM推理系统提供了新思路，尤其适用于多步复杂推理和Agent场景。粗到细的检索与动态扩展机制对工程实践有较好参考价值，但作为学术模型，实际落地时需考虑记忆库管理开销、检索延迟及与现有LLM推理流程的无缝集成问题。

### 社区活跃度 (评分: 8.0/10)
论文聚焦于当前大模型领域极具热度的“测试时计算”与“自我改进推理”话题，来源为arXiv预印本。其提出的动态记忆与推理优化方法高度契合社区对突破LLM推理能力瓶颈的迫切需求，在当前研究语境下具备较高的关注潜力和影响力。

## 项目链接
https://arxiv.org/abs/2607.06974
