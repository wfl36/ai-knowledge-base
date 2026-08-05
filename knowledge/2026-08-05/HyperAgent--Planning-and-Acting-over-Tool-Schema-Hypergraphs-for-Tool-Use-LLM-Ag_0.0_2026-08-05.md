# HyperAgent: Planning and Acting over Tool-Schema Hypergraphs for Tool-Use LLM Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02650v1 Announce Type: new Abstract: Large language model (LLM) agents increasingly rely on external tools to complete complex real-world tasks. However, reliable tool-use planning remains challenging due to the limitations of implicit reasoning and the evolving nature of real-world execution environments. Existing tool-use agents typically rely on LLMs to infer tool compositions from textual descriptions, which can lead to inefficient exploration and unreliable execution in complex tasks. To address these challenges, we model tool relations at the schema level and construct a directed Tool--Schema Hypergraph, in which tools are represented as hyperedges from their required input-schema nodes to their output-schema nodes. Furthermore, we propose HyperAgent, a Tool--Schema Hypergraph-guided framework for dynamic planning and execution. Given a task, HyperAgent first extracts a task-relevant tool context graph and uses it to guide the construction of a schema-aware Task DAG. During execution, HyperAgent dynamically realizes each subtask by constructing a state-conditioned tool support graph through deficit-oriented expansion, which identifies unresolved requirements and retrieves supporting producer tools according to the current agent state. Experiments on AppWorld demonstrate that HyperAgent improves task completion performance while reducing redundant API calls, LLM interactions, and token consumption compared with existing agent baselines.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02650
