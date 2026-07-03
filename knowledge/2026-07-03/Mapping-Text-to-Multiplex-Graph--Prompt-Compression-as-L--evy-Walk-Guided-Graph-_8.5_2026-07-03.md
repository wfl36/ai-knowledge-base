# Mapping Text to Multiplex Graph: Prompt Compression as L\'evy Walk-Guided Graph Pruning

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 提示词压缩, 图剪枝, 长上下文, 论文  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01241v1 Announce Type: new Abstract: Existing prompt compression methods treat text as flat token sequences, failing to capture the distributed nature of important information, which is often spread across multiple locations and connected through both local syntactic dependencies and global semantic relations. Such relational structure is naturally represented as a graph, where tokens or sentences become nodes and their dependencies become edges. To this end, we propose RAGP, which formulates prompt compression as Redundancy-Aware Graph Pruning on a multiplex graph that jointly models fine-grained attention-based dependencies and coarse-grained semantic relations. To efficiently identify non-redundant nodes in this heterogeneous structure (dense local subgraphs and sparse global connections), we employ Levy walks whose heavy-tailed step distribution naturally balances local exploitation with global exploration. Experiments on LongBench show that RAGP achieves an average score of 49.3 under a 4x compression ratio, outperforming existing LLM-based compression methods, such as LongLLMLingua, which attains 48.8 at a 3x compression ratio. Besides, RAGP also surpasses state-of-the-art vision-based text compression paradigms on multiple tasks. The code is available at https://anonymous.4open.science/r/RAGP-B0CB.

## 综合总结
本文提出RAGP方法，将提示词压缩重新定义为多重图上的冗余感知图剪枝问题。针对现有方法忽略信息分布式特性的不足，RAGP构建了联合建模细粒度注意力依赖和粗粒度语义关系的多重图，并创新性地利用Lévy walks的重尾分布特性，有效平衡了密集局部子图的开发与稀疏全局连接的探索。实验证明，在4倍压缩率下，RAGP在LongBench上表现优于现有LLM压缩及视觉压缩SOTA方法，为长上下文处理和推理成本优化提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在方法论上具有高度新颖性，打破了现有提示词压缩方法将文本视为扁平序列的局限，创新性地将其建模为多重图剪枝问题，同时捕捉细粒度的注意力依赖与粗粒度的语义关系。引入Lévy walks（莱维飞行）解决异构图中的非冗余节点搜索问题，利用其重尾分布自然平衡局部开发与全局探索，理论依据充分，技术深度与论证严谨度极高。

### 实用性 (评分: 8.0/10)
提示词压缩是解决大模型长上下文处理和高推理成本痛点的关键技术。本文提出的方法在4倍压缩比下性能超越现有SOTA（如LongLLMLingua的3倍压缩比），且代码已开源，对工业界优化RAG和长文本场景的Token消耗具有极高的实操指导价值。但多重图构建与随机游走可能带来一定的计算开销，实际落地时需权衡效果与延时。

### 社区活跃度 (评分: 8.5/10)
大模型长上下文处理与推理成本优化是当前AI社区的热点议题。该论文发表于arXiv，作者团队包含领域内知名学者，且提供了开源代码验证，来源可信度高。其跨学科的图剪枝与莱维飞行结合方案若能复现，有望在提示词压缩领域产生显著的学术与工程影响力。

## 项目链接
https://arxiv.org/abs/2607.01241
