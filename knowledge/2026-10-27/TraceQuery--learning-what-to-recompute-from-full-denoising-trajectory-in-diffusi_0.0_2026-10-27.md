# TraceQuery: learning what to recompute from full-denoising trajectory in diffusion language models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-27  
**来源：** rss  

## 项目描述
arXiv:2610.33008v1 Announce Type: new Abstract: Diffusion large language models (dLLMs) enable flexible generation through iterative masked denoising, but incur substantial inference cost because token representations are repeatedly recomputed across denoising steps. Existing cache-based methods reduce this cost by reusing intermediate results across denoising steps and recomputing only a subset of positions at each step, chosen either on a fixed schedule or by heuristic signals of change. Our trajectory experiments instead point to decoding trajectory as the more relevant quantity. Cached generation remains accurate when it stays close to the full-denoising trajectory, with errors concentrated around unmask-order deviations and reduced as longer reference prefixes are recovered. This suggests a more direct principle: limiting representation error helps, but keeping generation on the full-denoising trajectory is a more direct route to accurate decoding. We therefore formulate efficient dLLM inference as trajectory-guided querying. Rather than broadly repairing representation error, we use full-denoising trajectories to supervise which unresolved positions should receive limited fresh computation. Based on this formulation, we introduce TRACEQUERY, a lightweight sparse decoding framework that predicts a small set of near-future trajectory-relevant positions, queries only those candidates, and lets the backbone select which one to commit from their fresh predictions. TRACEQUERY delivers the strongest quality-computation trade-off among cache-based approaches, sustaining high accuracy with substantially fewer fresh token computations, and generalizes across tasks, model variants, and families. Code: https://github.com/fish1928/tracequery.git

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.33008
