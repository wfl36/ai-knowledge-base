# DAGGER: Deployment-Free Quality Estimation for Generative AI Workflows

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-26  
**来源：** rss  

## 项目描述
arXiv:2611.31252v1 Announce Type: new Abstract: Estimating the quality of generative AI workflows is challenging because these workflows comprise multiple stages, and errors can propagate across them, making end-to-end performance depend not only on the accuracy of individual models but also on how their outputs affect downstream stages. Each stage can use one of many candidate models. Estimating end-to-end workflow quality by deploying and evaluating every resulting model configuration is therefore prohibitively expensive. As a result, existing approaches face a tradeoff between estimation cost and accuracy: inexpensive methods often produce unreliable quality estimates, while accurate methods require deploying and evaluating many workflow configurations. In this paper, we introduce DAGGER, a framework for estimating the quality of generative AI workflows without exhaustive deployment and profiling. DAGGER represents a workflow as a graph, in which nodes correspond to stages and edges capture how outputs from one stage affect subsequent stages. It then decomposes workflow quality into per-node accuracy terms and per-edge dependency terms. Using a novel analytical formulation and SVD-based matrix completion, DAGGER estimates workflow quality from sparse observations without executing every candidate workflow. We evaluate DAGGER on three generative AI workflows across three datasets. DAGGER estimates workflow quality with a median error of 6.8 percentage points while reducing profiling cost by 10.2$\times$ relative to BenchPress, a state-of-the-art baseline, and selects workflow configurations competitive with state-of-the-art frameworks such as LLMSelector.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.31252
