# GES-TSP: Graph Edge Sparsification for TSP

**评分：** 8.8  
**状态：** 正常  
**标签：** 组合优化, TSP, 图稀疏化, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09708v1 Announce Type: new Abstract: Solving large-scale instances of the Traveling Salesman Problem (TSP) exactly is computationally expensive. Researchers often employ graph sparsification methods to improve computational efficiency. Traditional sparsification methods typically rely on fixed heuristics and fail to fully exploit instance-specific structural information. In this paper, we propose Graph Edge Sparsification (GES), a learning-based sparsification approach for Euclidean TSP. By incorporating geometric structural information and combinatorial optimization technology, our proposed method adaptively generates a sparsification graph for different instances, significantly reducing the graph size and accelerating the solving process. Experimental results demonstrate that our sparsification method can prune up to 95% of edges on the MATILDA dataset, while keeping the solution gap within 1% of the optimal value. Moreover, our approach exhibits strong generalization capability on the TSPLIB benchmark.In some large-scale instances, the pruning rate exceeds 99%, while the optimality gap remains below 1%.

## 综合总结
本文提出了一种基于学习的欧几里得TSP图边稀疏化方法（GES），通过结合几何结构信息与组合优化技术，自适应地为不同实例生成稀疏图。实验表明，该方法在MATILDA和TSPLIB数据集上表现出色，剪枝率最高可达99%，同时将最优性差距控制在1%以内，显著加速了大规模TSP的求解过程并具备良好的泛化能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
提出将学习型方法引入TSP图稀疏化，替代传统固定启发式规则，能够自适应利用实例特定的几何与结构信息。在保持极高剪枝率（最高99%）的同时，将最优性差距控制在1%以内，技术深度与论证严谨度极高。

### 实用性 (评分: 9.0/10)
对物流、路径规划等需要求解大规模TSP的行业具有极高的实用价值。极高的边剪枝率可大幅降低精确求解的计算资源消耗与时间成本，且在标准基准测试上表现出强泛化性，易于直接集成到现有求解流程中指导实践。

### 社区活跃度 (评分: 8.5/10)
机器学习与组合优化结合是当前AI for Science/OR的热点方向。论文来自arXiv，使用标准公开数据集验证，结果极具说服力，若能通过同行评审，将对大规模NP-Hard问题求解社区产生重要影响。

## 项目链接
https://arxiv.org/abs/2607.09708
