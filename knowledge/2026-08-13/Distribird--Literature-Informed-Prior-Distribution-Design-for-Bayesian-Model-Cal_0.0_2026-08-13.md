# Distribird: Literature-Informed Prior Distribution Design for Bayesian Model Calibration

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-13  
**来源：** rss  

## 项目描述
arXiv:2608.11210v1 Announce Type: new Abstract: Bayesian calibration of process-based models requires a prior distribution for each model parameter. Despite decades of methodological work, researchers almost always fall back on uniform priors. The main reason is that building informative priors from scientific literature is slow and needs both domain and statistical expertise. We present \textbf{Distribird}, an agentic web application that automates this process. Given a parameter name, physical description, and domain context, Distribird deploys a multi-agent pipeline that searches the literature, extracts and weights reported values by domain relevance, and fits a probability distribution via AIC model selection. When no literature is available, the system falls back to sensible uninformative alternatives, and clearly reports both the evidence behind and the confidence level of every prior it produces. It is designed for the problems where the models have physically interpretable parameters, where domain knowledge exists in the published literature. We evaluate the tool on 24~parameters across 10 scientific domains comparing three open-weight models (Qwen3.6 27B, Gemma 4 31B, Mistral Small 4 119B) with a single-prompt LLM baseline. On prior quality the full pipeline \emph{matches} this baseline. Every prior is traced to the specific papers and values from which it was constructed; a built-in validity layer declines to produce priors for out-of-scope requests, whereas the single-prompt baseline returns confident but unfounded priors for them in 11 of 30~model--parameter cases; and every language-model call runs locally, so no parameter description or unpublished modelling detail is transmitted to a third-party LLM provider (only generated search terms reach the public literature databases). For scientific use, we argue these properties matter more than a marginal improvement in point-estimate accuracy.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.11210
