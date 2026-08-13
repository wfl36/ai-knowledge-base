# ODE-Based Transformer Decoders for Iterative Sign Language Translation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-13  
**来源：** rss  

## 项目描述
arXiv:2608.11352v1 Announce Type: new Abstract: Sign language translation has achieved strong results with Transformer architectures, yet recent improvements largely rely on scaling model capacity at the cost of increased computation. We propose a parameter-efficient alternative that improves expressiveness without increasing model size. Rather than scaling capacity, we focus on enhancing the update dynamics of iterative refinement decoders, where each refinement step corresponds to one internal decoder iteration that progressively improves the latent representation before translation generation. We reinterpret residual refinement updates from an Ordinary Differential Equation (ODE) perspective and replace them with higher-order numerical integration schemes, namely Runge--Kutta methods (RK-2 and RK-4). These methods perform multiple function evaluations within each refinement step to produce more accurate and stable representation updates without adding decoder parameters. To the best of our knowledge, this is the first application of ODE-inspired update dynamics to sign language translation. RK-2 achieves 22.96 BLEU-4 on the PHOENIX-2014-T test set and 19.34 BLEU-4 on the CSL-Daily test set, outperforming the IPSLT baseline on both benchmarks, with fewer decoder layers and refinement iterations on CSL-Daily. These results suggest that stronger refinement dynamics can improve translation performance under parameter-efficient decoder designs, providing a complementary alternative to conventional model scaling.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.11352
