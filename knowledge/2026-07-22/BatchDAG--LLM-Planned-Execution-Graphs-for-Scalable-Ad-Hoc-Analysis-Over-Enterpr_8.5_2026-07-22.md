# BatchDAG: LLM-Planned Execution Graphs for Scalable Ad-Hoc Analysis Over Enterprise Data

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, Agent, 数据分析, 编排, DAG, 论文, 工程实践  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18241v1 Announce Type: new Abstract: Large language models (LLMs) excel at analyzing individual documents but break down on exhaustive, cross-entity analytical questions over enterprise-scale datasets due to context overflow, loss of per-entity attribution, and linear latency from sequential tool calls. We present BatchDAG, a system in which an LLM generates a typed directed acyclic graph (DAG) of operations -- SQL queries, semantic searches, in-memory transforms, parallel fan-outs, and single-shot analyses -- which a deterministic engine evaluates with topological-wave parallelism and structured JSON data flow. A key optimization, entity-aware batching, groups rows by logical entity before fan-out, reducing LLM calls by up to 47x. BatchDAG is not primarily an accuracy improvement over hand-optimized pipelines; rather, it is a general-purpose orchestration layer that replaces multiple hand-engineered workflows with a single system that generates the appropriate execution strategy from natural language. In controlled experiments on 12 transcript-heavy queries, BatchDAG (3.74/5) achieves quality comparable to an expert-designed pipeline (3.25/5) and significantly outperforms a ReAct agent (3.09/5, p<0.01), with superior provenance (77% transcript evidence rate vs. 46-60% for baselines). A controlled ablation shows structured JSON intermediates reduce hallucinations by 27% versus prose summaries (paired t-test, p=0.107, n=12). The planner achieves 98.8% valid-DAG rate across 300 planning calls. In production at Brevian.ai, BatchDAG processes queries over 50,000+ meetings in under 60 seconds, with measured per-query costs of $0.02-$0.24 at published GPT-5.1 pricing.

## 综合总结
BatchDAG提出了一种将LLM作为规划器生成类型化有向无环图（DAG）、由确定性引擎执行的系统架构，用于解决企业级数据跨实体分析中的上下文溢出、延迟和归因丢失问题。通过实体感知批处理优化，大幅减少了LLM调用次数（最高47倍），并利用结构化JSON数据流降低幻觉。实验及生产环境数据表明，该系统在质量、溯源和成本上均优于传统ReAct Agent和手工管道，为企业级数据分析提供了一种高效、低成本的通用编排方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了一种新颖的系统架构BatchDAG，将LLM作为规划器生成类型化DAG（包含SQL、搜索、转换等操作），交由确定性引擎以拓扑波并行方式执行。该方法有效解决了LLM在跨实体分析中的上下文溢出和顺序调用延迟问题。实体感知批处理优化将LLM调用减少47倍，结构化JSON中间体降低27%幻觉，实验设计严谨，包含对照和消融实验及统计检验，技术深度较高。

### 实用性 (评分: 9.0/10)
具有极高的落地价值。该系统已在Brevian.ai生产环境落地，能在60秒内处理5万+会议数据查询，单次查询成本极低（$0.02-$0.24）。其LLM规划+确定性执行的架构模式、实体感知批处理和JSON数据流设计，为从业者解决Agent在企业级数据分析中的成本、延迟和幻觉问题提供了极具参考价值的工程范式。

### 社区活跃度 (评分: 8.0/10)
话题紧扣当前大模型Agent编排和企业级数据分析的热点。论文来源于arXiv，有详实的实验数据和生产环境验证作为支撑，可信度高。其针对ReAct等顺序调用架构痛点的解决方案，对AI工程社区具有较强的影响力和参考意义。

## 项目链接
https://arxiv.org/abs/2607.18241
