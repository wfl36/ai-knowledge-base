# SynthCorp: A Platform for Creating Benchmarks for Data Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-14  
**来源：** rss  

## 项目描述
arXiv:2611.14765v1 Announce Type: new Abstract: Current benchmarks for LLM-driven data agents saturate quickly and cannot target specific capabilities. We present SynthCorp, a platform that creates customizable data estates and benchmarks by simulating how business events produce and modify corporate data over time. Each data estate combines relational databases, a document store, and a data catalog, paired with evaluation tasks and executable gold programs. First, given a scenario and target complexity dimensions, SynthCorp synthesizes reusable event types and compiles each into a program over predefined simulation primitives. Second, SynthCorp schedules event instances on a virtual calendar, interleaving routine and disruption events so that tables, documents, and catalog entries remain consistent. Third, SynthCorp executes the calendar to materialize the data estate and records every operation in a simulation log. Fourth, SynthCorp generates analytical tasks and derives verified gold programs from the log. We use SynthCorp to generate initial evaluation benchmarks comprising seven data estates (up to 1K operational tables) and 256 tasks across five domains. The data estates pass deterministic pipeline checks (such as foreign-key violations, undeclared writes, recurrence violations, and database execution failures) with a near-zero error rate, introduce cross-asset complexities, and cover all requested dimensions. Evaluating three models across four data-context settings shows that the benchmarks separate data contexts and model tiers. Auditing candidate queries against causal provenance in the simulation log verifies gold programs without manual annotation, including on multi-event composite tasks that expose reasoning failures in state-of-the-art agents. We hope the community uses SynthCorp to generate more challenging and useful data estates and benchmarks that foster the development of enterprise data agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.14765
