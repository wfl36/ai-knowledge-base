# Converge Then Diversify: Decoupling Convergence and Diversity in Multi-Objective Bayesian Optimisation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13396v1 Announce Type: new Abstract: Multi-objective Bayesian optimisation (MOBO) is a sample-efficient approach for optimising expensive black-box functions with multiple objectives. In MOBO, the goal is to adequately approximate the Pareto front; that is, to obtain a high-quality solution set with 1) good convergence (closeness to the Pareto front) and 2) good diversity (spread across the Pareto front). Existing MOBO methods typically aim to accomplish these two tasks simultaneously, i.e., driving the search towards the Pareto front while maintaining a diverse set of nondominated solutions, such that the solutions, ideally, can gradually approach the entire front. When sufficient search budgets are available, this approach is effective. However, considering both convergence and diversity throughout the search is not easy and requires careful design. Under very tight budgets, there may not be enough solutions generated to be able to simultaneously approach the entire Pareto front. To address this issue, this paper proposes a \textit{converge-then-diversify} (CTD) approach that decouples convergence and diversity into two stages. In the first stage, CTD focuses on convergence, aiming to quickly drive the search toward a single point on the Pareto front. In the second stage, CTD focuses on diversity, aiming to spread solutions across the front. We present two simple instantiations of CTD by using widely adopted acquisition functions in the area. Experimental results show that, across all 446 pairwise comparisons, CTD statistically outperforms state-of-the-art methods in 72.9\% of the cases, performs equivalently in 21.1\%, and is statistically worse in only 6.1\%, with the advantage being particularly evident in settings with very tight evaluation budgets or in high-dimensional problems.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13396
