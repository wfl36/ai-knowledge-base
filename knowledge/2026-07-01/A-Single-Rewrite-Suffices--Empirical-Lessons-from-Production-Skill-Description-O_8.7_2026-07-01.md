# A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 大模型, 路由, 提示词工程, 论文, 工程实践  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30775v1 Announce Type: new Abstract: Enterprise AI agents route user queries to specialized skills by matching queries against natural language skill descriptions. When two skills share overlapping descriptions, the routing LLM misroutes queries, a failure we term skill collision. As agents scale to dozens of skills, manually tuning descriptions to maintain routing accuracy becomes a significant engineering bottleneck. We deploy an automated description optimization pipeline on a production enterprise group chat agent (9 skills, 372 regression cases). The pipeline produces descriptions averaging 79.2% F1, matching manually tuned descriptions at 79.4% F1 (average per-skill difference -0.20%, within the 0.78% multi-seed noise floor), while reducing per-skill engineering effort from 120 minutes to 3.8 minutes (32 times speedup). We then examine which pipeline components actually drive this match. Systematic ablation on both the production system and ToolBench (16k tools) reveals that a single LLM rewrite using any available false-positive and false-negative cases captures most of the available improvement. Other design choices we tested (iteration budget, feedback signal composition, dual editing of confused pairs, and training set size) each affect final F1 by less than 0.5%. Description optimization addresses skill collisions caused by overlapping descriptions but cannot resolve cases where two skills intended scopes genuinely overlap. We identify a diagnostic (a large train-validation F1 gap) that flags the latter cases for architectural rather than text-level intervention.

## 综合总结
本文针对企业AI Agent中因技能描述重叠导致的“技能冲突”及手动调优成本高的问题，提出并验证了一种自动化描述优化流水线。研究表明，该流水线在F1得分上与人工调优相当，但工程效率提升32倍。更重要的是，通过系统消融实验发现，仅需利用假阳性和假阴性案例进行单次LLM重写即可获得大部分性能提升，其他复杂设计对结果影响微乎其微。此外，论文还提出了通过训练-验证F1差距来诊断技能真实范围重叠的方法，为架构级调整提供依据。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文通过严谨的系统消融实验（生产环境与ToolBench）揭示了反直觉的结论：在解决技能路由冲突的描述优化中，复杂的迭代和反馈机制并非必需，单次LLM重写即可捕获主要收益（其他因素影响<0.5%）。同时清晰界定了文本级优化的边界，并提出了诊断真实范围重叠的指标（train-val F1 gap），论证严谨且具有深度洞见。

### 实用性 (评分: 9.5/10)
对Agent开发者具有极高的实践指导价值。直接将单技能调优时间从120分钟缩短至3.8分钟（32倍提速），且给出了极简的落地方法（基于FP/FN案例的单次重写），无需构建复杂流水线。提供的诊断方法也能直接指导开发者何时应停止文本调优转向架构重构，适用范围广，落地门槛极低。

### 社区活跃度 (评分: 8.5/10)
话题直击当前Agent规模化落地中的核心痛点（路由冲突与扩展瓶颈），时效性强。基于真实生产环境数据验证，结论极具说服力，对Agent和RAG领域的工程社区有较大启发和影响力，来源权威性较高。

## 项目链接
https://arxiv.org/abs/2606.30775
