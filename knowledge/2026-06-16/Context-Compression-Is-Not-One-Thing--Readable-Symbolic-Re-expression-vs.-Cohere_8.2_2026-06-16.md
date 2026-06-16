# Context Compression Is Not One Thing: Readable Symbolic Re-expression vs. Coherent Summary at Matched Budget

**评分：** 8.2  
**状态：** 正常  
**标签：** 上下文压缩, RAG, 多跳问答, 小模型, 符号重表达, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.14875v1 Announce Type: new Abstract: We study context compression for multi-hop question answering with small language models. We propose Telegraph English, a readable symbolic format that rewrites retrieved passages into structured entity-relation statements, preserving reasoning evidence at lower token cost. In controlled experiments on MuSiQue, TwoWiki, and HotpotQA, Telegraph English outperforms three matched-budget compression baselines (character-level deletion, truncation, and random sub-sampling) on every dataset, with gains of 13 to 20 F1 percentage point. It also outperforms a coherent prose summary produced by the same encoder on the hardest dataset. A pre-registered depth-interaction hypothesis is null: the advantage does not grow with reasoning depth within datasets. We interpret these results as evidence that readable symbolic re-expression preserves entity content more densely than either natural language or coherent summarization at matched token budget.

## 综合总结
本文针对小模型多跳问答中的上下文压缩问题，提出了一种名为Telegraph English的可读符号重表达方法，将检索段落转化为结构化的实体-关系陈述。实验表明，在同等token预算下，该方法显著优于字符删除、截断等基线（F1提升13-20点），且在困难数据集上优于同编码器生成的连贯摘要。研究严谨地证伪了深度交互假设，证明了符号化重表达比自然语言摘要更密集地保留推理证据，对RAG和小模型应用具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了新颖的观点：上下文压缩并非单一维度，区分了'可读符号重表达'与'连贯摘要'。提出的Telegraph English方法将自然语言转化为结构化实体-关系陈述，在同等token预算下更密集地保留了推理证据。实验设计严谨，包含对照基线和预注册假设（虽被证伪，但增加了科学性），在多跳问答数据集上取得了13-20 F1的显著提升，论证深度与严谨性俱佳。

### 实用性 (评分: 8.0/10)
对RAG系统特别是资源受限的小模型场景具有极高的落地价值。Telegraph English可直接作为检索后、生成前的上下文预处理模块，有效降低token消耗并提升多跳推理准确率，为解决长上下文和高成本问题提供了明确的工程实践路径。

### 社区活跃度 (评分: 8.0/10)
研究聚焦当前大模型及RAG领域的核心痛点（上下文长度限制与成本），话题时效性极强。基于MuSiQue、HotpotQA等主流数据集的实验结果可信度高，对AI社区在上下文压缩与符号化表达方向的探索具有重要参考价值和影响力。

## 项目链接
https://arxiv.org/abs/2606.14875
