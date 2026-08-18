# Wiola 13M, a Gated Spiral Attention Architecture for Parameter Efficient Small Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-18  
**来源：** rss  

## 项目描述
arXiv:2608.14604v1 Announce Type: new Abstract: Small language models in the ten to one hundred million parameter range are attractive for on device inference, rapid experimentation, and controlled scientific study, yet most of them reuse the standard transformer block without adaptation to the small scale regime. We present Wiola, a decoder only language model whose novelty is concentrated in three drop in components of every layer. First, Spiral Rotary Positional Encoding perturbs the standard rotary frequencies by a slowly growing per dimension factor so that phase trajectories fan outward, improving long range discrimination while adding no parameters. Second, Gated Spiral Attention introduces a per head, content adaptive scalar gate derived from a causal cumulative statistic of the query stream, providing an implicit and differentiable form of soft head selection at negligible cost. Third, the Butterfly feed forward block replaces the conventional expansion layer with a multiplicative interaction and an intra block bypass path, matching the parameter count of a four times gated linear unit block while improving gradient flow in shallow stacks. We formalize each component, derive exact parameter and computation budgets, and prove that the gated attention admits an exact and numerically verified equivalence between full sequence training and cached autoregressive decoding, so that no approximation is introduced at inference time. We also describe a fully reproducible training and evaluation protocol on a standard tiny story corpus. The reference implementation is released as an open source package with weights ready publishing support.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.14604
