# When Chain-of-Thought Helps and When It Hurts: An Empirical Investigation of the Serial-Depth Bottleneck in LLM Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-12  
**来源：** rss  

## 项目描述
arXiv:2608.09942v1 Announce Type: new Abstract: It is widely assumed that chain-of-thought (CoT) prompting universally improves LLM reasoning. We investigate this through the conceptual framework of the H_dp bandwidth bound (Chen et al., 2024): although the formal bound binds only asymptotically (at astronomically large prompt lengths), it identifies a real architectural bottleneck -- serial computation exceeding a transformer's single-pass capacity must be externalised, which is what CoT does. Our central finding is a within-benchmark serial-depth gradient: single-pass (no-CoT) accuracy degrades monotonically with per-item serial depth, while CoT is approximately depth-invariant. We measure CoT effects across three instruction-tuned models (Qwen-2.5-7B/32B, Llama-3.1-8B) and five standard NLP benchmarks at practical context lengths. On high-depth P-complete tasks (GSM8K, MATH), CoT gives a +54 to +68 pp recovery gap across all models. On shallow TC^0 tasks (MMLU, ARC), CoT is structurally redundant (Delta in [0.0, +4.6] pp, no significant negative effect) -- though high no-CoT baselines (up to 95% on ARC) may reflect contamination, so this null is not a clean architectural test. The intermediate class L (HumanEval) shows a model-size-dependent transition: +23.2 pp (32B), +9.1 pp (8B), -28.7 pp (7B). The cross-benchmark depth-recovery correlation is Spearman rho = 0.661 (p = 0.007, n = 15); 9 of 15 benchmark-level McNemar tests are significant after Bonferroni correction. Pre-registered on OSF, our results indicate that CoT is not a universal reasoning enhancer but acts as a bandwidth bypass: it helps serial computation that strains single-pass capacity and is redundant for tasks that already fit.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.09942
