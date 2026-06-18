# CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, RAG, 大模型, 推理, 论文, 工程实践  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18406v1 Announce Type: new Abstract: Personalized dialogue agents require continuous long-term memory to maintain coherent interactions across multiple sessions. However, deploying these capabilities on consumer-grade hardware (e.g., 8 GB VRAM edge devices) introduces severe memory and compute bottlenecks. Existing systems typically rely on isotropic cosine similarity for retrieval and heuristic rules for context compression. These approaches lack a unified theoretical foundation, frequently suffering from the hubness problem in high-dimensional retrieval and syntactic fragmentation during compression. To overcome these limitations, we propose CoreMem, a resource-efficient edge-cloud memory architecture fundamentally unified by information geometry. First, Riemannian retrieval replaces cosine matching with a locally adaptive Fisher-Rao metric, effectively penalizing hub memories via Mahalanobis distance with O(Ndr) Woodbury acceleration for real-time search. Second, Fisher-guided discrete token distillation (FDTD) introduces a hierarchical sentence-to-token compression mechanism. It derives sensitivity scores from Fisher information traces, providing a principled compression-KL tradeoff augmented with explicit structural syntax protection. Evaluated on the LOCOMO and LongMemEval-S benchmarks, CoreMem achieves strong accuracy improvements, yielding substantial gains in Open-domain (+4.51 pp) and Temporal (+4.17 pp) reasoning. Extensive profiling confirms that CoreMem operates seamlessly within a strict 8 GB VRAM budget, successfully bridging the gap between resource-constrained edge devices and the demand for theoretically grounded, lifelong memory agents.

## 综合总结
CoreMem针对个性化对话代理在资源受限设备（8GB VRAM）上部署长期记忆的痛点，提出了一种基于信息几何统一理论的边云记忆架构。该架构通过黎曼检索（Fisher-Rao度量）解决高维检索的hubness问题，并利用Fisher引导的离散token蒸馏（FDTD）实现兼顾句法保护的层级上下文压缩。实验证明，该方法在严格显存限制下，于开放域和时序推理任务上取得了显著精度提升，为端侧终身记忆Agent的落地提供了兼具理论深度与工程可行性的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文在技术深度和新颖性上表现突出。它创新性地将信息几何引入对话代理的长期记忆系统，统一了检索与压缩的理论基础：在检索阶段，用黎曼检索（基于Fisher-Rao度量的Mahalanobis距离）替代传统的各向同性余弦相似度，有效缓解了高维检索中的hubness问题，并结合Woodbury加速保证了实时性；在压缩阶段，提出Fisher引导的离散token蒸馏（FDTD），利用Fisher信息迹推导敏感度分数，实现了有原则的压缩-KL权衡，并显式保护了句法结构。论证严谨，数学基础扎实。

### 实用性 (评分: 8.0/10)
对从业者的实际参考价值很高。论文直击端侧部署（8GB VRAM）的内存与计算瓶颈，提出的边云协同记忆架构CoreMem具有极强的落地指导意义。其O(Ndr)的Woodbury加速方案和层级式句子到token的压缩机制，直接回应了资源受限设备上的工程痛点。在LOCOMO和LongMemEval-S基准上的显著精度提升（开放域+4.51 pp，时序推理+4.17 pp）及严格的显存预算验证，证明了该方案可直接应用于智能客服、个人AI助手等边缘计算场景。

### 社区活跃度 (评分: 7.5/10)
话题时效性极强，契合当前大模型向Agent演进及端侧轻量化部署的行业热点。作为arXiv上的最新论文（2026年发布），其探讨的终身记忆机制是构建个性化Agent的核心痛点。虽然作者团队相对年轻，但解决的是当前AI社区高度关注的RAG与长上下文压缩问题，且实验基准选取恰当，具备在Agent和RAG开发者社区引发广泛讨论和引用的潜力。

## 项目链接
https://arxiv.org/abs/2606.18406
