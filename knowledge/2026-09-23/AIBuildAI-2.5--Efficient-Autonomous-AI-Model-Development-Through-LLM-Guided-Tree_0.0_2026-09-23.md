# AIBuildAI-2.5: Efficient Autonomous AI Model Development Through LLM-Guided Tree Search

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.25047v1 Announce Type: new Abstract: Autonomous agents that automatically build artificial intelligence (AI) models could broaden access to AI across science and engineering. A popular line of such agents frames model building as a code search problem and solves it by tree search, in which each node is a candidate program and the tree grows by generating a child program from a parent, and these agents now approach the capability of experienced AI engineers on realistic benchmarks. However, these agents have three weaknesses in efficiency that have not been fully addressed. First, only a small number of candidates can be executed within a realistic budget, so search rules that rank nodes by executed rewards, such as Monte Carlo-style tree search, rely on few and noisy scores and select the next node to explore less effectively. Second, no resource-aware strategy is used to schedule training jobs, which can lower hardware utilization and training efficiency. Third, every agent call is served by a single powerful model, which inflates inference cost. Here we introduce AIBuildAI-2.5, an agentic system that carries out the tree search with LLM agents and addresses each of the three issues. AIBuildAI-2.5 proposes a novel LLM-guided tree search, in which a judge scores each candidate on its expected improvement, grounding, and feasibility, and a selector ranks the pool of candidates from these scores and the state of the search. In addition, AIBuildAI-2.5 comprises a scheduler that launches training jobs with the current hardware resource status taken into account and a router that assigns lower-cost LLMs to less demanding tasks while reserving the most capable LLM for the most challenging sub-tasks in the AI model building workflow. AIBuildAI-2.5 ranks first on MLE-Bench with a medal rate of 73.3%, and outperforms a strong baseline on six autonomous AI research tasks from AIRS-Bench.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.25047
