# Asymmetric Attention Heads: Structured Head-Wise Context Allocation for Transformer Attention

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-21  
**来源：** rss  

## 项目描述
arXiv:2608.19203v1 Announce Type: new Abstract: Standard multi-head attention (MHA) gives every head the same full causal context span, although heads can serve different contextual roles. Some heads may rely mainly on nearby lexical or syntactic context, while others may depend on longer-range relations such as entity interactions, discourse links, or state changes. We present Asymmetric Attention Heads (AAH), a head-wise context- allocation framework that treats context length as an explicit per-head or per-group allocation variable. AAH groups heads using feature-derived statistics, organizes these groups hierarchically, and assigns causal local windows while preserving the standard flat MHA output interface. In 4096- token seed-0 experiments, several AAH-style local-allocation variants achieve lower validation loss than pure full attention. Short-budget ablations show that stable local allocation and head-window assignment structure matter, while fixed/local controls can be competitive with adaptive hierarchy. We interpret AAH as a structured head-wise context-allocation mechanism for quality and analysis, with Attention Coverage Ratio (ACR) reported as a selected-window routing diagnostic

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.19203
