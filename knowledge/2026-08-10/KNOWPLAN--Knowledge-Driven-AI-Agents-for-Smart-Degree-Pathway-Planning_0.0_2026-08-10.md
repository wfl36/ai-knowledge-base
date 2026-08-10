# KNOWPLAN: Knowledge-Driven AI Agents for Smart Degree Pathway Planning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06530v1 Announce Type: new Abstract: Planning a degree from official university sources requires solving two problems in order. The institution's curriculum must first be reconstructed from catalogs, departmental pages, JSON endpoints, and PDFs that share no schema, and only then can a student-specific path be optimized under prerequisite logic and overlapping requirement constraints. Coupling the two lets each failure mode hide the other, because a planner that drives its own crawling never learns facts its current plan does not need. We present KnowPlan, which enforces an extraction-first boundary and measures the interface between the stages rather than assuming it. CatalogBrowse explores with no access to any user profile. It scores legal actions by lower-confidence expected marginal gain over a finite set of atomic catalog obligations per unit of source access, parses deterministically through platform adapters with a span-constrained clause-to-AST model fallback, and terminates on a closure certificate over index, schema, provenance, and reference completeness instead of a reward threshold. Its output contract is three provenance-linked JSON documents. DegreeMap consumes only those documents. It compiles them into a typed requirement hypergraph and optimizes lexicographically with CP-SAT over hard feasibility, completion horizon, load and risk, personalized utility, and option value, so that each stage optimizes inside the previous stage's proven optimum and stays certifiable within the solver budget. Across a 100-university broad track and a six-school dense track, CatalogBrowse reaches 96.2% inventory recall and 88.7% masked-source recovery at 47% less source access than an exhaustive crawler, DegreeMap holds 100.0% hard feasibility while improving personalized utility by +0.066 over the strongest baseline, and the full pipeline certifies 99.5% of requests with a utility gap to the privileged gold graph of 0.015.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06530
