# Confidence scores for gated automation of large language models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-28  
**来源：** rss  

## 项目描述
arXiv:2611.33394v1 Announce Type: new Abstract: AI agents built on large language models (LLMs) demonstrate strong capabilities in automated decision-making. However, LLMs may produce incorrect answers with high confidence, limiting their applicability in decisions that affect individuals and organizations. Reliable confidence scores are necessary to gate such decisions, and existing estimates are frequently unavailable or too coarse to support effective gating. This work uses supervised learning to train models to predict the correctness of LLM-generated answers, enabling automated confident responses and routing uncertain ones for human review. A linear confidence score head is fitted to the final-layer hidden state of the frozen LLM backbone, and text-only metamodels are trained as an alternative for closed models. All results come from a single 2B-parameter backbone, on graded answers that are about 98% SQuAD and the remainder TruthfulQA. Against multiple baselines, the confidence score head outperforms all baselines and metamodels, automating the largest fraction of the workload at high accuracy targets. Prompted confidence scores can appear well calibrated yet lack the resolution needed for thresholding. Although transferability to unseen datasets is modest, the confidence score head remains the most robust approach. The proposed confidence scoring framework enhances the safety of automating LLM-based agents and can be adapted to gate other properties, including safety or compliance.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.33394
