# EXPO-SQL: Execution-based Clause-level Policy Optimization for Text-to-SQL

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, Text-to-SQL, 强化学习, 代码生成, 论文  
**更新日期：** 2026-06-24  
**来源：** rss  

## 项目描述
arXiv:2606.23693v1 Announce Type: new Abstract: Text-to-SQL enables users to query databases using natural language by generating executable SQL queries. Recent methods have increasingly adopted Large Language Models based reinforcement learning (RL) to leverage execution feedback for training. However, existing RL methods assign uniform query-level rewards to all clauses in a SQL query, treating correct and incorrect clauses equally. This coarse-grained reward design leads to insufficient learning signals for correct SQL generation. To address this issue, we propose EXPO-SQL (EXecution-based clause-level Policy Optimization for Text-to-SQL) which provides fine-grained supervision through clause-level rewards. To assign clause-level rewards, our method identifies erroneous clauses by analyzing execution results, including error messages and clause-wise incremental execution. Experiments on widely-used Text-to-SQL benchmarks demonstrate that EXPO-SQL significantly outperforms existing supervised fine-tuning, prompting, and RL-based methods through fine-grained clause-level learning. Our code is available at https://github. com/jhn25/EXPO-SQL.

## 综合总结
本文提出EXPO-SQL，针对Text-to-SQL任务中现有RL方法粗粒度查询级奖励导致学习信号不足的问题，引入细粒度的子句级奖励机制。该方法通过分析执行错误和增量执行结果识别错误子句并分配差异化奖励，在主流基准上显著超越现有SFT、提示及RL方法，为LLM的精确优化提供了有效方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对Text-to-SQL中强化学习方法采用粗粒度查询级奖励导致学习信号不足的痛点，创新性地提出了子句级细粒度奖励机制。通过分析执行错误信息和子句增量执行结果精准定位错误子句，技术深度结合了LLM、RL与执行反馈，方法新颖且论证严谨，实验效果显著优于现有基线。

### 实用性 (评分: 8.0/10)
提供了开源代码，便于从业者复现和工程集成。其细粒度奖励分配的思想不仅适用于Text-to-SQL，对代码生成等需要精确反馈的RLHF任务也具有极高的参考价值，能直接指导相关领域的模型优化实践。

### 社区活跃度 (评分: 7.5/10)
紧扣大模型与强化学习结合的前沿热点，针对Text-to-SQL领域的核心挑战提出解决方案。作为arXiv新文（标注时间为2026年），时效性极强，开源代码提升了来源可信度，但尚未经过正式的同行评审，影响力有待进一步验证。

## 项目链接
https://arxiv.org/abs/2606.23693
