# RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-30  
**来源：** rss  

## 项目描述
arXiv:2607.24771v1 Announce Type: new Abstract: Knowledge injection updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting full authoritative answers can cause drift in non-updated behavior. Online distillation mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned distillation provides coarse supervision: it can under-emphasize reference-supported rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE, a rollout-conditioned online distillation objective for knowledge injection. RoCo uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate additional distillation weight to reference-supported rollout tokens, while ACE adds sparse reference-side anchored correction for authoritative anchors omitted from the rollout without full-answer imitation. Across three knowledge-injection settings, six retention benchmarks, multiple baselines, and multiple base models, RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while keeping evaluated retention close to the base model.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.24771
