# Reinforcement Learning Unlearns Corrupted SFT Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-25  
**来源：** rss  

## 项目描述
arXiv:2611.26756v1 Announce Type: new Abstract: We show that reinforcement learning (RL) in reasoning tasks can succeed even when the supervised fine-tuning (SFT) data is severely corrupted. In a mathematical reasoning dataset (GSM8K), we systematically corrupt training trajectories across 361 configurations by injecting realistic error types, varying error locations, trace-answer consistency, and corruption ratios up to 100%. While aggregated SFT-only performance steadily deteriorates under corruption (dropping from 43.61% to 13.80%), Group Relative Policy Optimization (GRPO) post-training consistently restores model accuracy back to gold-baseline levels (approximately 60%). Crucially, initializing RL with as few as N = 8 minimal, incorrect, three-line "form-only" traces boosts post-RL performance to 69.30%, outperforming standard gold SFT initialization (60.71%) and GRPO without SFT (35.00%). Further, we show that SFT accuracy is largely uncorrelated with post-RL accuracy (r approximately 0), demonstrating a fundamental asymmetry in post-training: SFT primarily establishes structural layout (form), while RL independently discovers functional reasoning (function).

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.26756
