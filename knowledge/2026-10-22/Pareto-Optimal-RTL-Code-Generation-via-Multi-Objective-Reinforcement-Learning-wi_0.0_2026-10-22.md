# Pareto-Optimal RTL Code Generation via Multi-Objective Reinforcement Learning with Large Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-22  
**来源：** rss  

## 项目描述
arXiv:2610.26904v1 Announce Type: new Abstract: Recent studies have proposed reinforcement learning with verifiable rewards (RLVR) methods that enable LLMs to generate high-quality RTL circuits from natural-language specifications. Existing approaches optimize circuit PPA (Power, Performance, Area) by aggregating multiple objectives into a single scalar reward, making it difficult to simultaneously generate diverse Pareto-optimal solutions across different trade-offs such as low power, low latency, and small area. However, in practical design, the relative importance of each objective varies depending on product requirements and design constraints; thus, obtaining a diverse and high-quality candidate set is beneficial in that designers can choose a preferred trade-off a posteriori. In this work, we are the first to propose a learning method for LLM-based circuit generation that optimizes, not the quality of a single circuit, but the quality and diversity of the entire circuit set obtained through multiple generations in the PPA objective space. The proposed method consists of (1) a generation-based training pipeline that reformulates coverage improvement of the entire Pareto solution set into a sequential circuit generation problem, and (2) a reward function based on Hypervolume Contribution (HVC) that measures how much a generated circuit contributes to the Pareto front. Evaluation on the RTLLM v2 benchmark shows that the proposed method achieves +13.3 percentage points in relative Hypervolume over a baseline without PPA optimization and +14.4 percentage points over a single-objective reinforcement learning method, while also demonstrating superiority in circuit diversity.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26904
