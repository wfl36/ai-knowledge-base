# Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution

**评分：** 8.2  
**状态：** 正常  
**标签：** 可解释性, SAE, 长上下文, 归因, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28548v1 Announce Type: new Abstract: Sparse autoencoders (SAEs) have become a useful tool for extracting interpretable features in language models. However, standard SAE architectures operate on individual token activations, meaning that the number of active features scales linearly with context length, and studying long model transcripts becomes difficult. We introduce turn-averaged SAEs, which represent a single Human or Assistant turn with a fixed number of features by learning to reconstruct the average model activation across the turn. We find that turn-averaged features describe a single turn's high-level characteristics more completely than per-token features when judged by an LLM. We also demonstrate that turn-averaged SAEs greatly simplify common downstream uses of SAEs like attribution graphs. Broadly, turn-averaged SAEs make interpretability techniques practical at long context lengths.

## 综合总结
本文提出Turn-Averaged SAEs，通过重建对话轮次的平均模型激活，用固定数量的特征表示整个轮次，解决了传统单token SAE在长上下文中特征线性增长导致难以分析的问题。实验证明该方法能更完整地描述轮次高层特征，并大幅简化归因图等下游任务，使长上下文下的模型可解释性分析变得切实可行。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了一种创新的Turn-Averaged SAEs架构，突破了传统SAEs基于单token激活导致特征数量随上下文长度线性增长的限制。通过学习重建整个对话轮次的平均模型激活，将特征提取从token级别提升至轮次级别，不仅更好地捕捉了高层语义特征，还从理论和方法上显著简化了归因图等下游可解释性任务，技术洞见深且论证逻辑清晰。

### 实用性 (评分: 8.0/10)
对从事大模型可解释性和机制研究的从业者具有极高的参考价值。该架构直接解决了长上下文场景下SAE特征爆炸导致难以分析和可视化的痛点，简化了归因分析流程，能够直接指导长上下文对话模型的调试、对齐和特征挖掘工程实践。

### 社区活跃度 (评分: 8.0/10)
SAE与大模型长上下文机制均是当前AI可解释性领域的热点前沿方向。该论文精准切中了长上下文可解释性研究的痛点，提出的解决方案简洁且极具启发性，来源为arXiv最新预印本，具备较高的时效性和潜在的行业影响力。

## 项目链接
https://arxiv.org/abs/2606.28548
