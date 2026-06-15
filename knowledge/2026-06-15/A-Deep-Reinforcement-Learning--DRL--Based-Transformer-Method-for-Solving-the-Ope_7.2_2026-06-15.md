# A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem

**评分：** 7.2  
**状态：** 正常  
**标签：** 深度强化学习, Transformer, 组合优化, 调度问题, 泛化性, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13682v1 Announce Type: new Abstract: The open shop scheduling problem (OSSP) arises in many industrial and service settings but remains computationally challenging as the number of jobs and machines increases. While exact methods quickly become intractable, classical dispatching rules and metaheuristics may require substantial tuning to maintain solution quality at large scales. This study develops a Transformer-based scheduling policy for OSSP using an encoder-decoder architecture with multi-head attention. The model is trained on Taillard benchmark instances (4x4, 5x5, 7x7, and 10x10) using only the processing-time matrix as input and produces feasible schedules with makespans typically within 15-30% of best-known values. To evaluate scalability, the trained policy is applied without retraining to randomly generated instances from 40x40 to 100x100 and compared against classical dispatching heuristics, including SPT, LPT, MWKR, and EST. Across these large instances, the Transformer achieved average gaps of 12.89-15.12% relative to a standard lower bound. Compared with EST, the Transformer remained competitive, typically within a modest margin, while substantially outperforming SPT and LPT. These results indicate that a Transformer policy trained on small OSSP instances can generalize to substantially larger problems and provide a feature-light, learning-based alternative to classical dispatching rules.

## 综合总结
本文提出一种基于深度强化学习(DRL)的Transformer方法来解决开放车间调度问题(OSSP)。该模型仅使用处理时间矩阵作为输入，在小规模Taillard基准实例上训练后，无需重新训练即可直接泛化到40x40至100x100的大规模随机实例。实验表明，该模型在大规模实例上显著优于SPT和LPT等经典调度规则，与EST规则表现相当，且与标准下界的平均差距保持在12.89-15.12%。该研究证明了基于Transformer的调度策略具备出色的跨尺度泛化能力，为工业大规模调度提供了一种轻量级且易部署的学习型替代方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
提出一种基于DRL的Transformer编码器-解码器架构求解开放车间调度问题(OSSP)，仅以处理时间矩阵为输入。核心亮点在于验证了模型从小规模实例（4x4至10x10）向大规模实例（40x40至100x100）的零样本泛化能力，技术上证明了特征轻量化的注意力机制在组合优化中的尺度泛化潜力，但绝对求解精度（与已知最优解差距15-30%）仍有提升空间。

### 实用性 (评分: 8.0/10)
具有较高的工业落地参考价值。模型无需在大规模问题上重新训练即可直接部署，显著降低了实际应用中的训练成本和算力门槛。在应对大规模调度问题时，表现优于SPT、LPT等经典启发式规则，与EST竞争力相当，可作为传统调度规则的有效且轻量级的替代方案。

### 社区活跃度 (评分: 6.5/10)
针对经典的开放车间调度问题，结合了当前AI前沿的DRL与Transformer架构，属于运筹优化与AI交叉领域的热点研究。文章为arXiv预印本，作者知名度一般，虽未达到范式级的理论突破，但其跨尺度泛化性的验证对学术界和工业界均有较好的启发意义。

## 项目链接
https://arxiv.org/abs/2606.13682
