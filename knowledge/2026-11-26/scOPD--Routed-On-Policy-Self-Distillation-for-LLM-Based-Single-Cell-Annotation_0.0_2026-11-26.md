# scOPD: Routed On-Policy Self-Distillation for LLM-Based Single-Cell Annotation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-26  
**来源：** rss  

## 项目描述
arXiv:2611.31257v1 Announce Type: new Abstract: Motivation: Large language models (LLMs) have shown promise for single-cell annotation, but existing training methods mainly rely on scalar outcome rewards that provide limited supervision for intermediate biological reasoning. Batch-level annotation is particularly challenging because it requires jointly resolving local cell identities and a global one-to-one matching constraint, such that one local error can affect the entire assignment. Moreover, a single inference pass provides insufficient evidence for locating uncertain predictions. These limitations call for fine-grained reasoning supervision during training and uncertainty-aware refinement during inference. Results: To address these challenges, we propose scOPD, an on-policy self-distillation framework for LLM-based single-cell annotation. After reasoning fine-tuning, scOPD adaptively routes qualified rollouts to reward-based optimization, while erroneous rollouts receive privileged token-level supervision from successful sibling trajectories. During inference, rollout disagreement triggers constraint-aware pairwise refinement of uncertain assignments. Across CellPuzzles and four out-of-domain disease datasets, scOPD consistently improves the performance of diverse LLM backbones, achieving average cell-level and batch-level accuracies of 81.71% and 44.49% with Qwen3-8B. Availability and Implementation: Code and data are available at https://github.com/YuZhiyin/scOPD.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.31257
