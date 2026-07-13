# AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, RAG, 知识图谱, 事实校验, 强化学习, 模型蒸馏, 论文  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.09092v1 Announce Type: new Abstract: Knowledge graphs (KGs) are often automatically constructed from large-scale corpora, but they inevitably contain factual errors due to noisy sources and extraction failures, and verifying them reliably at industrial scale remains a critical challenge. To address this, we propose AgentKGV, the Agentic LLM-RAG framework for KG fact Verification, that integrates dynamic routing and iterative query rewriting, which handles surface-form mismatch in document-level retrieval. To make this framework more accurate and cost-efficient for industrial deployment, we further introduce a two-stage training strategy: turn-level distillation-based SFT that transfers reasoning ability from a large teacher model into a small model for stable query rewriting and reasoning, and trajectory-level GRPO that optimizes the search policy to reduce unnecessary retrieval at scale. On the long-tail-predicate split of the open-domain T-REx benchmark, our framework improves macro-F1 over single-turn RAG by 5.5 \%p, and two-stage training does it further by 9.4 \%p. GRPO also cuts the average number of search calls from 3.24 to 1.63 without lowering accuracy.

## 综合总结
本文提出AgentKGV框架，用于知识图谱(KG)的工业级事实校验。该框架结合Agentic RAG，通过动态路由和迭代查询重写解决检索中的表面形式不匹配问题。为降低部署成本，作者提出两阶段训练策略：第一阶段通过蒸馏SFT将大模型推理能力迁移至小模型以稳定查询重写；第二阶段利用轨迹级GRPO优化搜索策略以减少冗余检索。实验表明，该方法在T-REx长尾数据集上较单轮RAG提升macro-F1 5.5%，两阶段训练进一步提升9.4%，同时将平均搜索调用次数减半，实现了准确性与成本效率的双重优化。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
该论文在技术深度与创新性上表现良好。将Agentic RAG与知识图谱事实校验结合，通过动态路由和迭代查询重写解决文档级检索中的表面形式不匹配问题，设计合理。其最大的技术亮点在于引入了两阶段训练策略：Turn-level蒸馏SFT实现了大模型到小模型的推理能力迁移，保证了查询重写的稳定性；Trajectory-level GRPO（群组相对策略优化）则用于优化搜索策略，有效减少了冗余检索。整体方法逻辑严谨，将前沿RL算法应用于Agent策略优化，具有较好的理论结合度。

### 实用性 (评分: 9.0/10)
可落地性极高，直击工业界痛点。自动构建的知识图谱存在大量事实错误，而传统校验方法在大规模应用时成本高昂。该框架通过知识蒸馏使小模型具备复杂推理能力，同时利用GRPO将检索调用次数减半（3.24降至1.63），在不损失准确率的前提下大幅降低了推理与检索成本。这种兼顾准确性与成本效率的方案，对工业界大规模KG清洗与校验、以及RAG系统的成本控制具有极强的指导意义和实操价值。

### 社区活跃度 (评分: 8.0/10)
话题时效性强，紧跟当前AI Agent与强化学习微调（特别是GRPO）的研究热点。知识图谱质量保障也是业界持续关注的核心议题。论文在权威开放基准T-REx的长尾谓词分割上进行了充分验证，量化结果明确（macro-F1显著提升，检索成本下降），来源可信度高。虽然作者团队相对低调，但所涉主题契合当前社区对高效Agent和低成本RAG的强烈需求，预计将获得不错的社区关注度。

## 项目链接
https://arxiv.org/abs/2607.09092
