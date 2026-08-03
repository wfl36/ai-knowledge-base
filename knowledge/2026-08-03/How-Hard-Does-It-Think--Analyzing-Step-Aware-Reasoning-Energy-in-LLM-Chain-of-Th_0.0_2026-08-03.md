# How Hard Does It Think? Analyzing Step-Aware Reasoning Energy in LLM Chain-of-Thought Trajectories

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-03  
**来源：** rss  

## 项目描述
arXiv:2607.28674v1 Announce Type: new Abstract: Understanding how computational effort is allocated across individual chain-of-thought (CoT) reasoning steps remains an open challenge: existing interpretability methods rely on output-level signals or collapse processing depth into a single trajectory-level scalar, leaving step-wise effort opaque. We propose Step-Aware Reasoning Energy (SARE), a geometric framework that quantifies effort at the granularity of individual CoT steps via Centered Kernel Alignment (CKA) between Gram matrices of token hidden states across adjacent transformer layers, capturing inter-token relational structure without requiring eigenvector alignment or cluster correspondence. SARE further contextualizes this energy within reasoning's semantic progression by modeling CoT trajectories as transitions among latent semantic states. Across six reasoning benchmarks and three open-weight LLMs, we find that reasoning energy is highly non-uniform across step types, exhibiting phase-like transitions invisible to trajectory-level metrics; incorrect trajectories show systematically lower energy at critical reasoning junctions; and SARE-based features match or outperform output-based confidence baselines in most settings, indicating that internal geometric dynamics encode predictive information beyond surface-level signals.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.28674
