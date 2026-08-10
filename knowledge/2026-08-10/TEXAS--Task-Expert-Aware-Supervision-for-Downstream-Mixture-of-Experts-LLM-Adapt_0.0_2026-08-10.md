# TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06396v1 Announce Type: new Abstract: Mixture-of-Experts (MoE) language models route each token through a small subset of experts, making routing patterns useful for identifying task-relevant experts during downstream adaptation. Yet current approaches have two limitations: task experts are typically identified from aggregate routing statistics that reflect usage rather than association with successful task completion, and task-expert activations remain underexplored as signals for supervision allocation. We introduce Task-Expert-Aware Supervision (TEXAS), which combines correctness-conditioned task expert discovery with token-level supervision allocation. TEXAS compares expert activations on instances that the base model solves successfully and those it fails to solve, and retains experts more strongly activated on successful instances. During fine-tuning, it upweights answer tokens in failed instances when they activate these experts. TEXAS therefore leverages existing routing behavior without restricting adaptation to a fixed expert subset or imposing an explicit target routing distribution. Across three MoE models and six benchmarks, TEXAS achieves the best or tied-best performance in 17 of 18 settings and improves over the strongest baseline by 1.3--1.5 points on average. Ablations and further analyses validate both the discovered experts and the resulting supervision strategy.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06396
