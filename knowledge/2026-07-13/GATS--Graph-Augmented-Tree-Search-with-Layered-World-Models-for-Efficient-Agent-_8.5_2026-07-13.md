# GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 规划, 世界模型, 树搜索, 论文  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.08894v1 Announce Type: new Abstract: Large Language Model (LLM) agents have shown promise in multi-step planning tasks, but existing approaches like LATS (Language Agent Tree Search) and ReAct rely heavily on LLM inference during planning, leading to high computational costs and stochastic behavior. We present \textbf{GATS} (Graph-Augmented Tree Search), a planning framework that combines systematic UCB1-based tree search with a layered world model to eliminate LLM calls during inference while achieving superior planning performance. Our three-layer world model integrates: (L1) exact symbolic action matching, (L2) statistics learned from execution logs, and (L3) LLM-based prediction for unknown actions. On synthetic planning tasks with branching paths and dead-ends, GATS achieves \textbf{100\% success rate} compared to 92 % for LATS and 64\% for ReAct. On a comprehensive stress test spanning 12 challenging scenarios -- including coding workflows, web navigation, and long-horizon tasks -- GATS maintains \textbf{100\% success} while LATS drops to 88.9 % and ReAct to 23.9%. GATS requires \textbf{zero LLM calls per task} during planning (vs. 37 per task for LATS) and produces deterministic plans with zero variance across runs. Our results demonstrate that systematic search with learned world models can substantially outperform LLM-guided exploration for agent planning.

## 综合总结
GATS提出了一种图增强树搜索规划框架，通过三层分层世界模型（符号匹配、统计学习、LLM预测）将LLM调用从规划推理阶段完全移除，转而采用UCB1进行确定性搜索。在多项复杂任务测试中，GATS实现了100%的成功率和零方差，且规划阶段无需任何LLM调用，彻底解决了传统LLM Agent规划成本高、随机性大的问题，是Agent规划范式上的一项重要突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该论文提出了显著的创新，通过结合UCB1树搜索与三层分层世界模型（符号匹配、统计学习、LLM预测），将LLM从规划推理阶段剥离，转而用于离线知识提取。这种设计不仅解决了LATS和ReAct等方法中过度依赖LLM推理导致的高计算成本和随机性问题，还在理论和方法论上展现了极深的技术洞察力，实验数据（100%成功率、0次LLM调用、零方差）极具说服力。

### 实用性 (评分: 8.5/10)
对从业者具有极高的参考价值。在需要确定性输出和低延迟的生产环境（如自动化编码工作流、网页导航等），'零LLM调用'意味着极低的推理成本和稳定的响应时间，克服了现有LLM Agent难以落地的痛点。不过，构建和维护三层世界模型可能需要一定的冷启动成本和日志积累。

### 社区活跃度 (评分: 8.0/10)
Agent规划是当前AI领域的核心热点，该论文直击LLM Agent成本高、输出不稳定的社区痛点，话题时效性极强。虽然作者知名度一般且发布时间标注存在异常（2026年），但其展现的压倒性性能优势极易引发学术界和工程界的广泛关注与讨论，具有较高影响潜力。

## 项目链接
https://arxiv.org/abs/2607.08894
