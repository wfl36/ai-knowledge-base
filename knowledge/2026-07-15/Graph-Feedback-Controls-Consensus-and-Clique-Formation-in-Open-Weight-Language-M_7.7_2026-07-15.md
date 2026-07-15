# Graph Feedback Controls Consensus and Clique Formation in Open-Weight Language-Model Populations

**评分：** 7.7  
**状态：** 正常  
**标签：** 多智能体, 大模型, 图网络, 共识机制, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.12077v1 Announce Type: new Abstract: Multi-agent language-model systems increasingly route local interactions, yet the runtime interaction graph is often treated as an implementation detail. We study convention formation in open-weight LM populations spanning 1.1B-32B parameters with a naming-game protocol. Restricted first-token scores over tokenizer-safe labels let us measure prompt-conditioned score-state distributions, construct state-similarity graphs, and separate sampled-label agreement from latent state-space consensus. Across controlled interventions, in the main open-weight repair grids, retained partner-label evidence is necessary but not sufficient: homophilous threshold-similarity routing deletes cross-basin exposure and amplifies fragmentation, while bridge-seeking routing often repairs fragmentation when memory is available. In a three-seed mixed four-model grid, threshold-similarity produces no final behavioral or state consensus in 189 setting-seed runs, whereas state-component and label-disagreement bridges recover final behavioral consensus in 14/18 retained-memory runs. Across homogeneous model populations, retained history generally shifts fragmented dynamics toward consensus; the clearest case is Qwen2.5-32B, which reaches stable behavioral and final state consensus in all 18 retained-history well-mixed settings, while threshold-similarity reaches neither form of consensus in 189 settings. Robustness over state thresholds, population size, and vocabulary size preserves the qualitative ordering, and early-window graph-energy features provide useful within-grid diagnostics.

## 综合总结
本研究探讨了多智能体大语言模型系统中的共识与派系形成机制，将交互图视为动态反馈控制。实验表明，基于相似度的同质性路由会放大群体碎片化，而引入寻桥路由与历史记忆则能有效修复割裂并促成共识。该发现为多智能体系统的通信拓扑设计提供了关键理论洞见与工程指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文创新性地将多智能体大语言模型的交互图从“实现细节”提升为动态反馈控制系统。通过引入命名博弈协议，在1.1B-32B参数的开源模型上量化了惯例形成过程，并严谨区分了采样标签一致性与潜状态空间共识。实验设计严密，深入揭示了同质性路由导致派系分裂，而寻桥路由与记忆机制能修复碎片化的深层机理。

### 实用性 (评分: 7.5/10)
对多智能体系统开发者具有直接的工程指导价值。研究证明，在多模型交互时若仅采用相似度匹配（同质化路由）会导致共识崩溃和群体割裂，而引入寻桥路由和保留历史记忆机制能有效促成系统共识。这为设计鲁棒的多智能体通信拓扑和路由策略提供了高度可操作的实践方案。

### 社区活跃度 (评分: 7.0/10)
多智能体系统与大模型的结合是当前AI领域的核心热点，探讨群体共识和派系形成机制具有极强的前瞻性。研究基于Qwen2.5等主流开源权重，具备较好的可复现性；但作为arXiv预印本，其学术权威性仍需后续同行评审的进一步验证。

## 项目链接
https://arxiv.org/abs/2607.12077
