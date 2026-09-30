# When Successful Memories Mislead Embodied Agents:Memory Adaption For Task-Conditioned Execution

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35808v1 Announce Type: new Abstract: Experience reuse can reduce repeated exploration in embodied agents, but a trajectory that succeeded previously may be unsuitable for the current execution context. Existing memory systems pri marily optimize construction and retrieval; semantic relevance and historical success therefore remain insufficient when retrieved ex perience contains incompatible actions or an inappropriate level of structure. We introduce Memory Adaptation for Task-Conditioned Execution (MATE), a deterministic post-retrieval procedure that converts trajectories into execution-oriented memory. MATE re moves obsolete control context, extracts condition-action-effect transitions, applies verified action normalization, selects a task dependent representation, and serializes the result under a fixed budget without additional LLM inference. On 134 ALFWorld tasks, MATE achieves task success rates of 81.3% and 93.3% with Qwen2.5-14B and 72B while using approximately one-tenth of the tokens required by raw trajectories. Controlled comparisons show that verified action normalization is the principal mechanism by which MATE restores the utility of retrieved experience, support ing memory adaptation as a distinct stage between retrieval and embodied execution.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35808
