# PoolBench: A Benchmark for Pooling Strategies in Concept Representation Evaluation for Decoder-Only LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-08  
**来源：** rss  

## 项目描述
arXiv:2608.05162v1 Announce Type: new Abstract: Pooling is a consequential but under-examined design choice in decoder-only concept representation work: practitioners must collapse token-level hidden states into a passage-level vector, yet no shared protocol exists for comparing this choice across concepts, models, and tasks. Reported gains are confounded by simultaneous changes in dataset, layer, construction method, and pooling rule, making principled decisions impossible. We introduce PoolBench, a benchmark that isolates pooling as the experimental variable under a fixed evaluation protocol. PoolBench covers 17 concepts, 19 pooling strategies, and 3 open-weight decoder-only models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B), evaluated on a single audited corpus of 37,693 real-text passages. The primary axis is linear separability (D1/AUROC); steered concept prevalence (D2/SCP) and output-level disentanglement (D3) serve as diagnostic axes. The primary finding is decisive: W4_hierarchical reaches a cross-model mean AUROC of 0.7799, while the widely adopted P1_last_token baseline reaches only 0.7640 and is statistically significantly worse (Friedman+Nemenyi, p = 2.0e-36; 77 significant pairs among 18 effective strategies). Rankings are stable across layers (rho = 0.961--0.990). A key negative result: strong detection does not imply strong steering -- D2 and D3 are substantially weaker than D1 for most concepts, indicating a fundamental representational limit rather than a pooling failure. On mid-difficulty concepts, W4_hierarchical outperforms P1_last_token by 0.042--0.113 AUROC; construction method choice (DiffMean vs. REPE) has a larger effect (delta AUROC 0.15) than pooling (delta AUROC 0.016), establishing the correct practical hierarchy. We release the corpus, pre-extracted activations, scorer models, steering vectors, and evaluation code as a reusable protocol for pooling research.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.05162
