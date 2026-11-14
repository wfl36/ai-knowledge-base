# Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-14  
**来源：** rss  

## 项目描述
arXiv:2611.14769v1 Announce Type: new Abstract: Arena-style rankings of language models are a widely used evaluation framework in online leaderboards, research papers, and model evaluation in production. These rankings aim to realistically assess model performance using pairwise comparisons of anonymous models on user prompts, aggregating votes via the Bradley-Terry model to produce the final ranking. However, we find that these leaderboards are highly vulnerable to several manipulation strategies that unscrupulous providers could use to boost a model's rank: strategic voting (individual votes that boost a model's rank, including votes on irrelevant models), strategic prompting (choosing prompts that favor a model), and strategic nomination (boosting the rank of a model by inserting irrelevant models). We demonstrate these effects on public leaderboard data, analyze the circumstances that cause these vulnerabilities, and describe approaches to safeguard against each attack. Notably, these issues hold for any preference-based evaluation using the Bradley-Terry model that allows open prompting, voting, or model submission. These manipulations boost the rank of nearly every tested model; each attack can boost a model by up to 15-20 places in a ranking and, combined, they can boost a model by up to 45 places.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.14769
