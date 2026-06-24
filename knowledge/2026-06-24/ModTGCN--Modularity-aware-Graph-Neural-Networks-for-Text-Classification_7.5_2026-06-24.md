# ModTGCN: Modularity-aware Graph Neural Networks for Text Classification

**评分：** 7.5  
**状态：** 正常  
**标签：** 图神经网络, 文本分类, 模块度, 论文  
**更新日期：** 2026-06-24  
**来源：** rss  

## 项目描述
arXiv:2606.23694v1 Announce Type: new Abstract: Graph-based text classification models typically rely on local neighborhood aggregation and overlook global community structure, despite semantic document graphs exhibiting strong class-consistent clustering. Ignoring this can blur class boundaries and lead to over-smoothing. We propose ModTGCN, a modularity-aware graph neural network for text classification that jointly optimizes cross-entropy and a modularity-based auxiliary objective to promote class-coherent document communities while preserving discriminative representations. The modularity term is computed on a document-document similarity graph derived from transformer embeddings (pretrained or fine-tuned). To improve scalability, we decouple the original heterogeneous TextGCN graph into separate document-word and word-word components, achieving 2x-10x faster training. We further study graph construction strategies, label-aware edge reweighting, and supervision choices for modularity optimization. Experiments on five benchmarks show consistent gains, with larger improvements on complex, low homophily datasets such as Ohsumed and 20NG.

## 综合总结
本文提出ModTGCN模型，通过联合优化交叉熵和模块度目标，解决了图文本分类中忽略全局社区结构导致的过平滑问题。模型利用Transformer嵌入构建文档相似度图，并通过解耦异构图实现了2-10倍的训练加速。实验证明，该方法在五个基准数据集上均取得一致提升，尤其在低同质性复杂数据集上优势显著。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文针对图神经网络在文本分类中忽略全局社区结构导致过平滑和类边界模糊的问题，创新性地引入模块度辅助优化目标，以促进类一致的文档社区形成。同时，提出将异构TextGCN图解耦为文档-词和词-词组件，不仅提升了可扩展性，还实现了2-10倍的训练加速。整体方法新颖，针对性强，论证严谨。

### 实用性 (评分: 7.5/10)
对文本分类从业者具有较高的参考价值，特别是在处理低同质性、复杂结构的文本数据时。解耦图结构带来的显著训练加速，以及基于Transformer嵌入的图构建策略，降低了图方法在实际应用中的计算和部署门槛，具备较好的工程落地潜力。

### 社区活跃度 (评分: 7.0/10)
图神经网络与预训练语言模型的结合是当前NLP领域的持续热点，本文提出的模块度感知机制具有较好的时效性。作为arXiv预印本，其方法在多个主流基准上验证了有效性，但作者团队影响力相对一般，需等待同行评审进一步确认其权威性。

## 项目链接
https://arxiv.org/abs/2606.23694
