# Optimal Model Activation Policies for Inference Networks of Large Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-16  
**来源：** rss  

## 项目描述
arXiv:2609.15992v1 Announce Type: new Abstract: Recent advances in large language models (LLMs) have rendered them necessary for Natural Language Processing (NLP) tasks, and their high inference cost motivates the study of cost-performance trade-offs. In practice, several expert LLMs are used in synergy for inference, either in an ensemble mode or in series, yet without a principled approach on how to best use the available models. An adaptive approach can route simple queries to cheaper LLMs and complex ones to more capable, costly models. However, a clear understanding on how to best leverage available expert models is missing. We introduce inference networks, a graph-based framework, where nodes denote different LLMs, and links denote conditional model activations. The inference network design problem is to determine the best topology, namely the best way to use the models that best addresses the cost-performance trade-off. We start from the basic topology of a series of LLM experts, each of which has a different cost and a different level of expertise, which is captured via model confidence. We formulate the problem of optimal activation of these models so as to minimize the expected inference cost subject to a target performance constraint. For this special class of inference networks, we prove that the optimal activation policy has a threshold structure: query the lowest-cost LLM first, and invoke the more expensive LLM only if the confidence falls below a defined threshold. For discriminative tasks, the optimal policy consists of a set of thresholds, one threshold for each class, while for generative tasks, it consists of a single threshold. We provide a structured method to compute the thresholds, and practical confidence estimation mechanisms for both task types. Experiments with open-source LLMs show substantial cost reductions while meeting the specified performance budget.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.15992
