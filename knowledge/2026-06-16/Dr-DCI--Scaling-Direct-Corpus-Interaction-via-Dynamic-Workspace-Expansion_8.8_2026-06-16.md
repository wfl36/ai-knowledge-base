# Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, RAG, 搜索, 大模型, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.14885v1 Announce Type: new Abstract: Agentic search over large corpora relies on retriever-mediated interfaces (e.g., BM25 or ColBERT) for scalable candidate discovery. While effective at ranking relevant documents, these interfaces expose evidence only as ranked results or bounded document views, limiting agents' ability to reorganize material and verify constraints across documents. Direct Corpus Interaction (DCI) addresses this limitation by exposing shell-executable corpus operations for flexible search, filtering, comparison, and verification. However, full-corpus terminal commands become slow and unstable as the corpus grows, degrading performance and efficiency. We introduce DR-DCI, a retriever-steered DCI framework that treats retrieval as an agent-callable action for expanding a local workspace. Rather than operating directly over the full corpus, the agent dynamically pulls relevant documents into an evolving workspace and conducts DCI operations within it. This design combines retriever-level recall with DCI-style precision: retrieval keeps exploration scalable, while DCI preserves the local operations needed for effective evidence resolution. Experiments show that DR-DCI is both effective and efficient across scales. On Browsecomp-Plus, DR-DCI reaches 71.2\% accuracy, improving over raw DCI and ablated variants by up to 8.3 points while reducing tool usage, wall time, and estimated cost. With workspace-preserving context reset, accuracy further improves to 73.3\%. In corpus-scaling experiments, DR-DCI remains effective from 100K to 10M documents, whereas raw DCI becomes unstable and BM25 performs substantially worse. DR-DCI also scales to a 20M-scale file-per-document Wiki-18 QA setting, achieving an average score of 63.0 across six benchmarks and outperforming retrieval-based and trained search-agent baselines. Ablation analysis further shows that ranked previews and inter-document DCI are key to performance.

## 综合总结
本文提出DR-DCI框架，通过将检索作为Agent动作动态扩展本地工作区，解决了直接语料库交互（DCI）在大规模数据上的扩展性与稳定性问题。该框架结合了检索的召回率与DCI的精确性，在千万级语料库测试中显著提升了准确率（最高提升8.3点）并降低了运行成本，为Agentic Search和RAG系统提供了重要的架构创新与实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出DR-DCI框架，创新性地将检索器作为Agent可调用的动作，通过动态扩展本地工作区解决直接语料库交互（DCI）在大规模语料库上的扩展性瓶颈。该设计巧妙结合了检索器的高召回率与DCI的局部精确操作，论证严谨，消融实验深入揭示了排序预览与跨文档DCI的关键作用。

### 实用性 (评分: 8.5/10)
动态工作区扩展与保留工作区的上下文重置机制，对构建大规模搜索Agent和复杂RAG系统具有极高的工程指导价值。该方法有效降低了工具调用次数、运行时间及预估成本，可直接应用于需要跨文档验证与复杂推理的搜索场景。

### 社区活跃度 (评分: 9.0/10)
聚焦Agentic Search与RAG前沿热点，话题时效性极强。作者团队包含Wenhu Chen、Jimmy Lin等该领域知名学者，学术权威性高。实验在千万级（10M-20M）语料库上验证了有效性，显著优于传统BM25及现有搜索Agent基线，具有很高的社区影响力和参考价值。

## 项目链接
https://arxiv.org/abs/2606.14885
