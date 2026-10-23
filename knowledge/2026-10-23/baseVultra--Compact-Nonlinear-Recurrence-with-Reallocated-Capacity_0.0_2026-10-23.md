# baseVultra: Compact Nonlinear Recurrence with Reallocated Capacity

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-23  
**来源：** rss  

## 项目描述
arXiv:2610.30154v1 Announce Type: new Abstract: Nonlinear recurrent networks remain useful for streaming sequence modeling, yet gated cell design is still dominated by LSTM and GRU. We study whether recurrent computation can be reallocated away from gate transforms and toward candidate generation. We propose baseVultra, a compact recurrent cell that concentrates the dense recurrent budget on a single H x H candidate-generation matrix, while replacing recurrent gate matrices with O(H) diagonal interactions. The candidate update combines this dense branch with two low-rank auxiliary branches, an EMA cache, and learnable output blending; the gates additionally receive lightweight second-order access to h_{t-2} through diagonal terms. On TinyShakespeare character-level language modeling, baseVultra achieves a validation loss of 1.594 in the compact one-layer 200K setting, compared with 1.604 for a parameter-matched LSTM and 1.616 for a parameter-matched GRU, while its dense recurrent matrix-vector computation is about 54% of GRU under matched hidden size for this configuration. On text8, a roughly 45x larger benchmark, baseVultra is competitive with full-gate cells (1.854 bpc vs. 1.849 for GRU and 1.837 for LSTM). On formal-language probes, the largest gains appear under constrained hidden-state capacity (0.991 vs. 0.761 GRU and 0.691 LSTM OOD2 accuracy on Counter at H=16) and vanish as hidden size grows. These results characterize where and when candidate-focused recurrent capacity allocation helps: the benefit is concentrated in compact regimes, while full-gate cells remain competitive at scale.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.30154
