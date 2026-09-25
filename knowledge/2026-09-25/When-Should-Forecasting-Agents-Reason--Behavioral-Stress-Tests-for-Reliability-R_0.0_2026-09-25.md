# When Should Forecasting Agents Reason? Behavioral Stress Tests for Reliability Routing

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-25  
**来源：** rss  

## 项目描述
arXiv:2609.28475v1 Announce Type: new Abstract: Forecasting agents increasingly combine language-model reasoning, retrieval, ensembling, and calibration, but it remains unclear when each behavior should be trusted. We study this question on ForecastBench-style binary forecasting tasks, treating the choice to retrieve, reason, defer to a market prior, or use a historical analog as an observable agent behavior rather than a hidden implementation detail. Our central finding is that mechanism choice is source-dependent: structured analogs dominate for some data-generating processes, while market/crowd-style and conservative baselines are better for others. We introduce ReliabilityRoute, a structural intervention that steers forecasting-agent behavior using reliability features such as historical coverage, market-prior availability, source-prior sharpness, evidence strength, evidence disagreement, and horizon. A fixed 2024-fitted rule closely matches a hand taxonomy without hard-coded source-name decisions, while a walk-forward self-adjusting rule refits thresholds from previously resolved vintages and obtains the best mean Brier score among our deterministic systems across 16 later LLM vintages. The gain is modest and historical/search baselines remain highly competitive. The main contribution is therefore a behavioral stress test showing that more reasoning is not always better; forecasting agents should first estimate which evidence source deserves control, routing policies should themselves adapt under auditable constraints, and reproducibility artifacts are available at https://github.com/louiswang524/forcastagent

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.28475
