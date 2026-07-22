# Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 知识图谱, 强化学习, KGQA, R1, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18481v1 Announce Type: new Abstract: Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. We present Search-on-Graph-R1 (\sogrone{}), which internalizes this navigation into a compact 8B model through supervised fine-tuning (SFT) followed by reinforcement learning (RL). Our central idea is to scaffold a frontier teacher with each question's gold SPARQL query, so the teacher traverses a known answer-bearing path with a live \texttt{Search} tool rather than having to discover the path itself. Since every call executes against a live Freebase server, the resulting trajectories are grounded in the knowledge graph by construction. On WebQSP, CWQ, and GrailQA, \sogrone{} at 8B surpasses every frozen frontier-LLM system in our comparison and posts the strongest results on CWQ of any system we compare against. It does so using no auxiliary module at inference and no LLM judge during training. Isolating each training stage shows that SFT and RL contribute complementary gains, our approach transfers across model families, and RL learns to reach answers in fewer \texttt{Search} calls than its SFT initialization.

## 综合总结
本文提出Search-on-Graph-R1，通过SFT与RL将知识图谱导航能力内化至8B小模型。核心创新是利用前沿大模型结合黄金SPARQL生成真实KG搜索轨迹进行教学，避免了高昂的探索成本。实验显示，该8B模型在WebQSP、CWQ和GrailQA上超越所有冻结的前沿LLM系统，并在CWQ取得最佳结果。该方法推理无需辅助模块，训练无需LLM judge，RL还能显著减少搜索步数，实现了小模型在特定任务上对大模型的性能与效率双重突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
方法新颖且技术深度较高，巧妙利用前沿大模型结合黄金SPARQL查询生成轨迹（scaffold机制），避免了模型自行探索的高成本与错误率。通过SFT+RL两阶段训练，将图搜索能力内化至8B小模型，RL阶段进一步优化了搜索效率（减少Search调用次数）。消融实验充分论证了SFT与RL的互补性及跨模型家族的迁移能力，论证严谨。

### 实用性 (评分: 9.2/10)
极具落地价值。8B参数的小模型在性能上超越了依赖前沿大模型的系统，推理时无需辅助模块，训练时无需LLM judge，大幅降低了部署与推理成本。为资源受限场景下的知识图谱问答与推理提供了高效、可行的工程实践范式。

### 社区活跃度 (评分: 8.5/10)
话题紧扣当前火热的“RL+LLM（R1范式）”与知识图谱结合方向，时效性强。作者团队包含知名NLP学者，来源权威。8B模型超越前沿大模型的结果极具冲击力，有望在KGQA及结构化数据检索社区引发广泛关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.18481
