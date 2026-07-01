# Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 多智能体, AutoML, 知识管理, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30911v1 Announce Type: new Abstract: ML engineering agents waste compute rediscovering known techniques because every competition is a cold start. We present HASTE, a hierarchical multi-agent system that organizes cross-competition knowledge into three scope tiers (global, domain, and competition-specific), each coupled to a matching agent level. An orchestrator coordinates domain specialists and promotes learning between tiers via LLM-driven abstraction. A controlled ablation provides evidence for scoped loading: holding a 159-skill inventory constant across 8 competitions, tiered loading achieves a 100% medal rate while flat loading reaches only 62.5%, the same medal rate as loading no skills, and consumes 2x the output tokens. On the full MLE-Bench Lite benchmark (22 Kaggle competitions), HASTE reaches a medal rate of 77.3% using Claude Sonnet 4.6 at 12h per competition. In a cold-start run, the system begins with no accumulated skills. In warm-start runs, it reloads skills learned from earlier competitions, using only global and domain-level skills for transfer across competitions. Warm starts use 52% fewer refinement iterations, and the fraction of proposed changes kept by the agent rises from 42% at low inventory to 85% once 50+ skills are available. These results suggest that better knowledge organization can partly substitute for model strength and compute budget in ML-engineering agents.

## 综合总结
本文提出HASTE分层多智能体系统，解决ML工程Agent跨任务冷启动的算力浪费问题。系统将知识划分为全局、领域和特定任务三层，通过协调器与LLM抽象实现技能迁移。实验证明，分层加载技能效果远超扁平加载（100% vs 62.5%奖牌率），热启动减少52%迭代，技能保留率随库存增加从42%升至85%。研究揭示，优化的知识组织架构能有效替代部分模型能力与计算预算，为高效可迁移Agent构建提供了重要范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了新颖的分层多智能体架构（HASTE），将跨任务知识组织为全局、领域和特定三个层级，并通过LLM驱动的抽象促进技能迁移。技术深度体现在严谨的消融实验和量化论证上，如证明分层加载奖牌率达100%而扁平加载仅62.5%，且扁平加载等同于无技能加载，有力揭示了知识结构化的重要性，并提出了'知识组织可部分替代模型强度与算力'的深刻洞见。

### 实用性 (评分: 9.0/10)
对AI Agent开发者具有极高的落地指导价值。三层知识架构和热启动机制直接解决了当前Agent系统跨任务冷启动和知识复用的痛点，LLM驱动的技能抽象方法也可直接应用于各类工程Agent的记忆与知识库设计中，适用范围不仅限于ML工程，可广泛延伸至代码生成、数据分析等复杂任务场景。

### 社区活跃度 (评分: 8.5/10)
话题极具时效性，聚焦当前火热的AutoML和Agent工程领域。来源可信（arXiv论文，基于标准MLE-Bench基准测试及前沿模型），其核心观点对社区过度依赖堆算力和堆参数的现状具有启发性和纠偏意义，有望在Agent记忆系统与知识管理方向产生显著影响力。

## 项目链接
https://arxiv.org/abs/2606.30911
