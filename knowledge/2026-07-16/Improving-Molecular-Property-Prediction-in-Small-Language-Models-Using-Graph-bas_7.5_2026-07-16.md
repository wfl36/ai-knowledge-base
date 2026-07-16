# Improving Molecular Property Prediction in Small Language Models Using Graph-based Tools

**评分：** 7.5  
**状态：** 正常  
**标签：** AI4Science, 分子属性预测, 小语言模型, 图神经网络, Agent, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.13115v1 Announce Type: new Abstract: Small language models (SLMs) have shown promise for zero-shot molecular property prediction from SMILES strings, yet they often suffer from structural blindness because sequence representations under-specify key graph-topological cues. We propose a modular Context-Augmented Prompting framework that enables agentic tool use at inference time: a trained GNN expert model provides a predictive hint with confidence, and a GNN extracts an instance-specific explanatory subgraph (e.g., a subgraph SMILES and an accompanying explanatory paragraph). We evaluate three commonly used SLMs on MUTAG and Tox21 under five prompting configurations ranging from SMILES-only to using all available tools at hand. Across two datasets, enriching prompts with graph-derived context yields substantial accuracy gains, often exceeding 25% relative improvement and up to 74% on Tox21. We further validate the functional relevance of the extracted motifs via a necessity-based edge-drop intervention. Despite the observed gains, a persistent gap remains to specialized GNN models, highlighting both the value and limits of text-conditioned reasoning for molecular structure.

## 综合总结
本文针对小语言模型(SLM)在零样本分子属性预测中因序列表示导致的“结构盲”问题，提出了一种模块化的上下文增强提示框架。该框架通过Agent工具调用机制，在推理时引入GNN专家模型的预测提示和提取的实例特定解释性子图。实验表明，该方法在MUTAG和Tox21数据集上使准确率相对提升最高达74%。干预实验验证了提取基序的功能相关性，但SLM与专用GNN模型间仍存在性能差距，揭示了文本条件推理在分子结构处理上的价值与局限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文针对小语言模型(SLM)在零样本分子属性预测中因序列表示导致的'结构盲'问题，创新性地提出了基于Agent工具调用的上下文增强提示框架。该框架在推理时动态引入GNN专家模型的预测提示与实例特定的解释性子图，有效弥补了SLM对图拓扑线索的感知缺失。研究设计了基于必要性的边丢弃干预实验验证子图相关性，论证严谨，方法学深度较好，属于跨模态提示增强的增量创新。

### 实用性 (评分: 7.5/10)
该框架采用模块化设计，在推理阶段通过提示词注入图信息，无需修改SLM的模型权重，即插即用且工程实现成本低。对于AI4Science和药物发现领域的从业者具有直接的实践指导价值。不过，其适用范围相对局限，主要针对分子属性预测任务及小语言模型场景，且性能仍不及专用GNN，落地时需权衡精度与通用性。

### 社区活跃度 (评分: 7.0/10)
论文结合了小语言模型(SLM)、Agent工具调用和AI4Science等当前AI社区的热点方向，话题时效性强。研究基于arXiv预印本发布，在经典分子数据集(MUTAG, Tox21)上取得了显著的相对提升(最高74%)，数据与实验可信度良好。但在广泛的AI社区中，其影响力主要局限于垂直领域的跨模态结合探索，属于稳健的阶段性进展而非颠覆性热点。

## 项目链接
https://arxiv.org/abs/2607.13115
