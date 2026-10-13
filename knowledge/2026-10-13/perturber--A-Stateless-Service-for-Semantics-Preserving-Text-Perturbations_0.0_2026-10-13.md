# perturber: A Stateless Service for Semantics-Preserving Text Perturbations

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-13  
**来源：** rss  

## 项目描述
arXiv:2610.12667v1 Announce Type: new Abstract: Large language model (LLM) evaluations on clean benchmarks overstate model robustness: real inputs arrive perturbed, and these meaning-preserving variants routinely move model answers. Studying this systematically requires applying perturbations one at a time, reproducibly, and identically wherever they run, yet existing tools couple them to a benchmarking stack rather than packaging them as a reusable transform layer. We present perturber, a stateless service and Python library that applies exactly one semantics-preserving perturbation per call, drawn from a first-party catalog of 68 perturbations across 11 families. It turns on a single primitive, with composition left to the caller chaining calls, so the service and the library produce identical output by construction. We evaluate the tool itself, its correctness, reproducibility, and cost, rather than any model's robustness, measuring meaning-preservation per perturbation rather than assuming it. The demonstration adds a live playground, an introspectable catalog for benchmark selection, and a one-command reproducible evaluation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.12667
