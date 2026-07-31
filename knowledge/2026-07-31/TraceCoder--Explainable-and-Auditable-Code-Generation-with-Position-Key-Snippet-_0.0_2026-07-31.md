# TraceCoder: Explainable and Auditable Code Generation with Position-Key Snippet Versioning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-31  
**来源：** rss  

## 项目描述
arXiv:2607.26307v1 Announce Type: new Abstract: Contemporary LLM-based coding agents produce code as black-box outputs: the rationale behind each line is hidden, the evolution of the code through benchmark-driven repair is ephemeral, and post-hoc auditing is impossible. We present a code generation concept that addresses these shortcomings through three complementary mechanisms: (i) a relational snippet-history schema that records, per repair event, the benchmark reference, round number, failure text, and LLM explanation, enabling full provenance queries; (ii) a browser-based visualisation tool that renders this history as heat-mapped, hover-annotated source code; and (iii) a competitive fractional position-key indexing scheme with tree-node delimiters that assigns stable, lexicographically-ordered identifiers to each code snippet, enabling fine-grained tracking without disrupting surrounding lines. We evaluate TraceCoder on 30 algorithmic programming tasks spanning string processing, mathematical computation, and data-structure manipulation, across two provider configurations. Of these, 10 exhaust the 6-iteration budget on tasks with subtle edge-case behaviour. Mean Chg% reaches 30%, three in ten code snippets carry a traceable repair-event row, compared to 21% when using Gemini 2.0 Flash as sole provider on a 20-task subset. Three detailed case studies demonstrate how the system explains which specific benchmark failures shaped each line of the final program. The proposed mechanism makes the internal "narrative" of automated code generation auditable and replayable, a property essential for trust and accountability in production deployments.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.26307
