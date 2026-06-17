# Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 搜索, 推理, Test-time scaling, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17209v1 Announce Type: new Abstract: Test-time scaling for agentic search typically increases depth (i.e., more turns and tokens per trajectory) or breadth (i.e., more parallel rollouts). Here we focus on breadth scaling, showing that standard parallel sampling yields diminishing returns, tracing this to query redundancy at the first turn. When models issue similar first queries across rollouts, the threads retrieve overlapping evidence, and subsequent turns are conditioned on this shared retrieval. We address this limitation with DivInit, a training-free intervention at the first turn. Rather than sampling k independent first queries, DivInit draws n candidates from a single call, picks k < n diverse seeds, and runs them as parallel trajectories. Across five open-weight models and eight benchmarks, DivInit consistently improves over standard parallel sampling, with average gains of five to seven points on multi-hop QA at matched compute. Code available at https://github.com/cxcscmu/diverse-query-initialization

## 综合总结
本文针对智能体搜索中并行采样因初始查询冗余导致收益递减的问题，提出了一种无需训练的干预方法DivInit。该方法在首轮交互时从单次调用中抽取多个候选查询，并挑选多样化的子集作为并行轨迹的种子，从而避免检索重叠证据。实验表明，在同等计算量下，DivInit在多跳QA任务上带来了5-7分的平均提升。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
深刻揭示了智能体搜索中并行采样因首轮查询同质化导致检索证据重叠及收益递减的内在机制。提出的DivInit方法通过单次调用生成n个候选并挑选k个多样化种子，设计精巧且无需额外训练，实验论证严谨，跨5个模型和8个基准测试表现稳定。

### 实用性 (评分: 9.0/10)
极具工程落地价值。DivInit作为training-free的轻量级干预，对现有基于并行采样的Agent/RAG系统几乎无侵入性，在同等计算预算下即可显著提升多跳问答性能，可直接应用于各类搜索增强的智能体框架中。

### 社区活跃度 (评分: 8.5/10)
聚焦于当前大模型领域极度热门的Test-time scaling与Agentic Search，话题时效性极强。作者团队包含知名学者，且提供了开源代码，具备较高的学术权威性与社区影响力。

## 项目链接
https://arxiv.org/abs/2606.17209
